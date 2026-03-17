# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class ListProbeTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListProbeTaskResponseBodyData] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The response code.
        self.code = code
        # The information about the probe task.
        self.data = data
        # The response message.
        self.message = message
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

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
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListProbeTaskResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProbeTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        domain: str = None,
        enable: bool = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        packet_number: int = None,
        port: int = None,
        probe_task_id: str = None,
        probe_task_source_address: str = None,
        protocol: str = None,
        sag_id: str = None,
        sn: str = None,
        task_name: str = None,
        type: str = None,
    ):
        # The domain name that is probed by the task.
        self.domain = domain
        # Indicates whether the probe task is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.enable = enable
        # The time when the probe task was created.
        self.gmt_create = gmt_create
        # The time when the probe task was modified.
        self.gmt_modify = gmt_modify
        # The number of probe packets transmitted by the probe task per minute.
        self.packet_number = packet_number
        # The port that is probed by the task.
        self.port = port
        # The ID of the probe task.
        self.probe_task_id = probe_task_id
        # The source address of the probe task.
        self.probe_task_source_address = probe_task_source_address
        # The protocol of the probe task. Valid values:
        # 
        # *   **ICMP**
        # *   **TCP**
        # *   **HTTP**
        # 
        # > Tasks that probe private networks support only ICMP and TCP.
        self.protocol = protocol
        # The ID of the SAG instance.
        self.sag_id = sag_id
        # The serial number of the SAG device.
        self.sn = sn
        # The name of the probe task.
        self.task_name = task_name
        # The type of the probe task. Valid values:
        # 
        # *   **Internet**: probes a public network.
        # *   **Intranet**: probes a private network.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify

        if self.packet_number is not None:
            result['PacketNumber'] = self.packet_number

        if self.port is not None:
            result['Port'] = self.port

        if self.probe_task_id is not None:
            result['ProbeTaskId'] = self.probe_task_id

        if self.probe_task_source_address is not None:
            result['ProbeTaskSourceAddress'] = self.probe_task_source_address

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.sag_id is not None:
            result['SagId'] = self.sag_id

        if self.sn is not None:
            result['Sn'] = self.sn

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')

        if m.get('PacketNumber') is not None:
            self.packet_number = m.get('PacketNumber')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProbeTaskId') is not None:
            self.probe_task_id = m.get('ProbeTaskId')

        if m.get('ProbeTaskSourceAddress') is not None:
            self.probe_task_source_address = m.get('ProbeTaskSourceAddress')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('SagId') is not None:
            self.sag_id = m.get('SagId')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

