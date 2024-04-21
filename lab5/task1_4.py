import argparse
import task1_1
from task1_2 import analyzeLogs,readFile
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
    
    calcStatsGlobal_parser = subparsers.add_parser("calcStatsGlobal", help="calculate_statistics_global. Wyniki podane w sekundach.")
    
    calcStatsUser_parser = subparsers.add_parser("calcStatsForUser", help="calculate_statistic_for_user. Wyniki podane w sekundach.")
    
    loggingFrequency_parser = subparsers.add_parser("logFreq", help="get_user_logging_frequency")


    args = parser.parse_args()
    
    analyzeLogs(args)

    if args.subcommand == "rndUser":
        printRandomUserLogs(readFile(args.file), args.n)
    elif args.subcommand == "calcStatsGlobal":
        statisticsResults = calculateStatistics(readFile(args.file), global_=True)
        print(statisticsResults)
    elif args.subcommand == "calcStatsForUser":
        statisticsResults = calculateStatistics(readFile(args.file), global_=False)
        print(statisticsResults)
    elif args.subcommand == "logFreq":
        usersFrequency = getUsersLoggingFrequency(readFile(args.file))
        print(usersFrequency)

if __name__ == "__main__":
    main()