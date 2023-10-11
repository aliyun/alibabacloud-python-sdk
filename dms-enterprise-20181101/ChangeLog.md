2023-10-11 Version: 1.55.1
- Generated python 2018-11-01 for dms-enterprise.

2023-09-28 Version: 1.55.0
- Generated python 2018-11-01 for dms-enterprise.

2023-09-21 Version: 1.54.0
- Generated python 2018-11-01 for dms-enterprise.

2023-08-24 Version: 1.53.2
- Generated python 2018-11-01 for dms-enterprise.

2023-08-24 Version: 1.53.2
- Generated python 2018-11-01 for dms-enterprise.

2023-08-10 Version: 1.53.1
- Generated python 2018-11-01 for dms-enterprise.

2023-07-12 Version: 1.53.0
- Change API CreateDataArchiveOrder and GetDataArchiveCount to public.

2023-07-06 Version: 1.52.0
- Modify GetDataArchiveOrderDetail API. Add output parameter: TempTableNameMap.

2023-06-30 Version: 1.51.0
- Modify ListTaskFlowsByPage API. Add output parameter: DagOwnerId.
- Modify ReRunTaskFlowInstance, ReSumeTaskFlowInstance: input parameter DagVersion is not required.

2023-05-25 Version: 1.50.0
- Support AnalyzeLineage API.
- Modify ListTaskFlowsByPage API. Add input parameters: DagIdList. Add output parameters: CronSwitch, CronStr, CronParam, TriggerType, CronType, TimeZoneId
- Modify BackFill API. Add output parameters DagInstanceId (same as the existed parameter NodeId).
- Modify ListTaskFlowInstance API. Add Input parameters: StartBizTime、EndBizTime.

2023-05-18 Version: 1.49.0
- Support GetDatabase, GetPhysicalDatabase to return InstanceAlias information.

2023-05-15 Version: 1.48.0
- Support SkipDataCorrectRowCheck API.

2023-04-27 Version: 1.47.0
- Support GetDataExportPreCheckDetail API.
- Modify GetOpLog API.

2023-04-24 Version: 1.46.0
- Supported GetDatabaseExportOrderDetail,CreateDatabaseExportOrder,CreateDataExportOrder API.
- Supported CreateDataTrackOrder,GetDataTrackJobDegree,GetDataTrackJobTableMeta,GetDataTrackOrderDetail,SearchDataTrackResult,DownloadDataTrackResult,QueryDataTrackResultDownloadStatus API.

2023-04-11 Version: 1.45.0
- Supported ListDataImportSQLPreCheckDetail,GetDataImportSQL,ListDataImportSQLType API.

2023-01-13 Version: 1.44.0
- Supported GetProxy, ListProxies to return RegionId information.
- Supported SearchDatabase to return CatalogName information.

2022-12-21 Version: 1.43.0
- Supported GetProxyAccess API.

2022-12-02 Version: 1.42.0
- Supported GetStructSyncOrderDetail OrderId param required.

2022-11-23 Version: 1.41.0
- Supported GetDataCronClearConfig,GetDataCorrectRollbackFile,GetOrderAttachmentFile API.

2022-10-28 Version: 1.40.0
- Support BuyPayAsYouGoOrder, RefundPayAsYouGoOrder, ListEffectiveOrders, ListClassificationTemplates.
- Modify RegisterInstance, UpdateInstance, ListInstances, GetInstance, GetApprovalDetail.

2022-07-27 Version: 1.38.0
- Support ListProxies API to return protocolType, protocolPort and remove mysqlPort.
- Support GetProxy API to return protocolType, protocolPort and remove mysqlPort.

2022-06-08 Version: 1.37.0
- Support GetDataCorrectOrderDetail API to return execMode type.
- Support CreateDataCorrectOrder, CreateFreeLockCorrectOrder API submit with execMode type.


2022-04-21 Version: 1.36.0
- Add API OfflineTaskFlow.

2022-04-15 Version: 1.35.0
- Rename the return of ListTaskFlow API.

2022-04-12 Version: 1.34.0
- Remove redundant input for API ListTaskFlow.

2022-04-06 Version: 1.33.0
- Support output dagName, dagOwnerId for api listTaskFlowAndScenario.
- Change output DbType to DwDbType for api GetLhSpaceByName.

