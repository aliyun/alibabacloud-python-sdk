# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class GetRealTimeRiskInfoRequest(TeaModel):
    def __init__(
        self,
        atoken: str = None,
        data_source_id: str = None,
        extra: str = None,
    ):
        # This parameter is required.
        self.atoken = atoken
        # This parameter is required.
        self.data_source_id = data_source_id
        self.extra = extra

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.atoken is not None:
            result['atoken'] = self.atoken
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.extra is not None:
            result['extra'] = self.extra
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('atoken') is not None:
            self.atoken = m.get('atoken')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        return self


class GetRealTimeRiskInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        app_channel: str = None,
        fake_device: str = None,
        idfa: str = None,
        oaid: str = None,
        proxy_device: str = None,
        risk_level: str = None,
        risk_score: str = None,
        zid: str = None,
    ):
        self.app_channel = app_channel
        self.fake_device = fake_device
        self.idfa = idfa
        self.oaid = oaid
        self.proxy_device = proxy_device
        self.risk_level = risk_level
        self.risk_score = risk_score
        self.zid = zid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_channel is not None:
            result['appChannel'] = self.app_channel
        if self.fake_device is not None:
            result['fakeDevice'] = self.fake_device
        if self.idfa is not None:
            result['idfa'] = self.idfa
        if self.oaid is not None:
            result['oaid'] = self.oaid
        if self.proxy_device is not None:
            result['proxyDevice'] = self.proxy_device
        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level
        if self.risk_score is not None:
            result['riskScore'] = self.risk_score
        if self.zid is not None:
            result['zid'] = self.zid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appChannel') is not None:
            self.app_channel = m.get('appChannel')
        if m.get('fakeDevice') is not None:
            self.fake_device = m.get('fakeDevice')
        if m.get('idfa') is not None:
            self.idfa = m.get('idfa')
        if m.get('oaid') is not None:
            self.oaid = m.get('oaid')
        if m.get('proxyDevice') is not None:
            self.proxy_device = m.get('proxyDevice')
        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')
        if m.get('riskScore') is not None:
            self.risk_score = m.get('riskScore')
        if m.get('zid') is not None:
            self.zid = m.get('zid')
        return self


