# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetHoneypotStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetHoneypotStatisticsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code that is returned. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The honeypot usage statistics.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetHoneypotStatisticsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetHoneypotStatisticsResponseBodyData(DaraModel):
    def __init__(
        self,
        total_honeypot_count: int = None,
        total_node_status: int = None,
        total_probe_count: int = None,
        used_honeypot_count: int = None,
        used_host_probe_count: int = None,
        used_probe_count: int = None,
        used_vpc_probe_count: int = None,
    ):
        # The total number of honeypots.
        self.total_honeypot_count = total_honeypot_count
        # The health status of the management node. Valid values:
        # 
        # *   1: normal
        # *   2: abnormal
        self.total_node_status = total_node_status
        # The total number of authorized probes.
        self.total_probe_count = total_probe_count
        # The number of deployed honeypots.
        self.used_honeypot_count = used_honeypot_count
        # The number of deployed host probes.
        self.used_host_probe_count = used_host_probe_count
        # The number of deployed probes.
        self.used_probe_count = used_probe_count
        # The number of deployed VPC probes.
        self.used_vpc_probe_count = used_vpc_probe_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_honeypot_count is not None:
            result['TotalHoneypotCount'] = self.total_honeypot_count

        if self.total_node_status is not None:
            result['TotalNodeStatus'] = self.total_node_status

        if self.total_probe_count is not None:
            result['TotalProbeCount'] = self.total_probe_count

        if self.used_honeypot_count is not None:
            result['UsedHoneypotCount'] = self.used_honeypot_count

        if self.used_host_probe_count is not None:
            result['UsedHostProbeCount'] = self.used_host_probe_count

        if self.used_probe_count is not None:
            result['UsedProbeCount'] = self.used_probe_count

        if self.used_vpc_probe_count is not None:
            result['UsedVpcProbeCount'] = self.used_vpc_probe_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalHoneypotCount') is not None:
            self.total_honeypot_count = m.get('TotalHoneypotCount')

        if m.get('TotalNodeStatus') is not None:
            self.total_node_status = m.get('TotalNodeStatus')

        if m.get('TotalProbeCount') is not None:
            self.total_probe_count = m.get('TotalProbeCount')

        if m.get('UsedHoneypotCount') is not None:
            self.used_honeypot_count = m.get('UsedHoneypotCount')

        if m.get('UsedHostProbeCount') is not None:
            self.used_host_probe_count = m.get('UsedHostProbeCount')

        if m.get('UsedProbeCount') is not None:
            self.used_probe_count = m.get('UsedProbeCount')

        if m.get('UsedVpcProbeCount') is not None:
            self.used_vpc_probe_count = m.get('UsedVpcProbeCount')

        return self

