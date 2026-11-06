# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosdiversion20230701 import models as main_models
from darabonba.model import DaraModel

class QueryNetListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.QueryNetListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        # 
        # - 200: The request was successful.
        # 
        # - Other codes: The request failed.
        self.code = code
        # The CIDR blocks.
        self.data = data
        # The response parameters.
        self.message = message
        # The request ID.
        self.request_id = request_id

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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryNetListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryNetListResponseBodyData(DaraModel):
    def __init__(
        self,
        nets: List[main_models.QueryNetListResponseBodyDataNets] = None,
        num: int = None,
        page: int = None,
        total: int = None,
    ):
        # The CIDR blocks.
        self.nets = nets
        # The number of entries per page. Valid values: 1 to 100. Default value: 100.
        self.num = num
        # The page number.
        self.page = page
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.nets:
            for v1 in self.nets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nets'] = []
        if self.nets is not None:
            for k1 in self.nets:
                result['Nets'].append(k1.to_map() if k1 else None)

        if self.num is not None:
            result['Num'] = self.num

        if self.page is not None:
            result['Page'] = self.page

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nets = []
        if m.get('Nets') is not None:
            for k1 in m.get('Nets'):
                temp_model = main_models.QueryNetListResponseBodyDataNets()
                self.nets.append(temp_model.from_map(k1))

        if m.get('Num') is not None:
            self.num = m.get('Num')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryNetListResponseBodyDataNets(DaraModel):
    def __init__(
        self,
        ddo_sdefense: main_models.QueryNetListResponseBodyDataNetsDDoSDefense = None,
        declared: List[main_models.QueryNetListResponseBodyDataNetsDeclared] = None,
        declared_state: int = None,
        fwd_effect: int = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        mode: str = None,
        net: str = None,
        net_extend: str = None,
        net_main: str = None,
        net_type: str = None,
        permit: int = None,
        sale_id: str = None,
        upstream_type: str = None,
        user_id: str = None,
    ):
        # The DDoS mitigation configuration of the CIDR block.
        self.ddo_sdefense = ddo_sdefense
        # The advertising details.
        self.declared = declared
        # The advertising status of the CIDR block. Valid values:
        # 
        # - 0: The CIDR block is not advertised.
        # 
        # - 1: The CIDR block is advertised.
        self.declared_state = declared_state
        # Indicates whether the forwarding configuration takes effect. Valid values:
        # 
        # - 0: The forwarding configuration does not take effect.
        # 
        # - 1: The forwarding configuration takes effect.
        self.fwd_effect = fwd_effect
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modify = gmt_modify
        # The scheduling mode. Valid values:
        # 
        # - netflow-auto
        # 
        # - manual
        self.mode = mode
        # The CIDR block of the anti-DDoS diversion instance.
        self.net = net
        # Indicates whether the CIDR block needs to be extended. Valid values:
        # 
        # - 0: The CIDR block does not need to be extended.
        # 
        # - 1: The CIDR block needs to be extended.
        self.net_extend = net_extend
        # The primary CIDR block of the anti-DDoS diversion instance for which an extended CIDR block is configured. If no extended CIDR blocks are configured for the anti-DDoS diversion instance, this parameter is left empty.
        self.net_main = net_main
        # The type of the CIDR block.
        self.net_type = net_type
        # The review status. Valid values:
        # 
        # - 0: not reviewed.
        # 
        # - 1: reviewed.
        # 
        # - 2: under review.
        self.permit = permit
        # The ID of the anti-DDoS diversion instance.
        self.sale_id = sale_id
        # The reinjection type. Valid values:
        # 
        # - aliyun_line
        # 
        # - pccw_line
        # 
        # - gre_line
        # 
        # - private_line
        self.upstream_type = upstream_type
        # The user ID.
        self.user_id = user_id

    def validate(self):
        if self.ddo_sdefense:
            self.ddo_sdefense.validate()
        if self.declared:
            for v1 in self.declared:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddo_sdefense is not None:
            result['DDoSDefense'] = self.ddo_sdefense.to_map()

        result['Declared'] = []
        if self.declared is not None:
            for k1 in self.declared:
                result['Declared'].append(k1.to_map() if k1 else None)

        if self.declared_state is not None:
            result['DeclaredState'] = self.declared_state

        if self.fwd_effect is not None:
            result['FwdEffect'] = self.fwd_effect

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.net is not None:
            result['Net'] = self.net

        if self.net_extend is not None:
            result['NetExtend'] = self.net_extend

        if self.net_main is not None:
            result['NetMain'] = self.net_main

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.permit is not None:
            result['Permit'] = self.permit

        if self.sale_id is not None:
            result['SaleId'] = self.sale_id

        if self.upstream_type is not None:
            result['UpstreamType'] = self.upstream_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DDoSDefense') is not None:
            temp_model = main_models.QueryNetListResponseBodyDataNetsDDoSDefense()
            self.ddo_sdefense = temp_model.from_map(m.get('DDoSDefense'))

        self.declared = []
        if m.get('Declared') is not None:
            for k1 in m.get('Declared'):
                temp_model = main_models.QueryNetListResponseBodyDataNetsDeclared()
                self.declared.append(temp_model.from_map(k1))

        if m.get('DeclaredState') is not None:
            self.declared_state = m.get('DeclaredState')

        if m.get('FwdEffect') is not None:
            self.fwd_effect = m.get('FwdEffect')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Net') is not None:
            self.net = m.get('Net')

        if m.get('NetExtend') is not None:
            self.net_extend = m.get('NetExtend')

        if m.get('NetMain') is not None:
            self.net_main = m.get('NetMain')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Permit') is not None:
            self.permit = m.get('Permit')

        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')

        if m.get('UpstreamType') is not None:
            self.upstream_type = m.get('UpstreamType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class QueryNetListResponseBodyDataNetsDeclared(DaraModel):
    def __init__(
        self,
        declared: str = None,
        region: str = None,
    ):
        # Indicates whether the CIDR block is advertised. Valid values:
        # 
        # - 0: The CIDR block is not advertised.
        # 
        # - 1: The CIDR block is advertised.
        self.declared = declared
        # The region in which the CIDR block is advertised. Valid values:
        # 
        # - oe26: China (Hong Kong).
        # 
        # - us50: US (Virginia).
        # 
        # - oe24: US (Silicon Valley).
        # 
        # - oe28: Singapore.
        # 
        # - jp141: Japan (Tokyo).
        # 
        # - Gb145: UK (London).
        # 
        # - oi39: Germany (Frankfurt).
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.declared is not None:
            result['Declared'] = self.declared

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Declared') is not None:
            self.declared = m.get('Declared')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class QueryNetListResponseBodyDataNetsDDoSDefense(DaraModel):
    def __init__(
        self,
        clean_th: main_models.QueryNetListResponseBodyDataNetsDDoSDefenseCleanTh = None,
        custom_net_policy: main_models.QueryNetListResponseBodyDataNetsDDoSDefenseCustomNetPolicy = None,
        dj_policy: main_models.QueryNetListResponseBodyDataNetsDDoSDefenseDjPolicy = None,
        hole_th: main_models.QueryNetListResponseBodyDataNetsDDoSDefenseHoleTh = None,
    ):
        # The configuration of traffic scrubbing.
        self.clean_th = clean_th
        self.custom_net_policy = custom_net_policy
        # The configuration of the mitigation policy.
        self.dj_policy = dj_policy
        # The configuration of blackhole filtering.
        self.hole_th = hole_th

    def validate(self):
        if self.clean_th:
            self.clean_th.validate()
        if self.custom_net_policy:
            self.custom_net_policy.validate()
        if self.dj_policy:
            self.dj_policy.validate()
        if self.hole_th:
            self.hole_th.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clean_th is not None:
            result['CleanTh'] = self.clean_th.to_map()

        if self.custom_net_policy is not None:
            result['CustomNetPolicy'] = self.custom_net_policy.to_map()

        if self.dj_policy is not None:
            result['DjPolicy'] = self.dj_policy.to_map()

        if self.hole_th is not None:
            result['HoleTh'] = self.hole_th.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CleanTh') is not None:
            temp_model = main_models.QueryNetListResponseBodyDataNetsDDoSDefenseCleanTh()
            self.clean_th = temp_model.from_map(m.get('CleanTh'))

        if m.get('CustomNetPolicy') is not None:
            temp_model = main_models.QueryNetListResponseBodyDataNetsDDoSDefenseCustomNetPolicy()
            self.custom_net_policy = temp_model.from_map(m.get('CustomNetPolicy'))

        if m.get('DjPolicy') is not None:
            temp_model = main_models.QueryNetListResponseBodyDataNetsDDoSDefenseDjPolicy()
            self.dj_policy = temp_model.from_map(m.get('DjPolicy'))

        if m.get('HoleTh') is not None:
            temp_model = main_models.QueryNetListResponseBodyDataNetsDDoSDefenseHoleTh()
            self.hole_th = temp_model.from_map(m.get('HoleTh'))

        return self

class QueryNetListResponseBodyDataNetsDDoSDefenseHoleTh(DaraModel):
    def __init__(
        self,
        thresh_mbps: int = None,
    ):
        # The blackhole filtering threshold in Mbit/s. The value 0 indicates best-effort protection.
        self.thresh_mbps = thresh_mbps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.thresh_mbps is not None:
            result['ThreshMbps'] = self.thresh_mbps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ThreshMbps') is not None:
            self.thresh_mbps = m.get('ThreshMbps')

        return self

class QueryNetListResponseBodyDataNetsDDoSDefenseDjPolicy(DaraModel):
    def __init__(
        self,
        policy_name: str = None,
    ):
        # The name of the mitigation policy.
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        return self

class QueryNetListResponseBodyDataNetsDDoSDefenseCustomNetPolicy(DaraModel):
    def __init__(
        self,
        policy_name: str = None,
        tmpl_id: str = None,
    ):
        self.policy_name = policy_name
        self.tmpl_id = tmpl_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.tmpl_id is not None:
            result['TmplId'] = self.tmpl_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('TmplId') is not None:
            self.tmpl_id = m.get('TmplId')

        return self

class QueryNetListResponseBodyDataNetsDDoSDefenseCleanTh(DaraModel):
    def __init__(
        self,
        mbps: int = None,
        pps: int = None,
    ):
        # The traffic scrubbing threshold in Mbit/s.
        self.mbps = mbps
        # The traffic scrubbing threshold in packets per second (pps).
        self.pps = pps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mbps is not None:
            result['Mbps'] = self.mbps

        if self.pps is not None:
            result['Pps'] = self.pps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')

        if m.get('Pps') is not None:
            self.pps = m.get('Pps')

        return self