class GetRealTimeRiskInfoResponseBody(TeaModel):
    def __init__(
        self,
        msg: str = None,
        code: int = None,
        data: GetRealTimeRiskInfoResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.msg = msg
        self.code = code
        self.data = data
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetRealTimeRiskInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetRealTimeRiskInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRealTimeRiskInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRealTimeRiskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetZidTagByAtokenRequest(TeaModel):
    def __init__(
        self,
        atoken: str = None,
        data_source_id: str = None,
    ):
        # atoken
        # 
        # This parameter is required.
        self.atoken = atoken
        # This parameter is required.
        self.data_source_id = data_source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.atoken is not None:
            result['atoken'] = self.atoken
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('atoken') is not None:
            self.atoken = m.get('atoken')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        return self


class GetZidTagByAtokenResponseBodyData(TeaModel):
    def __init__(
        self,
        a_hook: str = None,
        debug: str = None,
        double_open: str = None,
        java_hook: str = None,
        native_hook: str = None,
        root: str = None,
        simulator: str = None,
        vpn_proxy: str = None,
        wifi_proxy: str = None,
        zid: str = None,
    ):
        # aHook
        self.a_hook = a_hook
        self.debug = debug
        self.double_open = double_open
        # javaHook
        self.java_hook = java_hook
        self.native_hook = native_hook
        self.root = root
        self.simulator = simulator
        self.vpn_proxy = vpn_proxy
        self.wifi_proxy = wifi_proxy
        self.zid = zid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.a_hook is not None:
            result['aHook'] = self.a_hook
        if self.debug is not None:
            result['debug'] = self.debug
        if self.double_open is not None:
            result['doubleOpen'] = self.double_open
        if self.java_hook is not None:
            result['javaHook'] = self.java_hook
        if self.native_hook is not None:
            result['nativeHook'] = self.native_hook
        if self.root is not None:
            result['root'] = self.root
        if self.simulator is not None:
            result['simulator'] = self.simulator
        if self.vpn_proxy is not None:
            result['vpnProxy'] = self.vpn_proxy
        if self.wifi_proxy is not None:
            result['wifiProxy'] = self.wifi_proxy
        if self.zid is not None:
            result['zid'] = self.zid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aHook') is not None:
            self.a_hook = m.get('aHook')
        if m.get('debug') is not None:
            self.debug = m.get('debug')
        if m.get('doubleOpen') is not None:
            self.double_open = m.get('doubleOpen')
        if m.get('javaHook') is not None:
            self.java_hook = m.get('javaHook')
        if m.get('nativeHook') is not None:
            self.native_hook = m.get('nativeHook')
        if m.get('root') is not None:
            self.root = m.get('root')
        if m.get('simulator') is not None:
            self.simulator = m.get('simulator')
        if m.get('vpnProxy') is not None:
            self.vpn_proxy = m.get('vpnProxy')
        if m.get('wifiProxy') is not None:
            self.wifi_proxy = m.get('wifiProxy')
        if m.get('zid') is not None:
            self.zid = m.get('zid')
        return self


class GetZidTagByAtokenResponseBody(TeaModel):
    def __init__(
        self,
        msg: str = None,
        code: int = None,
        data: GetZidTagByAtokenResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.msg = msg
        # code
        self.code = code
        self.data = data
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetZidTagByAtokenResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetZidTagByAtokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetZidTagByAtokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetZidTagByAtokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetZidTagScoreByAtokenRequest(TeaModel):
    def __init__(
        self,
        atoken: str = None,
        data_source_id: str = None,
    ):
        # atoken
        # 
        # This parameter is required.
        self.atoken = atoken
        # This parameter is required.
        self.data_source_id = data_source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.atoken is not None:
            result['atoken'] = self.atoken
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('atoken') is not None:
            self.atoken = m.get('atoken')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        return self


class GetZidTagScoreByAtokenResponseBodyData(TeaModel):
    def __init__(
        self,
        a_hook: str = None,
        debug: str = None,
        double_open: str = None,
        java_hook: str = None,
        native_hook: str = None,
        risk_level: str = None,
        risk_score: str = None,
        root: str = None,
        simulator: str = None,
        vpn_proxy: str = None,
        wifi_proxy: str = None,
        zid: str = None,
    ):
        # aHook
        self.a_hook = a_hook
        self.debug = debug
        self.double_open = double_open
        # javaHook
        self.java_hook = java_hook
        self.native_hook = native_hook
        self.risk_level = risk_level
        self.risk_score = risk_score
        self.root = root
        self.simulator = simulator
        self.vpn_proxy = vpn_proxy
        self.wifi_proxy = wifi_proxy
        self.zid = zid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.a_hook is not None:
            result['aHook'] = self.a_hook
        if self.debug is not None:
            result['debug'] = self.debug
        if self.double_open is not None:
            result['doubleOpen'] = self.double_open
        if self.java_hook is not None:
            result['javaHook'] = self.java_hook
        if self.native_hook is not None:
            result['nativeHook'] = self.native_hook
        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level
        if self.risk_score is not None:
            result['riskScore'] = self.risk_score
        if self.root is not None:
            result['root'] = self.root
        if self.simulator is not None:
            result['simulator'] = self.simulator
        if self.vpn_proxy is not None:
            result['vpnProxy'] = self.vpn_proxy
        if self.wifi_proxy is not None:
            result['wifiProxy'] = self.wifi_proxy
        if self.zid is not None:
            result['zid'] = self.zid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aHook') is not None:
            self.a_hook = m.get('aHook')
        if m.get('debug') is not None:
            self.debug = m.get('debug')
        if m.get('doubleOpen') is not None:
            self.double_open = m.get('doubleOpen')
        if m.get('javaHook') is not None:
            self.java_hook = m.get('javaHook')
        if m.get('nativeHook') is not None:
            self.native_hook = m.get('nativeHook')
        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')
        if m.get('riskScore') is not None:
            self.risk_score = m.get('riskScore')
        if m.get('root') is not None:
            self.root = m.get('root')
        if m.get('simulator') is not None:
            self.simulator = m.get('simulator')
        if m.get('vpnProxy') is not None:
            self.vpn_proxy = m.get('vpnProxy')
        if m.get('wifiProxy') is not None:
            self.wifi_proxy = m.get('wifiProxy')
        if m.get('zid') is not None:
            self.zid = m.get('zid')
        return self


class GetZidTagScoreByAtokenResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        data: GetZidTagScoreByAtokenResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        self.msg = msg
        self.data = data
        # requestId
        self.request_id = request_id
        # success
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('data') is not None:
            temp_model = GetZidTagScoreByAtokenResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetZidTagScoreByAtokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetZidTagScoreByAtokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetZidTagScoreByAtokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChannelRiskDetailsRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        data_source_id: str = None,
        end: str = None,
        is_all_channel: str = None,
        start: str = None,
    ):
        self.channel = channel
        # This parameter is required.
        self.data_source_id = data_source_id
        # This parameter is required.
        self.end = end
        self.is_all_channel = is_all_channel
        # This parameter is required.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.end is not None:
            result['end'] = self.end
        if self.is_all_channel is not None:
            result['isAllChannel'] = self.is_all_channel
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('isAllChannel') is not None:
            self.is_all_channel = m.get('isAllChannel')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class ListChannelRiskDetailsResponseBodyDataRiskDetails(TeaModel):
    def __init__(
        self,
        an: str = None,
        av: str = None,
        bn: str = None,
        c: str = None,
        date: str = None,
        fd: str = None,
        idfa: str = None,
        jb: str = None,
        oaid: str = None,
        py: str = None,
        rl: str = None,
        rs: str = None,
        zid: str = None,
    ):
        self.an = an
        self.av = av
        self.bn = bn
        self.c = c
        self.date = date
        self.fd = fd
        self.idfa = idfa
        self.jb = jb
        self.oaid = oaid
        self.py = py
        self.rl = rl
        self.rs = rs
        self.zid = zid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.an is not None:
            result['an'] = self.an
        if self.av is not None:
            result['av'] = self.av
        if self.bn is not None:
            result['bn'] = self.bn
        if self.c is not None:
            result['c'] = self.c
        if self.date is not None:
            result['date'] = self.date
        if self.fd is not None:
            result['fd'] = self.fd
        if self.idfa is not None:
            result['idfa'] = self.idfa
        if self.jb is not None:
            result['jb'] = self.jb
        if self.oaid is not None:
            result['oaid'] = self.oaid
        if self.py is not None:
            result['py'] = self.py
        if self.rl is not None:
            result['rl'] = self.rl
        if self.rs is not None:
            result['rs'] = self.rs
        if self.zid is not None:
            result['zid'] = self.zid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('an') is not None:
            self.an = m.get('an')
        if m.get('av') is not None:
            self.av = m.get('av')
        if m.get('bn') is not None:
            self.bn = m.get('bn')
        if m.get('c') is not None:
            self.c = m.get('c')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('fd') is not None:
            self.fd = m.get('fd')
        if m.get('idfa') is not None:
            self.idfa = m.get('idfa')
        if m.get('jb') is not None:
            self.jb = m.get('jb')
        if m.get('oaid') is not None:
            self.oaid = m.get('oaid')
        if m.get('py') is not None:
            self.py = m.get('py')
        if m.get('rl') is not None:
            self.rl = m.get('rl')
        if m.get('rs') is not None:
            self.rs = m.get('rs')
        if m.get('zid') is not None:
            self.zid = m.get('zid')
        return self


class ListChannelRiskDetailsResponseBodyDataRiskSumary(TeaModel):
    def __init__(
        self,
        date: str = None,
        risk_zid_emu_distinct_new: str = None,
    ):
        self.date = date
        self.risk_zid_emu_distinct_new = risk_zid_emu_distinct_new

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.risk_zid_emu_distinct_new is not None:
            result['riskZidEmuDistinctNew'] = self.risk_zid_emu_distinct_new
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('riskZidEmuDistinctNew') is not None:
            self.risk_zid_emu_distinct_new = m.get('riskZidEmuDistinctNew')
        return self


class ListChannelRiskDetailsResponseBodyData(TeaModel):
    def __init__(
        self,
        risk_details: List[ListChannelRiskDetailsResponseBodyDataRiskDetails] = None,
        risk_sumary: List[ListChannelRiskDetailsResponseBodyDataRiskSumary] = None,
    ):
        self.risk_details = risk_details
        self.risk_sumary = risk_sumary

    def validate(self):
        if self.risk_details:
            for k in self.risk_details:
                if k:
                    k.validate()
        if self.risk_sumary:
            for k in self.risk_sumary:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['riskDetails'] = []
        if self.risk_details is not None:
            for k in self.risk_details:
                result['riskDetails'].append(k.to_map() if k else None)
        result['riskSumary'] = []
        if self.risk_sumary is not None:
            for k in self.risk_sumary:
                result['riskSumary'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.risk_details = []
        if m.get('riskDetails') is not None:
            for k in m.get('riskDetails'):
                temp_model = ListChannelRiskDetailsResponseBodyDataRiskDetails()
                self.risk_details.append(temp_model.from_map(k))
        self.risk_sumary = []
        if m.get('riskSumary') is not None:
            for k in m.get('riskSumary'):
                temp_model = ListChannelRiskDetailsResponseBodyDataRiskSumary()
                self.risk_sumary.append(temp_model.from_map(k))
        return self


class ListChannelRiskDetailsResponseBody(TeaModel):
    def __init__(
        self,
        msg: str = None,
        code: int = None,
        data: ListChannelRiskDetailsResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.msg = msg
        self.code = code
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListChannelRiskDetailsResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListChannelRiskDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChannelRiskDetailsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListChannelRiskDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUninstallDetailRequest(TeaModel):
    def __init__(
        self,
        data_source_id: str = None,
        end_ds: str = None,
        start_ds: str = None,
    ):
        # This parameter is required.
        self.data_source_id = data_source_id
        # This parameter is required.
        self.end_ds = end_ds
        # This parameter is required.
        self.start_ds = start_ds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.end_ds is not None:
            result['endDs'] = self.end_ds
        if self.start_ds is not None:
            result['startDs'] = self.start_ds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('endDs') is not None:
            self.end_ds = m.get('endDs')
        if m.get('startDs') is not None:
            self.start_ds = m.get('startDs')
        return self


class ListUninstallDetailResponseBodyDataDetails(TeaModel):
    def __init__(
        self,
        active_datetime: str = None,
        city: str = None,
        device_brand: str = None,
        device_model: str = None,
        first_active_datetime: str = None,
        idfa: str = None,
        imei: str = None,
        install_app_version: str = None,
        install_channel: str = None,
        oaid: str = None,
        os_version: str = None,
        puid: str = None,
        umid: str = None,
        uninstall_count: int = None,
        uninstall_datetime: str = None,
        zid: str = None,
    ):
        self.active_datetime = active_datetime
        self.city = city
        # deviceBrand
        self.device_brand = device_brand
        # deviceModel
        self.device_model = device_model
        # firstActiveDatetime
        self.first_active_datetime = first_active_datetime
        # idfa
        self.idfa = idfa
        # imei
        self.imei = imei
        # installAppVersion
        self.install_app_version = install_app_version
        # installChannel
        self.install_channel = install_channel
        # oaid
        self.oaid = oaid
        # osVersion
        self.os_version = os_version
        # puid
        self.puid = puid
        self.umid = umid
        self.uninstall_count = uninstall_count
        self.uninstall_datetime = uninstall_datetime
        # zid
        self.zid = zid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_datetime is not None:
            result['activeDatetime'] = self.active_datetime
        if self.city is not None:
            result['city'] = self.city
        if self.device_brand is not None:
            result['deviceBrand'] = self.device_brand
        if self.device_model is not None:
            result['deviceModel'] = self.device_model
        if self.first_active_datetime is not None:
            result['firstActiveDatetime'] = self.first_active_datetime
        if self.idfa is not None:
            result['idfa'] = self.idfa
        if self.imei is not None:
            result['imei'] = self.imei
        if self.install_app_version is not None:
            result['installAppVersion'] = self.install_app_version
        if self.install_channel is not None:
            result['installChannel'] = self.install_channel
        if self.oaid is not None:
            result['oaid'] = self.oaid
        if self.os_version is not None:
            result['osVersion'] = self.os_version
        if self.puid is not None:
            result['puid'] = self.puid
        if self.umid is not None:
            result['umid'] = self.umid
        if self.uninstall_count is not None:
            result['uninstallCount'] = self.uninstall_count
        if self.uninstall_datetime is not None:
            result['uninstallDatetime'] = self.uninstall_datetime
        if self.zid is not None:
            result['zid'] = self.zid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeDatetime') is not None:
            self.active_datetime = m.get('activeDatetime')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('deviceBrand') is not None:
            self.device_brand = m.get('deviceBrand')
        if m.get('deviceModel') is not None:
            self.device_model = m.get('deviceModel')
        if m.get('firstActiveDatetime') is not None:
            self.first_active_datetime = m.get('firstActiveDatetime')
        if m.get('idfa') is not None:
            self.idfa = m.get('idfa')
        if m.get('imei') is not None:
            self.imei = m.get('imei')
        if m.get('installAppVersion') is not None:
            self.install_app_version = m.get('installAppVersion')
        if m.get('installChannel') is not None:
            self.install_channel = m.get('installChannel')
        if m.get('oaid') is not None:
            self.oaid = m.get('oaid')
        if m.get('osVersion') is not None:
            self.os_version = m.get('osVersion')
        if m.get('puid') is not None:
            self.puid = m.get('puid')
        if m.get('umid') is not None:
            self.umid = m.get('umid')
        if m.get('uninstallCount') is not None:
            self.uninstall_count = m.get('uninstallCount')
        if m.get('uninstallDatetime') is not None:
            self.uninstall_datetime = m.get('uninstallDatetime')
        if m.get('zid') is not None:
            self.zid = m.get('zid')
        return self


class ListUninstallDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        details: List[ListUninstallDetailResponseBodyDataDetails] = None,
    ):
        self.details = details

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['details'] = []
        if self.details is not None:
            for k in self.details:
                result['details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('details') is not None:
            for k in m.get('details'):
                temp_model = ListUninstallDetailResponseBodyDataDetails()
                self.details.append(temp_model.from_map(k))
        return self


class ListUninstallDetailResponseBody(TeaModel):
    def __init__(
        self,
        msg: str = None,
        success: bool = None,
        code: int = None,
        data: ListUninstallDetailResponseBodyData = None,
        request_id: str = None,
    ):
        # msg
        self.msg = msg
        # success
        self.success = success
        # code
        self.code = code
        self.data = data
        # requestId
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListUninstallDetailResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListUninstallDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUninstallDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUninstallDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


