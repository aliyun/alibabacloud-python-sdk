# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class GetAliYunSafeCenterResultRequest(DaraModel):
    def __init__(
        self,
        create_similar_security_events_query_task_request: main_models.GetAliYunSafeCenterResultRequestCreateSimilarSecurityEventsQueryTaskRequest = None,
        describe_instances_full_status_request: main_models.GetAliYunSafeCenterResultRequestDescribeInstancesFullStatusRequest = None,
        describe_security_event_operation_status_request: main_models.GetAliYunSafeCenterResultRequestDescribeSecurityEventOperationStatusRequest = None,
        describe_similar_security_events_request: main_models.GetAliYunSafeCenterResultRequestDescribeSimilarSecurityEventsRequest = None,
        get_asset_detail_by_uuid_request: main_models.GetAliYunSafeCenterResultRequestGetAssetDetailByUuidRequest = None,
        handle_security_events_request: main_models.GetAliYunSafeCenterResultRequestHandleSecurityEventsRequest = None,
        handle_similar_security_events_request: main_models.GetAliYunSafeCenterResultRequestHandleSimilarSecurityEventsRequest = None,
        interface_code: str = None,
        list_instances_request: main_models.GetAliYunSafeCenterResultRequestListInstancesRequest = None,
        region_id: str = None,
    ):
        # Creates a node to query security alerting events triggered by the same rule or alerting type.
        self.create_similar_security_events_query_task_request = create_similar_security_events_query_task_request
        # Queries the running status of ECS instances.
        self.describe_instances_full_status_request = describe_instances_full_status_request
        # Queries whether the list of security alerting events that match the same IP rule or same alerting type as the alerting event to be handled is empty.
        self.describe_security_event_operation_status_request = describe_security_event_operation_status_request
        # Queries identical security alert events in Security Center.
        self.describe_similar_security_events_request = describe_similar_security_events_request
        # The request parameters for querying the Security Center Agent status.
        self.get_asset_detail_by_uuid_request = get_asset_detail_by_uuid_request
        # Handles security alert events.
        self.handle_security_events_request = handle_security_events_request
        # Handles security alert events in batches based on the same IP rule or type.
        self.handle_similar_security_events_request = handle_similar_security_events_request
        # The code of the public API operation.
        # 
        # - **GetAssetDetailByUuid**: Retrieves the Agent status. Request parameter: GetAssetDetailByUuidRequest.
        # 
        # - **DescribeSimilarSecurityEvents**: Retrieves the list of instance IDs for identical security alerting events. Request parameter: DescribeSimilarSecurityEventsRequest.
        # 
        # - **CreateSimilarSecurityEventsQueryTask**: Creates a node to query security alerting events triggered by the same rule or alerting type. Request parameter: CreateSimilarSecurityEventsQueryTaskRequest.
        # 
        # - **DescribeSecurityEventOperationStatus**: Queries whether the list of security alerting events that match the same IP rule or same alerting type as the alerting event to be handled is empty. Request parameter: DescribeSecurityEventOperationStatusRequest.
        # 
        # - **HandleSimilarSecurityEvents**: Handles security alerting events in batches based on the same IP rule or type. Request parameter: HandleSimilarSecurityEventsRequest.
        # HandleSecurityEvents: Handles security alerting events. Request parameter: HandleSecurityEventsRequest.
        # 
        # - **DescribeInstancesFullStatus**: Queries the running status of ECS instances. Request parameter: DescribeInstancesFullStatusRequest.
        # 
        # - **ListInstances**: Queries the running status of simple application servers. Request parameter: ListInstancesRequest.
        # 
        # - **StartConfigRuleEvaluation**: Re-evaluates security check rules.
        # 
        # > Each API operation name corresponds to its own request parameters.
        # 
        # This parameter is required.
        self.interface_code = interface_code
        # Queries the running status of simple application servers.
        self.list_instances_request = list_instances_request
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.create_similar_security_events_query_task_request:
            self.create_similar_security_events_query_task_request.validate()
        if self.describe_instances_full_status_request:
            self.describe_instances_full_status_request.validate()
        if self.describe_security_event_operation_status_request:
            self.describe_security_event_operation_status_request.validate()
        if self.describe_similar_security_events_request:
            self.describe_similar_security_events_request.validate()
        if self.get_asset_detail_by_uuid_request:
            self.get_asset_detail_by_uuid_request.validate()
        if self.handle_security_events_request:
            self.handle_security_events_request.validate()
        if self.handle_similar_security_events_request:
            self.handle_similar_security_events_request.validate()
        if self.list_instances_request:
            self.list_instances_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_similar_security_events_query_task_request is not None:
            result['CreateSimilarSecurityEventsQueryTaskRequest'] = self.create_similar_security_events_query_task_request.to_map()

        if self.describe_instances_full_status_request is not None:
            result['DescribeInstancesFullStatusRequest'] = self.describe_instances_full_status_request.to_map()

        if self.describe_security_event_operation_status_request is not None:
            result['DescribeSecurityEventOperationStatusRequest'] = self.describe_security_event_operation_status_request.to_map()

        if self.describe_similar_security_events_request is not None:
            result['DescribeSimilarSecurityEventsRequest'] = self.describe_similar_security_events_request.to_map()

        if self.get_asset_detail_by_uuid_request is not None:
            result['GetAssetDetailByUuidRequest'] = self.get_asset_detail_by_uuid_request.to_map()

        if self.handle_security_events_request is not None:
            result['HandleSecurityEventsRequest'] = self.handle_security_events_request.to_map()

        if self.handle_similar_security_events_request is not None:
            result['HandleSimilarSecurityEventsRequest'] = self.handle_similar_security_events_request.to_map()

        if self.interface_code is not None:
            result['InterfaceCode'] = self.interface_code

        if self.list_instances_request is not None:
            result['ListInstancesRequest'] = self.list_instances_request.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateSimilarSecurityEventsQueryTaskRequest') is not None:
            temp_model = main_models.GetAliYunSafeCenterResultRequestCreateSimilarSecurityEventsQueryTaskRequest()
            self.create_similar_security_events_query_task_request = temp_model.from_map(m.get('CreateSimilarSecurityEventsQueryTaskRequest'))

        if m.get('DescribeInstancesFullStatusRequest') is not None:
            temp_model = main_models.GetAliYunSafeCenterResultRequestDescribeInstancesFullStatusRequest()
            self.describe_instances_full_status_request = temp_model.from_map(m.get('DescribeInstancesFullStatusRequest'))

        if m.get('DescribeSecurityEventOperationStatusRequest') is not None:
            temp_model = main_models.GetAliYunSafeCenterResultRequestDescribeSecurityEventOperationStatusRequest()
            self.describe_security_event_operation_status_request = temp_model.from_map(m.get('DescribeSecurityEventOperationStatusRequest'))

        if m.get('DescribeSimilarSecurityEventsRequest') is not None:
            temp_model = main_models.GetAliYunSafeCenterResultRequestDescribeSimilarSecurityEventsRequest()
            self.describe_similar_security_events_request = temp_model.from_map(m.get('DescribeSimilarSecurityEventsRequest'))

        if m.get('GetAssetDetailByUuidRequest') is not None:
            temp_model = main_models.GetAliYunSafeCenterResultRequestGetAssetDetailByUuidRequest()
            self.get_asset_detail_by_uuid_request = temp_model.from_map(m.get('GetAssetDetailByUuidRequest'))

        if m.get('HandleSecurityEventsRequest') is not None:
            temp_model = main_models.GetAliYunSafeCenterResultRequestHandleSecurityEventsRequest()
            self.handle_security_events_request = temp_model.from_map(m.get('HandleSecurityEventsRequest'))

        if m.get('HandleSimilarSecurityEventsRequest') is not None:
            temp_model = main_models.GetAliYunSafeCenterResultRequestHandleSimilarSecurityEventsRequest()
            self.handle_similar_security_events_request = temp_model.from_map(m.get('HandleSimilarSecurityEventsRequest'))

        if m.get('InterfaceCode') is not None:
            self.interface_code = m.get('InterfaceCode')

        if m.get('ListInstancesRequest') is not None:
            temp_model = main_models.GetAliYunSafeCenterResultRequestListInstancesRequest()
            self.list_instances_request = temp_model.from_map(m.get('ListInstancesRequest'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class GetAliYunSafeCenterResultRequestListInstancesRequest(DaraModel):
    def __init__(
        self,
        instance_ids: str = None,
        region_id: str = None,
    ):
        # The instance IDs of simple application servers. The value is a JSON array that can contain up to 100 IDs. Separate multiple IDs with commas (,).
        self.instance_ids = instance_ids
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class GetAliYunSafeCenterResultRequestHandleSimilarSecurityEventsRequest(DaraModel):
    def __init__(
        self,
        alert_type: str = None,
        instance_id: str = None,
        ip: str = None,
        operation_code: str = None,
        operation_params: str = None,
        region_id: str = None,
        source_ip: str = None,
        task_id: int = None,
    ):
        # The alerting type.
        self.alert_type = alert_type
        # The instance ID.
        self.instance_id = instance_id
        # The IP address of the instance.
        self.ip = ip
        # The operation type for batch handling similar security alert events.
        # 
        # > You can call the DescribeSecurityEventOperations operation to obtain this parameter.
        self.operation_code = operation_code
        # The configuration of the sub-operation for handling alerting events. The value is in JSON format.
        # 
        # > This parameter is required only when **OperationCode** is set to **kill_and_quara**, **block_ip**, or **virus_quara**. For other values of **OperationCode**, this parameter can be left empty.
        # 
        # > When **OperationCode** is set to **block_ip**, the following field is included:
        # > - **expireTime**: The lock expiration time. Unit: milliseconds.
        # >
        # > When **OperationCode** is set to **kill_and_quara**, the following field is included:
        # > - **subOperation**: The method for killing and quarantining. Valid values:
        # >     - **killAndQuaraFileByMd5andPath**: Terminates the process and quarantines the file.
        # >     - **killByMd5andPath**: Terminates the running process.
        # >
        # > When **OperationCode** is set to **virus_quara**, the following field is included:
        # > - **subOperation**: The method for killing and quarantining. Valid values:
        # >    - **quaraFileByMd5andPath**: Quarantines the source file of the process.
        self.operation_params = operation_params
        # The region ID.
        self.region_id = region_id
        # The IP address of the access source.
        self.source_ip = source_ip
        # The ID of the task for batch handling all security alert events of the same type.
        # 
        # > You can call the CreateSimilarSecurityEventsQueryTask operation to obtain this parameter.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code

        if self.operation_params is not None:
            result['OperationParams'] = self.operation_params

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')

        if m.get('OperationParams') is not None:
            self.operation_params = m.get('OperationParams')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class GetAliYunSafeCenterResultRequestHandleSecurityEventsRequest(DaraModel):
    def __init__(
        self,
        alert_type: str = None,
        file_md_5: str = None,
        file_path: str = None,
        instance_id: str = None,
        ip: str = None,
        mark_batch: str = None,
        mark_miss_param: str = None,
        operation_code: str = None,
        operation_params: str = None,
        region_id: str = None,
        remark: str = None,
        security_event_ids: List[str] = None,
    ):
        # The alert rule type.
        self.alert_type = alert_type
        # The MD5 hash of the file.
        self.file_md_5 = file_md_5
        # The path of the sensitive file.
        self.file_path = file_path
        # The instance ID.
        self.instance_id = instance_id
        # The user IP address.
        self.ip = ip
        # Specifies whether to add to the whitelist in batches.
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.mark_batch = mark_batch
        # The whitelist rule configuration. The value is in JSON format and contains the following fields:
        # 
        # - **field**: The whitelist field.
        # - **operate**: The whitelist method. Valid values:
        #   - **notContains**: Does not contain.
        #   - **contains**: Contains.
        #   - **regex**: Regular expression match.
        #   - **strEqual**: Equals.
        #   - **strNotEqual**: Does not equal.
        # - **fieldValue**: The match value.
        # - **uuid**: The scope of the whitelist rule. Valid values:
        #   - **part**: Only the current asset.
        #   - **ALL**: All assets.
        # 
        # > Call the DescribeSecurityEventOperations operation to obtain the field whitelist field.
        self.mark_miss_param = mark_miss_param
        # The method for handling the security alert event. Valid values:
        # 
        # - **block_ip**: Block.
        # - **advance_mark_mis_info**: Add to whitelist.
        # - **ignore**: Ignore.
        # - **manual_handled**: Manually handled.
        # - **kill_process**: Terminate process.
        # - **cleanup**: Deep scan and cleanup.
        # - **kill_and_quara**: Virus scan and quarantine.
        # - **disable_malicious_defense**: Disable malicious behavior defense.
        # - **client_problem_check**: Troubleshoot.
        # - **quara**: Quarantine.
        self.operation_code = operation_code
        # The configuration of the sub-operation for handling security alert events.
        # 
        # When OperationCode is set to kill_and_quara, specify the parameter type "subOperation":${code}.
        # Valid code values:
        # - Quarantined file: quaraFileByMd5andPath
        # - Kill process and quarantined file by process ID and path: killAndQuaraFileByPidAndMd5andPath
        # - Kill process only: killByMd5andPath
        # - Kill process and quarantined file: killAndQuaraFileByMd5andPath
        # - Kill container process by process ID and path: killProcessByPidandPathandCmdline
        # - Kill container process by file MD5 and path: killContainerProcessByMd5AndPath
        # 
        # When OperationCode is set to block_ip, the parameter is:
        # - Expiration time: expireTime:${timestamp}
        # > This parameter is required only when OperationCode is set to `kill_and_quara` or `block_ip`. For other values of OperationCode, this parameter can be left empty. ${timestamp} indicates the timestamp of the deadline for blocking this IP address.
        self.operation_params = operation_params
        # The region ID.
        self.region_id = region_id
        # The remarks.
        self.remark = remark
        # The collection of IDs of the security alert events to handle.
        # 
        # Example:
        self.security_event_ids = security_event_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.file_md_5 is not None:
            result['FileMd5'] = self.file_md_5

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.mark_batch is not None:
            result['MarkBatch'] = self.mark_batch

        if self.mark_miss_param is not None:
            result['MarkMissParam'] = self.mark_miss_param

        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code

        if self.operation_params is not None:
            result['OperationParams'] = self.operation_params

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.security_event_ids is not None:
            result['SecurityEventIds'] = self.security_event_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('FileMd5') is not None:
            self.file_md_5 = m.get('FileMd5')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('MarkBatch') is not None:
            self.mark_batch = m.get('MarkBatch')

        if m.get('MarkMissParam') is not None:
            self.mark_miss_param = m.get('MarkMissParam')

        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')

        if m.get('OperationParams') is not None:
            self.operation_params = m.get('OperationParams')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SecurityEventIds') is not None:
            self.security_event_ids = m.get('SecurityEventIds')

        return self

class GetAliYunSafeCenterResultRequestGetAssetDetailByUuidRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        uuid: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The UUID of the asset to query.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class GetAliYunSafeCenterResultRequestDescribeSimilarSecurityEventsRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        task_id: int = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The ID of the query task. You can call the CreateSimilarSecurityEventsQueryTask operation to obtain this parameter.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class GetAliYunSafeCenterResultRequestDescribeSecurityEventOperationStatusRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        security_event_ids: List[str] = None,
        task_id: int = None,
    ):
        # The region ID. Example: ap-southeast-1.
        self.region_id = region_id
        # The list of security alert event IDs.
        # 
        # > You must specify either TaskId or SecurityEventIds.N. At least one of these parameters is required for a successful call.
        self.security_event_ids = security_event_ids
        # The ID of the task for handling security alert events.
        # 
        # > You must specify either TaskId or SecurityEventIds. At least one of these parameters is required for a successful call.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_event_ids is not None:
            result['SecurityEventIds'] = self.security_event_ids

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityEventIds') is not None:
            self.security_event_ids = m.get('SecurityEventIds')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class GetAliYunSafeCenterResultRequestDescribeInstancesFullStatusRequest(DaraModel):
    def __init__(
        self,
        instance_id: List[str] = None,
        region_id: str = None,
    ):
        # The list of instance IDs.
        self.instance_id = instance_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class GetAliYunSafeCenterResultRequestCreateSimilarSecurityEventsQueryTaskRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        security_event_id: int = None,
        similar_event_scenario_code: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The ID of the security alert event.
        self.security_event_id = security_event_id
        # The code of the alerting event that has the same type or rule hits.
        self.similar_event_scenario_code = similar_event_scenario_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id

        if self.similar_event_scenario_code is not None:
            result['SimilarEventScenarioCode'] = self.similar_event_scenario_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')

        if m.get('SimilarEventScenarioCode') is not None:
            self.similar_event_scenario_code = m.get('SimilarEventScenarioCode')

        return self

