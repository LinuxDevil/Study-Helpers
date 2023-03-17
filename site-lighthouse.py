import subprocess
import json
import argparse
import datetime


def run_lighthouse(url, flags):
    """Runs Lighthouse audit on the given URL with the given flags"""
    lighthouse_command = f'lighthouse {url} --output=json --quiet {" ".join(flags)}'
    process = subprocess.Popen(lighthouse_command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if error:
        raise Exception(error)
    return json.loads(output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Google Lighthouse as a CLI')
    parser.add_argument('url', help='URL to run Lighthouse audit on')
    parser.add_argument('-p', '--performance', action='store_true', help='Include performance audit')
    parser.add_argument('-a', '--accessibility', action='store_true', help='Include accessibility audit')
    parser.add_argument('-b', '--best-practices', action='store_true', help='Include best practices audit')
    parser.add_argument('-s', '--seo', action='store_true', help='Include SEO audit')
    args = parser.parse_args()

    flags = []
    if args.performance:
        flags.append('--only-categories=performance')
    if args.accessibility:
        flags.append('--only-categories=accessibility')
    if args.best_practices:
        flags.append('--only-categories=best-practices')
    if args.seo:
        flags.append('--only-categories=seo')

    # Get the current date and time
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y-%m-%d')

    # Extract the website name from the URL
    website_name = args.url.split('//')[1].split('/')[0]

    # Run Lighthouse audit and save the report
    result = run_lighthouse(args.url, flags)
    report_name = f'{website_name}-{timestamp}.json'
    with open(report_name, 'w') as f:
        f.write(json.dumps(result, indent=4))

    print(f'Lighthouse report saved as {report_name}')
