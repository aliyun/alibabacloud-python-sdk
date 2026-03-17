# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeFlowLogsResponseBody(DaraModel):
    def __init__(
        self,
        flow_logs: main_models.DescribeFlowLogsResponseBodyFlowLogs = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.flow_logs = flow_logs
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of flow logs.
        self.total_count = total_count

    def validate(self):
        if self.flow_logs:
            self.flow_logs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_logs is not None:
            result['FlowLogs'] = self.flow_logs.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowLogs') is not None:
            temp_model = main_models.DescribeFlowLogsResponseBodyFlowLogs()
            self.flow_logs = temp_model.from_map(m.get('FlowLogs'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeFlowLogsResponseBodyFlowLogs(DaraModel):
    def __init__(
        self,
        flow_log_set_type: List[main_models.DescribeFlowLogsResponseBodyFlowLogsFlowLogSetType] = None,
    ):
        self.flow_log_set_type = flow_log_set_type

    def validate(self):
        if self.flow_log_set_type:
            for v1 in self.flow_log_set_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FlowLogSetType'] = []
        if self.flow_log_set_type is not None:
            for k1 in self.flow_log_set_type:
                result['FlowLogSetType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flow_log_set_type = []
        if m.get('FlowLogSetType') is not None:
            for k1 in m.get('FlowLogSetType'):
                temp_model = main_models.DescribeFlowLogsResponseBodyFlowLogsFlowLogSetType()
                self.flow_log_set_type.append(temp_model.from_map(k1))

        return self

class DescribeFlowLogsResponseBodyFlowLogsFlowLogSetType(DaraModel):
    def __init__(
        self,
        active_aging: int = None,
        description: str = None,
        flow_log_id: str = None,
        inactive_aging: int = None,
        logstore_name: str = None,
        name: str = None,
        netflow_server_ip: str = None,
        netflow_server_port: str = None,
        netflow_version: str = None,
        output_type: str = None,
        project_name: str = None,
        resource_group_id: str = None,
        sls_region_id: str = None,
        status: str = None,
        total_sag_num: int = None,
    ):
        self.active_aging = active_aging
        self.description = description
        self.flow_log_id = flow_log_id
        self.inactive_aging = inactive_aging
        self.logstore_name = logstore_name
        self.name = name
        self.netflow_server_ip = netflow_server_ip
        self.netflow_server_port = netflow_server_port
        self.netflow_version = netflow_version
        self.output_type = output_type
        self.project_name = project_name
        self.resource_group_id = resource_group_id
        self.sls_region_id = sls_region_id
        self.status = status
        self.total_sag_num = total_sag_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_aging is not None:
            result['ActiveAging'] = self.active_aging

        if self.description is not None:
            result['Description'] = self.description

        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id

        if self.inactive_aging is not None:
            result['InactiveAging'] = self.inactive_aging

        if self.logstore_name is not None:
            result['LogstoreName'] = self.logstore_name

        if self.name is not None:
            result['Name'] = self.name

        if self.netflow_server_ip is not None:
            result['NetflowServerIp'] = self.netflow_server_ip

        if self.netflow_server_port is not None:
            result['NetflowServerPort'] = self.netflow_server_port

        if self.netflow_version is not None:
            result['NetflowVersion'] = self.netflow_version

        if self.output_type is not None:
            result['OutputType'] = self.output_type

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.total_sag_num is not None:
            result['TotalSagNum'] = self.total_sag_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAging') is not None:
            self.active_aging = m.get('ActiveAging')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')

        if m.get('InactiveAging') is not None:
            self.inactive_aging = m.get('InactiveAging')

        if m.get('LogstoreName') is not None:
            self.logstore_name = m.get('LogstoreName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetflowServerIp') is not None:
            self.netflow_server_ip = m.get('NetflowServerIp')

        if m.get('NetflowServerPort') is not None:
            self.netflow_server_port = m.get('NetflowServerPort')

        if m.get('NetflowVersion') is not None:
            self.netflow_version = m.get('NetflowVersion')

        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalSagNum') is not None:
            self.total_sag_num = m.get('TotalSagNum')

        return self

