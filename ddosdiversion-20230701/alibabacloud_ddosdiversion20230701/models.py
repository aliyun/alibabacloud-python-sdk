# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ConfigNetStatusRequest(TeaModel):
    def __init__(
        self,
        net: str = None,
        regions: List[str] = None,
        sale_id: str = None,
        status: str = None,
        sub_nets: List[str] = None,
    ):
        # The CIDR block of the anti-DDoS diversion instance.
        # 
        # This parameter is required.
        self.net = net
        # The regions in which the CIDR block needs to be advertised or withdrawn from advertising. If you leave this parameter empty, the CIDR blocks in all regions are configured.
        # 
        # >  You can call the [QueryNetList](https://help.aliyun.com/document_detail/2639086.html) operation to obtain the regions of the CIDR blocks.
        self.regions = regions
        # The ID of the anti-DDoS diversion instance.
        # 
        # This parameter is required.
        self.sale_id = sale_id
        # The status of the CIDR block. Valid values:
        # 
        # *   enable: advertises the CIDR block.
        # *   disable: withdraws the advertising of the CIDR block.
        # 
        # This parameter is required.
        self.status = status
        # The subnet CIDR blocks of the CIDR block.
        self.sub_nets = sub_nets

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net is not None:
            result['Net'] = self.net
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.sale_id is not None:
            result['SaleId'] = self.sale_id
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_nets is not None:
            result['SubNets'] = self.sub_nets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Net') is not None:
            self.net = m.get('Net')
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubNets') is not None:
            self.sub_nets = m.get('SubNets')
        return self


class ConfigNetStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        # 
        # *   **200**: The request was successful.
        # *   Other codes: The request failed.
        self.code = code
        # The response parameters.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigNetStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigNetStatusResponseBody = None,
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
            temp_model = ConfigNetStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        num: int = None,
        page: int = None,
        sale_id: str = None,
        status: str = None,
    ):
        # The name of the instance.
        self.name = name
        # The number of entries per page. Default value: 100.
        self.num = num
        # The page number. Default value: 1
        self.page = page
        # The ID of the anti-DDoS diversion instance.
        self.sale_id = sale_id
        # The status of the instance. Valid values:
        # 
        # - normal
        # - expired
        # - deleting
        # - stopped
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.num is not None:
            result['Num'] = self.num
        if self.page is not None:
            result['Page'] = self.page
        if self.sale_id is not None:
            result['SaleId'] = self.sale_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstanceResponseBodyDataInstancesSpec(TeaModel):
    def __init__(
        self,
        coverage: str = None,
        diversion_type: str = None,
        edition: str = None,
        idc_numbers: str = None,
        initial_installation: str = None,
        initial_qty: str = None,
        ip_subnet_nums: str = None,
        mitigation_analysis: str = None,
        mitigation_analysis_capacity: str = None,
        mitigation_capacity: str = None,
        mitigation_nums: str = None,
        normal_bandwidth: str = None,
    ):
        # The region of the asset.
        self.coverage = coverage
        # The diversion mode. Valid values: on-demand always-on
        self.diversion_type = diversion_type
        # The mitigation plan.
        self.edition = edition
        # The number of data centers. Valid values: 1 to 10.
        self.idc_numbers = idc_numbers
        # The initial installation mode.
        self.initial_installation = initial_installation
        # The initial installation quantity.
        self.initial_qty = initial_qty
        # The number of CIDR blocks. Value range: 1 to 10000.
        self.ip_subnet_nums = ip_subnet_nums
        # The mitigation analysis feature.
        self.mitigation_analysis = mitigation_analysis
        # The log storage capacity.
        self.mitigation_analysis_capacity = mitigation_analysis_capacity
        # The maximum mitigation capability.
        self.mitigation_capacity = mitigation_capacity
        # The number of mitigation sessions.
        self.mitigation_nums = mitigation_nums
        # The service traffic. Unit: Mbit/s.
        self.normal_bandwidth = normal_bandwidth

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coverage is not None:
            result['Coverage'] = self.coverage
        if self.diversion_type is not None:
            result['DiversionType'] = self.diversion_type
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.idc_numbers is not None:
            result['IdcNumbers'] = self.idc_numbers
        if self.initial_installation is not None:
            result['InitialInstallation'] = self.initial_installation
        if self.initial_qty is not None:
            result['InitialQty'] = self.initial_qty
        if self.ip_subnet_nums is not None:
            result['IpSubnetNums'] = self.ip_subnet_nums
        if self.mitigation_analysis is not None:
            result['MitigationAnalysis'] = self.mitigation_analysis
        if self.mitigation_analysis_capacity is not None:
            result['MitigationAnalysisCapacity'] = self.mitigation_analysis_capacity
        if self.mitigation_capacity is not None:
            result['MitigationCapacity'] = self.mitigation_capacity
        if self.mitigation_nums is not None:
            result['MitigationNums'] = self.mitigation_nums
        if self.normal_bandwidth is not None:
            result['NormalBandwidth'] = self.normal_bandwidth
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')
        if m.get('DiversionType') is not None:
            self.diversion_type = m.get('DiversionType')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('IdcNumbers') is not None:
            self.idc_numbers = m.get('IdcNumbers')
        if m.get('InitialInstallation') is not None:
            self.initial_installation = m.get('InitialInstallation')
        if m.get('InitialQty') is not None:
            self.initial_qty = m.get('InitialQty')
        if m.get('IpSubnetNums') is not None:
            self.ip_subnet_nums = m.get('IpSubnetNums')
        if m.get('MitigationAnalysis') is not None:
            self.mitigation_analysis = m.get('MitigationAnalysis')
        if m.get('MitigationAnalysisCapacity') is not None:
            self.mitigation_analysis_capacity = m.get('MitigationAnalysisCapacity')
        if m.get('MitigationCapacity') is not None:
            self.mitigation_capacity = m.get('MitigationCapacity')
        if m.get('MitigationNums') is not None:
            self.mitigation_nums = m.get('MitigationNums')
        if m.get('NormalBandwidth') is not None:
            self.normal_bandwidth = m.get('NormalBandwidth')
        return self


