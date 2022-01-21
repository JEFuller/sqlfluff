"""A list of all SQL key words.

https://docs.microsoft.com/en-us/sql/t-sql/language-elements/reserved-keywords-transact-sql?view=sql-server-ver15
"""

RESERVED_KEYWORDS = [
    "ADD",
    "ALL",
    "ALTER",
    "AND",
    "ANY",
    "AS",
    "ASC",
    "AUTHORIZATION",
    "BACKUP",
    "BEGIN",
    "BETWEEN",
    "BREAK",
    "BROWSE",
    "BULK",
    "BY",
    "CASCADE",
    "CASE",
    "CHECK",
    "CHECKPOINT",
    "CLOSE",
    "CLUSTERED",
    "COALESCE",
    "COLLATE",
    "COLUMN",
    "COMMIT",
    "COMPUTE",
    "CONSTRAINT",
    "CONTAINS",
    "CONTAINSTABLE",
    "CONTINUE",
    "CONVERT",
    "CREATE",
    "CROSS",
    "CURRENT_DATE",
    "CURRENT_TIME",
    "CURRENT_TIMESTAMP",
    "CURRENT_USER",
    "CURRENT",
    "CURSOR",
    "DATABASE",
    "DBCC",
    "DEALLOCATE",
    "DECLARE",
    "DEFAULT",
    "DELETE",
    "DENY",
    "DESC",
    "DISTINCT",
    "DISTRIBUTED",
    "DOUBLE",
    "DROP",
    "ELSE",
    "END",
    "ERRLVL",
    "ESCAPE",
    "EXCEPT",
    "EXEC",
    "EXECUTE",
    "EXISTS",
    "EXIT",
    "EXTERNAL",
    "FETCH",
    "FILE",
    "FILLFACTOR",
    "FOR",
    "FOREIGN",
    "FREETEXT",
    "FREETEXTTABLE",
    "FROM",
    "FULL",
    "FUNCTION",
    "GOTO",
    "GRANT",
    "GROUP",
    "HAVING",
    "HOLDLOCK",
    "IDENTITY_INSERT",
    "IDENTITY",
    "IDENTITYCOL",
    "IF",
    "IN",
    "INDEX",
    "INNER",
    "INSERT",
    "INTERSECT",
    "INTO",
    "IS",
    "JOIN",
    "KEY",
    "KILL",
    "LEFT",
    "LIKE",
    "LINENO",
    "MERGE",
    "NATIONAL",
    "NOCHECK",
    "NONCLUSTERED",
    "NOT",
    "NULL",
    "NULLIF",
    "OF",
    "OFF",
    "OFFSETS",
    "ON",
    "OPEN",
    "OPENDATASOURCE",
    "OPENQUERY",
    "OPENROWSET",
    "OPENXML",
    "OPTION",
    "OR",
    "ORDER",
    "OUTER",
    "OVER",
    "PERCENT",
    "PIVOT",
    "PLAN",
    "PRIMARY",
    "PRINT",
    "PROC",
    "PROCEDURE",
    "PUBLIC",
    "RAISERROR",
    "READ",
    "READTEXT",
    "RECONFIGURE",
    "REFERENCES",
    "REPLICATION",
    "RESTORE",
    "RESTRICT",
    "RETURN",
    "REVERT",
    "REVOKE",
    "RIGHT",
    "ROLLBACK",
    "ROWCOUNT",
    "ROWGUIDCOL",
    "RULE",
    "SAVE",
    "SCHEMA",
    "SELECT",
    "SEMANTICKEYPHRASETABLE",
    "SEMANTICSIMILARITYDETAILSTABLE",
    "SEMANTICSIMILARITYTABLE",
    "SESSION_USER",
    "SET",
    "SETUSER",
    "SHUTDOWN",
    "SOME",
    "STATISTICS",
    "SYSTEM_USER",
    "TABLE",
    "TABLESAMPLE",
    "TEXTSIZE",
    "THEN",
    "TO",
    "TOP",
    "TRAN",
    "TRANSACTION",
    "TRANS",
    "TRIGGER",
    "TRUNCATE",
    "TRY_CONVERT",
    "TSEQUAL",
    "UNION",
    "UNIQUE",
    "UNPIVOT",
    "UPDATE",
    "UPDATETEXT",
    "USE",
    "USER",
    "VALUES",
    "VARYING",
    "VIEW",
    "WAITFOR",
    "WHEN",
    "WHERE",
    "WHILE",
    "WITH",
    "WRITETEXT",
]


