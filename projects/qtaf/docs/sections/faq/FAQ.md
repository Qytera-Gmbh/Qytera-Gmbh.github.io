| :x:                  | When running `mvn:exec`, I get an error message `java.lang.ClassNotFoundException: some.package.TestRunner`. |
| :------------------: | ------------------------------------------------------------------------------------------------------------ |
| :information_source: | Make sure to run `mvn install -DskipTests` first.                                                            |

| :x:                  | I get the following error message ```
com.google.inject.ConfigurationException: Guice configuration errors:

1) [Guice/MissingConstructor]: No injectable constructor for type TimeSeriesTable.

class TimeSeriesTable does not have a @Inject annotated constructor or a no-arg constructor.
```. |
| :------------------: | ------------------------------------------------------------------------------------------------------------ |
| :information_source: | Your class needs to have a default constructor with no arguments.                                            |