class ListInstanceResponseBodyDataInstances(TeaModel):
    def __init__(
        self,
        comment: str = None,
        gmt_create: str = None,
        gmt_expire: str = None,
        gmt_modify: str = None,
        instance_id: str = None,
        message: str = None,
        name: str = None,
        sale_id: str = None,
        spec: ListInstanceResponseBodyDataInstancesSpec = None,
        status: str = None,
        user_id: str = None,
    ):
        # The description.
        self.comment = comment
        # The purchase time.
        self.gmt_create = gmt_create
        # The expiration time.
        self.gmt_expire = gmt_expire
        # The update time.
        self.gmt_modify = gmt_modify
        # The alias of the instance.
        self.instance_id = instance_id
        # The configurations of the instance.
        self.message = message
        # The name of the instance.
        self.name = name
        # The ID of the instance.
        self.sale_id = sale_id
        # The specifications of the instance.
        self.spec = spec
        # The status of the instance. Valid values:
        # 
        # - normal
        # - expired
        # - deleting
        # - stopped
        self.status = status
        # The user ID.
        self.user_id = user_id

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_expire is not None:
            result['GmtExpire'] = self.gmt_expire
        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.sale_id is not None:
            result['SaleId'] = self.sale_id
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtExpire') is not None:
            self.gmt_expire = m.get('GmtExpire')
        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')
        if m.get('Spec') is not None:
            temp_model = ListInstanceResponseBodyDataInstancesSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        instances: List[ListInstanceResponseBodyDataInstances] = None,
        num: int = None,
        page: int = None,
        total: int = None,
    ):
        # The details of the anti-DDoS diversion instance.
        self.instances = instances
        # The number of entries per page.
        self.num = num
        # The page number.
        self.page = page
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.num is not None:
            result['Num'] = self.num
        if self.page is not None:
            result['Page'] = self.page
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstanceResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        # 
        # - 200: The request was successful.
        # - Other codes: The request failed.
        self.code = code
        # The returned result.
        self.data = data
        # The response parameters.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
            temp_model = ListInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceResponseBody = None,
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
            temp_model = ListInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryNetListRequest(TeaModel):
    def __init__(
        self,
        main_net: str = None,
        mode: str = None,
        net: str = None,
        num: int = None,
        page: int = None,
        sale_id: str = None,
    ):
        # The primary CIDR block of the anti-DDoS diversion instance for which an extended CIDR block is configured. If no extended CIDR blocks are configured for the anti-DDoS diversion instance, leave this parameter empty.
        self.main_net = main_net
        # The scheduling mode. Valid values:
        # 
        # - manual: manual scheduling
        # - netflow-auto: automatic scheduling
        self.mode = mode
        # The CIDR block of the anti-DDoS diversion instance.
        # 
        # 
        # > If no extended CIDR blocks are configured for the anti-DDoS diversion instance, this parameter specifies the CIDR block of the instance. If an extended CIDR block is configured for the anti-DDoS diversion instance, this parameter specifies the extended CIDR block that is configured for the instance. If this parameter is specified, the MainNet parameter is required.
        self.net = net
        # The number of entries per page. Default value: 100.
        self.num = num
        # The page number. Default value: 1
        self.page = page
        # The ID of the anti-DDoS diversion instance.
        self.sale_id = sale_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.main_net is not None:
            result['MainNet'] = self.main_net
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.net is not None:
            result['Net'] = self.net
        if self.num is not None:
            result['Num'] = self.num
        if self.page is not None:
            result['Page'] = self.page
        if self.sale_id is not None:
            result['SaleId'] = self.sale_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MainNet') is not None:
            self.main_net = m.get('MainNet')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Net') is not None:
            self.net = m.get('Net')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')
        return self