2022-03-31 Version: 1.32.0
- Supported ListTaskFlow, ListTaskFlowInstance, GetTaskInstanceRelation, GetLhSpaceByName, DeleteLakeHouseSpace, DeleteTaskFlow API.

2022-03-24 Version: 1.31.0
- Supported CreateLakeHouseSpace,AddLhMembers,DeleteLhMembers,ListLhTaskFlowAndScenario,ChangeLhDagOwner,ReDeployLhDagVersion API.

2022-03-18 Version: 1.30.0
- Supported CreateStandardGroup, ListStandardGroups API.

2022-03-10 Version: 1.29.0
- Disabled Spark Job API.

2022-01-21 Version: 1.28.0
- Supported RestartDataCorrectSQLJob,PauseDataCorrectSQLJob API.
- Supported ListDataCorrectPreCheckSQL to return tableNames information.

2022-01-07 Version: 1.27.0
- Supported GetSparkJobDetail,GetSparkJobExecutorLogs,KillSparkJob,GetSparkJobDriverLog,GetSparkJobLog,SubmitSparkJob API.

2021-12-20 Version: 1.26.0
- Supported ListLogicDatabases to return Alias information.
- Supported ListDBTaskSQLJobDetail to return sql execute startTime and endTime information.

2021-11-29 Version: 1.25.0
- Supported ListLogicTableRouteConfig, AddLogicTableRouteConfig, DeleteLogicTableRouteConfig API.
- Supported ModifyDataCorrectExecSQL, RetryDataCorrectPreCheck API.
- Supported GetDBTaskSQLJobLog API.
- Supported ListDBTaskSQLJobDetail to return execute log information.

2021-11-18 Version: 1.24.0
- Support ListInstanceLoginAuditLog, ListProxySQLExecAuditLog API.
- Support GetOpLog API to return OpUserId information.

2021-11-04 Version: 1.23.0
- Support ListSQLExecAuditLog API.
- Support ListUsers, GetUser API to return information of Email, Webhook and DingRobot.
- Support GetApprovalDetail API to return information of CreateTime.

2021-10-25 Version: 1.22.0
- Support ListInstances and GetInstance API to return StandardGroup information.
- Support ListUserPermissions, GrantUserPermission, GrantUserPermission to operate instance permission.
- Support ChangeColumnSecLevel API.
- Support CreateLogicDatabase, EditLogicDatabase, DeleteLogicDatabase API.

2021-08-12 Version: 1.21.0
- Support CreateProxy, DeleteProxy, GetProxy, ListProxies, CreateProxyAccess, DeleteProxyAccess, ListProxyAccesses, InspectProxyAccessSecret Safety Protection Management APIs.

2021-07-06 Version: 1.20.0
- Support ListDataCorrectPreCheckDB,ListDataCorrectPreCheckSQL Order API.

2021-06-28 Version: 1.19.0
- Support GetSQLReviewOptimizeDetail,ListSQLReviewOriginSQL Order API.

2021-04-22 Version: 1.17.0
- Support GetPhysicalDatabase API.

2021-04-12 Version: 1.16.0
- Support GetDBTopology API.

2021-03-30 Version: 1.15.1
- Generated python 2018-11-01 for dms-enterprise.

2021-03-30 Version: 1.15.0
- Support ListDDLPublishRecords API.
- Fixed GetMetaTableColumn, GetMetaTableDetailInfo API response param DataLength lack of precision.

2021-03-10 Version: 1.14.0
- Support CreateDataCorrectOrder, CreateDataImportOrder, CreateFreeLockCorrectOrder, CreateDataCronClearOrder API.
- Support GetDataCorrectTaskDetail API.
- Support GetTableTopology API.
- Support CreateOrder API to apply order attachment.

2021-03-01 Version: 1.13.0
- Support TableStructSync Order API.
- Support Upload File API.
- Support GetOwnerApplyOrderDetail, GetPermApplyOrderDetail API.
- Support ListDBTaskSQLJob, ListDBTaskSQLJobDetail API.
- Support GetDataCorrectSQLFile API.

2020-12-30 Version: 1.0.0
- AMP Version Change.

