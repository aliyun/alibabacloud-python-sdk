# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportRecordRequest(DaraModel):
    def __init__(
        self,
        export_file_type: str = None,
        export_type: str = None,
        lang: str = None,
        params: str = None,
        resource_directory_account_id: int = None,
    ):
        # The type of the file to export. Valid values:
        # - **virusScanExport**: The detail export of virus scan tasks. This parameter is required when ExportType is set to virusScanExport.
        self.export_file_type = export_file_type
        # The type of the detection result list to export. Valid values:
        # 
        # - **assetInstance**: The server list in Asset Center.
        # - **user**: The Asset Fingerprints list of accounts.
        # - **port**: The Asset Fingerprints list of ports.
        # - **process**: The Asset Fingerprints list of processes.
        # - **sca**: The Asset Fingerprints list of middleware.
        # - **database**: The Asset Fingerprints list of databases.
        # - **web**: The Asset Fingerprints list of web services.
        # - **software**: The Asset Fingerprints list of software.
        # - **cron**: The Asset Fingerprints list of scheduled nodes.
        # - **autorun**: The Asset Fingerprints list of startup items.
        # - **lkm**: The Asset Fingerprints list of kernel modules.
        # - **webserver**: The Asset Fingerprints list of websites.
        # - **virusScanExport**: The list of virus scan node details.
        # - **imageVulExport**: The image system vulnerability list.
        # - **imageBaseLineExport**: The image baseline check result list.
        # - **imageAffectedMaliciousExport**: The image malicious sample check result list.
        # - **baselineCspm**: The detection result list of cloud platform configuration checks.
        # - **attack**: The list of attack analysis alerting events.
        # - **attackEvent**: The list of network defense alerting events.
        # - **accessKey**: The list of AccessKey leak detection alerting events.
        # - **exportObjectScanEvents**: The list of malicious file detection alerting events.
        # - **domainDetail**: The website assets.
        # - **assetsPropertyScaProcessDetail**: The protected processes of Runtime Application Self-Protection (RASP).
        # - **exportHcWarning**: The system baseline risk list.
        # - **raspAttackAlert**: The list of RASP attack alerting.
        # - **raspApplicationConfiguration**: The list of RASP application configurations.
        # - **raspWeaknessDetection**: The list of RASP weakness detections.
        # - **raspInMemoryWebshellDetection**: The list of RASP in-memory webshell detection alerting.
        # - **raspInMemoryWebshellInsertion**: The list of RASP in-memory webshell injection alerting.
        # - **listAgentExport**: The agent list.
        # - **listSkillExport**: The skill list.
        # - **listModelExport**: The model list.
        # - **listAiAgentEventExport**: The AI agent risk list.
        # 
        # This parameter is required.
        self.export_type = export_type
        # Specifies the language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # Specifies the filter conditions for the exported content.
        # 
        # > - When **ExportType** is set to **assetInstance**, the JSON supports the following filter conditions:
        # >> - **MachineTypes**: the asset types. Separate multiple values with commas.
        # >> - **Criteria**: the combined filter conditions in JSON array format, such as `[{"name":"fieldName","value":"value"},...]`. If you specify multiple values for the same field, a multi-value filter is applied. Multiple conditions are combined by using the OR operator by default. Valid values for **name**:
        # >>> - **internetIp**: the public IP address.
        # >>> - **intranetIp**: the private IP address.
        # >>> - **instanceName**: the instance name.
        # >>> - **instanceId**: the instance ID.
        # >>> - **vpcInstanceId**: the VPC instance ID.
        # >>> - **machineType**: the asset type.
        # >>> - **osName**: the operating system name.
        # >>> - **osType**: the operating system type. Valid values:
        # >>>> - **linux**: Linux.
        # >>>> - **windows**: Windows.
        # >>> - **hcStatus**: the baseline risk status. Valid values:
        # >>>> - **NO**: No baseline risks.
        # >>>> - **YES**: Baseline risks exist.
        # >>> - **vulStatus**: the vulnerability risk status. Valid values:
        # >>>> - **NO**: No vulnerability risks.
        # >>>> - **YES**: Vulnerability risks exist.
        # >>> - **asapVulStatus**: the urgent vulnerability risk status. Valid values:
        # >>>> - **NO**: No urgent vulnerability risks.
        # >>>> - **YES**: Urgent vulnerability risks exist.
        # >>> - **alarmStatus**: the alert status. Valid values:
        # >>>> - **NO**: No alerts.
        # >>>> - **YES**: Alerts exist.
        # >>> - **riskStatus**: the overall risk status. Valid values:
        # >>>> - **NO**: No risks.
        # >>>> - **YES**: Risks exist.
        # >>>> - **UNKNOWN**: Unknown.
        # >>> - **clientStatus**: the client status. Valid values:
        # >>>> - **online**: Online.
        # >>>> - **offline**: Offline.
        # >>>> - **pause**: Paused.
        # >>> - **clientSubStatus**: the client sub-status. Valid values:
        # >>>> - **online**: Online.
        # >>>> - **offline**: Offline.
        # >>>> - **pause**: Paused.
        # >>>> - **stopped**: Stopped.
        # >>>> - **uninstalled**: Uninstalled.
        # >>> - **runningStatus**: the running status. Valid values:
        # >>>> - **Running**: Running.
        # >>>> - **notRunning**: Not running.
        # >>>> - **UNKNOWN**: Unknown.
        # >>> - **tagName**: the tag name.
        # >>> - **tagKeyValue**: the tag key-value pair.
        # >>> - **vendorAuthAlias**: the alias of the cloud service provider account.
        # >>> - **vendorUid**: the UID of the cloud service provider account.
        # >>> - **vendorUserName**: the name of the cloud service provider account.
        # >>> - **clusterId**: the cluster ID.
        # >>> - **clusterIdList**: the cluster IDs. Separate multiple IDs with commas.
        # >>> - **namespace**: the namespace.
        # >>> - **appName**: the application name.
        # >>> - **serviceId**: the service ID in the container dimension.
        # >>> - **clusterNodeStatus**: the cluster node status. Valid values:
        # >>>> - **true**: The asset is a cluster node.
        # >>>> - **false**: The asset is not a cluster node.
        # >>> - **groupName**: the asset group name.
        # >>> - **groupId**: the asset group ID.
        # >>> - **regionId**: the region ID.
        # >>> - **importance**: the importance level. Valid values:
        # >>>> - **important**: Important asset.
        # >>>> - **general**: General asset.
        # >>>> - **test**: Test asset.
        # >>> - **newInstance**: the identifier for newly added assets. Valid values:
        # >>>> - **NO**: Not a newly added asset.
        # >>>> - **YES**: Newly added asset.
        # >>> - **containerStatus**: the container status. Valid values:
        # >>>> - **NO**: No containers.
        # >>>> - **YES**: Containers exist.
        # >>> - **exposedStatus**: the exposure status. Valid values:
        # >>>> - **NO**: Not exposed.
        # >>>> - **YES**: Exposed.
        # >>> - **aiStatus**: the AI asset status. Valid values:
        # >>>> - **true**: AI asset.
        # >>>> - **false**: Non-AI asset.
        # >>> - **authVersion**: the client version. Valid values:
        # >>>> - **1**: Free Edition.
        # >>>> - **3**: Enterprise Edition.
        # >>>> - **5**: Advanced Edition.
        # >>>> - **6**: Anti-virus Edition.
        # >>>> - **7**: Ultimate Edition.
        # >>> - **ipList**: the IP addresses. Separate multiple IP addresses with commas.
        # >>> - **uuidList**: the asset UUIDs.
        # >>> - **ecsType**: the instance type.
        # >>> - **alisecguardStatus**: the status of the protection plugin. Valid values:
        # >>>> - **0**: Online.
        # >>>> - **1**: Disabled.
        # >>>> - **2**: Offline.
        # >>>> - **-99**: Installation failed.
        # >>> - **alihipsStatus**: the status of the host intrusion prevention plugin. Valid values:
        # >>>> - **0**: Online.
        # >>>> - **1**: Disabled.
        # >>>> - **2**: Offline.
        # >>>> - **-99**: Installation failed.
        # >>> - **alinetStatus**: the status of the network protection plugin. Valid values:
        # >>>> - **0**: Online.
        # >>>> - **1**: Disabled.
        # >>>> - **2**: Offline.
        # >>>> - **-99**: Installation failed.
        # >>> - **alidetStatus**: the status of the detection plugin. Valid values:
        # >>>> - **0**: Online.
        # >>>> - **1**: Disabled.
        # >>>> - **2**: Offline.
        # >>>> - **-99**: Installation failed.
        # >>> - **yundunMonitorStatus**: the status of the monitoring plugin. Valid values:
        # >>>> - **0**: Online.
        # >>>> - **1**: Disabled.
        # >>>> - **2**: Offline.
        # >>>> - **-99**: Installation failed.
        # >> - **Importance**: the importance level.
        # >> - **LogicalExp**: the logical operator used to combine multiple conditions. Valid values:
        # >>> - **AND**: All conditions must be met.
        # >>> - **OR**: Any condition is met. This is the default value.
        # > - When **ExportType** is set to **user**, the JSON supports the following filter conditions:
        # >> - **User**: the account name.
        # >> - **IsRoot**: specifies whether the account has root permissions. Valid values:
        # >>> - **1**: Yes.
        # >>> - **2**: No.
        # >> - **LastLoginTimeStart**: the start time of the query range for the last logon time. Unit: milliseconds.
        # >> - **LastLoginTimeEnd**: the end time of the query range for the last logon time. Unit: milliseconds.
        # >> - **uuid**: the asset UUIDs. Separate multiple UUIDs with commas.
        # >> - **remark**: the remarks. This parameter matches the server name, public IP address, and private IP address at the same time.
        # > - When **ExportType** is set to **port**, the JSON supports the following filter conditions:
        # >> - **port**: the port number.
        # >> - **procName**: the process name.
        # >> - **bindIp**: the bound IP address.
        # >> - **remark**: the remarks. This parameter matches the server name, public IP address, and private IP address at the same time.
        # > - When **ExportType** is set to **process**, the JSON supports the following filter conditions:
        # >> - **name**: the process name.
        # >> - **user**: the user that runs the process.
        # >> - **cmdline**: the command line.
        # >> - **procTimeStart**: the start time of the query range for the process startup time. Unit: milliseconds.
        # >> - **procTimeEnd**: the end time of the query range for the process startup time. Unit: milliseconds.
        # >> - **uuid**: the asset UUIDs. Separate multiple UUIDs with commas. Only the data of the specified assets is exported.
        # >> - **remark**: the remarks. This parameter matches the server name, public IP address, and private IP address at the same time.
        # > - When **ExportType** is set to **sca**, the JSON supports the following filter conditions:
        # >> - **scaName**: the middleware name.
        # >> - **scaVersion**: the middleware version.
        # >> - **port**: the port.
        # >> - **pid**: the process ID.
        # >> - **user**: the user.
        # >> - **processStartedStart**: the start time of the query range for the process startup time. Unit: milliseconds.
        # >> - **processStartedEnd**: the end time of the query range for the process startup time. Unit: milliseconds.
        # >> - **searchItem**: the search field name. This parameter is used together with **searchInfo** to specify the field by which to search. Valid values:
        # >>> - **name**: searches by component name. In this case, set **searchInfo** to the component name.
        # >>> - **type**: searches by component type. In this case, set **searchInfo** to the component type.
        # >> - **searchInfo**: the search value. This parameter is used together with **searchItem**.
        # >> - **uuid**: the asset UUIDs. Separate multiple UUIDs with commas. Only the data of the specified assets is exported.
        # >> - **remark**: the remarks. This parameter matches the server name, public IP address, and private IP address at the same time.
        # > - When **ExportType** is set to **database**, the JSON supports the following filter conditions:
        # >> - **port**: the port.
        # >> - **pid**: the process ID.
        # >> - **user**: the user.
        # >> - **ScaVersion**: the version.
        # >> - **processStartedStart**: the start time of the query range for the process startup time. Unit: milliseconds.
        # >> - **processStartedEnd**: the end time of the query range for the process startup time. Unit: milliseconds.
        # >> - **searchItem**: the search field name. This parameter is used together with **searchInfo** to specify the field by which to search. Valid values:
        # >>> - **name**: searches by database name. In this case, set **searchInfo** to the component name.
        # >> - **searchInfo**: the search value. This parameter is used together with **searchItem**.
        # >> - **uuid**: the asset UUIDs. Separate multiple UUIDs with commas. Only the data of the specified assets is exported.
        # >> - **remark**: the remarks. This parameter matches the server name, public IP address, and private IP address at the same time.
        # > - When **ExportType** is set to **web**, the JSON supports the following filter conditions:
        # >> - **scaName**: the web service name.
        # >> - **scaNamePattern**: the component name for fuzzy search.
        # >> - **scaVersion**: the version.
        # >> - **bizType**: the type. Set the value to **sca_web**.
        # >> - **port**: the port.
        # >> - **pid**: the process ID.
        # >> - **user**: the user.
        # >> - **processStartedStart**: the start time of the query range for the process startup time. Unit: milliseconds.
        # >> - **processStartedEnd**: the end time of the query range for the process startup time. Unit: milliseconds.
        # >> - **searchItem**: the search field name. This parameter is used together with **searchInfo** to specify the field by which to search. Valid values:
        # >>> - **name**: searches by component name. In this case, set **searchInfo** to the component name.
        # >>> - **type**: searches by component type. In this case, set **searchInfo** to the component type.
        # >> - **searchInfo**: the search value. This parameter is used together with **searchItem**.
        # >> - **uuid**: the asset UUIDs. Separate multiple UUIDs with commas. Only the data of the specified assets is exported.
        # >> - **remark**: the remarks. This parameter matches the server name, public IP address, and private IP address at the same time.
        # > - When **ExportType** is set to **software**, the JSON supports the following filter conditions:
        # >> - **name**: the software name.
        # >> - **softwareVersion**: the version.
        # >> - **path**: the software startup path.
        # >> - **installTimeStart**: the start time of the query range for the software update time. Unit: milliseconds.
        # >> - **installTimeEnd**: the end time of the query range for the software update time. Unit: milliseconds.
        # >> - **uuid**: the asset UUIDs. Separate multiple UUIDs with commas. Only the data of the specified assets is exported.
        # >> - **remark**: the remarks. This parameter matches the server name, public IP address, and private IP address at the same time.
        # > - When **ExportType** is set to **cron**, the JSON supports the following filter conditions:
        # >> - **source**: the task path.
        # >> - **user**: the account name.
        # >> - **uuid**: the asset UUIDs. Separate multiple UUIDs with commas. Only the data of the specified assets is exported.
        # >> - **remark**: the remarks. This parameter matches the server name, public IP address, and private IP address at the same time.
        # > - When **ExportType** is set to **autorun**, the JSON supports the following filter conditions:
        # >> - **itemName**: the startup item path.
        # >> - **uuid**: the asset UUIDs. Separate multiple UUIDs with commas. Only the data of the specified assets is exported.
        # >> - **remark**: the remarks. This parameter matches the server name, public IP address, and private IP address at the same time.
        # > - When **ExportType** is set to **lkm**, the JSON supports the following filter conditions:
        # >> - **itemName**: the kernel module name.
        # >> - **uuid**: the asset UUIDs. Separate multiple UUIDs with commas. Only the data of the specified assets is exported.
        # >> - **remark**: the remarks. This parameter matches the server name, public IP address, and private IP address at the same time.
        # > - When **ExportType** is set to **webserver**, the JSON supports the following filter conditions:
        # >> - **itemName**: the site domain name.
        # >> - **uuid**: the asset UUIDs. Separate multiple UUIDs with commas. Only the data of the specified assets is exported.
        # >> - **remark**: the remarks. This parameter matches the server name, public IP address, and private IP address at the same time.
        # > - When **ExportType** is set to **virusScanExport**, the JSON supports the following filter conditions:
        # >> - **status**: the scan task status. Valid values:
        # >>> - **INIT**: Pending.
        # >>> - **START**: Started.
        # >>> - **DISTRIBUTE**: Dispatched.
        # >>> - **PROCESSING**: In progress.
        # >>> - **BEGIN**: Begun.
        # >>> - **SUCCESS**: Completed.
        # >>> - **FAIL**: Failed.
        # >>> - **TIMEOUT**: Timed out.
        # > - When **ExportType** is set to **imageVulExport**, the JSON supports the following filter conditions:
        # >> - **Type**: the vulnerability type. Valid values:
        # >>> - **cve**: CVE vulnerability.
        # >>> - **sca**: SCA vulnerability (Software Composition Analysis vulnerability).
        # >> - **aliasName**: the alias of the vulnerability name.
        # >> - **Necessity**: the vulnerability priority. Valid values:
        # >>> - **asap**: High.
        # >>> - **later**: Medium.
        # >>> - **nntf**: Low.
        # >> - **Dealed**: the handling status. Valid values:
        # >>> - **y**: Handled.
        # >>> - **n**: Unhandled.
        # >> - **RepoInstanceId**: the image repository instance ID.
        # >> - **RepoName**: the image repository name.
        # >> - **RepoNamespace**: the image repository namespace.
        # >> - **Uuids**: the asset UUIDs. Separate multiple UUIDs with commas.
        # >> - **ScanRange**: the scan scope. Valid values:
        # >>> - **image**: Image scan.
        # >>> - **container**: Container runtime image scan.
        # >> - **IsLatest**: specifies whether to export only the latest image versions. Valid values:
        # >>> - **true**: Exports only the latest image versions.
        # >>> - **false**: No limit.
        # > - When **ExportType** is set to **imageBaseLineExport**, the JSON supports the following filter conditions:
        # >> - **scanRange**: the scan scope. Valid values:
        # >>> - **image**: Image scan.
        # >>> - **container**: Container runtime image scan.
        # >> - **CriteriaType**: the combined condition type. This parameter is used together with **Criteria**. Valid values:
        # >>> - **BaselineNameAlias**: filters by baseline name. In this case, set **Criteria** to the baseline name.
        # >>> - **BaselineClassAlias**: filters by baseline category. In this case, set **Criteria** to the baseline category name.
        # >> - **Criteria**: the value of the combined condition. This parameter is used together with **CriteriaType**.
        # >> - **RiskLevel**: the risk level. Valid values:
        # >>> - **high**: High.
        # >>> - **medium**: Medium.
        # >>> - **low**: Low.
        # >> - **BaselineNameKey**: the baseline name.
        # >> - **RepoInstanceId**: the image repository instance ID.
        # >> - **RepoName**: the image repository name.
        # >> - **RepoNamespace**: the image repository namespace.
        # >> - **RepoRegionId**: the region of the image repository.
        # >> - **ImageDigest**: the image digest.
        # >> - **ImageTag**: the image tag.
        # >> - **ImageUuid**: the image asset UUID.
        # > - When **ExportType** is set to **imageAffectedMaliciousExport**, the JSON supports the following filter conditions:
        # >> - **Levels**: the risk levels. Separate multiple levels with commas. Valid values:
        # >>> - **serious**: Urgent.
        # >>> - **suspicious**: Suspicious.
        # >>> - **remind**: Reminder.
        # >> - **MaliciousMd5**: the MD5 hash of the malicious sample.
        # >> - **FuzzyMaliciousName**: the name of the malicious sample for fuzzy search.
        # >> - **RepoInstanceId**: the image repository instance ID.
        # >> - **RepoNamespace**: the image repository namespace.
        # >> - **RepoName**: the image repository name.
        # >> - **ImageDigest**: the image digest.
        # >> - **ScanRange**: the scan scope. Valid values:
        # >>> - **image**: Image scan.
        # >>> - **container**: Container runtime image scan.
        # > - When **ExportType** is set to **baselineCspm**, the JSON supports the following filter conditions:
        # >> - **CheckKey**: the check item name.
        # >> - **Statuses**: the check result statuses. The value is a JSON array. Valid values:
        # >>> - **PASS**: Passed.
        # >>> - **NOT_PASS**: Failed.
        # >>> - **CHECKING**: Checking.
        # >>> - **NOT_CHECK**: Not checked.
        # >>> - **WHITELIST**: Whitelisted.
        # >>> - **FAILED**: Check failed.
        # >> - **RiskLevels**: the risk levels. The value is a JSON array. Valid values:
        # >>> - **HIGH**: High.
        # >>> - **MEDIUM**: Medium.
        # >>> - **LOW**: Low.
        # >> - **OperationTypes**: specifies whether fixing is supported. The value is a JSON array. Valid values:
        # >>> - **SUPPORT_REPAIR**: Supported.
        # >>> - **NOT_SUPPORT_REPAIR**: Not supported.
        # >> - **Vendors**: the cloud service providers. The value is a JSON array. Valid values:
        # >>> - **ALIYUN**: Alibaba Cloud.
        # >>> - **AWS**: Amazon Web Services (AWS).
        # >>> - **MICROSOFT**: Microsoft Azure.
        # >>> - **HUAWEICLOUD**: Huawei Cloud.
        # >>> - **TENCENT**: Tencent Cloud.
        # >>> - **VOLCENGINE**: Volcengine.
        # >>> - **GOOGLE**: Google Cloud.
        # >>> - **STATECLOUD**: Tianyi Cloud.
        # >>> - **BAIDUCLOUD**: Baidu Cloud.
        # >>> - **UCLOUD**: UCloud.
        # >>> - **KINGSOFTCLOUD**: Kingsoft Cloud.
        # >>> - **ORACLECLOUD**: Oracle Cloud.
        # >>> - **KSPM**: Other (Kubernetes).
        # >> - **InstanceTypes**: the asset types. The value is a JSON array.
        # >> - **InstanceSubTypes**: the asset subtypes. The value is a JSON array.
        # >> - **InstanceIds**: the asset instance IDs. The value is a JSON array.
        # >> - **CheckIds**: the check item IDs. The value is a JSON array. You can specify up to 500 IDs.
        # >> - **CheckTypes**: the check types. The value is a JSON array. Valid values:
        # >>> - **CUSTOM**: Custom.
        # >>> - **SYSTEM**: Predefined.
        # >> - **StandardIds**: the compliance standard IDs. The value is a JSON array.
        # >> - **RequirementIds**: the compliance requirement IDs. The value is a JSON array.
        # >> - **CustomParam**: specifies whether custom parameters are supported. Valid values:
        # >>> - **true**: Yes.
        # >>> - **false**: No.
        # > - When **ExportType** is set to **attack**, the JSON supports the following filter conditions:
        # >> - **Type**: the attack analysis data type. Exact match. Valid values:
        # >>> - **TOTAL**: Total attack statistics.
        # >>> - **TREND**: Attack trend data.
        # >>> - **PIE_CHART**: Attack type distribution data.
        # >>> - **SOURCE_TOP**: Top source IP addresses of attacks.
        # >>> - **CLIENT_TOP**: Top attacked assets.
        # >>> - **DETAILS**: Attack details (paginated). Used when exporting the detail list.
        # >>> - **ATTACK_SCREEN**: Attack dashboard data.
        # >>> - **GC_LEVEL**: Security level data.
        # >> - **StartTime**: the start time of the query range for the attack time. Unit: milliseconds.
        # >> - **EndTime**: the end time of the query range for the attack time. Unit: milliseconds.
        # >> - **Data**: the data payload, which can be a JSON string or an encoded string.
        # >> - **Base64**: specifies whether to decode the **Data** parameter. Valid values:
        # >>> - **true**: Decodes the **Data** parameter by using Base64.
        # >>> - **false**: Does not decode the **Data** parameter.
        # > - When **ExportType** is set to **attackEvent**, the JSON supports the following filter conditions:
        # >> - **AttackType**: the attack type. Valid values:
        # >>> - **9**: SQL Server brute-force attack.
        # >>> - **5**: SSH brute-force attack.
        # >>> - **6**: RDP brute-force attack.
        # >>> - **101**: Java Struts2 attack interception.
        # >>> - **102**: Redis attack interception.
        # >>> - **103**: AntSword web shell communication.
        # >>> - **104**: Chopper web shell communication.
        # >>> - **133**: XISE web shell communication.
        # >>> - **161**: Web shell upload.
        # >>> - **209**: PHP web shell upload.
        # >>> - **210**: JSP web shell upload.
        # >>> - **211**: ASP web shell upload.
        # >>> - **215**: Web shell upload with a special extension.
        # >>> - **ai_webshell**: Intelligent defense against web shell upload.
        # >>> - **java_common_rce**: Interception of common Java RCE vulnerabilities.
        # >>> - **alinet_webrce**: Adaptive web attack defense.
        # >> - **StartTime**: the start time of the query range for the attack time. Unit: milliseconds.
        # >> - **EndTime**: the end time of the query range for the attack time. Unit: milliseconds.
        # >> - **AttackInstance**: the attacked asset. This parameter matches the server name, public IP address, and private IP address at the same time.
        # >> - **SrcIp**: the source IP address of the attack.
        # >> - **RemoteIp**: the actual source IP address.
        # >> - **DstPort**: the destination port.
        # > - When **ExportType** is set to **accessKey**, the JSON supports the following filter conditions:
        # >> - **Status**: the handling status. Valid values:
        # >>> - **dealed**: Handled.
        # >>> - **pending**: Unhandled.
        # >> - **Query**: the AccessKey ID.
        # > - When **ExportType** is set to **exportObjectScanEvents**, the JSON supports the following filter conditions:
        # >> - **AiDetect**: specifies whether the event is detected by AI. Valid values:
        # >>> - **true**: Yes.
        # >>> - **false**: No.
        # >> - **RiskLevel**: the risk level. Valid values:
        # >>> - **high**: High.
        # >>> - **medium**: Medium.
        # >>> - **low**: Low.
        # >> - **Status**: the status. Valid values:
        # >>> - **0**: Unhandled.
        # >>> - **1**: Manually handled.
        # >>> - **2**: Whitelisted.
        # >>> - **3**: Ignored.
        # >>> - **4**: Access denied.
        # >> - **TimeStart**: the start time of the query range for the latest detection time. Unit: milliseconds.
        # >> - **TimeEnd**: the end time of the query range for the latest detection time. Unit: milliseconds.
        # >> - **EventName**: the threat tag.
        # >> - **Md5**: the MD5 hash of the file.
        # >> - **OssKey**: the file name.
        # > - When **ExportType** is set to **domainDetail**, the JSON supports the following filter conditions:
        # >> - **fuzzyDomain**: the domain name for fuzzy search.
        # >> - **domainType**: the domain name type. Valid values:
        # >>> - **root**: Root domain name.
        # >>> - **sub**: Subdomain name.
        # > - When **ExportType** is set to **exportHcWarning**, the JSON supports the following filter conditions:
        # >> - **CheckWarningStatusList**: the status list. The value is a JSON array. Valid values:
        # >>> - **1**: Failed.
        # >>> - **3**: Passed.
        # >>> - **6**: Whitelisted.
        # >>> - **8**: Fixed.
        # >> - **UuidList**: the asset UUIDs. The value is a JSON array.
        # >> - **CheckLevel**: the risk level. Valid values:
        # >>> - **high**: High.
        # >>> - **medium**: Medium.
        # >>> - **low**: Low.
        # >> - **Source**: the source. Set the value to **default**.
        # >> - **RiskType**: the risk type. Valid values:
        # >>> - **hc_custom**: Custom baseline.
        # >>> - **cis**: CIS benchmarks.
        # >>> - **hc_exploit**: Unauthorized access.
        # >>> - **hc_djbh**: Classified protection compliance.
        # >>> - **weak_password**: Weak password.
        # >>> - **hw_security**: Basic protection security practices.
        # >>> - **hc_container**: Container security.
        # >>> - **hc_best_secruity**: Best security practices.
        # >> - **RiskName**: the baseline name.
        # >> - **CheckItemFuzzy**: the check item name for fuzzy search.
        # >> - **CleartextPwd**: the export method for weak password baseline check results. Valid values:
        # >>> - **0**: Exports weak passwords after data masking.
        # >>> - **1**: Exports weak passwords in plaintext.
        # >> - **StrategyId**: the policy ID.
        # >> - **GroupId**: the asset group ID.
        # > - When **ExportType** is set to **assetsPropertyScaProcessDetail**, the JSON supports the following filter conditions:
        # >> - **uuid**: the asset UUID.
        # >> - **pid**: the process ID.
        # >> - **remark**: the remarks. This parameter matches the server name, public IP address, and private IP address at the same time.
        # >> - **cmdline**: the command line.
        # >> - **bizType**: the component type.
        # > - When **ExportType** is set to **raspAttackAlert**, the JSON supports the following filter conditions:
        # >> - **day**: the number of days to query. If this parameter is empty, the query is based on the specified time range. Valid values:
        # >>> - **0**: Today.
        # >>> - **7**: Last 7 days.
        # >>> - **30**: Last 30 days.
        # >> - **StartTimestamp**: the start time. Unit: milliseconds.
        # >> - **EndTimestamp**: the end time. Unit: milliseconds.
        # >> - **Severity**: the severity level. Valid values:
        # >>> - **high**: High.
        # >>> - **medium**: Medium.
        # >>> - **low**: Low.
        # >> - **HandlerType**: the handling action. Valid values:
        # >>> - **monitor**: Monitor.
        # >>> - **block**: Block.
        # >> - **HandleStatus**: the handling status. Valid values:
        # >>> - **0**: Unhandled.
        # >>> - **1**: Handled.
        # >> - **AttackUrl**: the request URL.
        # >> - **Hostname**: the hostname.
        # >> - **Remote**: the attacker IP address.
        # >> - **Pid**: the process ID.
        # >> - **ApplicationId**: the application ID.
        # >> - **RaspType**: the application language. Valid values:
        # >>> - **java**: Java.
        # >>> - **php**: PHP.
        # >>> - **python**: Python.
        # >>> - **nodejs**: Node.js.
        # >> - **AttackType**: the attack type. Valid values:
        # >>> - **file_read**: Arbitrary file read.
        # >>> - **sql**: SQL injection.
        # >>> - **xxe**: XXE.
        # >>> - **ssrf**: SSRF.
        # >>> - **rce**: Remote command execution.
        # >>> - **file**: Malicious file read and write.
        # >>> - **thread_inject**: Thread injection.
        # >>> - **file_upload**: Malicious file upload.
        # >>> - **file_list**: Directory traversal.
        # >>> - **memory_shell**: In-memory webshell injection.
        # >>> - **jni**: JNI injection.
        # >>> - **dns**: Malicious DNS query.
        # >>> - **reflect**: Malicious reflection call.
        # >>> - **file_delete**: Arbitrary file deletion.
        # >>> - **jndi**: JNDI injection.
        # >>> - **read_object**: Deserialization attack.
        # >>> - **dangerous_protocol**: Dangerous protocol usage.
        # >>> - **attach**: Malicious attach.
        # >>> - **expression**: Expression injection.
        # >>> - **engine**: Engine injection.
        # >>> - **beans**: Malicious beans binding.
        # >>> - **classloader**: Malicious class loading.
        # >>> - **jstl**: JSTL arbitrary file inclusion.
        # >>> - **callable**: Callback function execution.
        # >>> - **unserialize**: Deserialization.
        # >>> - **include**: Malicious file inclusion.
        # >>> - **eval**: Arbitrary code execution.
        # >>> - **template**: Server-side template injection.
        # >>> - **process_binding**: Malicious process binding.
        # >>> - **fork**: Malicious process creation.
        # >>> - **file_link**: Malicious file link.
        # >>> - **file_write**: Arbitrary file write.
        # > - When **ExportType** is set to **raspApplicationConfiguration**, the JSON supports the following filter conditions:
        # >> - **ProtectionSwitch**: the protection switch. Valid values:
        # >>> - **true**: Enabled.
        # >>> - **false**: Disabled.
        # >> - **RaspType**: the application language. Valid values:
        # >>> - **java**: Java.
        # >>> - **php**: PHP.
        # >>> - **python**: Python.
        # >>> - **nodejs**: Node.js.
        # >> - **ProtectionMode**: the protection mode. Valid values:
        # >>> - **monitor**: Monitor.
        # >>> - **block**: Block.
        # >> - **ApplicationName**: the application group name.
        # >> - **SortField**: the sort field. Valid values:
        # >>> - **authorizedProcess**: Authorized processes.
        # >>> - **accessedProcess**: Connected processes.
        # >> - **SortOrder**: the sort order. Valid values:
        # >>> - **desc**: Descending.
        # >>> - **asc**: Ascending.
        # > - When **ExportType** is set to **raspWeaknessDetection**, the JSON supports the following filter conditions:
        # >> - **day**: the number of days to query. If this parameter is empty, the query is based on the specified time range. Valid values:
        # >>> - **0**: Today.
        # >>> - **7**: Last 7 days.
        # >>> - **30**: Last 30 days.
        # >> - **StartTimestamp**: the start time of the check time range. Unit: milliseconds.
        # >> - **EndTimestamp**: the end time of the check time range. Unit: milliseconds.
        # >> - **CheckState**: the status. Valid values:
        # >>> - **0**: To be confirmed.
        # >>> - **1**: Confirmed.
        # >>> - **2**: False positive.
        # >>> - **3**: Ignored.
        # >> - **Severity**: the risk level. Valid values:
        # >>> - **high**: High.
        # >>> - **medium**: Medium.
        # >>> - **low**: Low.
        # >> - **Type**: the weakness type. Valid values:
        # >>> - **fastjson**: Insecure Fastjson configuration.
        # >>> - **jmx_config**: Insecure JMX configuration.
        # >>> - **jndi_config**: Insecure JNDI configuration.
        # >>> - **log4j**: Insecure Log4j component.
        # >>> - **rhino_config**: Insecure Rhino configuration.
        # >>> - **risk_start_up_param**: Insecure startup parameters.
        # >>> - **shiro**: Weak Shiro key.
        # >>> - **spring_config**: Insecure Spring configuration.
        # >>> - **weak_auth**: Weak server-side password.
        # >>> - **xml_config**: Insecure XML configuration.
        # >>> - **sql_connection**: Weak database password.
        # >> - **ApplicationId**: the application ID.
        # > - When **ExportType** is set to **raspInMemoryWebshellDetection**, the JSON supports the following filter conditions:
        # >> - **day**: the number of days to query. If this parameter is empty, the query is based on the specified time range. Valid values:
        # >>> - **0**: Today.
        # >>> - **7**: Last 7 days.
        # >>> - **30**: Last 30 days.
        # >> - **StartTimestamp**: the start time of the check time range. Unit: milliseconds.
        # >> - **EndTimestamp**: the end time of the check time range. Unit: milliseconds.
        # >> - **HandlerType**: the handling action. Valid values:
        # >>> - **monitor**: Monitor.
        # >>> - **block**: Block.
        # >> - **ApplicationId**: the application ID.
        # >> - **Confidence**: the confidence level. Valid values:
        # >>> - **high**: High.
        # >>> - **medium**: Medium.
        # >>> - **low**: Low.
        # >> - **HandleStatus**: the handling status. Valid values:
        # >>> - **0**: Unhandled.
        # >>> - **1**: Automatically handled.
        # >>> - **2**: Manually handled.
        # >>> - **3**: Ignored.
        # >>> - **4**: False positive.
        # >> - **ClassName**: the class name.
        # > - When **ExportType** is set to **raspInMemoryWebshellInsertion**, the JSON supports the following filter conditions:
        # >> - **day**: the number of days to query. If this parameter is empty, the query is based on the specified time range. Valid values:
        # >>> - **0**: Today.
        # >>> - **7**: Last 7 days.
        # >>> - **30**: Last 30 days.
        # >> - **StartTimestamp**: the start time of the check time range. Unit: milliseconds.
        # >> - **EndTimestamp**: the end time of the check time range. Unit: milliseconds.
        # >> - **HandlerType**: the handling action. Valid values:
        # >>> - **monitor**: Monitor.
        # >>> - **block**: Block.
        # >> - **ApplicationId**: the application ID.
        # >> - **Severity**: the attack severity level. Valid values:
        # >>> - **high**: High.
        # >>> - **medium**: Medium.
        # >>> - **low**: Low.
        # >> - **AttackUrl**: the request URL.
        # >> - **Hostname**: the hostname.
        # >> - **Remote**: the attacker IP address.
        # >> - **Pid**: the process ID.
        # >> - **RaspType**: the application language. Valid values:
        # >>> - **java**: Java.
        # >>> - **php**: PHP.
        # >>> - **python**: Python.
        # >>> - **nodejs**: Node.js.
        # > - When **ExportType** is set to **listAgentExport**, the JSON supports the following filter conditions:
        # >> - **Vendor**: the agent vendor. Set the value to the vendor type ID. Valid values:
        # >>> - **300**: Dify.
        # >>> - **301**: Alibaba Cloud Model Studio.
        # >>> - **302**: PAI.
        # >>> - **303**: Volcengine.
        # >>> - **304**: Agent Run.
        # >>> - **305**: OpenClaw.
        # >>> - **306**: ZeroClaw.
        # >>> - **307**: Hermes Agent.
        # >>> - **308**: QwenPaw.
        # >>> - **309**: CoPaw.
        # >>> - **310**: Gemini.
        # >>> - **311**: Claude.
        # >>> - **312**: CodeX.
        # >>> - **313**: OpenCode.
        # >>>
        self.params = params
        # The ID of the Alibaba Cloud account to which the member accounts in the resource folder belong.
        # > You can invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain the value of this parameter.
        self.resource_directory_account_id = resource_directory_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_file_type is not None:
            result['ExportFileType'] = self.export_file_type

        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.params is not None:
            result['Params'] = self.params

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportFileType') is not None:
            self.export_file_type = m.get('ExportFileType')

        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        return self