class QueryNetListResponseBodyDataNetsDDoSDefenseCleanTh(TeaModel):
    def __init__(
        self,
        mbps: int = None,
        pps: int = None,
    ):
        # The traffic scrubbing threshold in Mbit/s.
        self.mbps = mbps
        # The traffic scrubbing threshold in packets per second (pps)
        self.pps = pps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class QueryNetListResponseBodyDataNetsDDoSDefenseDjPolicy(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
    ):
        # The name of the mitigation policy.
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class QueryNetListResponseBodyDataNetsDDoSDefenseHoleTh(TeaModel):
    def __init__(
        self,
        thresh_mbps: int = None,
    ):
        # The blackhole filtering threshold.
        self.thresh_mbps = thresh_mbps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.thresh_mbps is not None:
            result['ThreshMbps'] = self.thresh_mbps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ThreshMbps') is not None:
            self.thresh_mbps = m.get('ThreshMbps')
        return self


class QueryNetListResponseBodyDataNetsDDoSDefense(TeaModel):
    def __init__(
        self,
        clean_th: QueryNetListResponseBodyDataNetsDDoSDefenseCleanTh = None,
        dj_policy: QueryNetListResponseBodyDataNetsDDoSDefenseDjPolicy = None,
        hole_th: QueryNetListResponseBodyDataNetsDDoSDefenseHoleTh = None,
    ):
        # The configuration of traffic scrubbing.
        self.clean_th = clean_th
        # The configuration of the mitigation policy.
        self.dj_policy = dj_policy
        # The configuration of blackhole filtering.
        self.hole_th = hole_th

    def validate(self):
        if self.clean_th:
            self.clean_th.validate()
        if self.dj_policy:
            self.dj_policy.validate()
        if self.hole_th:
            self.hole_th.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clean_th is not None:
            result['CleanTh'] = self.clean_th.to_map()
        if self.dj_policy is not None:
            result['DjPolicy'] = self.dj_policy.to_map()
        if self.hole_th is not None:
            result['HoleTh'] = self.hole_th.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CleanTh') is not None:
            temp_model = QueryNetListResponseBodyDataNetsDDoSDefenseCleanTh()
            self.clean_th = temp_model.from_map(m['CleanTh'])
        if m.get('DjPolicy') is not None:
            temp_model = QueryNetListResponseBodyDataNetsDDoSDefenseDjPolicy()
            self.dj_policy = temp_model.from_map(m['DjPolicy'])
        if m.get('HoleTh') is not None:
            temp_model = QueryNetListResponseBodyDataNetsDDoSDefenseHoleTh()
            self.hole_th = temp_model.from_map(m['HoleTh'])
        return self


