import subprocess
import json
import argparse
import datetime


def get_cli_flags(args) -> [str]:
    cli_flags = []
    if args.performance:
        cli_flags.append('--only-categories=performance')
    if args.accessibility:
        cli_flags.append('--only-categories=accessibility')
    if args.best_practices:
        cli_flags.append('--only-categories=best-practices')
    if args.seo:
        cli_flags.append('--only-categories=seo')
    return cli_flags


def get_cli_args():
    parser = argparse.ArgumentParser(description='Run Google Lighthouse as a CLI')
    parser.add_argument('url', help='URL to run Lighthouse audit on')
    parser.add_argument('-p', '--performance', action='store_true', help='Include performance audit')
    parser.add_argument('-a', '--accessibility', action='store_true', help='Include accessibility audit')
    parser.add_argument('-b', '--best-practices', action='store_true', help='Include best practices audit')
    parser.add_argument('-s', '--seo', action='store_true', help='Include SEO audit')
    return parser.parse_args()


def run_lighthouse(url, flags):
    """Runs Lighthouse audit on the given URL with the given flags"""
    lighthouse_command = f'lighthouse {url} --output=json --quiet {" ".join(flags)}'
    process = subprocess.Popen(lighthouse_command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if error:
        raise Exception(error)
    return json.loads(output)


def save_report(args, result):
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y-%m-%d')
    website_name = args.url.split('//')[1].split('/')[0]

    report_name = f'{website_name}-{timestamp}.json'
    with open(report_name, 'w') as f:
        f.write(json.dumps(result, indent=4))

    print(f'Lighthouse report saved as {report_name}')


if __name__ == '__main__':
    _args = get_cli_args()
    _flags = get_cli_flags(_args)

    # Run Lighthouse audit and save the report
    _result = run_lighthouse(_args.url, _flags)
    print('Light house finished! Saving Report...')
    save_report(_args, _result)

