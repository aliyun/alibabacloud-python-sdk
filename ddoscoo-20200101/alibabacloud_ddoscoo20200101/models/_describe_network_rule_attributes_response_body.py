# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkRuleAttributesResponseBody(DaraModel):
    def __init__(
        self,
        network_rule_attributes: List[main_models.DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributes] = None,
        request_id: str = None,
    ):
        # An array that consists of the mitigation settings of the port forwarding rule for a non-website service. The mitigation settings include session persistence and DDoS mitigation policies.
        self.network_rule_attributes = network_rule_attributes
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.network_rule_attributes:
            for v1 in self.network_rule_attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkRuleAttributes'] = []
        if self.network_rule_attributes is not None:
            for k1 in self.network_rule_attributes:
                result['NetworkRuleAttributes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_rule_attributes = []
        if m.get('NetworkRuleAttributes') is not None:
            for k1 in m.get('NetworkRuleAttributes'):
                temp_model = main_models.DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributes()
                self.network_rule_attributes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributes(DaraModel):
    def __init__(
        self,
        config: main_models.DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfig = None,
        frontend_port: int = None,
        instance_id: str = None,
        protocol: str = None,
    ):
        # The mitigation settings of the port forwarding rule.
        self.config = config
        # The forwarding port.
        self.frontend_port = frontend_port
        # The ID of the instance.
        self.instance_id = instance_id
        # The forwarding protocol. Valid values:
        # 
        # *   **tcp**
        # *   **udp**
        self.protocol = protocol

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = main_models.DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfig(DaraModel):
    def __init__(
        self,
        cc: main_models.DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCc = None,
        nodata_conn: str = None,
        payload_len: main_models.DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigPayloadLen = None,
        persistence_timeout: int = None,
        sla: main_models.DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSla = None,
        slimit: main_models.DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSlimit = None,
        synproxy: str = None,
    ):
        # The protection policy applied when the number of connections initiated from a source IP address frequently exceeds the limit.
        self.cc = cc
        # The status of the Empty Connection switch. Valid values:
        # 
        # *   **on**: The switch is turned on.
        # *   **off**: The switch is turned off.
        self.nodata_conn = nodata_conn
        # The settings of the Packet Length Limit policy.
        self.payload_len = payload_len
        # The timeout period of session persistence. Valid values: **30** to **3600**. Unit: seconds. Default value: **0**, which indicates that session persistence is disabled.
        self.persistence_timeout = persistence_timeout
        # The settings of the Speed Limit for Destination policy.
        self.sla = sla
        # The settings of the Speed Limit for Source policy.
        self.slimit = slimit
        # The status of the False Source switch. Valid values:
        # 
        # *   **on**: The switch is turned on.
        # *   **off**: The switch is turned off.
        self.synproxy = synproxy

    def validate(self):
        if self.cc:
            self.cc.validate()
        if self.payload_len:
            self.payload_len.validate()
        if self.sla:
            self.sla.validate()
        if self.slimit:
            self.slimit.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cc is not None:
            result['Cc'] = self.cc.to_map()

        if self.nodata_conn is not None:
            result['NodataConn'] = self.nodata_conn

        if self.payload_len is not None:
            result['PayloadLen'] = self.payload_len.to_map()

        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout

        if self.sla is not None:
            result['Sla'] = self.sla.to_map()

        if self.slimit is not None:
            result['Slimit'] = self.slimit.to_map()

        if self.synproxy is not None:
            result['Synproxy'] = self.synproxy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cc') is not None:
            temp_model = main_models.DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCc()
            self.cc = temp_model.from_map(m.get('Cc'))

        if m.get('NodataConn') is not None:
            self.nodata_conn = m.get('NodataConn')

        if m.get('PayloadLen') is not None:
            temp_model = main_models.DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigPayloadLen()
            self.payload_len = temp_model.from_map(m.get('PayloadLen'))

        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')

        if m.get('Sla') is not None:
            temp_model = main_models.DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSla()
            self.sla = temp_model.from_map(m.get('Sla'))

        if m.get('Slimit') is not None:
            temp_model = main_models.DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSlimit()
            self.slimit = temp_model.from_map(m.get('Slimit'))

        if m.get('Synproxy') is not None:
            self.synproxy = m.get('Synproxy')

        return self

class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSlimit(DaraModel):
    def __init__(
        self,
        bps: int = None,
        cps: int = None,
        cps_enable: int = None,
        cps_mode: int = None,
        maxconn: int = None,
        maxconn_enable: int = None,
        pps: int = None,
    ):
        # The bandwidth limit for a source IP address. Valid values: **1024** to **268435456**. Unit: bytes/s. Default value: **0**, which indicates that the bandwidth for a source IP address is unlimited.
        self.bps = bps
        # The maximum number of new connections per second that can be initiated from a source IP address. Valid values: **1** to **500000**.
        self.cps = cps
        # The status of the Source New Connection Rate Limit switch. Valid values:
        # 
        # *   **0**: The switch is turned off.
        # *   **1**: The switch is turned on.
        self.cps_enable = cps_enable
        # The mode of the Source New Connection Rate Limit switch. Valid values:
        # 
        # *   **1**: the manual mode
        # *   **2**: the automatic mode
        self.cps_mode = cps_mode
        # The maximum number of concurrent connections initiated from a source IP address. Valid values: **1** to **500000**.
        self.maxconn = maxconn
        # The status of the Source Concurrent Connection Rate Limit switch. Valid values:
        # 
        # *   **0**: The switch is turned off.
        # *   **1**: The switch is turned on.
        self.maxconn_enable = maxconn_enable
        # The packets per second (pps) limit for a source IP address. Valid values: **1** to **100000**. Unit: packets/s. Default value: **0**, which indicates that the pps for a source IP address is unlimited.
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

        if self.cps is not None:
            result['Cps'] = self.cps

        if self.cps_enable is not None:
            result['CpsEnable'] = self.cps_enable

        if self.cps_mode is not None:
            result['CpsMode'] = self.cps_mode

        if self.maxconn is not None:
            result['Maxconn'] = self.maxconn

        if self.maxconn_enable is not None:
            result['MaxconnEnable'] = self.maxconn_enable

        if self.pps is not None:
            result['Pps'] = self.pps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')

        if m.get('Cps') is not None:
            self.cps = m.get('Cps')

        if m.get('CpsEnable') is not None:
            self.cps_enable = m.get('CpsEnable')

        if m.get('CpsMode') is not None:
            self.cps_mode = m.get('CpsMode')

        if m.get('Maxconn') is not None:
            self.maxconn = m.get('Maxconn')

        if m.get('MaxconnEnable') is not None:
            self.maxconn_enable = m.get('MaxconnEnable')

        if m.get('Pps') is not None:
            self.pps = m.get('Pps')

        return self

class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigSla(DaraModel):
    def __init__(
        self,
        cps: int = None,
        cps_enable: int = None,
        maxconn: int = None,
        maxconn_enable: int = None,
    ):
        # The maximum number of new connections per second that can be established over the port of the destination instance. Valid values: **100** to **100000**.
        self.cps = cps
        # The status of the Destination New Connection Rate Limit switch. Valid values:
        # 
        # *   **0**: The switch is turned off.
        # *   **1**: The switch is turned on.
        self.cps_enable = cps_enable
        # The maximum number of concurrent connections that can be established over the port of the destination instance. Valid values: **1000** to **1000000**.
        self.maxconn = maxconn
        # The status of the Destination Concurrent Connection Rate Limit switch. Valid values:
        # 
        # *   **0**: The switch is turned off.
        # *   **1**: The switch is turned on.
        self.maxconn_enable = maxconn_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cps is not None:
            result['Cps'] = self.cps

        if self.cps_enable is not None:
            result['CpsEnable'] = self.cps_enable

        if self.maxconn is not None:
            result['Maxconn'] = self.maxconn

        if self.maxconn_enable is not None:
            result['MaxconnEnable'] = self.maxconn_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')

        if m.get('CpsEnable') is not None:
            self.cps_enable = m.get('CpsEnable')

        if m.get('Maxconn') is not None:
            self.maxconn = m.get('Maxconn')

        if m.get('MaxconnEnable') is not None:
            self.maxconn_enable = m.get('MaxconnEnable')

        return self

class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigPayloadLen(DaraModel):
    def __init__(
        self,
        max: int = None,
        min: int = None,
    ):
        # The maximum length of a packet. Valid values: **0** to **6000**. Unit: bytes.
        self.max = max
        # The minimum length of a packet. Valid values: **0** to **6000**. Unit: bytes.
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        return self

class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCc(DaraModel):
    def __init__(
        self,
        sblack: List[main_models.DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCcSblack] = None,
    ):
        # The protection policy that a source IP address is added to the blacklist when the number of connections initiated from the IP address frequently exceeds the limit.
        self.sblack = sblack

    def validate(self):
        if self.sblack:
            for v1 in self.sblack:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Sblack'] = []
        if self.sblack is not None:
            for k1 in self.sblack:
                result['Sblack'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sblack = []
        if m.get('Sblack') is not None:
            for k1 in m.get('Sblack'):
                temp_model = main_models.DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCcSblack()
                self.sblack.append(temp_model.from_map(k1))

        return self

class DescribeNetworkRuleAttributesResponseBodyNetworkRuleAttributesConfigCcSblack(DaraModel):
    def __init__(
        self,
        cnt: int = None,
        during: int = None,
        expires: int = None,
        type: int = None,
    ):
        # The threshold that the number of connections initiated from a source IP address can exceed the limit. Set the value to **5**. If the number of connections initiated from a source IP address exceeds the limit five times during the check, the source IP address is added to the blacklist.
        self.cnt = cnt
        # The interval at which checks are performed. Set the value to **60**. Unit: seconds.
        self.during = during
        # The validity period of the IP address in the blacklist. Valid values: **60** to **604800**. Unit: seconds.
        self.expires = expires
        # The type of the limit that causes a source IP address to be added to the blacklist. Valid values:
        # 
        # *   **1**: Source New Connection Rate Limit
        # *   **2**: Source Concurrent Connection Rate Limit
        # *   **3**: PPS Limit for Source
        # *   **4**: Bandwidth Limit for Source
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cnt is not None:
            result['Cnt'] = self.cnt

        if self.during is not None:
            result['During'] = self.during

        if self.expires is not None:
            result['Expires'] = self.expires

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cnt') is not None:
            self.cnt = m.get('Cnt')

        if m.get('During') is not None:
            self.during = m.get('During')

        if m.get('Expires') is not None:
            self.expires = m.get('Expires')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