class QueryNetListResponseBodyDataNetsDeclared(TeaModel):
    def __init__(
        self,
        declared: str = None,
        region: str = None,
    ):
        # Indicates whether the CIDR block is advertised. Valid values:
        # 
        # - 0: The CIDR block is not advertised.
        # - 1: The CIDR block is advertised.
        self.declared = declared
        # The region in which the CIDR block is advertised.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class QueryNetListResponseBodyDataNets(TeaModel):
    def __init__(
        self,
        ddo_sdefense: QueryNetListResponseBodyDataNetsDDoSDefense = None,
        declared: List[QueryNetListResponseBodyDataNetsDeclared] = None,
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
        # - 0: The CIDR block is not advertised.
        # - 1: The CIDR block is advertised.
        self.declared_state = declared_state
        # Indicates whether the forwarding configuration takes effect. Valid values:
        # 
        # - 0: The forwarding configuration takes effect.
        # - 1: The forwarding configuration does not take effect.
        # - -1: The forwarding configuration is being deleted.
        self.fwd_effect = fwd_effect
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modify = gmt_modify
        # The scheduling mode.
        self.mode = mode
        # The CIDR block of the anti-DDoS diversion instance.
        self.net = net
        # Indicates whether the CIDR block needs to be extended. Valid values:
        # 
        # - 0: The CIDR block needs to be extended.
        # - 1: The CIDR block does not need to be extended.
        self.net_extend = net_extend
        # The primary CIDR block.
        self.net_main = net_main
        # The type of the CIDR block.
        self.net_type = net_type
        self.permit = permit
        # The ID of the anti-DDoS diversion instance.
        self.sale_id = sale_id
        # The reinjection type.
        self.upstream_type = upstream_type
        # The user ID.
        self.user_id = user_id

    def validate(self):
        if self.ddo_sdefense:
            self.ddo_sdefense.validate()
        if self.declared:
            for k in self.declared:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddo_sdefense is not None:
            result['DDoSDefense'] = self.ddo_sdefense.to_map()
        result['Declared'] = []
        if self.declared is not None:
            for k in self.declared:
                result['Declared'].append(k.to_map() if k else None)
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
            temp_model = QueryNetListResponseBodyDataNetsDDoSDefense()
            self.ddo_sdefense = temp_model.from_map(m['DDoSDefense'])
        self.declared = []
        if m.get('Declared') is not None:
            for k in m.get('Declared'):
                temp_model = QueryNetListResponseBodyDataNetsDeclared()
                self.declared.append(temp_model.from_map(k))
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


class QueryNetListResponseBodyData(TeaModel):
    def __init__(
        self,
        nets: List[QueryNetListResponseBodyDataNets] = None,
        num: int = None,
        page: int = None,
        total: int = None,
    ):
        # The configuration of the CIDR block.
        self.nets = nets
        # The number of entries per page.
        self.num = num
        # The page number.
        self.page = page
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.nets:
            for k in self.nets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nets'] = []
        if self.nets is not None:
            for k in self.nets:
                result['Nets'].append(k.to_map() if k else None)
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
            for k in m.get('Nets'):
                temp_model = QueryNetListResponseBodyDataNets()
                self.nets.append(temp_model.from_map(k))
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryNetListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryNetListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        # 
        # - 200: The request was successful.
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = QueryNetListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryNetListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryNetListResponseBody = None,
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
            temp_model = QueryNetListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


