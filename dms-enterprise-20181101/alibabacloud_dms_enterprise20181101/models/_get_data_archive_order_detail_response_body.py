# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetDataArchiveOrderDetailResponseBody(DaraModel):
    def __init__(
        self,
        data_archive_order_detail: main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetail = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The details of data archiving tickets.
        self.data_archive_order_detail = data_archive_order_detail
        # The error code returned if the call failed.
        self.error_code = error_code
        # The error message that is returned if the request failed.
        self.error_message = error_message
        # The ID of the request, which is used to query logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # Tracks service requests.
        self.trace_id = trace_id

    def validate(self):
        if self.data_archive_order_detail:
            self.data_archive_order_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_archive_order_detail is not None:
            result['DataArchiveOrderDetail'] = self.data_archive_order_detail.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataArchiveOrderDetail') is not None:
            temp_model = main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetail()
            self.data_archive_order_detail = temp_model.from_map(m.get('DataArchiveOrderDetail'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetail(DaraModel):
    def __init__(
        self,
        comment: str = None,
        committer: str = None,
        committer_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        plugin_extra_data: main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraData = None,
        plugin_param: main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginParam = None,
        plugin_type: str = None,
        related_user_list: List[int] = None,
        related_user_nick_list: List[str] = None,
        status_code: str = None,
        status_desc: str = None,
        workflow_instance_id: int = None,
        workflow_status_desc: str = None,
    ):
        # The description of the data archiving tickets.
        self.comment = comment
        # The user who submitted the ticket.
        self.committer = committer
        # The ID of the user who submitted the ticket. The ID is a user ID and not the ID of an Alibaba Cloud account.
        self.committer_id = committer_id
        # The time when the ticket was created.
        self.gmt_create = gmt_create
        # The time when the ticket was last modified.
        self.gmt_modified = gmt_modified
        # The ID of data archiving tickets.
        self.id = id
        # The additional information about the ticket.
        self.plugin_extra_data = plugin_extra_data
        # The ticket creation parameter. The value is a JSON string. For more information, see [PluginType parameter](https://help.aliyun.com/document_detail/429109.html).
        self.plugin_param = plugin_param
        # The plug-in type that corresponds to the type of the ticket. The plug-in type for data archiving is DATA_ARCHIVE. For more information, see [PluginType parameter](https://help.aliyun.com/document_detail/429109.html).
        self.plugin_type = plugin_type
        # The user IDs related to the ticket.
        self.related_user_list = related_user_list
        # The nicknames of the users that are related to the ticket.
        self.related_user_nick_list = related_user_nick_list
        # The status code of the ticket. Valid values:
        # 
        # *   **new**: newly created.
        # *   **toaudit**: being reviewed.
        # *   **Approved**: approved.
        # *   **reject**: rejected.
        # *   **processing**: being executed.
        # *   **Success**: successful.
        # *   **closed**: disabled.
        self.status_code = status_code
        # The status description of the ticket.
        self.status_desc = status_desc
        # The ID of the approval process. You can call the [GetOrderBaseInfo](https://help.aliyun.com/document_detail/144642.html) operation to obtain the ID of the approval process.
        self.workflow_instance_id = workflow_instance_id
        # The description of the approval process.
        self.workflow_status_desc = workflow_status_desc

    def validate(self):
        if self.plugin_extra_data:
            self.plugin_extra_data.validate()
        if self.plugin_param:
            self.plugin_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.committer is not None:
            result['Committer'] = self.committer

        if self.committer_id is not None:
            result['CommitterId'] = self.committer_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.plugin_extra_data is not None:
            result['PluginExtraData'] = self.plugin_extra_data.to_map()

        if self.plugin_param is not None:
            result['PluginParam'] = self.plugin_param.to_map()

        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type

        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list

        if self.related_user_nick_list is not None:
            result['RelatedUserNickList'] = self.related_user_nick_list

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id

        if self.workflow_status_desc is not None:
            result['WorkflowStatusDesc'] = self.workflow_status_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Committer') is not None:
            self.committer = m.get('Committer')

        if m.get('CommitterId') is not None:
            self.committer_id = m.get('CommitterId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PluginExtraData') is not None:
            temp_model = main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraData()
            self.plugin_extra_data = temp_model.from_map(m.get('PluginExtraData'))

        if m.get('PluginParam') is not None:
            temp_model = main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginParam()
            self.plugin_param = temp_model.from_map(m.get('PluginParam'))

        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')

        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')

        if m.get('RelatedUserNickList') is not None:
            self.related_user_nick_list = m.get('RelatedUserNickList')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')

        if m.get('WorkflowStatusDesc') is not None:
            self.workflow_status_desc = m.get('WorkflowStatusDesc')

        return self

class GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginParam(DaraModel):
    def __init__(
        self,
        archive_method: str = None,
        db_schema: str = None,
        logic: bool = None,
        order_after: List[str] = None,
        run_method: str = None,
        source_database_id: int = None,
        table_includes: List[main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginParamTableIncludes] = None,
        table_mapping: List[str] = None,
        target_instance_id: str = None,
        variables: List[str] = None,
    ):
        # The type of the archiving destination.
        self.archive_method = archive_method
        # The schema of the database and table to be archived.
        self.db_schema = db_schema
        # Indicates whether the database is logical.
        # 
        # *   **true**
        # *   **false**
        self.logic = logic
        # The post behavior of archiving.
        self.order_after = order_after
        # The running method, which indicates whether to run the task immediately or at a specific point in time.
        self.run_method = run_method
        # The ID of the source database.
        self.source_database_id = source_database_id
        # The list of the archived tables and the filter conditions.
        self.table_includes = table_includes
        # The mapping of schemas.
        self.table_mapping = table_mapping
        # The ID of the destination instance.
        self.target_instance_id = target_instance_id
        # The time variable defined for scheduled archiving.
        self.variables = variables

    def validate(self):
        if self.table_includes:
            for v1 in self.table_includes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_method is not None:
            result['ArchiveMethod'] = self.archive_method

        if self.db_schema is not None:
            result['DbSchema'] = self.db_schema

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.order_after is not None:
            result['OrderAfter'] = self.order_after

        if self.run_method is not None:
            result['RunMethod'] = self.run_method

        if self.source_database_id is not None:
            result['SourceDatabaseId'] = self.source_database_id

        result['TableIncludes'] = []
        if self.table_includes is not None:
            for k1 in self.table_includes:
                result['TableIncludes'].append(k1.to_map() if k1 else None)

        if self.table_mapping is not None:
            result['TableMapping'] = self.table_mapping

        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id

        if self.variables is not None:
            result['Variables'] = self.variables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveMethod') is not None:
            self.archive_method = m.get('ArchiveMethod')

        if m.get('DbSchema') is not None:
            self.db_schema = m.get('DbSchema')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('OrderAfter') is not None:
            self.order_after = m.get('OrderAfter')

        if m.get('RunMethod') is not None:
            self.run_method = m.get('RunMethod')

        if m.get('SourceDatabaseId') is not None:
            self.source_database_id = m.get('SourceDatabaseId')

        self.table_includes = []
        if m.get('TableIncludes') is not None:
            for k1 in m.get('TableIncludes'):
                temp_model = main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginParamTableIncludes()
                self.table_includes.append(temp_model.from_map(k1))

        if m.get('TableMapping') is not None:
            self.table_mapping = m.get('TableMapping')

        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')

        if m.get('Variables') is not None:
            self.variables = m.get('Variables')

        return self

class GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginParamTableIncludes(DaraModel):
    def __init__(
        self,
        table_name: str = None,
        table_where: str = None,
    ):
        # The table name.
        self.table_name = table_name
        # The filter condition.
        self.table_where = table_where

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_where is not None:
            result['TableWhere'] = self.table_where

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableWhere') is not None:
            self.table_where = m.get('TableWhere')

        return self

class GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraData(DaraModel):
    def __init__(
        self,
        dag_info: main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraDataDagInfo = None,
        db_base_info: main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraDataDbBaseInfo = None,
        instance_total: int = None,
        instances: List[main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraDataInstances] = None,
        next_fire_time_result: main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraDataNextFireTimeResult = None,
        page_index: int = None,
        page_size: int = None,
        temp_table_name_map: Dict[str, Any] = None,
    ):
        # The information about the workflow.
        self.dag_info = dag_info
        # The database information related to data archiving tickets.
        self.db_base_info = db_base_info
        # The total number of archiving tasks.
        self.instance_total = instance_total
        # The list of archiving tasks.
        self.instances = instances
        # The time when the next task is triggered.
        self.next_fire_time_result = next_fire_time_result
        # The page number.
        self.page_index = page_index
        # The number of entries per page.
        self.page_size = page_size
        # The name of the temporary table that is generated by the archiving task (indicated by the archiving task ID).
        self.temp_table_name_map = temp_table_name_map

    def validate(self):
        if self.dag_info:
            self.dag_info.validate()
        if self.db_base_info:
            self.db_base_info.validate()
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()
        if self.next_fire_time_result:
            self.next_fire_time_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_info is not None:
            result['DagInfo'] = self.dag_info.to_map()

        if self.db_base_info is not None:
            result['DbBaseInfo'] = self.db_base_info.to_map()

        if self.instance_total is not None:
            result['InstanceTotal'] = self.instance_total

        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.next_fire_time_result is not None:
            result['NextFireTimeResult'] = self.next_fire_time_result.to_map()

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.temp_table_name_map is not None:
            result['TempTableNameMap'] = self.temp_table_name_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagInfo') is not None:
            temp_model = main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraDataDagInfo()
            self.dag_info = temp_model.from_map(m.get('DagInfo'))

        if m.get('DbBaseInfo') is not None:
            temp_model = main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraDataDbBaseInfo()
            self.db_base_info = temp_model.from_map(m.get('DbBaseInfo'))

        if m.get('InstanceTotal') is not None:
            self.instance_total = m.get('InstanceTotal')

        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraDataInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('NextFireTimeResult') is not None:
            temp_model = main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraDataNextFireTimeResult()
            self.next_fire_time_result = temp_model.from_map(m.get('NextFireTimeResult'))

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TempTableNameMap') is not None:
            self.temp_table_name_map = m.get('TempTableNameMap')

        return self

class GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraDataNextFireTimeResult(DaraModel):
    def __init__(
        self,
        cron_fire_type: str = None,
    ):
        # The type of scheduled triggering.
        self.cron_fire_type = cron_fire_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_fire_type is not None:
            result['CronFireType'] = self.cron_fire_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronFireType') is not None:
            self.cron_fire_type = m.get('CronFireType')

        return self

class GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraDataInstances(DaraModel):
    def __init__(
        self,
        business_time: str = None,
        dag_id: int = None,
        end_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        history_dag_id: int = None,
        id: int = None,
        last_running_context: str = None,
        msg: str = None,
        status: int = None,
        tenant_id: str = None,
        trigger_type: int = None,
        version: str = None,
    ):
        # The business time of the task flow. The time is displayed in the yyyy-MM-DD HH:mm:ss format.
        self.business_time = business_time
        # The task flow ID. You can call the [ListTaskFlow](https://help.aliyun.com/document_detail/424565.html) or [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to obtain the value of this parameter.
        self.dag_id = dag_id
        # The time when the task flow ended. The time is displayed in the yyyy-MM-DD HH:mm:ss format.
        self.end_time = end_time
        # The time when the task flow was created.
        self.gmt_create = gmt_create
        # The time when the task flow was last modified.
        self.gmt_modified = gmt_modified
        # The ID of the historical task flow.
        self.history_dag_id = history_dag_id
        # The ID of the instance in the task flow that is executed.
        self.id = id
        # The context of the previous execution of the task flow.
        self.last_running_context = last_running_context
        # The context of the current execution of the task flow.
        self.msg = msg
        # The status of the task. Valid values:
        # 
        # *   **0**: The task is waiting for execution.
        # *   **1**: The task is in progress.
        # *   **2**: The task is suspended.
        # *   **3**: The task failed.
        # *   **4**: The task is successful.
        # *   **5**: The task is complete.
        self.status = status
        # The tenant ID.
        self.tenant_id = tenant_id
        # The mode in which the task flow was triggered. Valid values:
        # 
        # *   **0**: The task flow was triggered based on a schedule.
        # *   **1**: The task flow was manually triggered.
        self.trigger_type = trigger_type
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_time is not None:
            result['BusinessTime'] = self.business_time

        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.history_dag_id is not None:
            result['HistoryDagId'] = self.history_dag_id

        if self.id is not None:
            result['Id'] = self.id

        if self.last_running_context is not None:
            result['LastRunningContext'] = self.last_running_context

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessTime') is not None:
            self.business_time = m.get('BusinessTime')

        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('HistoryDagId') is not None:
            self.history_dag_id = m.get('HistoryDagId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastRunningContext') is not None:
            self.last_running_context = m.get('LastRunningContext')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraDataDbBaseInfo(DaraModel):
    def __init__(
        self,
        alias: str = None,
        alter_timeout: int = None,
        asset_control: bool = None,
        catalog_name: str = None,
        cluster_node: str = None,
        db_id: int = None,
        db_type: str = None,
        dba_id: int = None,
        dba_name: str = None,
        description: str = None,
        encoding: str = None,
        env_type: str = None,
        follow: bool = None,
        host: str = None,
        idc: str = None,
        idc_title: str = None,
        instance_id: int = None,
        instance_source: str = None,
        last_sync_time: str = None,
        level: str = None,
        logic: bool = None,
        owner_ids: List[int] = None,
        owner_names: List[str] = None,
        port: int = None,
        schema_name: str = None,
        search_name: str = None,
        standard_group: main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraDataDbBaseInfoStandardGroup = None,
        state: str = None,
        table_count: int = None,
        tns_name: str = None,
        unit_type: str = None,
    ):
        # The alias of the database instance.
        self.alias = alias
        # The timeout period of queries on the database.
        self.alter_timeout = alter_timeout
        # Indicates whether access control is enabled for data assets. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.asset_control = asset_control
        # The name of the instance in the instance list.
        self.catalog_name = catalog_name
        # Indicates whether the instance is added to the DMS whitelist.
        self.cluster_node = cluster_node
        # The ID of the database. You can call the [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation to query the ID of the database.
        # 
        # >  You can call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) operation to query the ID of a physical database or the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) operation to query the ID of a logical database.
        self.db_id = db_id
        # The type of the database. For information about the valid values of this parameter, see [DbType parameter](https://help.aliyun.com/document_detail/198106.html).
        self.db_type = db_type
        # The ID of the database administrator (DBA) of the instance.
        self.dba_id = dba_id
        # The nickname of the DBA of the instance.
        self.dba_name = dba_name
        # The complete endpoint of the database.
        self.description = description
        # The encoding format of the database.
        self.encoding = encoding
        # The type of the environment to which the database belongs. Valid values:
        # 
        # *   **product**: production environment
        # *   **dev**: development environment
        # *   **pre**: staging environment
        # *   **test**: test environment
        # *   **sit**: system integration testing (SIT) environment
        # *   **uat**: user acceptance testing (UAT) environment
        # *   **pet**: stress testing environment
        # *   **stag**: STAG environment
        self.env_type = env_type
        # Indicates whether the instance needs special attention. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.follow = follow
        # The endpoint that is used to connect to the database.
        self.host = host
        # The region in which the database instance resides.
        self.idc = idc
        # The name of the region in which the database instance resides.
        self.idc_title = idc_title
        # The ID of the instance to which the database belongs.
        self.instance_id = instance_id
        # The source of the database instance.Valid values:
        # 
        # *   **RDS**: an ApsaraDB RDS instance.
        # *   **ECS_OWN**: a self-managed database deployed on an Elastic Compute Service (ECS) instance.
        # *   **PUBLIC_OWN**: a self-managed database instance that is connected over the Internet.
        # *   **VPC_ID**: a self-managed database instance in a virtual private cloud (VPC) that is connected over Express Connect circuits.
        # *   **GATEWAY**: a database instance connected by using a database gateway.
        self.instance_source = instance_source
        # The time when the database information was last obtained.
        self.last_sync_time = last_sync_time
        # The instance level.
        self.level = level
        # Indicates whether the database is logical. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.logic = logic
        # The IDs of the owners of the databases, which are stored as an array. You can call the [GetUser](https://help.aliyun.com/document_detail/147098.html) or [ListUsers](https://help.aliyun.com/document_detail/141938.html) operation to query the IDs of the owners.
        # 
        # >  The value of OwnerIds is the same as the value of UserId
        self.owner_ids = owner_ids
        # The usernames of the database owners.
        self.owner_names = owner_names
        # The port that is used to connect to the database.
        self.port = port
        # The name of the database.
        self.schema_name = schema_name
        # The name that is used to search for the database.
        self.search_name = search_name
        # The details of the control mode of the instance.
        self.standard_group = standard_group
        # The status of the database. Valid values:
        # 
        # *   **NORMAL**: The database is running as expected.
        # *   **DISABLE**: The database is disabled.
        # *   **OFFLINE**: The database is unpublished.
        # *   **NOT_EXIST**: The database does not exist.
        self.state = state
        # The number of tables.
        self.table_count = table_count
        # The name of TNS.
        self.tns_name = tns_name
        # The unit type.
        self.unit_type = unit_type

    def validate(self):
        if self.standard_group:
            self.standard_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.alter_timeout is not None:
            result['AlterTimeout'] = self.alter_timeout

        if self.asset_control is not None:
            result['AssetControl'] = self.asset_control

        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.cluster_node is not None:
            result['ClusterNode'] = self.cluster_node

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.dba_id is not None:
            result['DbaId'] = self.dba_id

        if self.dba_name is not None:
            result['DbaName'] = self.dba_name

        if self.description is not None:
            result['Description'] = self.description

        if self.encoding is not None:
            result['Encoding'] = self.encoding

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.follow is not None:
            result['Follow'] = self.follow

        if self.host is not None:
            result['Host'] = self.host

        if self.idc is not None:
            result['Idc'] = self.idc

        if self.idc_title is not None:
            result['IdcTitle'] = self.idc_title

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source

        if self.last_sync_time is not None:
            result['LastSyncTime'] = self.last_sync_time

        if self.level is not None:
            result['Level'] = self.level

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids

        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names

        if self.port is not None:
            result['Port'] = self.port

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        if self.standard_group is not None:
            result['StandardGroup'] = self.standard_group.to_map()

        if self.state is not None:
            result['State'] = self.state

        if self.table_count is not None:
            result['TableCount'] = self.table_count

        if self.tns_name is not None:
            result['TnsName'] = self.tns_name

        if self.unit_type is not None:
            result['UnitType'] = self.unit_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('AlterTimeout') is not None:
            self.alter_timeout = m.get('AlterTimeout')

        if m.get('AssetControl') is not None:
            self.asset_control = m.get('AssetControl')

        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('ClusterNode') is not None:
            self.cluster_node = m.get('ClusterNode')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')

        if m.get('DbaName') is not None:
            self.dba_name = m.get('DbaName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Follow') is not None:
            self.follow = m.get('Follow')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Idc') is not None:
            self.idc = m.get('Idc')

        if m.get('IdcTitle') is not None:
            self.idc_title = m.get('IdcTitle')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')

        if m.get('LastSyncTime') is not None:
            self.last_sync_time = m.get('LastSyncTime')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')

        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        if m.get('StandardGroup') is not None:
            temp_model = main_models.GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraDataDbBaseInfoStandardGroup()
            self.standard_group = temp_model.from_map(m.get('StandardGroup'))

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TableCount') is not None:
            self.table_count = m.get('TableCount')

        if m.get('TnsName') is not None:
            self.tns_name = m.get('TnsName')

        if m.get('UnitType') is not None:
            self.unit_type = m.get('UnitType')

        return self

class GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraDataDbBaseInfoStandardGroup(DaraModel):
    def __init__(
        self,
        db_type: str = None,
        description: str = None,
        free_or_stable: bool = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        group_mode: str = None,
        group_name: str = None,
        id: int = None,
        last_mender_id: int = None,
    ):
        # The type of the instance engine. For information about the valid values of this parameter, see [DbType parameter](https://help.aliyun.com/document_detail/198106.html).
        self.db_type = db_type
        # The description of the security rule set.
        self.description = description
        # Indicates whether the instance is managed in Flexible Management or Stable Change mode. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.free_or_stable = free_or_stable
        # The time when the security rule was created.
        self.gmt_create = gmt_create
        # The time when the security rule was last modified.
        self.gmt_modified = gmt_modified
        # The type of the control mode of the instance. Valid values:
        # 
        # *   **COMMON**: The instance is managed in Security Collaboration mode.
        # *   **NONE_CONTROL**: The instance is managed in Flexible Management mode.
        # *   **STABLE**: The instance is managed in Stable Change mode.
        self.group_mode = group_mode
        # The name of the security rule that corresponds to the control mode.
        self.group_name = group_name
        # The ID of the security rule.
        self.id = id
        # The user ID of the last modified security rule.
        self.last_mender_id = last_mender_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.description is not None:
            result['Description'] = self.description

        if self.free_or_stable is not None:
            result['FreeOrStable'] = self.free_or_stable

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.group_mode is not None:
            result['GroupMode'] = self.group_mode

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.id is not None:
            result['Id'] = self.id

        if self.last_mender_id is not None:
            result['LastMenderId'] = self.last_mender_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FreeOrStable') is not None:
            self.free_or_stable = m.get('FreeOrStable')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GroupMode') is not None:
            self.group_mode = m.get('GroupMode')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastMenderId') is not None:
            self.last_mender_id = m.get('LastMenderId')

        return self

class GetDataArchiveOrderDetailResponseBodyDataArchiveOrderDetailPluginExtraDataDagInfo(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        cron_begin_date: str = None,
        cron_end_date: str = None,
        cron_trigger: bool = None,
        dwdevelop: bool = None,
        dag_name: str = None,
        dag_owner_id: str = None,
        deploy_id: int = None,
        description: str = None,
        edit_dag_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_public: int = None,
        legacy: bool = None,
        system: bool = None,
        tenant_id: str = None,
        trigger_once: bool = None,
    ):
        # The ID of the user who created the task flow.
        self.creator_id = creator_id
        # The start time for scheduling. The task flow is not scheduled before this point in time.
        self.cron_begin_date = cron_begin_date
        # The end time for scheduling. The task flow is not scheduled after this point in time.
        self.cron_end_date = cron_end_date
        # Indicates whether the archiving task is a scheduled task. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.cron_trigger = cron_trigger
        # Indicates whether the task is used to develop warehouses.
        # 
        # >  This field is a retained field that is not in use.
        self.dwdevelop = dwdevelop
        # The name of the workflow.
        self.dag_name = dag_name
        # The ID of the owner of the workflow.
        self.dag_owner_id = dag_owner_id
        # The ID of the deployment record.
        self.deploy_id = deploy_id
        # The description of the workflow.
        self.description = description
        # The ID of the editable workflow version.
        self.edit_dag_id = edit_dag_id
        # The time when the workflow was created.
        self.gmt_create = gmt_create
        # The time when the workflow was last modified.
        self.gmt_modified = gmt_modified
        # The ID of the task flow.
        self.id = id
        # Indicates whether the workflow is public. Valid values:
        # 
        # *   **0**: not public.
        # *   **1**: public.
        self.is_public = is_public
        # Indicates whether the task is a historical task. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.legacy = legacy
        # Indicates whether the task was created by the system. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.system = system
        # The tenant ID.
        self.tenant_id = tenant_id
        # Indicates whether the workflow is triggered to run once. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.trigger_once = trigger_once

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.cron_begin_date is not None:
            result['CronBeginDate'] = self.cron_begin_date

        if self.cron_end_date is not None:
            result['CronEndDate'] = self.cron_end_date

        if self.cron_trigger is not None:
            result['CronTrigger'] = self.cron_trigger

        if self.dwdevelop is not None:
            result['DWDevelop'] = self.dwdevelop

        if self.dag_name is not None:
            result['DagName'] = self.dag_name

        if self.dag_owner_id is not None:
            result['DagOwnerId'] = self.dag_owner_id

        if self.deploy_id is not None:
            result['DeployId'] = self.deploy_id

        if self.description is not None:
            result['Description'] = self.description

        if self.edit_dag_id is not None:
            result['EditDagId'] = self.edit_dag_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.is_public is not None:
            result['IsPublic'] = self.is_public

        if self.legacy is not None:
            result['Legacy'] = self.legacy

        if self.system is not None:
            result['System'] = self.system

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.trigger_once is not None:
            result['TriggerOnce'] = self.trigger_once

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('CronBeginDate') is not None:
            self.cron_begin_date = m.get('CronBeginDate')

        if m.get('CronEndDate') is not None:
            self.cron_end_date = m.get('CronEndDate')

        if m.get('CronTrigger') is not None:
            self.cron_trigger = m.get('CronTrigger')

        if m.get('DWDevelop') is not None:
            self.dwdevelop = m.get('DWDevelop')

        if m.get('DagName') is not None:
            self.dag_name = m.get('DagName')

        if m.get('DagOwnerId') is not None:
            self.dag_owner_id = m.get('DagOwnerId')

        if m.get('DeployId') is not None:
            self.deploy_id = m.get('DeployId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EditDagId') is not None:
            self.edit_dag_id = m.get('EditDagId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsPublic') is not None:
            self.is_public = m.get('IsPublic')

        if m.get('Legacy') is not None:
            self.legacy = m.get('Legacy')

        if m.get('System') is not None:
            self.system = m.get('System')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TriggerOnce') is not None:
            self.trigger_once = m.get('TriggerOnce')

        return self

