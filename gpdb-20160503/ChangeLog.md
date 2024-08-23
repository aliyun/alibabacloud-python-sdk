2024-08-23 Version: 4.0.0
- Update API CheckHadoopNetConnection: add param DataSourceId.
- Update API CheckHadoopNetConnection: update param EmrInstanceId.
- Update API CheckJDBCSourceNetConnection: add param DataSourceId.
- Update API CheckJDBCSourceNetConnection: update param JdbcConnectionString.
- Update API CreateAccount: add param AccountType.
- Update API DescribeAccounts: add param AccountType.
- Update API DescribeAccounts: update response param.
- Update API DescribeDBInstanceDataBloat: add param Database.
- Update API DescribeDBInstanceDataBloat: add param OrderBy.
- Update API DescribeDBInstanceDataSkew: add param Database.
- Update API DescribeDBInstanceDataSkew: add param OrderBy.
- Update API DescribeDBInstanceIndexUsage: add param Database.
- Update API DescribeDBInstanceIndexUsage: add param OrderBy.
- Update API DescribeDBInstanceIndexUsage: update response param.
- Update API DescribeHadoopDataSource: update response param.
- Update API DescribeJDBCDataSource: update response param.


2024-08-04 Version: 3.9.1
- Update API CancelUpsertCollectionDataJob: add param WorkspaceId.
- Update API CancelUpsertCollectionDataJob: update param DBInstanceId.
- Update API CreateCollection: add param WorkspaceId.
- Update API CreateCollection: update param DBInstanceId.
- Update API CreateNamespace: add param WorkspaceId.
- Update API CreateNamespace: update param DBInstanceId.
- Update API DeleteCollection: add param WorkspaceId.
- Update API DeleteCollection: update param DBInstanceId.
- Update API DeleteCollectionData: add param WorkspaceId.
- Update API DeleteCollectionData: update param DBInstanceId.
- Update API DeleteNamespace: add param WorkspaceId.
- Update API DeleteNamespace: update param DBInstanceId.
- Update API DescribeCollection: add param WorkspaceId.
- Update API DescribeCollection: update param DBInstanceId.
- Update API DescribeNamespace: add param WorkspaceId.
- Update API DescribeNamespace: update param DBInstanceId.
- Update API GetUpsertCollectionDataJob: add param WorkspaceId.
- Update API GetUpsertCollectionDataJob: update param DBInstanceId.
- Update API InitVectorDatabase: add param WorkspaceId.
- Update API InitVectorDatabase: update param DBInstanceId.
- Update API ListCollections: add param WorkspaceId.
- Update API ListCollections: update param DBInstanceId.
- Update API ListNamespaces: add param WorkspaceId.
- Update API ListNamespaces: update param DBInstanceId.
- Update API QueryCollectionData: add param WorkspaceId.
- Update API QueryCollectionData: update param DBInstanceId.
- Update API UpdateCollectionDataMetadata: add param WorkspaceId.
- Update API UpdateCollectionDataMetadata: update param DBInstanceId.
- Update API UpsertCollectionData: add param WorkspaceId.
- Update API UpsertCollectionData: update param DBInstanceId.
- Update API UpsertCollectionDataAsync: add param WorkspaceId.
- Update API UpsertCollectionDataAsync: update param DBInstanceId.


2024-07-19 Version: 3.9.0
- Support API CreateSecret.
- Support API DeleteSecret.
- Support API DescribeTable.
- Support API ExecuteStatement.
- Support API GetSecretValue.
- Support API ListDatabases.
- Support API ListSchemas.
- Support API ListSecrets.
- Support API ListTables.


2024-07-18 Version: 3.8.3
- Update API ListDocuments: add param MaxResults.
- Update API ListDocuments: add param NextToken.
- Update API ListDocuments: update response param.
- Update API QueryContent: add param IncludeFileUrl.


2024-07-03 Version: 3.8.2
- Update API DescribeDocument: update response param.


2024-06-27 Version: 3.8.1
- Update API DescribeStreamingDataService: update response param.
- Update API ListStreamingDataServices: update response param.


2024-05-28 Version: 3.8.0
- Support API BindDBResourceGroupWithRole.
- Support API CreateDBResourceGroup.
- Support API DeleteDBResourceGroup.
- Support API DescribeDBResourceGroup.
- Support API DescribeRoles.
- Support API DisableDBResourceGroup.
- Support API EnableDBResourceGroup.
- Support API ModifyDBResourceGroup.
- Support API PauseDataRedistribute.
- Support API ResumeDataRedistribute.
- Support API UnbindDBResourceGroupWithRole.


