# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeLogStoreOfEndpointGroupResponseBody(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        access_log_record_customized_header_list: List[str] = None,
        access_log_record_customized_headers_enabled: bool = None,
        endpoint_group_id: str = None,
        listener_id: str = None,
        request_id: str = None,
        sls_log_store_name: str = None,
        sls_project_name: str = None,
        sls_region_id: str = None,
        status: str = None,
    ):
        # The ID of the GA instance.
        self.accelerator_id = accelerator_id
        self.access_log_record_customized_header_list = access_log_record_customized_header_list
        self.access_log_record_customized_headers_enabled = access_log_record_customized_headers_enabled
        # The ID of the endpoint group.
        self.endpoint_group_id = endpoint_group_id
        # The ID of the listener.
        self.listener_id = listener_id
        # The response parameters.
        self.request_id = request_id
        # The name of the Logstore.
        self.sls_log_store_name = sls_log_store_name
        # The name of the Simple Log Service project.
        self.sls_project_name = sls_project_name
        # The region ID of the Simple Log Service project.
        self.sls_region_id = sls_region_id
        # Indicates whether the endpoint group is bound to the Simple Log Service project.
        # 
        # *   **on:** The endpoint group is bound to the Simple Log Service project.
        # *   **off:** The endpoint group is not bound to the Simple Log Service project.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.access_log_record_customized_header_list is not None:
            result['AccessLogRecordCustomizedHeaderList'] = self.access_log_record_customized_header_list

        if self.access_log_record_customized_headers_enabled is not None:
            result['AccessLogRecordCustomizedHeadersEnabled'] = self.access_log_record_customized_headers_enabled

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sls_log_store_name is not None:
            result['SlsLogStoreName'] = self.sls_log_store_name

        if self.sls_project_name is not None:
            result['SlsProjectName'] = self.sls_project_name

        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('AccessLogRecordCustomizedHeaderList') is not None:
            self.access_log_record_customized_header_list = m.get('AccessLogRecordCustomizedHeaderList')

        if m.get('AccessLogRecordCustomizedHeadersEnabled') is not None:
            self.access_log_record_customized_headers_enabled = m.get('AccessLogRecordCustomizedHeadersEnabled')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlsLogStoreName') is not None:
            self.sls_log_store_name = m.get('SlsLogStoreName')

        if m.get('SlsProjectName') is not None:
            self.sls_project_name = m.get('SlsProjectName')

        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

