import argparse
import task1_1
from task1_2 import analyze_logs,readFile,runGetIpv4FromLog,runGetMessageType,runGetUserFromLog
from task1_3 import printRandomUserLogs, calculateStatistics, getUsersLoggingFrequency

def main():
    parser = argparse.ArgumentParser(description="Laboratorium 5")
    parser.add_argument("file", help="Scieżka do pliku z logami")
    parser.add_argument("-l", "--log-level", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                        default="DEBUG", help="Minimalny poziom logowania(opcjonalny)")
    subparsers = parser.add_subparsers(title="Komendy", dest="subcommand")

    ipv4_parser = subparsers.add_parser("ipv4", help="get_ipv4")
    
    user_parser = subparsers.add_parser("user", help="get_users")
    
    message_parser = subparsers.add_parser("message", help="get_message")
    
    randomUser_parser = subparsers.add_parser("rndUser", help="get_random_user_logs. Użycie: rndUser+spacja+n")
    randomUser_parser.add_argument("n", type=int, help="Liczba logów do wyświetlenia")
    
    calcStatsGlobal_parser = subparsers.add_parser("calcStatsGlobal", help="calculate_statistics_global")
    
    calcStatsUser_parser = subparsers.add_parser("calcStatsForUser", help="calculate_statistic_for_user")
    
    loggingFrequency_parser = subparsers.add_parser("logFreq", help="get_user_logging_frequency")


    args = parser.parse_args()
    
    analyze_logs(args)

    if args.subcommand == "rndUser":
        printRandomUserLogs(readFile(args.file), 5)
    elif args.subcommand == "calcStatsGlobal":
        statistics_results = calculateStatistics(readFile(args.file), global_=True)
        print(statistics_results)
    elif args.subcommand == "calcStatsForUser":
        statistics_results = calculateStatistics(readFile(args.file), global_=False)
        print(statistics_results)
    elif args.subcommand == "logFreq":
        users_frequency = getUsersLoggingFrequency(readFile(args.file))
        print(users_frequency)

if __name__ == "__main__":
    main()