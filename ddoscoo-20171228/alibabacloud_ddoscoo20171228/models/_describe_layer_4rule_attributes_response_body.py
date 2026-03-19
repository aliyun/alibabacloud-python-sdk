# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20171228 import models as main_models
from darabonba.model import DaraModel

class DescribeLayer4RuleAttributesResponseBody(DaraModel):
    def __init__(
        self,
        listeners: List[main_models.DescribeLayer4RuleAttributesResponseBodyListeners] = None,
        request_id: str = None,
    ):
        self.listeners = listeners
        self.request_id = request_id

    def validate(self):
        if self.listeners:
            for v1 in self.listeners:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Listeners'] = []
        if self.listeners is not None:
            for k1 in self.listeners:
                result['Listeners'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listeners = []
        if m.get('Listeners') is not None:
            for k1 in m.get('Listeners'):
                temp_model = main_models.DescribeLayer4RuleAttributesResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLayer4RuleAttributesResponseBodyListeners(DaraModel):
    def __init__(
        self,
        config: main_models.DescribeLayer4RuleAttributesResponseBodyListenersConfig = None,
        frontend_port: int = None,
        instance_id: str = None,
        protocol: str = None,
    ):
        self.config = config
        self.frontend_port = frontend_port
        self.instance_id = instance_id
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
            temp_model = main_models.DescribeLayer4RuleAttributesResponseBodyListenersConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

class DescribeLayer4RuleAttributesResponseBodyListenersConfig(DaraModel):
    def __init__(
        self,
        cc: main_models.DescribeLayer4RuleAttributesResponseBodyListenersConfigCc = None,
        nodata_conn: str = None,
        payload_len: main_models.DescribeLayer4RuleAttributesResponseBodyListenersConfigPayloadLen = None,
        persistence_timeout: int = None,
        sla: main_models.DescribeLayer4RuleAttributesResponseBodyListenersConfigSla = None,
        slimit: main_models.DescribeLayer4RuleAttributesResponseBodyListenersConfigSlimit = None,
        synproxy: str = None,
    ):
        self.cc = cc
        self.nodata_conn = nodata_conn
        self.payload_len = payload_len
        self.persistence_timeout = persistence_timeout
        self.sla = sla
        self.slimit = slimit
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
            temp_model = main_models.DescribeLayer4RuleAttributesResponseBodyListenersConfigCc()
            self.cc = temp_model.from_map(m.get('Cc'))

        if m.get('NodataConn') is not None:
            self.nodata_conn = m.get('NodataConn')

        if m.get('PayloadLen') is not None:
            temp_model = main_models.DescribeLayer4RuleAttributesResponseBodyListenersConfigPayloadLen()
            self.payload_len = temp_model.from_map(m.get('PayloadLen'))

        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')

        if m.get('Sla') is not None:
            temp_model = main_models.DescribeLayer4RuleAttributesResponseBodyListenersConfigSla()
            self.sla = temp_model.from_map(m.get('Sla'))

        if m.get('Slimit') is not None:
            temp_model = main_models.DescribeLayer4RuleAttributesResponseBodyListenersConfigSlimit()
            self.slimit = temp_model.from_map(m.get('Slimit'))

        if m.get('Synproxy') is not None:
            self.synproxy = m.get('Synproxy')

        return self

class DescribeLayer4RuleAttributesResponseBodyListenersConfigSlimit(DaraModel):
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
        self.bps = bps
        self.cps = cps
        self.cps_enable = cps_enable
        self.cps_mode = cps_mode
        self.maxconn = maxconn
        self.maxconn_enable = maxconn_enable
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

class DescribeLayer4RuleAttributesResponseBodyListenersConfigSla(DaraModel):
    def __init__(
        self,
        cps: int = None,
        cps_enable: int = None,
        maxconn: int = None,
        maxconn_enable: int = None,
    ):
        self.cps = cps
        self.cps_enable = cps_enable
        self.maxconn = maxconn
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

class DescribeLayer4RuleAttributesResponseBodyListenersConfigPayloadLen(DaraModel):
    def __init__(
        self,
        max: int = None,
        min: int = None,
    ):
        self.max = max
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

class DescribeLayer4RuleAttributesResponseBodyListenersConfigCc(DaraModel):
    def __init__(
        self,
        sblack: List[main_models.DescribeLayer4RuleAttributesResponseBodyListenersConfigCcSblack] = None,
    ):
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
                temp_model = main_models.DescribeLayer4RuleAttributesResponseBodyListenersConfigCcSblack()
                self.sblack.append(temp_model.from_map(k1))

        return self

class DescribeLayer4RuleAttributesResponseBodyListenersConfigCcSblack(DaraModel):
    def __init__(
        self,
        cnt: int = None,
        during: int = None,
        expires: int = None,
        type: int = None,
    ):
        self.cnt = cnt
        self.during = during
        self.expires = expires
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

