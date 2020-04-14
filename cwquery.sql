
@message       - raw unparsed log event.
@timestamp     - event timestamp contained in the log events.
@ingestionTime - time of log event was received by CloudWatch Logs.
@logStream     - name of the log stream that the log event was added.
@log           - log group identifier eg. account-id:log-group-name.

# selecting last / latest message.
fields @timestamp, latest(@message)

# selecting first / earliest message.
fields @timestamp, earliest(@message)

# selecting 25 most recently added log events.
fields @timestamp, @message |
sort   @timestamp desc      |
limit  25

# selecting number of exceptions per hour.
filter @message like /Exception/             |
stats  count(*) as exceptionCount by bin(1h) |
sort   exceptionCount desc

# selecting log events excluding Exception string.
fields @message |
filter @message not like /Exception/

# selecting messages sorting by time
# in descending order with limit 10.
fields @message        |
sort   @timestamp desc |
limit  10

# selecting messages contains "Status: 200",
# sorting by descending order with limit 10.
fields @message                    |
filter @message like "Status: 200" |
sort   @timestamp desc             |
limit  10

# selecting messages contains "Status: 2xx",
# sorting by descending order with limit 10.
fields @message                      |
filter @message like "Status: 2\d\d" |
sort   @timestamp desc               |
limit  10

# selecting count of log events 
# in the log group for each log stream.
# Visualization -> arrow by Line -> Bar
stats count(*) by @logStream

# 
stats avg(f1) by bin(5m)

# Visualization -> arrow next to Line
stats count(*) by bin(30s)

# selecting loggingMessage from message field,
# with condition ERROR.
fields  @message                                        |
parse   @message "[*] *" as loggingType, loggingMessage |
filter  loggingType = "ERROR"                           |
display loggingMessage

#
fields  @message                                                       |
parse   @message "* [*] *" as loggingTime, loggingType, loggingMessage |
filter  loggingType in ["ERROR", "INFO"]                               |
display loggingMessage, loggingType = "ERROR" as isError

# selecting messages contains 400 and 500.
fields @timestamp, @message |
filter @message in [400, 500]

# selecting messages not contains 400 and 500.
fields @timestamp, @message |
filter @message not in [400, 500]

fields @timestamp, @message |
filter (duration > 2000)

fields f1, f2 |
filter (f1 = 10 or f3 > 25)

stats avg(f1) by f2

fields f1, f2 |
sort   f1 desc

fields abs(f1) as Field1, f2

stats avg(f1) as AvgField |
sort  AvgField desc

