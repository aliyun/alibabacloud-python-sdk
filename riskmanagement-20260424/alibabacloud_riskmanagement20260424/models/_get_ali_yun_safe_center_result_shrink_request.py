# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAliYunSafeCenterResultShrinkRequest(DaraModel):
    def __init__(
        self,
        create_similar_security_events_query_task_request_shrink: str = None,
        describe_instances_full_status_request_shrink: str = None,
        describe_security_event_operation_status_request_shrink: str = None,
        describe_similar_security_events_request_shrink: str = None,
        get_asset_detail_by_uuid_request_shrink: str = None,
        handle_security_events_request_shrink: str = None,
        handle_similar_security_events_request_shrink: str = None,
        interface_code: str = None,
        list_instances_request_shrink: str = None,
        region_id: str = None,
    ):
        self.create_similar_security_events_query_task_request_shrink = create_similar_security_events_query_task_request_shrink
        self.describe_instances_full_status_request_shrink = describe_instances_full_status_request_shrink
        self.describe_security_event_operation_status_request_shrink = describe_security_event_operation_status_request_shrink
        self.describe_similar_security_events_request_shrink = describe_similar_security_events_request_shrink
        self.get_asset_detail_by_uuid_request_shrink = get_asset_detail_by_uuid_request_shrink
        self.handle_security_events_request_shrink = handle_security_events_request_shrink
        self.handle_similar_security_events_request_shrink = handle_similar_security_events_request_shrink
        # This parameter is required.
        self.interface_code = interface_code
        self.list_instances_request_shrink = list_instances_request_shrink
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_similar_security_events_query_task_request_shrink is not None:
            result['CreateSimilarSecurityEventsQueryTaskRequest'] = self.create_similar_security_events_query_task_request_shrink

        if self.describe_instances_full_status_request_shrink is not None:
            result['DescribeInstancesFullStatusRequest'] = self.describe_instances_full_status_request_shrink

        if self.describe_security_event_operation_status_request_shrink is not None:
            result['DescribeSecurityEventOperationStatusRequest'] = self.describe_security_event_operation_status_request_shrink

        if self.describe_similar_security_events_request_shrink is not None:
            result['DescribeSimilarSecurityEventsRequest'] = self.describe_similar_security_events_request_shrink

        if self.get_asset_detail_by_uuid_request_shrink is not None:
            result['GetAssetDetailByUuidRequest'] = self.get_asset_detail_by_uuid_request_shrink

        if self.handle_security_events_request_shrink is not None:
            result['HandleSecurityEventsRequest'] = self.handle_security_events_request_shrink

        if self.handle_similar_security_events_request_shrink is not None:
            result['HandleSimilarSecurityEventsRequest'] = self.handle_similar_security_events_request_shrink

        if self.interface_code is not None:
            result['InterfaceCode'] = self.interface_code

        if self.list_instances_request_shrink is not None:
            result['ListInstancesRequest'] = self.list_instances_request_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateSimilarSecurityEventsQueryTaskRequest') is not None:
            self.create_similar_security_events_query_task_request_shrink = m.get('CreateSimilarSecurityEventsQueryTaskRequest')

        if m.get('DescribeInstancesFullStatusRequest') is not None:
            self.describe_instances_full_status_request_shrink = m.get('DescribeInstancesFullStatusRequest')

        if m.get('DescribeSecurityEventOperationStatusRequest') is not None:
            self.describe_security_event_operation_status_request_shrink = m.get('DescribeSecurityEventOperationStatusRequest')

        if m.get('DescribeSimilarSecurityEventsRequest') is not None:
            self.describe_similar_security_events_request_shrink = m.get('DescribeSimilarSecurityEventsRequest')

        if m.get('GetAssetDetailByUuidRequest') is not None:
            self.get_asset_detail_by_uuid_request_shrink = m.get('GetAssetDetailByUuidRequest')

        if m.get('HandleSecurityEventsRequest') is not None:
            self.handle_security_events_request_shrink = m.get('HandleSecurityEventsRequest')

        if m.get('HandleSimilarSecurityEventsRequest') is not None:
            self.handle_similar_security_events_request_shrink = m.get('HandleSimilarSecurityEventsRequest')

        if m.get('InterfaceCode') is not None:
            self.interface_code = m.get('InterfaceCode')

        if m.get('ListInstancesRequest') is not None:
            self.list_instances_request_shrink = m.get('ListInstancesRequest')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