2024-05-17 Version: 3.7.0
- Support API CheckHadoopDataSource.
- Support API CheckHadoopNetConnection.
- Support API CheckJDBCSourceNetConnection.
- Support API CreateExtensions.
- Support API CreateExternalDataService.
- Support API CreateHadoopDataSource.
- Support API CreateJDBCDataSource.
- Support API CreateStreamingDataService.
- Support API CreateStreamingDataSource.
- Support API CreateStreamingJob.
- Support API DeleteExtension.
- Support API DeleteExternalDataService.
- Support API DeleteHadoopDataSource.
- Support API DeleteJDBCDataSource.
- Support API DeleteStreamingDataService.
- Support API DeleteStreamingDataSource.
- Support API DeleteStreamingJob.
- Support API DescribeExternalDataService.
- Support API DescribeHadoopClustersInSameNet.
- Support API DescribeHadoopConfigs.
- Support API DescribeHadoopDataSource.
- Support API DescribeJDBCDataSource.
- Support API DescribeStreamingDataService.
- Support API DescribeStreamingDataSource.
- Support API DescribeStreamingJob.
- Support API ListExternalDataServices.
- Support API ListExternalDataSources.
- Support API ListInstanceExtensions.
- Support API ListStreamingDataServices.
- Support API ListStreamingDataSources.
- Support API ListStreamingJobs.
- Support API ModifyExternalDataService.
- Support API ModifyHadoopDataSource.
- Support API ModifyJDBCDataSource.
- Support API ModifyStreamingDataService.
- Support API ModifyStreamingDataSource.
- Support API ModifyStreamingJob.
- Support API UpgradeExtensions.


2024-05-13 Version: 3.6.2
- Update API CreateDBInstance: update param SecurityIPList.


2024-05-11 Version: 3.6.1
- Generated python 2016-05-03 for gpdb.

2024-05-09 Version: 3.6.0
- Support API DescribeDBResourceManagementMode.


2024-04-29 Version: 3.5.4
- Update API QueryCollectionData: add param IncludeMetadataFields.
- Update API QueryCollectionData: add param Offset.
- Update API QueryCollectionData: add param OrderBy.
- Update API QueryCollectionData: update param HybridSearchArgs.
- Update API QueryCollectionData: update response param.
- Update API QueryContent: add param IncludeMetadataFields.


2024-04-22 Version: 3.5.3
- Update API DescribeSampleData: update response param.
- Update API QueryCollectionData: add param HybridSearch.
- Update API QueryCollectionData: add param HybridSearchArgs.
- Update API QueryContent: add param HybridSearch.
- Update API QueryContent: add param HybridSearchArgs.
- Update API QueryContent: add param IncludeVector.
- Update API QueryContent: add param RecallWindow.
- Update API QueryContent: add param RerankFactor.
- Update API QueryContent: update response param.


2024-02-19 Version: 3.5.2
- Update API DescribeSampleData: update response param.
- Update API QueryContent: add param IncludeVector.
- Update API QueryContent: add param RecallWindow.
- Update API QueryContent: add param RerankFactor.
- Update API QueryContent: update response param.


2024-01-18 Version: 3.5.1
- Generated python 2016-05-03 for gpdb.

2024-01-18 Version: 3.5.1
- Generated python 2016-05-03 for gpdb.

2024-01-18 Version: 3.5.0
- Generated python 2016-05-03 for gpdb.

2024-01-17 Version: 3.4.1
- Generated python 2016-05-03 for gpdb.

2024-01-10 Version: 3.4.0
- Generated python 2016-05-03 for gpdb.

2023-12-18 Version: 3.3.3
- Generated python 2016-05-03 for gpdb.

2023-12-11 Version: 3.3.2
- Generated python 2016-05-03 for gpdb.

2023-11-07 Version: 3.3.1
- Generated python 2016-05-03 for gpdb.

2023-11-06 Version: 3.3.0
- Generated python 2016-05-03 for gpdb.

2023-09-20 Version: 3.2.2
- Generated python 2016-05-03 for gpdb.

2023-09-18 Version: 3.2.1
- Generated python 2016-05-03 for gpdb.

2023-09-18 Version: 3.2.1
- Generated python 2016-05-03 for gpdb.

2023-09-18 Version: 3.2.1
- Generated python 2016-05-03 for gpdb.

2023-09-11 Version: 3.2.0
- Generated python 2016-05-03 for gpdb.

2023-08-18 Version: 3.1.0
- Generated python 2016-05-03 for gpdb.

2023-08-09 Version: 3.0.0
- Generated python 2016-05-03 for gpdb.

2023-08-02 Version: 2.0.2
- Add Cloud Disk Encryption.

2023-07-26 Version: 2.0.1
- Add Cloud Disk Encryption.

2023-07-10 Version: 2.0.0
- Add Cloud Disk Encryption.

2023-01-09 Version: 1.1.21
- Support Pause and Resume Instance.


2022-12-13 Version: 1.1.20
- Support describe cluster support features.


2022-12-12 Version: 1.1.19
- Support describe cluster support features.


2022-12-08 Version: 1.1.18
- Support describe cluster support features.


2022-11-02 Version: 1.1.16
- Support serverless v2


2022-09-26 Version: 1.1.15
- Support Openapi Tag.
- Support Tag Ram.


2022-09-14 Version: 1.1.14
- Support Openapi Tag.
- Support Tag Ram.


2022-09-05 Version: 1.1.13
- Support Resource Group.

2022-08-25 Version: 1.1.11
- Support diagnose instance.

2022-08-10 Version: 1.1.10
- Support diagnose instance.

2022-06-27 Version: 1.1.9
- Support diagnose instance.

2022-05-30 Version: 1.1.8
- Support rebalance instance.

2022-04-28 Version: 1.1.7
- Support upgrade instance.

2022-04-19 Version: 1.1.6
- Support set datashare.

2022-02-16 Version: 1.1.5
- Support set datashare.

2022-02-15 Version: 1.0.1
- AMP Version Change.

2021-09-15 Version: 1.0.0
- AMP version.

