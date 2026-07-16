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
        self.create_similar_security_events_query_task_request = create_similar_security_events_query_task_request
        self.describe_instances_full_status_request = describe_instances_full_status_request
        self.describe_security_event_operation_status_request = describe_security_event_operation_status_request
        self.describe_similar_security_events_request = describe_similar_security_events_request
        self.get_asset_detail_by_uuid_request = get_asset_detail_by_uuid_request
        self.handle_security_events_request = handle_security_events_request
        self.handle_similar_security_events_request = handle_similar_security_events_request
        # This parameter is required.
        self.interface_code = interface_code
        self.list_instances_request = list_instances_request
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
        self.instance_ids = instance_ids
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
        self.alert_type = alert_type
        self.instance_id = instance_id
        self.ip = ip
        self.operation_code = operation_code
        self.operation_params = operation_params
        self.region_id = region_id
        self.source_ip = source_ip
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
        self.alert_type = alert_type
        self.file_md_5 = file_md_5
        self.file_path = file_path
        self.instance_id = instance_id
        self.ip = ip
        self.mark_batch = mark_batch
        self.mark_miss_param = mark_miss_param
        self.operation_code = operation_code
        self.operation_params = operation_params
        self.region_id = region_id
        self.remark = remark
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
        self.region_id = region_id
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
        self.region_id = region_id
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
        self.region_id = region_id
        self.security_event_ids = security_event_ids
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
        self.instance_id = instance_id
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
        self.region_id = region_id
        self.security_event_id = security_event_id
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