UNRESERVED_KEYWORDS = [
    "ABORT_AFTER_WAIT",
    "ALGORITHM",
    "ALLOW_PAGE_LOCKS",
    "ALLOW_ROW_LOCKS",
    "ALWAYS",
    "ANSI_DEFAULTS",
    "ANSI_NULL_DFLT_OFF",
    "ANSI_NULL_DFLT_ON",
    "ANSI_NULLS",
    "ANSI_PADDING",
    "ANSI_WARNINGS",
    "APPLY",
    "ARITHABORT",
    "ARITHIGNORE",
    "BERNOULLI",
    "BLOCKERS",
    "CACHE",
    "CALLED",
    "CALLER",
    "CAST",
    "CATCH",
    "COLUMN_ENCRYPTION_KEY",
    "COLUMNSTORE",
    "COLUMNSTORE_ARCHIVE",
    "CONCAT",
    "CONCAT_NULL_YIELDS_NULL",
    "COMPRESSION_DELAY",
    "CURSOR_CLOSE_ON_COMMIT",
    "CYCLE",
    "D",
    "DATA_COMPRESSION",
    "DATE",
    "DATEADD",
    "DATEDIFF",
    "DATEDIFF_BIG",
    "DATEFIRST",
    "DATEFORMAT",
    "DATENAME",
    "DAY",
    "DAYOFYEAR",
    "DD",
    "DEADLOCK_PRIORITY",
    "DENSE_RANK",
    "DETERMINISTIC",
    "DISABLE",
    "DISK",  # listed as reserved but functionally unreserved
    "DISTRIBUTION",  # Azure Synapse Analytics specific
    "DROP_EXISTING",
    "DUMP",  # listed as reserved but functionally unreserved
    "DW",
    "DY",
    "ENCRYPTED",
    "ENCRYPTION",
    "ENCRYPTION_TYPE",
    "EXPAND",
    "EXPLAIN",  # Azure Synapse Analytics specific
    "EXTERNALPUSHDOWN",
    "FAST",
    "FILESTREAM",
    "FILESTREAM_ON",
    "FILTER",
    "FIPS_FLAGGER",
    "FMTONLY",
    "FORCE",
    "FORCEPLAN",
    "FORCESCAN",
    "FORCESEEK",
    "GO",
    "HASH",
    "HEAP",  # Azure Synapse Analytics specific
    "HH",
    "HIDDEN",
    "HINT",
    "HOUR",
    "IGNORE",
    "IGNORE_CONSTRAINTS",
    "IGNORE_DUP_KEY",
    "IGNORE_NONCLUSTERED_COLUMNSTORE_INDEX",
    "IGNORE_TRIGGERS",
    "IMPLICIT_TRANSACTIONS",
    "INCLUDE",
    "INCREMENT",
    "INLINE",
    "INTERVAL",
    "IO",
    "ISOLATION",
    "GENERATED",
    "KEEP",
    "KEEPDEFAULTS",
    "KEEPFIXED",
    "KEEPIDENTITY",
    "LABEL",  # Azure Synapse Analytics specific, reserved keyword but could break TSQL parsing to add there
    "LANGUAGE",
    "LEVEL",
    "LOAD",  # listed as reserved but functionally unreserved
    "LOCATION",
    "LOCK_TIMEOUT",
    "LOOP",
    "M",
    "MAX_DURATION",
    "MAX_GRANT_PERCENT",
    "MASKED",
    "MATCHED",
    "MAXDOP",
    "MAXRECURSION",
    "MAXVALUE",
    "MCS",
    "MI",
    "MICROSECOND",
    "MILLISECOND",
    "MIN_GRANT_PERCENT",
    "MINUTE",
    "MINUTES",
    "MINVALUE",
    "MM",
    "MONTH",
    "MS",
    "N",
    "NANOSECOND",
    "NEXT",
    "NO",
    "NO_PERFORMANCE_SPOOL",
    "NOCOUNT",
    "NOEXEC",
    "NOEXPAND",
    "NOLOCK",
    "NONE",
    "NOWAIT",
    "NS",
    "NTILE",
    "NUMERIC_ROUNDABORT",
    "OBJECT",
    "OFFSET",
    "ONLINE",
    "OPTIMIZE",
    "OPTIMIZE_FOR_SEQUENTIAL_KEY",
    "OUTPUT",
    "OWNER",
    "PAD_INDEX",
    "PAGE",
    "PAGLOCK",
    "PARAMETER",
    "PARAMETERIZATION",
    "PARSEONLY",
    "PARTITION",
    "PARTITIONS",
    "PERCENTILE_CONT",
    "PERCENTILE_DISC",
    "PERSISTED",
    "PRECISION",  # listed as reserved but functionally unreserved
    "PRIOR",
    "PROFILE",
    "Q",
    "QQ",
    "QUARTER",
    "QUERY_GOVERNOR_COST_LIMIT",
    "QUERYTRACEON",
    "QUOTED_IDENTIFIER",
    "RANDOMIZED",
    "RANGE",
    "RANK",
    "READCOMMITTED",
    "READCOMMITTEDLOCK",
    "READPAST",
    "READUNCOMMITTED",
    "RECOMPILE",
    "RECURSIVE",
    "REMOTE_PROC_TRANSACTIONS",
    "RENAME",  # Azure Synapse Analytics specific
    "REPEATABLE",
    "REPEATABLEREAD",
    "REPLACE",
    "REPLICATE",  # Azure Synapse Analytics
    "RESPECT",
    "RESULT_SET_CACHING",  # Azure Synapse Analytics specific
    "RESUMABLE",
    "RETURNS",
    "ROBUST",
    "ROLE",
    "ROUND_ROBIN",  # Azure Synapse Analytics specific
    "ROW",
    "ROW_NUMBER",
    "ROWGUIDCOL",
    "ROWLOCK",
    "ROWS",
    "S",
    "SCALEOUTEXECUTION",
    "SCHEMABINDING",
    "SECOND",
    "SECURITYAUDIT",  # listed as reserved but functionally unreserved
    "SELF",
    "SEQUENCE",
    "SEQUENCE_NUMBER",
    "SERIALIZABLE",
    "SHOWPLAN_ALL",
    "SHOWPLAN_TEXT",
    "SHOWPLAN_XML",
    "SNAPSHOT",
    "SORT_IN_TEMPDB",
    "SOURCE",
    "SPARSE",
    "SPATIAL_WINDOW_MAX_CELLS",
    "SS",
    "START",
    "STATISTICS_INCREMENTAL",
    "STATISTICS_NORECOMPUTE",
    "STRING_AGG",
    "SWITCH",
    "SYSTEM",
    "TABLOCK",
    "TABLOCKX",
    "TARGET",
    "TEXTIMAGE_ON",
    "THROW",
    "TIES",
    "TIME",
    "TIMESTAMP",
    "TRANSACTION_ID",
    "TRUNCATE_TARGET",  # Azure Synapse Analytics specific
    "TRY",
    "TYPE",
    "UPDLOCK",
    "UNKNOWN",
    "USER_DB",  # Azure Synapse Analytics specific, deprecated
    "USING",
    "VALUE",
    "VIEW_METADATA",
    "W",
    "WAIT_AT_LOW_PRIORITY",
    "WEEK",
    "WEEKDAY",
    "WITHIN",
    "WK",
    "WORK",
    "WW",
    "XACT_ABORT",
    "XLOCK",
    "XML",
    "YEAR",
    "Y",
    "YY",
    "YYYY",
]
