2025-12-24 Version: 4.0.0
- Delete API BatchModifyInstanceStatus.
- Delete API DescribeNodeUsedInfos.
- Delete API DescribePopApiItemList.
- Delete API ModifyPlaybookInstanceStatus.
- Delete API RenamePlaybookNode.
- Update API CreatePlaybook: add request parameters InputParams.
- Update API CreatePlaybook: add request parameters OutputParams.
- Update API DescribeComponentPlaybook: add response parameters Body.Playbooks.$.ParamType.
- Update API DescribePlaybooks: add response parameters Body.Playbooks.$.Description.
- Update API DescribePlaybooks: add response parameters Body.Playbooks.$.TenantId.
- Update API DescribePlaybooks: update request parameters Sort' type has changed.
- Update API DescribePlaybooks: update request parameters Sort' format has changed.
- Update API DescribePopApi: add response parameters Body.OpenApiMetaList.$.Style.
- Update API DescribePopApi: delete request parameters Env.
- Update API DescribeProcessTasks: add request parameters ReqUuid.
- Update API DescribeSoarRecords: add request parameters CompletedBeginTime.
- Update API DescribeSoarRecords: add request parameters CompletedEndTime.
- Update API DescribeSoarRecords: add request parameters QueryValue.
- Update API DescribeSoarRecords: add request parameters TriggerType.
- Update API DescribeSoarRecords: add response parameters Body.SoarExecuteRecords.$.OutputList.
- Update API DescribeSoarRecords: delete response parameters Body.SoarExecuteRecords.$.ResultMessage.
- Update API DescribeSoarRecords: delete response parameters Body.SoarExecuteRecords.$.TaskType.
- Update API DescribeSoarTaskAndActions: add request parameters PageNumber.
- Update API DescribeSoarTaskAndActions: add request parameters PageSize.
- Update API DescribeSoarTaskAndActions: add request parameters QueryType.
- Update API DescribeSoarTaskAndActions: add request parameters QueryValue.
- Update API DescribeSoarTaskAndActions: add response parameters Body.Page.
- Update API DescribeSoarTaskAndActions: add response parameters Body.Details.ActionLogNum.
- Update API DescribeSoarTaskAndActions: delete response parameters Body.Details.Actions.$.RequestUuid.
- Update API DescribeSoarTaskAndActions: delete response parameters Body.Details.Actions.$.TaskName.
- Update API DescribeSoarTaskAndActions: delete response parameters Body.Details.Actions.$.TaskStatus.
- Update API DescribeSoarTaskAndActions: delete response parameters Body.Details.Actions.$.TriggerUser.
- Update API DescribeSoarTaskAndActions: delete response parameters Body.Details.ResultLevel.
- Update API DescribeSoarTaskAndActions: delete response parameters Body.Details.ResultMessage.
- Update API DescribeSoarTaskAndActions: delete response parameters Body.Details.TaskTenantId.
- Update API RunNotifyComponentWithEmail: update request parameters AssetId' type has changed.
- Update API RunNotifyComponentWithEmail: update request parameters AssetId' format has changed.
- Update API RunNotifyComponentWithMessageCenter: update request parameters AssetId' type has changed.
- Update API RunNotifyComponentWithMessageCenter: update request parameters AssetId' format has changed.
- Update API RunNotifyComponentWithWebhook: update request parameters AssetId' type has changed.
- Update API RunNotifyComponentWithWebhook: update request parameters AssetId' format has changed.
- Update API RunPython3Script: add request parameters PythonVersion.
- Update API VerifyPlaybook: add response parameters Body.Prerequisites.


2025-03-18 Version: 3.0.0
- Support API ConvertPlaybook.
- Support API CopyPlaybook.
- Support API DescribeGroupProductions.
- Support API DescribeNotifyTemplateList.
- Support API DescribeOpenApiInfo.
- Support API DescribeOpenApiList.
- Support API DescribeProcessStatistics.
- Support API DescribeVendorApiList.
- Support API RunNotifyComponentWithEmail.
- Support API RunNotifyComponentWithMessageCenter.
- Support API RunNotifyComponentWithWebhook.
- Delete API DescribeApiList.
- Delete API DescribePopApiVersionList.
- Update API DescribePlaybook: update response param.
- Update API DescribePlaybooks: add param PlaybookUuids.
- Update API DescribePlaybooks: update param PageNumber.
- Update API DescribePlaybooks: update param PageSize.
- Update API DescribeProcessTasks: add param EventUuid.
- Update API DescribeProcessTasks: add param TriggerSource.
- Update API DescribeProcessTasks: update param PageNumber.
- Update API DescribeProcessTasks: update response param.
- Update API DescribeSoarRecords: add param RequestUuid.


2024-11-04 Version: 2.1.0
- Support API DescribeProcessTaskCount.


2024-11-02 Version: 2.0.1
- Update API CreatePlaybook: add param TaskflowType.
- Update API DescribeDistinctReleases: update response param.
- Update API DescribePlaybooks: add param Order.
- Update API DescribePlaybooks: add param ParamTypes.
- Update API DescribePlaybooks: add param Sort.
- Update API DescribePlaybooks: update response param.
- Update API DescribeProcessTasks: add param EntityUuid.
- Update API DescribeProcessTasks: update response param.


2024-06-28 Version: 2.0.0
- Update API CreatePlaybook: add param TaskflowType.
- Update API DescribeDistinctReleases: update response param.
- Update API DescribePlaybooks: add param Order.
- Update API DescribePlaybooks: add param Sort.
- Update API DescribePlaybooks: update response param.
- Update API DescribeProcessTasks: update response param.


2024-03-22 Version: 1.0.3
- Update API DescribeExecutePlaybooks: add param InputMode.
- Update API DescribePlaybook: update response param.
- Update API DescribePlaybookInputOutput: update response param.
- Update API DescribeProcessTasks: update response param.


2024-01-16 Version: 1.0.2
- Generated python 2022-07-28 for sophonsoar.

2023-12-07 Version: 1.0.1
- Generated python 2022-07-28 for sophonsoar.

2023-11-17 Version: 1.0.0
- Generated python 2022-07-28 for sophonsoar.

