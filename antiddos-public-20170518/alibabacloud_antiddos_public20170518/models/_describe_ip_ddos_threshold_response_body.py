# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_antiddos_public20170518 import models as main_models
from darabonba.model import DaraModel

class DescribeIpDdosThresholdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        threshold: main_models.DescribeIpDdosThresholdResponseBodyThreshold = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the details of the threshold.
        self.threshold = threshold

    def validate(self):
        if self.threshold:
            self.threshold.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.threshold is not None:
            result['Threshold'] = self.threshold.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Threshold') is not None:
            temp_model = main_models.DescribeIpDdosThresholdResponseBodyThreshold()
            self.threshold = temp_model.from_map(m.get('Threshold'))

        return self

class DescribeIpDdosThresholdResponseBodyThreshold(DaraModel):
    def __init__(
        self,
        bps: int = None,
        ddos_type: str = None,
        elastic_bps: int = None,
        instance_id: str = None,
        internet_ip: str = None,
        is_auto: bool = None,
        max_bps: int = None,
        max_pps: int = None,
        pps: int = None,
    ):
        # If the value of the **DdosType** parameter is **defense**, the Bps parameter indicates the current traffic scrubbing threshold. Unit: Mbit/s.
        # 
        # If the value of the **DdosType** parameter is **blackhole**, the Bps parameter indicates the basic protection threshold. Unit: Mbit/s.
        self.bps = bps
        # The type of the threshold. Valid values:
        # 
        # - **defense**: traffic scrubbing threshold
        # 
        # - **blackhole**: DDoS mitigation threshold
        self.ddos_type = ddos_type
        # The burstable protection threshold (the maximum DDoS mitigation threshold). Unit: Mbit/s.
        # 
        # > This parameter is returned only when the value of the **DdosType** parameter is **blackhole**.
        self.elastic_bps = elastic_bps
        # The ID of the instance.
        self.instance_id = instance_id
        # The IP address of the asset.
        self.internet_ip = internet_ip
        # Indicates whether the threshold is automatically adjusted. Valid values:
        # 
        # - **true**: The scrubbing thresholds are automatically adjusted based on the traffic load on the asset.
        # 
        # - **false**: The scrubbing thresholds are not automatically adjusted. You must manually specify the scrubbing thresholds.
        self.is_auto = is_auto
        # The maximum traffic scrubbing threshold. Unit: Mbit/s.
        self.max_bps = max_bps
        # The maximum packet scrubbing threshold. Unit: pps.
        self.max_pps = max_pps
        # The packet scrubbing threshold. Unit: packets per second (pps).
        # 
        # > This parameter is returned only when the value of the **DdosType** parameter is **defense**.
        self.pps = pps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bps is not None:
            result['Bps'] = self.bps

        if self.ddos_type is not None:
            result['DdosType'] = self.ddos_type

        if self.elastic_bps is not None:
            result['ElasticBps'] = self.elastic_bps

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.is_auto is not None:
            result['IsAuto'] = self.is_auto

        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps

        if self.max_pps is not None:
            result['MaxPps'] = self.max_pps

        if self.pps is not None:
            result['Pps'] = self.pps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')

        if m.get('DdosType') is not None:
            self.ddos_type = m.get('DdosType')

        if m.get('ElasticBps') is not None:
            self.elastic_bps = m.get('ElasticBps')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IsAuto') is not None:
            self.is_auto = m.get('IsAuto')

        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')

        if m.get('MaxPps') is not None:
            self.max_pps = m.get('MaxPps')

        if m.get('Pps') is not None:
            self.pps = m.get('Pps')

        return self

