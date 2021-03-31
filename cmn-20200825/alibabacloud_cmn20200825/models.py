# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateDedicatedLineRequest(TeaModel):
    def __init__(
        self,
        physical_space_id: str = None,
        isp: str = None,
        bandwidth: int = None,
        dedicated_line_ip: str = None,
        dedicated_line_gateway: str = None,
        dedicated_line_role: str = None,
        device_id: str = None,
        device_port: str = None,
        client_token: str = None,
        instance_id: str = None,
    ):
        # 物理空间ID
        self.physical_space_id = physical_space_id
        # 运营商
        self.isp = isp
        # 宽带（Mbps）
        self.bandwidth = bandwidth
        # 专线IP
        self.dedicated_line_ip = dedicated_line_ip
        # 专线网关
        self.dedicated_line_gateway = dedicated_line_gateway
        # 专线角色
        self.dedicated_line_role = dedicated_line_role
        # 关联设备ID
        self.device_id = device_id
        # 关联设备端口名称
        self.device_port = device_port
        # 幂等校验 token
        self.client_token = client_token
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.dedicated_line_ip is not None:
            result['DedicatedLineIp'] = self.dedicated_line_ip
        if self.dedicated_line_gateway is not None:
            result['DedicatedLineGateway'] = self.dedicated_line_gateway
        if self.dedicated_line_role is not None:
            result['DedicatedLineRole'] = self.dedicated_line_role
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_port is not None:
            result['DevicePort'] = self.device_port
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('DedicatedLineIp') is not None:
            self.dedicated_line_ip = m.get('DedicatedLineIp')
        if m.get('DedicatedLineGateway') is not None:
            self.dedicated_line_gateway = m.get('DedicatedLineGateway')
        if m.get('DedicatedLineRole') is not None:
            self.dedicated_line_role = m.get('DedicatedLineRole')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DevicePort') is not None:
            self.device_port = m.get('DevicePort')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateDedicatedLineResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_line_id: str = None,
        request_id: str = None,
    ):
        # 资源实例ID，如ECS实例的创建接口CreateInstance应返回InstanceId。
        self.dedicated_line_id = dedicated_line_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDedicatedLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDedicatedLineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDedicatedLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeviceRequest(TeaModel):
    def __init__(
        self,
        device_form_id: str = None,
        physical_space_id: str = None,
        host_name: str = None,
        ip: str = None,
        sn: str = None,
        mac: str = None,
        vendor: str = None,
        model: str = None,
        service_status: str = None,
        security_domain: str = None,
        login_type: str = None,
        login_username: str = None,
        login_password: str = None,
        snmp_account_version: str = None,
        snmp_community: str = None,
        snmp_account_type: str = None,
        snmp_security_level: str = None,
        snmp_username: str = None,
        snmp_auth_passphrase: str = None,
        snmp_auth_protocol: str = None,
        snmp_privacy_passphase: str = None,
        snmp_privacy_protocol: str = None,
        ext_attributes: str = None,
        client_token: str = None,
        instance_id: str = None,
    ):
        # 设备形态ID
        self.device_form_id = device_form_id
        # 物理空间ID
        self.physical_space_id = physical_space_id
        # 主机名
        self.host_name = host_name
        # 设备IP
        self.ip = ip
        # 设备SN
        self.sn = sn
        # 设备MAC地址
        self.mac = mac
        # 设备厂商
        self.vendor = vendor
        # 设备型号
        self.model = model
        # 设备状态
        self.service_status = service_status
        # 设备安全域
        self.security_domain = security_domain
        # 登录类型
        self.login_type = login_type
        # 登录账号
        self.login_username = login_username
        # 登录密码
        self.login_password = login_password
        # SNMP 版本号
        self.snmp_account_version = snmp_account_version
        # SNMP Community
        self.snmp_community = snmp_community
        # SNMP 账号类型
        self.snmp_account_type = snmp_account_type
        # SNMP 安全级别
        self.snmp_security_level = snmp_security_level
        # SNMP 用户名
        self.snmp_username = snmp_username
        # SNMP Auth PassPhrase
        self.snmp_auth_passphrase = snmp_auth_passphrase
        # SNMP Auth Protocol
        self.snmp_auth_protocol = snmp_auth_protocol
        # SNMP Privacy Passphase
        self.snmp_privacy_passphase = snmp_privacy_passphase
        # SNMP Privacy Protocol
        self.snmp_privacy_protocol = snmp_privacy_protocol
        # 设备额外属性
        self.ext_attributes = ext_attributes
        # 幂等校验 token
        self.client_token = client_token
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.model is not None:
            result['Model'] = self.model
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.login_type is not None:
            result['LoginType'] = self.login_type
        if self.login_username is not None:
            result['LoginUsername'] = self.login_username
        if self.login_password is not None:
            result['LoginPassword'] = self.login_password
        if self.snmp_account_version is not None:
            result['SnmpAccountVersion'] = self.snmp_account_version
        if self.snmp_community is not None:
            result['SnmpCommunity'] = self.snmp_community
        if self.snmp_account_type is not None:
            result['SnmpAccountType'] = self.snmp_account_type
        if self.snmp_security_level is not None:
            result['SnmpSecurityLevel'] = self.snmp_security_level
        if self.snmp_username is not None:
            result['SnmpUsername'] = self.snmp_username
        if self.snmp_auth_passphrase is not None:
            result['SnmpAuthPassphrase'] = self.snmp_auth_passphrase
        if self.snmp_auth_protocol is not None:
            result['SnmpAuthProtocol'] = self.snmp_auth_protocol
        if self.snmp_privacy_passphase is not None:
            result['SnmpPrivacyPassphase'] = self.snmp_privacy_passphase
        if self.snmp_privacy_protocol is not None:
            result['SnmpPrivacyProtocol'] = self.snmp_privacy_protocol
        if self.ext_attributes is not None:
            result['ExtAttributes'] = self.ext_attributes
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('LoginType') is not None:
            self.login_type = m.get('LoginType')
        if m.get('LoginUsername') is not None:
            self.login_username = m.get('LoginUsername')
        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')
        if m.get('SnmpAccountVersion') is not None:
            self.snmp_account_version = m.get('SnmpAccountVersion')
        if m.get('SnmpCommunity') is not None:
            self.snmp_community = m.get('SnmpCommunity')
        if m.get('SnmpAccountType') is not None:
            self.snmp_account_type = m.get('SnmpAccountType')
        if m.get('SnmpSecurityLevel') is not None:
            self.snmp_security_level = m.get('SnmpSecurityLevel')
        if m.get('SnmpUsername') is not None:
            self.snmp_username = m.get('SnmpUsername')
        if m.get('SnmpAuthPassphrase') is not None:
            self.snmp_auth_passphrase = m.get('SnmpAuthPassphrase')
        if m.get('SnmpAuthProtocol') is not None:
            self.snmp_auth_protocol = m.get('SnmpAuthProtocol')
        if m.get('SnmpPrivacyPassphase') is not None:
            self.snmp_privacy_passphase = m.get('SnmpPrivacyPassphase')
        if m.get('SnmpPrivacyProtocol') is not None:
            self.snmp_privacy_protocol = m.get('SnmpPrivacyProtocol')
        if m.get('ExtAttributes') is not None:
            self.ext_attributes = m.get('ExtAttributes')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 资源实例ID，如ECS实例的创建接口CreateInstance应返回InstanceId。
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class CreateDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeviceFormRequest(TeaModel):
    def __init__(
        self,
        device_form_name: str = None,
        config_compare: bool = None,
        account_config: bool = None,
        detail_display: bool = None,
        unique_key: str = None,
        client_token: str = None,
        instance_id: str = None,
    ):
        # 设备形态名称
        self.device_form_name = device_form_name
        # 是否支持配置生成
        self.config_compare = config_compare
        # 是否需要账号配置
        self.account_config = account_config
        # 是否展示设备详情
        self.detail_display = detail_display
        # 设备形态的主键
        self.unique_key = unique_key
        # 幂等校验 token
        self.client_token = client_token
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        if self.config_compare is not None:
            result['ConfigCompare'] = self.config_compare
        if self.account_config is not None:
            result['AccountConfig'] = self.account_config
        if self.detail_display is not None:
            result['DetailDisplay'] = self.detail_display
        if self.unique_key is not None:
            result['UniqueKey'] = self.unique_key
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        if m.get('ConfigCompare') is not None:
            self.config_compare = m.get('ConfigCompare')
        if m.get('AccountConfig') is not None:
            self.account_config = m.get('AccountConfig')
        if m.get('DetailDisplay') is not None:
            self.detail_display = m.get('DetailDisplay')
        if m.get('UniqueKey') is not None:
            self.unique_key = m.get('UniqueKey')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateDeviceFormResponseBody(TeaModel):
    def __init__(
        self,
        device_form_id: str = None,
        request_id: str = None,
    ):
        # 资源实例ID，如ECS实例的创建接口CreateInstance应返回InstanceId。
        self.device_form_id = device_form_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDeviceFormResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDeviceFormResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDeviceFormResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDevicePropertyRequest(TeaModel):
    def __init__(
        self,
        device_form_id: str = None,
        property_name: str = None,
        property_key: str = None,
        property_format: str = None,
        property_content: str = None,
        client_token: str = None,
        instance_id: str = None,
    ):
        # 设备形态ID
        self.device_form_id = device_form_id
        # 属性名称
        self.property_name = property_name
        # 属性主键
        self.property_key = property_key
        # 属性格式
        self.property_format = property_format
        # 属性内容
        self.property_content = property_content
        # 幂等校验 token
        self.client_token = client_token
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.property_format is not None:
            result['PropertyFormat'] = self.property_format
        if self.property_content is not None:
            result['PropertyContent'] = self.property_content
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('PropertyFormat') is not None:
            self.property_format = m.get('PropertyFormat')
        if m.get('PropertyContent') is not None:
            self.property_content = m.get('PropertyContent')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateDevicePropertyResponseBody(TeaModel):
    def __init__(
        self,
        device_property_id: str = None,
        request_id: str = None,
    ):
        # 资源实例ID，如ECS实例的创建接口CreateInstance应返回InstanceId。
        self.device_property_id = device_property_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_property_id is not None:
            result['DevicePropertyId'] = self.device_property_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevicePropertyId') is not None:
            self.device_property_id = m.get('DevicePropertyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDevicePropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDevicePropertyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDevicePropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMonitorItemRequestAlarmRuleList(TeaModel):
    def __init__(
        self,
        alarm_status: str = None,
        variable: str = None,
        expression: str = None,
        value: str = None,
    ):
        # 告警状态
        self.alarm_status = alarm_status
        # 指标名
        self.variable = variable
        # 表达式
        self.expression = expression
        # 比较值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.variable is not None:
            result['Variable'] = self.variable
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('Variable') is not None:
            self.variable = m.get('Variable')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateMonitorItemRequest(TeaModel):
    def __init__(
        self,
        monitor_item_name: str = None,
        monitor_item_description: str = None,
        data_item: str = None,
        security_domain: str = None,
        analysis_code: str = None,
        collection_type: str = None,
        effective: int = None,
        config: str = None,
        exec_interval: int = None,
        device_form: str = None,
        alarm_rule_list: List[CreateMonitorItemRequestAlarmRuleList] = None,
        type: str = None,
        client_token: str = None,
        instance_id: str = None,
    ):
        # 监控项名称
        self.monitor_item_name = monitor_item_name
        # 监控项描述
        self.monitor_item_description = monitor_item_description
        # 数据项
        self.data_item = data_item
        # 安全域
        self.security_domain = security_domain
        # 解析代码
        self.analysis_code = analysis_code
        # 采集类型
        self.collection_type = collection_type
        # 是否启用
        self.effective = effective
        # 监控项参数配置
        self.config = config
        # 执行间隔(s)
        self.exec_interval = exec_interval
        # 设备形态
        self.device_form = device_form
        # 告警规则列表
        self.alarm_rule_list = alarm_rule_list
        # 类型
        self.type = type
        # 幂等参数
        self.client_token = client_token
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        if self.alarm_rule_list:
            for k in self.alarm_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.monitor_item_name is not None:
            result['MonitorItemName'] = self.monitor_item_name
        if self.monitor_item_description is not None:
            result['MonitorItemDescription'] = self.monitor_item_description
        if self.data_item is not None:
            result['DataItem'] = self.data_item
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.analysis_code is not None:
            result['AnalysisCode'] = self.analysis_code
        if self.collection_type is not None:
            result['CollectionType'] = self.collection_type
        if self.effective is not None:
            result['Effective'] = self.effective
        if self.config is not None:
            result['Config'] = self.config
        if self.exec_interval is not None:
            result['ExecInterval'] = self.exec_interval
        if self.device_form is not None:
            result['DeviceForm'] = self.device_form
        result['AlarmRuleList'] = []
        if self.alarm_rule_list is not None:
            for k in self.alarm_rule_list:
                result['AlarmRuleList'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorItemName') is not None:
            self.monitor_item_name = m.get('MonitorItemName')
        if m.get('MonitorItemDescription') is not None:
            self.monitor_item_description = m.get('MonitorItemDescription')
        if m.get('DataItem') is not None:
            self.data_item = m.get('DataItem')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('AnalysisCode') is not None:
            self.analysis_code = m.get('AnalysisCode')
        if m.get('CollectionType') is not None:
            self.collection_type = m.get('CollectionType')
        if m.get('Effective') is not None:
            self.effective = m.get('Effective')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ExecInterval') is not None:
            self.exec_interval = m.get('ExecInterval')
        if m.get('DeviceForm') is not None:
            self.device_form = m.get('DeviceForm')
        self.alarm_rule_list = []
        if m.get('AlarmRuleList') is not None:
            for k in m.get('AlarmRuleList'):
                temp_model = CreateMonitorItemRequestAlarmRuleList()
                self.alarm_rule_list.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateMonitorItemResponseBody(TeaModel):
    def __init__(
        self,
        monitor_item_id: str = None,
        request_id: str = None,
    ):
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMonitorItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMonitorItemResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateMonitorItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePhysicalSpaceRequest(TeaModel):
    def __init__(
        self,
        physical_space_name: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        address: str = None,
        client_token: str = None,
        instance_id: str = None,
    ):
        # 物理空间名称
        self.physical_space_name = physical_space_name
        # 所属国家
        self.country = country
        # 所属省份
        self.province = province
        # 所属城市
        self.city = city
        # 具体地址
        self.address = address
        # 幂等校验 token
        self.client_token = client_token
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.physical_space_name is not None:
            result['PhysicalSpaceName'] = self.physical_space_name
        if self.country is not None:
            result['Country'] = self.country
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.address is not None:
            result['Address'] = self.address
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalSpaceName') is not None:
            self.physical_space_name = m.get('PhysicalSpaceName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreatePhysicalSpaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        physical_space_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 物理空间ID
        self.physical_space_id = physical_space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        return self


class CreatePhysicalSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePhysicalSpaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreatePhysicalSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRealtimeTaskRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        script: str = None,
        instance_id: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 模板执行脚本
        self.script = script
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.script is not None:
            result['Script'] = self.script
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateRealtimeTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 实时任务ID
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateRealtimeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRealtimeTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRealtimeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTimePeriodRequest(TeaModel):
    def __init__(
        self,
        time_period_name: str = None,
        time_period_description: str = None,
        expression: str = None,
        client_token: str = None,
        instance_id: str = None,
    ):
        # 时间段名称
        self.time_period_name = time_period_name
        # 描述
        self.time_period_description = time_period_description
        # cron表达式
        self.expression = expression
        # 幂等参数
        self.client_token = client_token
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time_period_name is not None:
            result['TimePeriodName'] = self.time_period_name
        if self.time_period_description is not None:
            result['TimePeriodDescription'] = self.time_period_description
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimePeriodName') is not None:
            self.time_period_name = m.get('TimePeriodName')
        if m.get('TimePeriodDescription') is not None:
            self.time_period_description = m.get('TimePeriodDescription')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateTimePeriodResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        time_period_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 时间段ID
        self.time_period_id = time_period_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_period_id is not None:
            result['TimePeriodId'] = self.time_period_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimePeriodId') is not None:
            self.time_period_id = m.get('TimePeriodId')
        return self


class CreateTimePeriodResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTimePeriodResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateTimePeriodResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDedicatedLineRequest(TeaModel):
    def __init__(
        self,
        dedicated_line_id: str = None,
        instance_id: str = None,
    ):
        # 实例 ID。
        self.dedicated_line_id = dedicated_line_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteDedicatedLineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDedicatedLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDedicatedLineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDedicatedLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeviceRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        instance_id: str = None,
    ):
        # 实例 ID。
        self.device_id = device_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeviceFormRequest(TeaModel):
    def __init__(
        self,
        device_form_id: str = None,
        instance_id: str = None,
    ):
        # 实例 ID。
        self.device_form_id = device_form_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteDeviceFormResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDeviceFormResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDeviceFormResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDeviceFormResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDevicePropertyRequest(TeaModel):
    def __init__(
        self,
        device_property_id: str = None,
        instance_id: str = None,
    ):
        # 实例 ID。
        self.device_property_id = device_property_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_property_id is not None:
            result['DevicePropertyId'] = self.device_property_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevicePropertyId') is not None:
            self.device_property_id = m.get('DevicePropertyId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteDevicePropertyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDevicePropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDevicePropertyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDevicePropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInspectionTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        instance_id: str = None,
    ):
        # 周期性任务的ID
        self.task_id = task_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteInspectionTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInspectionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInspectionTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteInspectionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePhysicalSpaceRequest(TeaModel):
    def __init__(
        self,
        physical_space_id: str = None,
        instance_id: str = None,
    ):
        # 实例 ID。
        self.physical_space_id = physical_space_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeletePhysicalSpaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePhysicalSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePhysicalSpaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeletePhysicalSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableNotificationRequestList(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        monitor_item_id: str = None,
        aggregate_data_id: str = None,
        type: str = None,
        dedicated_line_id: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 类型
        self.type = type
        # 专线ID
        self.dedicated_line_id = dedicated_line_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.type is not None:
            result['Type'] = self.type
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        return self


class DisableNotificationRequest(TeaModel):
    def __init__(
        self,
        expiry_time: str = None,
        reason: str = None,
        list: List[DisableNotificationRequestList] = None,
        instance_id: str = None,
    ):
        # 到期时间
        self.expiry_time = expiry_time
        # 关闭原因
        self.reason = reason
        # 关闭通知的对象
        self.list = list
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        if self.reason is not None:
            result['Reason'] = self.reason
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DisableNotificationRequestList()
                self.list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisableNotificationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # request id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableNotificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableNotificationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableNotificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableNotificationRequestList(TeaModel):
    def __init__(
        self,
        type: str = None,
        monitor_item_id: str = None,
        device_id: str = None,
        aggregate_data_id: str = None,
        dedicated_line_id: str = None,
    ):
        # 类型
        self.type = type
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 设备ID
        self.device_id = device_id
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 专线ID
        self.dedicated_line_id = dedicated_line_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        return self


class EnableNotificationRequest(TeaModel):
    def __init__(
        self,
        list: List[EnableNotificationRequestList] = None,
        instance_id: str = None,
    ):
        # 通知对象
        self.list = list
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = EnableNotificationRequestList()
                self.list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EnableNotificationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # request id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableNotificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableNotificationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableNotificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlarmStatusRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        monitor_item_id: str = None,
        type: str = None,
        aggregate_data_id: str = None,
        dedicated_line_id: str = None,
        instance_id: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 数据类型
        self.type = type
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 专线ID
        self.dedicated_line_id = dedicated_line_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.type is not None:
            result['Type'] = self.type
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetAlarmStatusResponseBodyAlarmStatusResourceDevice(TeaModel):
    def __init__(
        self,
        host_name: str = None,
        ip: str = None,
        vendor: str = None,
        model: str = None,
        status: str = None,
        sn: str = None,
        space: str = None,
        device_id: str = None,
        security_domain: str = None,
        device_form: str = None,
    ):
        # 设备名
        self.host_name = host_name
        # IP
        self.ip = ip
        # 厂商
        self.vendor = vendor
        # 型号
        self.model = model
        # 状态
        self.status = status
        # sn
        self.sn = sn
        # 物理空间
        self.space = space
        # 设备ID
        self.device_id = device_id
        # 安全域
        self.security_domain = security_domain
        # 设备形态
        self.device_form = device_form

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.model is not None:
            result['Model'] = self.model
        if self.status is not None:
            result['Status'] = self.status
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.space is not None:
            result['Space'] = self.space
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.device_form is not None:
            result['DeviceForm'] = self.device_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Space') is not None:
            self.space = m.get('Space')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('DeviceForm') is not None:
            self.device_form = m.get('DeviceForm')
        return self


class GetAlarmStatusResponseBodyAlarmStatusMonitorItem(TeaModel):
    def __init__(
        self,
        monitor_item_name: str = None,
        monitor_item_description: str = None,
        security_domain: str = None,
        collection_type: str = None,
        exec_interval: str = None,
        monitor_item_id: str = None,
        device_form: str = None,
        effective: int = None,
    ):
        # 监控项名称
        self.monitor_item_name = monitor_item_name
        # 描述
        self.monitor_item_description = monitor_item_description
        # 安全域
        self.security_domain = security_domain
        # 采集类型
        self.collection_type = collection_type
        # 执行间隔
        self.exec_interval = exec_interval
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 设备形态
        self.device_form = device_form
        # 是否启用
        self.effective = effective

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.monitor_item_name is not None:
            result['MonitorItemName'] = self.monitor_item_name
        if self.monitor_item_description is not None:
            result['MonitorItemDescription'] = self.monitor_item_description
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.collection_type is not None:
            result['CollectionType'] = self.collection_type
        if self.exec_interval is not None:
            result['ExecInterval'] = self.exec_interval
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.device_form is not None:
            result['DeviceForm'] = self.device_form
        if self.effective is not None:
            result['Effective'] = self.effective
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorItemName') is not None:
            self.monitor_item_name = m.get('MonitorItemName')
        if m.get('MonitorItemDescription') is not None:
            self.monitor_item_description = m.get('MonitorItemDescription')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('CollectionType') is not None:
            self.collection_type = m.get('CollectionType')
        if m.get('ExecInterval') is not None:
            self.exec_interval = m.get('ExecInterval')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('DeviceForm') is not None:
            self.device_form = m.get('DeviceForm')
        if m.get('Effective') is not None:
            self.effective = m.get('Effective')
        return self


class GetAlarmStatusResponseBodyAlarmStatusNotificationSwitch(TeaModel):
    def __init__(
        self,
        reason: str = None,
        expiry_time: str = None,
    ):
        # 关闭原因
        self.reason = reason
        # 关闭到期时间
        self.expiry_time = expiry_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        return self


class GetAlarmStatusResponseBodyAlarmStatusAggregateData(TeaModel):
    def __init__(
        self,
        aggregate_mode: str = None,
        aggregate_data_description: str = None,
        data_item: str = None,
        aggregate_data_name: str = None,
        device_id: str = None,
        is_all_device: int = None,
        aggregate_data_id: str = None,
        monitor_item_id: str = None,
    ):
        # 聚合方式
        self.aggregate_mode = aggregate_mode
        # 描述
        self.aggregate_data_description = aggregate_data_description
        # 数据项
        self.data_item = data_item
        # 聚合数据名称
        self.aggregate_data_name = aggregate_data_name
        # 设备ID
        self.device_id = device_id
        # 是否聚合全部设备
        self.is_all_device = is_all_device
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 监控项ID
        self.monitor_item_id = monitor_item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregate_mode is not None:
            result['AggregateMode'] = self.aggregate_mode
        if self.aggregate_data_description is not None:
            result['AggregateDataDescription'] = self.aggregate_data_description
        if self.data_item is not None:
            result['DataItem'] = self.data_item
        if self.aggregate_data_name is not None:
            result['AggregateDataName'] = self.aggregate_data_name
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.is_all_device is not None:
            result['IsAllDevice'] = self.is_all_device
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregateMode') is not None:
            self.aggregate_mode = m.get('AggregateMode')
        if m.get('AggregateDataDescription') is not None:
            self.aggregate_data_description = m.get('AggregateDataDescription')
        if m.get('DataItem') is not None:
            self.data_item = m.get('DataItem')
        if m.get('AggregateDataName') is not None:
            self.aggregate_data_name = m.get('AggregateDataName')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('IsAllDevice') is not None:
            self.is_all_device = m.get('IsAllDevice')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        return self


class GetAlarmStatusResponseBodyAlarmStatusDedicatedLine(TeaModel):
    def __init__(
        self,
        dedicated_line_name: str = None,
        space: str = None,
        port_name: str = None,
        device_id: str = None,
        bandwidth: str = None,
        ip: str = None,
    ):
        # 专线名称
        self.dedicated_line_name = dedicated_line_name
        # 物理空间
        self.space = space
        # 端口名
        self.port_name = port_name
        # 设备ID
        self.device_id = device_id
        # 带宽
        self.bandwidth = bandwidth
        # IP
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_line_name is not None:
            result['DedicatedLineName'] = self.dedicated_line_name
        if self.space is not None:
            result['Space'] = self.space
        if self.port_name is not None:
            result['PortName'] = self.port_name
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedLineName') is not None:
            self.dedicated_line_name = m.get('DedicatedLineName')
        if m.get('Space') is not None:
            self.space = m.get('Space')
        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class GetAlarmStatusResponseBodyAlarmStatus(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        monitor_item_id: str = None,
        collection_time: str = None,
        receive_time: str = None,
        alarm_rule: str = None,
        alarm_status: str = None,
        result: str = None,
        abnormal_data_item: str = None,
        unique_key: str = None,
        response_code: str = None,
        resource_device: GetAlarmStatusResponseBodyAlarmStatusResourceDevice = None,
        monitor_item: GetAlarmStatusResponseBodyAlarmStatusMonitorItem = None,
        first_abnormal_time: str = None,
        notification_switch: GetAlarmStatusResponseBodyAlarmStatusNotificationSwitch = None,
        aggregate_data_id: str = None,
        dedicated_line_id: str = None,
        aggregate_data: GetAlarmStatusResponseBodyAlarmStatusAggregateData = None,
        dedicated_line: GetAlarmStatusResponseBodyAlarmStatusDedicatedLine = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 采集时间
        self.collection_time = collection_time
        # 接收时间
        self.receive_time = receive_time
        # 命中告警规则
        self.alarm_rule = alarm_rule
        # 告警状态
        self.alarm_status = alarm_status
        # 采集结果
        self.result = result
        # 异常数据项
        self.abnormal_data_item = abnormal_data_item
        # 索引
        self.unique_key = unique_key
        # 采集状态码
        self.response_code = response_code
        # 设备
        self.resource_device = resource_device
        # 监控项
        self.monitor_item = monitor_item
        # 首次异常时间
        self.first_abnormal_time = first_abnormal_time
        # 告警开关
        self.notification_switch = notification_switch
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 专线ID
        self.dedicated_line_id = dedicated_line_id
        # 聚合数据详情
        self.aggregate_data = aggregate_data
        # 专线详情
        self.dedicated_line = dedicated_line

    def validate(self):
        if self.resource_device:
            self.resource_device.validate()
        if self.monitor_item:
            self.monitor_item.validate()
        if self.notification_switch:
            self.notification_switch.validate()
        if self.aggregate_data:
            self.aggregate_data.validate()
        if self.dedicated_line:
            self.dedicated_line.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.collection_time is not None:
            result['CollectionTime'] = self.collection_time
        if self.receive_time is not None:
            result['ReceiveTime'] = self.receive_time
        if self.alarm_rule is not None:
            result['AlarmRule'] = self.alarm_rule
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.result is not None:
            result['Result'] = self.result
        if self.abnormal_data_item is not None:
            result['AbnormalDataItem'] = self.abnormal_data_item
        if self.unique_key is not None:
            result['UniqueKey'] = self.unique_key
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.resource_device is not None:
            result['ResourceDevice'] = self.resource_device.to_map()
        if self.monitor_item is not None:
            result['MonitorItem'] = self.monitor_item.to_map()
        if self.first_abnormal_time is not None:
            result['FirstAbnormalTime'] = self.first_abnormal_time
        if self.notification_switch is not None:
            result['NotificationSwitch'] = self.notification_switch.to_map()
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.aggregate_data is not None:
            result['AggregateData'] = self.aggregate_data.to_map()
        if self.dedicated_line is not None:
            result['DedicatedLine'] = self.dedicated_line.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('CollectionTime') is not None:
            self.collection_time = m.get('CollectionTime')
        if m.get('ReceiveTime') is not None:
            self.receive_time = m.get('ReceiveTime')
        if m.get('AlarmRule') is not None:
            self.alarm_rule = m.get('AlarmRule')
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('AbnormalDataItem') is not None:
            self.abnormal_data_item = m.get('AbnormalDataItem')
        if m.get('UniqueKey') is not None:
            self.unique_key = m.get('UniqueKey')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('ResourceDevice') is not None:
            temp_model = GetAlarmStatusResponseBodyAlarmStatusResourceDevice()
            self.resource_device = temp_model.from_map(m['ResourceDevice'])
        if m.get('MonitorItem') is not None:
            temp_model = GetAlarmStatusResponseBodyAlarmStatusMonitorItem()
            self.monitor_item = temp_model.from_map(m['MonitorItem'])
        if m.get('FirstAbnormalTime') is not None:
            self.first_abnormal_time = m.get('FirstAbnormalTime')
        if m.get('NotificationSwitch') is not None:
            temp_model = GetAlarmStatusResponseBodyAlarmStatusNotificationSwitch()
            self.notification_switch = temp_model.from_map(m['NotificationSwitch'])
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('AggregateData') is not None:
            temp_model = GetAlarmStatusResponseBodyAlarmStatusAggregateData()
            self.aggregate_data = temp_model.from_map(m['AggregateData'])
        if m.get('DedicatedLine') is not None:
            temp_model = GetAlarmStatusResponseBodyAlarmStatusDedicatedLine()
            self.dedicated_line = temp_model.from_map(m['DedicatedLine'])
        return self


class GetAlarmStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        alarm_status: GetAlarmStatusResponseBodyAlarmStatus = None,
    ):
        # request Id
        self.request_id = request_id
        # 告警状态
        self.alarm_status = alarm_status

    def validate(self):
        if self.alarm_status:
            self.alarm_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AlarmStatus') is not None:
            temp_model = GetAlarmStatusResponseBodyAlarmStatus()
            self.alarm_status = temp_model.from_map(m['AlarmStatus'])
        return self


class GetAlarmStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAlarmStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAlarmStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDedicatedLineRequest(TeaModel):
    def __init__(
        self,
        dedicated_line_id: str = None,
        instance_id: str = None,
    ):
        # 实例 ID。
        self.dedicated_line_id = dedicated_line_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetDedicatedLineResponseBodyDedicatedLine(TeaModel):
    def __init__(
        self,
        dedicated_line_id: str = None,
        isp: str = None,
        bandwidth: int = None,
        dedicated_line_ip: str = None,
        dedicated_line_gateway: str = None,
        dedicated_line_role: str = None,
        device_id: str = None,
        device_port: str = None,
        device_name: str = None,
        physical_space_id: str = None,
    ):
        # 专线ID
        self.dedicated_line_id = dedicated_line_id
        # 运营商
        self.isp = isp
        # 宽带（Mbps）
        self.bandwidth = bandwidth
        # 专线IP
        self.dedicated_line_ip = dedicated_line_ip
        # 专线网关
        self.dedicated_line_gateway = dedicated_line_gateway
        # 专线角色
        self.dedicated_line_role = dedicated_line_role
        # 关联设备ID
        self.device_id = device_id
        # 关联设备端口名称
        self.device_port = device_port
        # 关联设备名称
        self.device_name = device_name
        # 物理空间ID
        self.physical_space_id = physical_space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.dedicated_line_ip is not None:
            result['DedicatedLineIp'] = self.dedicated_line_ip
        if self.dedicated_line_gateway is not None:
            result['DedicatedLineGateway'] = self.dedicated_line_gateway
        if self.dedicated_line_role is not None:
            result['DedicatedLineRole'] = self.dedicated_line_role
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_port is not None:
            result['DevicePort'] = self.device_port
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('DedicatedLineIp') is not None:
            self.dedicated_line_ip = m.get('DedicatedLineIp')
        if m.get('DedicatedLineGateway') is not None:
            self.dedicated_line_gateway = m.get('DedicatedLineGateway')
        if m.get('DedicatedLineRole') is not None:
            self.dedicated_line_role = m.get('DedicatedLineRole')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DevicePort') is not None:
            self.device_port = m.get('DevicePort')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        return self


class GetDedicatedLineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dedicated_line: GetDedicatedLineResponseBodyDedicatedLine = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 物理空间专线详情
        self.dedicated_line = dedicated_line

    def validate(self):
        if self.dedicated_line:
            self.dedicated_line.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dedicated_line is not None:
            result['DedicatedLine'] = self.dedicated_line.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DedicatedLine') is not None:
            temp_model = GetDedicatedLineResponseBodyDedicatedLine()
            self.dedicated_line = temp_model.from_map(m['DedicatedLine'])
        return self


class GetDedicatedLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDedicatedLineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDedicatedLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        instance_id: str = None,
    ):
        # 实例 ID。
        self.device_id = device_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetDeviceResponseBodyDevice(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        device_form_id: str = None,
        device_form_name: str = None,
        physical_space_id: str = None,
        physical_space_name: str = None,
        host_name: str = None,
        ip: str = None,
        sn: str = None,
        mac: str = None,
        vendor: str = None,
        model: str = None,
        security_domain: str = None,
        service_status: str = None,
        login_type: str = None,
        login_username: str = None,
        login_password: str = None,
        snmp_account_version: str = None,
        snmp_community: str = None,
        snmp_account_type: str = None,
        snmp_security_level: str = None,
        snmp_username: str = None,
        snmp_auth_passphrase: str = None,
        snmp_auth_protocol: str = None,
        snmp_privacy_passphase: str = None,
        snmp_privacy_protocol: str = None,
        ext_attributes: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 设备形态ID
        self.device_form_id = device_form_id
        # 设备形态名称
        self.device_form_name = device_form_name
        # 物理空间ID
        self.physical_space_id = physical_space_id
        # 物理空间名称
        self.physical_space_name = physical_space_name
        # 主机名
        self.host_name = host_name
        # 设备IP
        self.ip = ip
        # 设备SN
        self.sn = sn
        # 设备MAC地址
        self.mac = mac
        # 设备厂商
        self.vendor = vendor
        # 设备型号
        self.model = model
        # 设备安全域
        self.security_domain = security_domain
        # 设备状态
        self.service_status = service_status
        # 登录类型
        self.login_type = login_type
        # 登录账号
        self.login_username = login_username
        # 登录密码
        self.login_password = login_password
        # SNMP版本号
        self.snmp_account_version = snmp_account_version
        # SNMP Community
        self.snmp_community = snmp_community
        # SNMP 账号类型
        self.snmp_account_type = snmp_account_type
        # SNMP 安全级别
        self.snmp_security_level = snmp_security_level
        # SNMP 用户名
        self.snmp_username = snmp_username
        # SNMP Auth PassPhrase
        self.snmp_auth_passphrase = snmp_auth_passphrase
        # SNMP Auth Protocol
        self.snmp_auth_protocol = snmp_auth_protocol
        # SNMP Privacy Passphase
        self.snmp_privacy_passphase = snmp_privacy_passphase
        # SNMP Privacy Protocol
        self.snmp_privacy_protocol = snmp_privacy_protocol
        # 设备额外属性
        self.ext_attributes = ext_attributes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.physical_space_name is not None:
            result['PhysicalSpaceName'] = self.physical_space_name
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.model is not None:
            result['Model'] = self.model
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.login_type is not None:
            result['LoginType'] = self.login_type
        if self.login_username is not None:
            result['LoginUsername'] = self.login_username
        if self.login_password is not None:
            result['LoginPassword'] = self.login_password
        if self.snmp_account_version is not None:
            result['SnmpAccountVersion'] = self.snmp_account_version
        if self.snmp_community is not None:
            result['SnmpCommunity'] = self.snmp_community
        if self.snmp_account_type is not None:
            result['SnmpAccountType'] = self.snmp_account_type
        if self.snmp_security_level is not None:
            result['SnmpSecurityLevel'] = self.snmp_security_level
        if self.snmp_username is not None:
            result['SnmpUsername'] = self.snmp_username
        if self.snmp_auth_passphrase is not None:
            result['SnmpAuthPassphrase'] = self.snmp_auth_passphrase
        if self.snmp_auth_protocol is not None:
            result['SnmpAuthProtocol'] = self.snmp_auth_protocol
        if self.snmp_privacy_passphase is not None:
            result['SnmpPrivacyPassphase'] = self.snmp_privacy_passphase
        if self.snmp_privacy_protocol is not None:
            result['SnmpPrivacyProtocol'] = self.snmp_privacy_protocol
        if self.ext_attributes is not None:
            result['ExtAttributes'] = self.ext_attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('PhysicalSpaceName') is not None:
            self.physical_space_name = m.get('PhysicalSpaceName')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('LoginType') is not None:
            self.login_type = m.get('LoginType')
        if m.get('LoginUsername') is not None:
            self.login_username = m.get('LoginUsername')
        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')
        if m.get('SnmpAccountVersion') is not None:
            self.snmp_account_version = m.get('SnmpAccountVersion')
        if m.get('SnmpCommunity') is not None:
            self.snmp_community = m.get('SnmpCommunity')
        if m.get('SnmpAccountType') is not None:
            self.snmp_account_type = m.get('SnmpAccountType')
        if m.get('SnmpSecurityLevel') is not None:
            self.snmp_security_level = m.get('SnmpSecurityLevel')
        if m.get('SnmpUsername') is not None:
            self.snmp_username = m.get('SnmpUsername')
        if m.get('SnmpAuthPassphrase') is not None:
            self.snmp_auth_passphrase = m.get('SnmpAuthPassphrase')
        if m.get('SnmpAuthProtocol') is not None:
            self.snmp_auth_protocol = m.get('SnmpAuthProtocol')
        if m.get('SnmpPrivacyPassphase') is not None:
            self.snmp_privacy_passphase = m.get('SnmpPrivacyPassphase')
        if m.get('SnmpPrivacyProtocol') is not None:
            self.snmp_privacy_protocol = m.get('SnmpPrivacyProtocol')
        if m.get('ExtAttributes') is not None:
            self.ext_attributes = m.get('ExtAttributes')
        return self


class GetDeviceResponseBody(TeaModel):
    def __init__(
        self,
        device: GetDeviceResponseBodyDevice = None,
        request_id: str = None,
    ):
        # 设备详情
        self.device = device
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.device:
            self.device.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device is not None:
            result['Device'] = self.device.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Device') is not None:
            temp_model = GetDeviceResponseBodyDevice()
            self.device = temp_model.from_map(m['Device'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceConfigRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        date: str = None,
        instance_id: str = None,
    ):
        # 实例 ID。
        self.device_id = device_id
        # 查询日期，格式 yyyy-MM-dd
        self.date = date
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.date is not None:
            result['Date'] = self.date
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetDeviceConfigResponseBody(TeaModel):
    def __init__(
        self,
        device_config: str = None,
        request_id: str = None,
    ):
        # 设备配置内容
        self.device_config = device_config
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_config is not None:
            result['DeviceConfig'] = self.device_config
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceConfig') is not None:
            self.device_config = m.get('DeviceConfig')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeviceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDeviceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceConfigDiffRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        start_date: str = None,
        end_date: str = None,
        instance_id: str = None,
    ):
        # 实例 ID。
        self.device_id = device_id
        # 查询日期1，格式 yyyy-MM-dd
        self.start_date = start_date
        # 查询日期2，格式 yyyy-MM-dd
        self.end_date = end_date
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetDeviceConfigDiffResponseBodyDeviceConfigDiff(TeaModel):
    def __init__(
        self,
        extract_diff: str = None,
        total_diff: str = None,
    ):
        # 差异提取
        self.extract_diff = extract_diff
        # 全量比对
        self.total_diff = total_diff

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extract_diff is not None:
            result['ExtractDiff'] = self.extract_diff
        if self.total_diff is not None:
            result['TotalDiff'] = self.total_diff
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtractDiff') is not None:
            self.extract_diff = m.get('ExtractDiff')
        if m.get('TotalDiff') is not None:
            self.total_diff = m.get('TotalDiff')
        return self


class GetDeviceConfigDiffResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_config_diff: GetDeviceConfigDiffResponseBodyDeviceConfigDiff = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.device_config_diff = device_config_diff

    def validate(self):
        if self.device_config_diff:
            self.device_config_diff.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_config_diff is not None:
            result['DeviceConfigDiff'] = self.device_config_diff.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceConfigDiff') is not None:
            temp_model = GetDeviceConfigDiffResponseBodyDeviceConfigDiff()
            self.device_config_diff = temp_model.from_map(m['DeviceConfigDiff'])
        return self


class GetDeviceConfigDiffResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceConfigDiffResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDeviceConfigDiffResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceFormRequest(TeaModel):
    def __init__(
        self,
        device_form_id: str = None,
        instance_id: str = None,
    ):
        # 实例 ID。
        self.device_form_id = device_form_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetDeviceFormResponseBodyDeviceFormAttributeList(TeaModel):
    def __init__(
        self,
        attribute_key: str = None,
        attribute_name: str = None,
        attribute_requirement: bool = None,
        attribute_uniqueness: bool = None,
        attribute_format: str = None,
        attribute_type: str = None,
        attribute_reference: str = None,
        attribute_table_display: bool = None,
        attribute_placeholder: str = None,
        attribute_query: bool = None,
        attribute_fuzzy_query: bool = None,
        attribute_built_in: bool = None,
    ):
        # 设备形态属性主键
        self.attribute_key = attribute_key
        # 设备形态属性名称
        self.attribute_name = attribute_name
        # 设备形态属性是否必填
        self.attribute_requirement = attribute_requirement
        # 设备形态属性是否唯一
        self.attribute_uniqueness = attribute_uniqueness
        # 设备形态属性值格式
        self.attribute_format = attribute_format
        # 设备形态属性值类型
        self.attribute_type = attribute_type
        # 设备形态属性关联对象
        self.attribute_reference = attribute_reference
        # 设备形态属性是否表格可见
        self.attribute_table_display = attribute_table_display
        # 前端查询控件占位符
        self.attribute_placeholder = attribute_placeholder
        # 前端是否展示对应的查询控件
        self.attribute_query = attribute_query
        # 前端查询控件是否支持模糊搜索
        self.attribute_fuzzy_query = attribute_fuzzy_query
        # 设备形态属性是否内置
        self.attribute_built_in = attribute_built_in

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_requirement is not None:
            result['AttributeRequirement'] = self.attribute_requirement
        if self.attribute_uniqueness is not None:
            result['AttributeUniqueness'] = self.attribute_uniqueness
        if self.attribute_format is not None:
            result['AttributeFormat'] = self.attribute_format
        if self.attribute_type is not None:
            result['AttributeType'] = self.attribute_type
        if self.attribute_reference is not None:
            result['AttributeReference'] = self.attribute_reference
        if self.attribute_table_display is not None:
            result['AttributeTableDisplay'] = self.attribute_table_display
        if self.attribute_placeholder is not None:
            result['AttributePlaceholder'] = self.attribute_placeholder
        if self.attribute_query is not None:
            result['AttributeQuery'] = self.attribute_query
        if self.attribute_fuzzy_query is not None:
            result['AttributeFuzzyQuery'] = self.attribute_fuzzy_query
        if self.attribute_built_in is not None:
            result['AttributeBuiltIn'] = self.attribute_built_in
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeRequirement') is not None:
            self.attribute_requirement = m.get('AttributeRequirement')
        if m.get('AttributeUniqueness') is not None:
            self.attribute_uniqueness = m.get('AttributeUniqueness')
        if m.get('AttributeFormat') is not None:
            self.attribute_format = m.get('AttributeFormat')
        if m.get('AttributeType') is not None:
            self.attribute_type = m.get('AttributeType')
        if m.get('AttributeReference') is not None:
            self.attribute_reference = m.get('AttributeReference')
        if m.get('AttributeTableDisplay') is not None:
            self.attribute_table_display = m.get('AttributeTableDisplay')
        if m.get('AttributePlaceholder') is not None:
            self.attribute_placeholder = m.get('AttributePlaceholder')
        if m.get('AttributeQuery') is not None:
            self.attribute_query = m.get('AttributeQuery')
        if m.get('AttributeFuzzyQuery') is not None:
            self.attribute_fuzzy_query = m.get('AttributeFuzzyQuery')
        if m.get('AttributeBuiltIn') is not None:
            self.attribute_built_in = m.get('AttributeBuiltIn')
        return self


class GetDeviceFormResponseBodyDeviceForm(TeaModel):
    def __init__(
        self,
        config_compare: bool = None,
        attribute_list: List[GetDeviceFormResponseBodyDeviceFormAttributeList] = None,
        device_form_id: str = None,
        device_form_name: str = None,
        form_built_in: bool = None,
        account_config: bool = None,
        detail_display: bool = None,
        unique_key: str = None,
    ):
        # 是否支持配置生成
        self.config_compare = config_compare
        # 设备形态属性列表
        self.attribute_list = attribute_list
        # 设备形态ID
        self.device_form_id = device_form_id
        # 设备形态名称
        self.device_form_name = device_form_name
        # 设备形态是否内置
        self.form_built_in = form_built_in
        # 是否需要账号配置
        self.account_config = account_config
        # 是否展示设备详情
        self.detail_display = detail_display
        # 设备形态主键
        self.unique_key = unique_key

    def validate(self):
        if self.attribute_list:
            for k in self.attribute_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_compare is not None:
            result['ConfigCompare'] = self.config_compare
        result['AttributeList'] = []
        if self.attribute_list is not None:
            for k in self.attribute_list:
                result['AttributeList'].append(k.to_map() if k else None)
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        if self.form_built_in is not None:
            result['FormBuiltIn'] = self.form_built_in
        if self.account_config is not None:
            result['AccountConfig'] = self.account_config
        if self.detail_display is not None:
            result['DetailDisplay'] = self.detail_display
        if self.unique_key is not None:
            result['UniqueKey'] = self.unique_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigCompare') is not None:
            self.config_compare = m.get('ConfigCompare')
        self.attribute_list = []
        if m.get('AttributeList') is not None:
            for k in m.get('AttributeList'):
                temp_model = GetDeviceFormResponseBodyDeviceFormAttributeList()
                self.attribute_list.append(temp_model.from_map(k))
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        if m.get('FormBuiltIn') is not None:
            self.form_built_in = m.get('FormBuiltIn')
        if m.get('AccountConfig') is not None:
            self.account_config = m.get('AccountConfig')
        if m.get('DetailDisplay') is not None:
            self.detail_display = m.get('DetailDisplay')
        if m.get('UniqueKey') is not None:
            self.unique_key = m.get('UniqueKey')
        return self


class GetDeviceFormResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_form: GetDeviceFormResponseBodyDeviceForm = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 设备详情
        self.device_form = device_form

    def validate(self):
        if self.device_form:
            self.device_form.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_form is not None:
            result['DeviceForm'] = self.device_form.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceForm') is not None:
            temp_model = GetDeviceFormResponseBodyDeviceForm()
            self.device_form = temp_model.from_map(m['DeviceForm'])
        return self


class GetDeviceFormResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDeviceFormResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDeviceFormResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDevicePropertyRequest(TeaModel):
    def __init__(
        self,
        device_property_id: str = None,
        property_key: str = None,
        device_form_id: str = None,
        instance_id: str = None,
    ):
        # 实例 ID。
        self.device_property_id = device_property_id
        # 属性主键
        self.property_key = property_key
        # 设备形态ID
        self.device_form_id = device_form_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_property_id is not None:
            result['DevicePropertyId'] = self.device_property_id
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevicePropertyId') is not None:
            self.device_property_id = m.get('DevicePropertyId')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetDevicePropertyResponseBodyDeviceProperty(TeaModel):
    def __init__(
        self,
        device_property_id: str = None,
        device_form_id: str = None,
        device_form_name: str = None,
        property_name: str = None,
        property_key: str = None,
        property_format: str = None,
        property_content: str = None,
        built_in: bool = None,
    ):
        # 设备属性ID
        self.device_property_id = device_property_id
        # 设备形态ID
        self.device_form_id = device_form_id
        # 设备形态名称
        self.device_form_name = device_form_name
        # 属性名称
        self.property_name = property_name
        # 属性主键
        self.property_key = property_key
        # 属性格式
        self.property_format = property_format
        # 属性内容
        self.property_content = property_content
        # 是否内置属性
        self.built_in = built_in

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_property_id is not None:
            result['DevicePropertyId'] = self.device_property_id
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.property_format is not None:
            result['PropertyFormat'] = self.property_format
        if self.property_content is not None:
            result['PropertyContent'] = self.property_content
        if self.built_in is not None:
            result['BuiltIn'] = self.built_in
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevicePropertyId') is not None:
            self.device_property_id = m.get('DevicePropertyId')
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('PropertyFormat') is not None:
            self.property_format = m.get('PropertyFormat')
        if m.get('PropertyContent') is not None:
            self.property_content = m.get('PropertyContent')
        if m.get('BuiltIn') is not None:
            self.built_in = m.get('BuiltIn')
        return self


class GetDevicePropertyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_property: GetDevicePropertyResponseBodyDeviceProperty = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 设备属性详情
        self.device_property = device_property

    def validate(self):
        if self.device_property:
            self.device_property.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_property is not None:
            result['DeviceProperty'] = self.device_property.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceProperty') is not None:
            temp_model = GetDevicePropertyResponseBodyDeviceProperty()
            self.device_property = temp_model.from_map(m['DeviceProperty'])
        return self


class GetDevicePropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDevicePropertyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDevicePropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInspectionTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        instance_id: str = None,
    ):
        # 巡检项ID
        self.task_id = task_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetInspectionTaskResponseBodyInspectionAlarmRules(TeaModel):
    def __init__(
        self,
        expression: str = None,
        operator: str = None,
        value: str = None,
        actual_value: str = None,
        level: str = None,
    ):
        # 告警符号
        self.expression = expression
        # 告警操作符
        self.operator = operator
        # 告警值
        self.value = value
        # 告警实际值
        self.actual_value = actual_value
        # 告警级别
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value
        if self.level is not None:
            result['Level'] = self.level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        return self


class GetInspectionTaskResponseBody(TeaModel):
    def __init__(
        self,
        space: str = None,
        request_id: str = None,
        device_id: str = None,
        inspection_result: str = None,
        inspection_alarm_rules: List[GetInspectionTaskResponseBodyInspectionAlarmRules] = None,
        ip: str = None,
        host_name: str = None,
        vendor: str = None,
        task_status: str = None,
        item_id: str = None,
        execution_end_time: str = None,
        execution_begin_time: str = None,
        model: List[str] = None,
        item_name: str = None,
        error_code: str = None,
        script_id: str = None,
        task_id: str = None,
    ):
        # 物理空间
        self.space = space
        # 请求ID
        self.request_id = request_id
        # 设备ID
        self.device_id = device_id
        # 巡检结果
        self.inspection_result = inspection_result
        # 告警规则
        self.inspection_alarm_rules = inspection_alarm_rules
        # IP地址
        self.ip = ip
        # 主机名
        self.host_name = host_name
        # 厂商
        self.vendor = vendor
        # 任务状态
        self.task_status = task_status
        # 巡检项ID
        self.item_id = item_id
        # 巡检结束时间
        self.execution_end_time = execution_end_time
        # 巡检开始时间
        self.execution_begin_time = execution_begin_time
        # 型号
        self.model = model
        # 巡检项名字
        self.item_name = item_name
        # 错误码
        self.error_code = error_code
        # 模板ID
        self.script_id = script_id
        # 任务ID
        self.task_id = task_id

    def validate(self):
        if self.inspection_alarm_rules:
            for k in self.inspection_alarm_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space is not None:
            result['Space'] = self.space
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.inspection_result is not None:
            result['InspectionResult'] = self.inspection_result
        result['InspectionAlarmRules'] = []
        if self.inspection_alarm_rules is not None:
            for k in self.inspection_alarm_rules:
                result['InspectionAlarmRules'].append(k.to_map() if k else None)
        if self.ip is not None:
            result['IP'] = self.ip
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.execution_end_time is not None:
            result['ExecutionEndTime'] = self.execution_end_time
        if self.execution_begin_time is not None:
            result['ExecutionBeginTime'] = self.execution_begin_time
        if self.model is not None:
            result['Model'] = self.model
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Space') is not None:
            self.space = m.get('Space')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('InspectionResult') is not None:
            self.inspection_result = m.get('InspectionResult')
        self.inspection_alarm_rules = []
        if m.get('InspectionAlarmRules') is not None:
            for k in m.get('InspectionAlarmRules'):
                temp_model = GetInspectionTaskResponseBodyInspectionAlarmRules()
                self.inspection_alarm_rules.append(temp_model.from_map(k))
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ExecutionEndTime') is not None:
            self.execution_end_time = m.get('ExecutionEndTime')
        if m.get('ExecutionBeginTime') is not None:
            self.execution_begin_time = m.get('ExecutionBeginTime')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetInspectionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInspectionTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInspectionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhysicalSpaceRequest(TeaModel):
    def __init__(
        self,
        physical_space_id: str = None,
        instance_id: str = None,
    ):
        # 实例 ID。
        self.physical_space_id = physical_space_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetPhysicalSpaceResponseBodyPhysicalSpace(TeaModel):
    def __init__(
        self,
        physical_space_id: str = None,
        physical_space_name: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        address: str = None,
    ):
        # 物理空间ID
        self.physical_space_id = physical_space_id
        # 物理空间名称
        self.physical_space_name = physical_space_name
        # 所属国家
        self.country = country
        # 所属省份
        self.province = province
        # 所属城市
        self.city = city
        # 具体地址
        self.address = address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.physical_space_name is not None:
            result['PhysicalSpaceName'] = self.physical_space_name
        if self.country is not None:
            result['Country'] = self.country
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.address is not None:
            result['Address'] = self.address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('PhysicalSpaceName') is not None:
            self.physical_space_name = m.get('PhysicalSpaceName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        return self


class GetPhysicalSpaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        physical_space: GetPhysicalSpaceResponseBodyPhysicalSpace = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 物理空间详情
        self.physical_space = physical_space

    def validate(self):
        if self.physical_space:
            self.physical_space.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.physical_space is not None:
            result['PhysicalSpace'] = self.physical_space.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PhysicalSpace') is not None:
            temp_model = GetPhysicalSpaceResponseBodyPhysicalSpace()
            self.physical_space = temp_model.from_map(m['PhysicalSpace'])
        return self


class GetPhysicalSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPhysicalSpaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPhysicalSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRealtimeTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        instance_id: str = None,
    ):
        # 实时任务ID
        self.task_id = task_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetRealtimeTaskResponseBodyInspectionTask(TeaModel):
    def __init__(
        self,
        task_status: str = None,
        inspection_result: str = None,
        error_code: str = None,
        inspection_message: str = None,
    ):
        # 巡检状态
        self.task_status = task_status
        # 巡检输出
        self.inspection_result = inspection_result
        # 巡检错误码
        self.error_code = error_code
        # 巡检错误信息
        self.inspection_message = inspection_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.inspection_result is not None:
            result['InspectionResult'] = self.inspection_result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.inspection_message is not None:
            result['InspectionMessage'] = self.inspection_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('InspectionResult') is not None:
            self.inspection_result = m.get('InspectionResult')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InspectionMessage') is not None:
            self.inspection_message = m.get('InspectionMessage')
        return self


class GetRealtimeTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        inspection_task: GetRealtimeTaskResponseBodyInspectionTask = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 请求任务结果
        self.inspection_task = inspection_task

    def validate(self):
        if self.inspection_task:
            self.inspection_task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.inspection_task is not None:
            result['InspectionTask'] = self.inspection_task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InspectionTask') is not None:
            temp_model = GetRealtimeTaskResponseBodyInspectionTask()
            self.inspection_task = temp_model.from_map(m['InspectionTask'])
        return self


class GetRealtimeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRealtimeTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRealtimeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmStatusRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        space: str = None,
        device_form: str = None,
        status: str = None,
        device_id: str = None,
        monitor_item_id: str = None,
        type: str = None,
        instance_id: str = None,
    ):
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 物理空间
        self.space = space
        # 设备形态
        self.device_form = device_form
        # 告警状态
        self.status = status
        # 设备ID
        self.device_id = device_id
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 数据类型
        self.type = type
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.space is not None:
            result['Space'] = self.space
        if self.device_form is not None:
            result['DeviceForm'] = self.device_form
        if self.status is not None:
            result['Status'] = self.status
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.type is not None:
            result['Type'] = self.type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Space') is not None:
            self.space = m.get('Space')
        if m.get('DeviceForm') is not None:
            self.device_form = m.get('DeviceForm')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListAlarmStatusResponseBodyAlarmStatusResourceDevice(TeaModel):
    def __init__(
        self,
        host_name: str = None,
    ):
        # 设备名
        self.host_name = host_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_name is not None:
            result['HostName'] = self.host_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        return self


class ListAlarmStatusResponseBodyAlarmStatusMonitorItem(TeaModel):
    def __init__(
        self,
        monitor_item_name: str = None,
    ):
        # 监控项名称
        self.monitor_item_name = monitor_item_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.monitor_item_name is not None:
            result['MonitorItemName'] = self.monitor_item_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorItemName') is not None:
            self.monitor_item_name = m.get('MonitorItemName')
        return self


class ListAlarmStatusResponseBodyAlarmStatusNotificationSwitch(TeaModel):
    def __init__(
        self,
        reason: str = None,
        expiry_time: str = None,
    ):
        # 关闭原因
        self.reason = reason
        # 关闭到期时间
        self.expiry_time = expiry_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        return self


class ListAlarmStatusResponseBodyAlarmStatusAggregateData(TeaModel):
    def __init__(
        self,
        aggregate_data_name: str = None,
        data_item: str = None,
    ):
        # 聚合数据名称
        self.aggregate_data_name = aggregate_data_name
        # 数据项
        self.data_item = data_item

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregate_data_name is not None:
            result['AggregateDataName'] = self.aggregate_data_name
        if self.data_item is not None:
            result['DataItem'] = self.data_item
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregateDataName') is not None:
            self.aggregate_data_name = m.get('AggregateDataName')
        if m.get('DataItem') is not None:
            self.data_item = m.get('DataItem')
        return self


class ListAlarmStatusResponseBodyAlarmStatusDedicatedLine(TeaModel):
    def __init__(
        self,
        dedicated_line_name: str = None,
    ):
        # 专线名称
        self.dedicated_line_name = dedicated_line_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_line_name is not None:
            result['DedicatedLineName'] = self.dedicated_line_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedLineName') is not None:
            self.dedicated_line_name = m.get('DedicatedLineName')
        return self


class ListAlarmStatusResponseBodyAlarmStatus(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        monitor_item_id: str = None,
        collection_time: str = None,
        receive_time: str = None,
        alarm_rule: str = None,
        alarm_status: str = None,
        result: str = None,
        abnormal_data_item: str = None,
        unique_key: str = None,
        response_code: str = None,
        resource_device: ListAlarmStatusResponseBodyAlarmStatusResourceDevice = None,
        monitor_item: ListAlarmStatusResponseBodyAlarmStatusMonitorItem = None,
        first_abnormal_time: str = None,
        notification_switch: ListAlarmStatusResponseBodyAlarmStatusNotificationSwitch = None,
        aggregate_data_id: str = None,
        aggregate_data: ListAlarmStatusResponseBodyAlarmStatusAggregateData = None,
        dedicated_line_id: str = None,
        dedicated_line: ListAlarmStatusResponseBodyAlarmStatusDedicatedLine = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 检测时间
        self.collection_time = collection_time
        # 接收时间
        self.receive_time = receive_time
        # 命中告警规则
        self.alarm_rule = alarm_rule
        # 告警状态
        self.alarm_status = alarm_status
        # 采集结果
        self.result = result
        # 异常数据项
        self.abnormal_data_item = abnormal_data_item
        # 索引
        self.unique_key = unique_key
        # 采集状态码
        self.response_code = response_code
        # 设备
        self.resource_device = resource_device
        # 监控项
        self.monitor_item = monitor_item
        # 首次异常时间
        self.first_abnormal_time = first_abnormal_time
        # 告警开关配置
        self.notification_switch = notification_switch
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 聚合数据
        self.aggregate_data = aggregate_data
        # 专线ID
        self.dedicated_line_id = dedicated_line_id
        # 专线
        self.dedicated_line = dedicated_line

    def validate(self):
        if self.resource_device:
            self.resource_device.validate()
        if self.monitor_item:
            self.monitor_item.validate()
        if self.notification_switch:
            self.notification_switch.validate()
        if self.aggregate_data:
            self.aggregate_data.validate()
        if self.dedicated_line:
            self.dedicated_line.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.collection_time is not None:
            result['CollectionTime'] = self.collection_time
        if self.receive_time is not None:
            result['ReceiveTime'] = self.receive_time
        if self.alarm_rule is not None:
            result['AlarmRule'] = self.alarm_rule
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.result is not None:
            result['Result'] = self.result
        if self.abnormal_data_item is not None:
            result['AbnormalDataItem'] = self.abnormal_data_item
        if self.unique_key is not None:
            result['UniqueKey'] = self.unique_key
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.resource_device is not None:
            result['ResourceDevice'] = self.resource_device.to_map()
        if self.monitor_item is not None:
            result['MonitorItem'] = self.monitor_item.to_map()
        if self.first_abnormal_time is not None:
            result['FirstAbnormalTime'] = self.first_abnormal_time
        if self.notification_switch is not None:
            result['NotificationSwitch'] = self.notification_switch.to_map()
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.aggregate_data is not None:
            result['AggregateData'] = self.aggregate_data.to_map()
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.dedicated_line is not None:
            result['DedicatedLine'] = self.dedicated_line.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('CollectionTime') is not None:
            self.collection_time = m.get('CollectionTime')
        if m.get('ReceiveTime') is not None:
            self.receive_time = m.get('ReceiveTime')
        if m.get('AlarmRule') is not None:
            self.alarm_rule = m.get('AlarmRule')
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('AbnormalDataItem') is not None:
            self.abnormal_data_item = m.get('AbnormalDataItem')
        if m.get('UniqueKey') is not None:
            self.unique_key = m.get('UniqueKey')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('ResourceDevice') is not None:
            temp_model = ListAlarmStatusResponseBodyAlarmStatusResourceDevice()
            self.resource_device = temp_model.from_map(m['ResourceDevice'])
        if m.get('MonitorItem') is not None:
            temp_model = ListAlarmStatusResponseBodyAlarmStatusMonitorItem()
            self.monitor_item = temp_model.from_map(m['MonitorItem'])
        if m.get('FirstAbnormalTime') is not None:
            self.first_abnormal_time = m.get('FirstAbnormalTime')
        if m.get('NotificationSwitch') is not None:
            temp_model = ListAlarmStatusResponseBodyAlarmStatusNotificationSwitch()
            self.notification_switch = temp_model.from_map(m['NotificationSwitch'])
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('AggregateData') is not None:
            temp_model = ListAlarmStatusResponseBodyAlarmStatusAggregateData()
            self.aggregate_data = temp_model.from_map(m['AggregateData'])
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('DedicatedLine') is not None:
            temp_model = ListAlarmStatusResponseBodyAlarmStatusDedicatedLine()
            self.dedicated_line = temp_model.from_map(m['DedicatedLine'])
        return self


class ListAlarmStatusResponseBodyStatistics(TeaModel):
    def __init__(
        self,
        count: int = None,
        status: str = None,
    ):
        # 数量
        self.count = count
        # 告警状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAlarmStatusResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        next_token: str = None,
        max_results: int = None,
        alarm_status: List[ListAlarmStatusResponseBodyAlarmStatus] = None,
        statistics: List[ListAlarmStatusResponseBodyStatistics] = None,
    ):
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count
        # Id of the request
        self.request_id = request_id
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # MaxResults本次请求所返回的最大记录条数
        self.max_results = max_results
        # 告警状态列表
        self.alarm_status = alarm_status
        # 告警状态统计
        self.statistics = statistics

    def validate(self):
        if self.alarm_status:
            for k in self.alarm_status:
                if k:
                    k.validate()
        if self.statistics:
            for k in self.statistics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['AlarmStatus'] = []
        if self.alarm_status is not None:
            for k in self.alarm_status:
                result['AlarmStatus'].append(k.to_map() if k else None)
        result['Statistics'] = []
        if self.statistics is not None:
            for k in self.statistics:
                result['Statistics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.alarm_status = []
        if m.get('AlarmStatus') is not None:
            for k in m.get('AlarmStatus'):
                temp_model = ListAlarmStatusResponseBodyAlarmStatus()
                self.alarm_status.append(temp_model.from_map(k))
        self.statistics = []
        if m.get('Statistics') is not None:
            for k in m.get('Statistics'):
                temp_model = ListAlarmStatusResponseBodyStatistics()
                self.statistics.append(temp_model.from_map(k))
        return self


class ListAlarmStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlarmStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlarmStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmStatusHistoriesRequest(TeaModel):
    def __init__(
        self,
        start: int = None,
        end: int = None,
        device_id: str = None,
        monitor_item_id: str = None,
        type: str = None,
        aggregate_data_id: str = None,
        dedicated_line_id: str = None,
        instance_id: str = None,
    ):
        # 开始时间秒级时间戳
        self.start = start
        # 结束时间秒级时间戳
        self.end = end
        # 设备ID
        self.device_id = device_id
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 类型
        self.type = type
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 专线ID
        self.dedicated_line_id = dedicated_line_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start is not None:
            result['Start'] = self.start
        if self.end is not None:
            result['End'] = self.end
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.type is not None:
            result['Type'] = self.type
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListAlarmStatusHistoriesResponseBodyAlarmStatusHistories(TeaModel):
    def __init__(
        self,
        timestamp: int = None,
        value: str = None,
    ):
        # 时间戳
        self.timestamp = timestamp
        # 数值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListAlarmStatusHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        alarm_status_histories: List[ListAlarmStatusHistoriesResponseBodyAlarmStatusHistories] = None,
    ):
        # request id
        self.request_id = request_id
        # 数据列表
        self.alarm_status_histories = alarm_status_histories

    def validate(self):
        if self.alarm_status_histories:
            for k in self.alarm_status_histories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AlarmStatusHistories'] = []
        if self.alarm_status_histories is not None:
            for k in self.alarm_status_histories:
                result['AlarmStatusHistories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.alarm_status_histories = []
        if m.get('AlarmStatusHistories') is not None:
            for k in m.get('AlarmStatusHistories'):
                temp_model = ListAlarmStatusHistoriesResponseBodyAlarmStatusHistories()
                self.alarm_status_histories.append(temp_model.from_map(k))
        return self


class ListAlarmStatusHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAlarmStatusHistoriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAlarmStatusHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDedicatedLinesRequest(TeaModel):
    def __init__(
        self,
        physical_space_id: str = None,
        instance_id: str = None,
    ):
        # 物理空间ID
        self.physical_space_id = physical_space_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListDedicatedLinesResponseBodyDedicatedLines(TeaModel):
    def __init__(
        self,
        dedicated_line_id: str = None,
        isp: str = None,
        bandwidth: int = None,
        dedicated_line_ip: str = None,
        dedicated_line_gateway: str = None,
        dedicated_line_role: str = None,
        device_id: str = None,
        device_port: str = None,
        device_name: str = None,
        physical_space_id: str = None,
    ):
        # 物理空间专线ID
        self.dedicated_line_id = dedicated_line_id
        # 运营商
        self.isp = isp
        # 宽带（Mbps）
        self.bandwidth = bandwidth
        # 专线IP
        self.dedicated_line_ip = dedicated_line_ip
        # 专线网关
        self.dedicated_line_gateway = dedicated_line_gateway
        # 专线角色
        self.dedicated_line_role = dedicated_line_role
        # 关联设备ID
        self.device_id = device_id
        # 关联设备端口
        self.device_port = device_port
        # 关联设备名称
        self.device_name = device_name
        # 关联物理空间ID
        self.physical_space_id = physical_space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.dedicated_line_ip is not None:
            result['DedicatedLineIp'] = self.dedicated_line_ip
        if self.dedicated_line_gateway is not None:
            result['DedicatedLineGateway'] = self.dedicated_line_gateway
        if self.dedicated_line_role is not None:
            result['DedicatedLineRole'] = self.dedicated_line_role
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_port is not None:
            result['DevicePort'] = self.device_port
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('DedicatedLineIp') is not None:
            self.dedicated_line_ip = m.get('DedicatedLineIp')
        if m.get('DedicatedLineGateway') is not None:
            self.dedicated_line_gateway = m.get('DedicatedLineGateway')
        if m.get('DedicatedLineRole') is not None:
            self.dedicated_line_role = m.get('DedicatedLineRole')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DevicePort') is not None:
            self.device_port = m.get('DevicePort')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        return self


class ListDedicatedLinesResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_lines: List[ListDedicatedLinesResponseBodyDedicatedLines] = None,
        request_id: str = None,
    ):
        # 数组，返回示例目录。
        self.dedicated_lines = dedicated_lines
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.dedicated_lines:
            for k in self.dedicated_lines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DedicatedLines'] = []
        if self.dedicated_lines is not None:
            for k in self.dedicated_lines:
                result['DedicatedLines'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dedicated_lines = []
        if m.get('DedicatedLines') is not None:
            for k in m.get('DedicatedLines'):
                temp_model = ListDedicatedLinesResponseBodyDedicatedLines()
                self.dedicated_lines.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDedicatedLinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDedicatedLinesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDedicatedLinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceFormsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        instance_id: str = None,
    ):
        # 返回结果的最大个数。
        self.max_results = max_results
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListDeviceFormsResponseBodyDeviceFormsAttributeList(TeaModel):
    def __init__(
        self,
        attribute_key: str = None,
        attribute_name: str = None,
        attribute_requirement: bool = None,
        attribute_uniqueness: bool = None,
        attribute_format: str = None,
        attribute_type: str = None,
        attribute_reference: str = None,
        attribute_table_display: bool = None,
        attribute_placeholder: str = None,
        attribute_query: bool = None,
        attribute_fuzzy_query: bool = None,
        attribute_built_in: bool = None,
    ):
        # 设备形态属性主键
        self.attribute_key = attribute_key
        # 设备形态属性名称
        self.attribute_name = attribute_name
        # 设备形态属性是否必填
        self.attribute_requirement = attribute_requirement
        # 设备形态属性是否唯一
        self.attribute_uniqueness = attribute_uniqueness
        # 设备形态属性值格式
        self.attribute_format = attribute_format
        # 设备形态属性值类型
        self.attribute_type = attribute_type
        # 设备形态属性关联对象
        self.attribute_reference = attribute_reference
        # 设备形态属性是否表格可见
        self.attribute_table_display = attribute_table_display
        # 前端查询控件占位符
        self.attribute_placeholder = attribute_placeholder
        # 前端是否展示对应的查询控件
        self.attribute_query = attribute_query
        # 前端查询控件是否支持模糊搜索
        self.attribute_fuzzy_query = attribute_fuzzy_query
        # 设备形态属性是否内置
        self.attribute_built_in = attribute_built_in

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_requirement is not None:
            result['AttributeRequirement'] = self.attribute_requirement
        if self.attribute_uniqueness is not None:
            result['AttributeUniqueness'] = self.attribute_uniqueness
        if self.attribute_format is not None:
            result['AttributeFormat'] = self.attribute_format
        if self.attribute_type is not None:
            result['AttributeType'] = self.attribute_type
        if self.attribute_reference is not None:
            result['AttributeReference'] = self.attribute_reference
        if self.attribute_table_display is not None:
            result['AttributeTableDisplay'] = self.attribute_table_display
        if self.attribute_placeholder is not None:
            result['AttributePlaceholder'] = self.attribute_placeholder
        if self.attribute_query is not None:
            result['AttributeQuery'] = self.attribute_query
        if self.attribute_fuzzy_query is not None:
            result['AttributeFuzzyQuery'] = self.attribute_fuzzy_query
        if self.attribute_built_in is not None:
            result['AttributeBuiltIn'] = self.attribute_built_in
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeRequirement') is not None:
            self.attribute_requirement = m.get('AttributeRequirement')
        if m.get('AttributeUniqueness') is not None:
            self.attribute_uniqueness = m.get('AttributeUniqueness')
        if m.get('AttributeFormat') is not None:
            self.attribute_format = m.get('AttributeFormat')
        if m.get('AttributeType') is not None:
            self.attribute_type = m.get('AttributeType')
        if m.get('AttributeReference') is not None:
            self.attribute_reference = m.get('AttributeReference')
        if m.get('AttributeTableDisplay') is not None:
            self.attribute_table_display = m.get('AttributeTableDisplay')
        if m.get('AttributePlaceholder') is not None:
            self.attribute_placeholder = m.get('AttributePlaceholder')
        if m.get('AttributeQuery') is not None:
            self.attribute_query = m.get('AttributeQuery')
        if m.get('AttributeFuzzyQuery') is not None:
            self.attribute_fuzzy_query = m.get('AttributeFuzzyQuery')
        if m.get('AttributeBuiltIn') is not None:
            self.attribute_built_in = m.get('AttributeBuiltIn')
        return self


class ListDeviceFormsResponseBodyDeviceForms(TeaModel):
    def __init__(
        self,
        config_compare: bool = None,
        attribute_list: List[ListDeviceFormsResponseBodyDeviceFormsAttributeList] = None,
        account_config: bool = None,
        detail_display: bool = None,
        form_built_in: bool = None,
        unique_key: str = None,
        device_form_id: str = None,
        device_form_name: str = None,
    ):
        # 是否支持配置生成
        self.config_compare = config_compare
        # 设备形态属性列表
        self.attribute_list = attribute_list
        # 是否需要账号配置
        self.account_config = account_config
        # 是否展示详情
        self.detail_display = detail_display
        # 设备形态是否内置
        self.form_built_in = form_built_in
        # 设备形态主键
        self.unique_key = unique_key
        # 设备形态ID
        self.device_form_id = device_form_id
        # 设备形态名称
        self.device_form_name = device_form_name

    def validate(self):
        if self.attribute_list:
            for k in self.attribute_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_compare is not None:
            result['ConfigCompare'] = self.config_compare
        result['AttributeList'] = []
        if self.attribute_list is not None:
            for k in self.attribute_list:
                result['AttributeList'].append(k.to_map() if k else None)
        if self.account_config is not None:
            result['AccountConfig'] = self.account_config
        if self.detail_display is not None:
            result['DetailDisplay'] = self.detail_display
        if self.form_built_in is not None:
            result['FormBuiltIn'] = self.form_built_in
        if self.unique_key is not None:
            result['UniqueKey'] = self.unique_key
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigCompare') is not None:
            self.config_compare = m.get('ConfigCompare')
        self.attribute_list = []
        if m.get('AttributeList') is not None:
            for k in m.get('AttributeList'):
                temp_model = ListDeviceFormsResponseBodyDeviceFormsAttributeList()
                self.attribute_list.append(temp_model.from_map(k))
        if m.get('AccountConfig') is not None:
            self.account_config = m.get('AccountConfig')
        if m.get('DetailDisplay') is not None:
            self.detail_display = m.get('DetailDisplay')
        if m.get('FormBuiltIn') is not None:
            self.form_built_in = m.get('FormBuiltIn')
        if m.get('UniqueKey') is not None:
            self.unique_key = m.get('UniqueKey')
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        return self


class ListDeviceFormsResponseBody(TeaModel):
    def __init__(
        self,
        device_forms: List[ListDeviceFormsResponseBodyDeviceForms] = None,
        total_count: int = None,
        request_id: str = None,
        next_token: int = None,
        max_results: int = None,
    ):
        # 数组，返回示例目录。
        self.device_forms = device_forms
        # 总记录数。
        self.total_count = total_count
        # Id of the request
        self.request_id = request_id
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 每页数量。
        self.max_results = max_results

    def validate(self):
        if self.device_forms:
            for k in self.device_forms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceForms'] = []
        if self.device_forms is not None:
            for k in self.device_forms:
                result['DeviceForms'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_forms = []
        if m.get('DeviceForms') is not None:
            for k in m.get('DeviceForms'):
                temp_model = ListDeviceFormsResponseBodyDeviceForms()
                self.device_forms.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListDeviceFormsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceFormsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDeviceFormsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevicePropertiesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        device_form_id: str = None,
        instance_id: str = None,
    ):
        # 返回结果的最大个数。
        self.max_results = max_results
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 设备形态ID
        self.device_form_id = device_form_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListDevicePropertiesResponseBodyDeviceProperties(TeaModel):
    def __init__(
        self,
        device_property_id: str = None,
        device_form_id: str = None,
        device_form_name: str = None,
        property_name: str = None,
        property_key: str = None,
        property_format: str = None,
        property_content: str = None,
        built_in: bool = None,
    ):
        # 设备属性ID
        self.device_property_id = device_property_id
        # 设备形态ID
        self.device_form_id = device_form_id
        # 设备形态名称
        self.device_form_name = device_form_name
        # 属性名称
        self.property_name = property_name
        # 属性主键
        self.property_key = property_key
        # 属性格式
        self.property_format = property_format
        # 属性内容
        self.property_content = property_content
        # 是否内置属性
        self.built_in = built_in

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_property_id is not None:
            result['DevicePropertyId'] = self.device_property_id
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.property_format is not None:
            result['PropertyFormat'] = self.property_format
        if self.property_content is not None:
            result['PropertyContent'] = self.property_content
        if self.built_in is not None:
            result['BuiltIn'] = self.built_in
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevicePropertyId') is not None:
            self.device_property_id = m.get('DevicePropertyId')
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('PropertyFormat') is not None:
            self.property_format = m.get('PropertyFormat')
        if m.get('PropertyContent') is not None:
            self.property_content = m.get('PropertyContent')
        if m.get('BuiltIn') is not None:
            self.built_in = m.get('BuiltIn')
        return self


class ListDevicePropertiesResponseBody(TeaModel):
    def __init__(
        self,
        device_properties: List[ListDevicePropertiesResponseBodyDeviceProperties] = None,
        next_token: int = None,
        request_id: str = None,
        total_count: int = None,
        max_results: int = None,
    ):
        # 数组，返回示例目录。
        self.device_properties = device_properties
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # 总记录数。
        self.total_count = total_count
        # 每页数量。
        self.max_results = max_results

    def validate(self):
        if self.device_properties:
            for k in self.device_properties:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceProperties'] = []
        if self.device_properties is not None:
            for k in self.device_properties:
                result['DeviceProperties'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_properties = []
        if m.get('DeviceProperties') is not None:
            for k in m.get('DeviceProperties'):
                temp_model = ListDevicePropertiesResponseBodyDeviceProperties()
                self.device_properties.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListDevicePropertiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDevicePropertiesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDevicePropertiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDevicesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        device_form_id: str = None,
        device_form_name: str = None,
        physical_space_id: str = None,
        host_name: List[str] = None,
        ip: List[str] = None,
        sn: List[str] = None,
        mac: List[str] = None,
        vendor: List[str] = None,
        model: List[str] = None,
        service_status: List[str] = None,
        security_domain: List[str] = None,
        ext_attributes: str = None,
        instance_id: str = None,
    ):
        # 返回结果的最大个数。
        self.max_results = max_results
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 设备形态ID
        self.device_form_id = device_form_id
        # 设备形态名称
        self.device_form_name = device_form_name
        # 物理空间ID
        self.physical_space_id = physical_space_id
        # 设备主机名
        self.host_name = host_name
        # 设备IP
        self.ip = ip
        # 设备SN
        self.sn = sn
        # 设备MAC
        self.mac = mac
        # 设备厂商
        self.vendor = vendor
        # 设备型号
        self.model = model
        # 设备服务状态
        self.service_status = service_status
        # 安全域
        self.security_domain = security_domain
        # 设备额外属性
        self.ext_attributes = ext_attributes
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.model is not None:
            result['Model'] = self.model
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.ext_attributes is not None:
            result['ExtAttributes'] = self.ext_attributes
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('ExtAttributes') is not None:
            self.ext_attributes = m.get('ExtAttributes')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListDevicesResponseBodyDevices(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        device_form_name: str = None,
        device_form_id: str = None,
        physical_space_id: str = None,
        physical_space_name: str = None,
        host_name: str = None,
        ip: str = None,
        sn: str = None,
        mac: str = None,
        vendor: str = None,
        model: str = None,
        security_domain: str = None,
        service_status: str = None,
        login_type: str = None,
        login_username: str = None,
        login_password: str = None,
        snmp_account_version: str = None,
        snmp_community: str = None,
        snmp_account_type: str = None,
        snmp_security_level: str = None,
        snmp_username: str = None,
        snmp_auth_pass_phrase: str = None,
        snmp_auth_protocol: str = None,
        snmp_privacy_passphase: str = None,
        snmp_privacy_protocol: str = None,
        ext_attributes: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 设备形态名称
        self.device_form_name = device_form_name
        # 设备形态ID
        self.device_form_id = device_form_id
        # 物理空间ID
        self.physical_space_id = physical_space_id
        # 物理空间名称
        self.physical_space_name = physical_space_name
        # 主机名
        self.host_name = host_name
        # 设备IP
        self.ip = ip
        # 设备SN
        self.sn = sn
        # 设备MAC地址
        self.mac = mac
        # 设备厂商
        self.vendor = vendor
        # 设备型号
        self.model = model
        # 设备安全域
        self.security_domain = security_domain
        # 设备状态
        self.service_status = service_status
        # 登录类型
        self.login_type = login_type
        # 登录账号
        self.login_username = login_username
        # 登录密码
        self.login_password = login_password
        # SNMP版本号
        self.snmp_account_version = snmp_account_version
        # SNMP Community
        self.snmp_community = snmp_community
        # SNMP 账号类型
        self.snmp_account_type = snmp_account_type
        # SNMP 安全级别
        self.snmp_security_level = snmp_security_level
        # SNMP 用户名
        self.snmp_username = snmp_username
        # SNMP Auth PassPhrase
        self.snmp_auth_pass_phrase = snmp_auth_pass_phrase
        # SNMP Auth Protocol
        self.snmp_auth_protocol = snmp_auth_protocol
        # SNMP Privacy Passphase
        self.snmp_privacy_passphase = snmp_privacy_passphase
        # SNMP Privacy Protocol
        self.snmp_privacy_protocol = snmp_privacy_protocol
        # 设备额外属性
        self.ext_attributes = ext_attributes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.physical_space_name is not None:
            result['PhysicalSpaceName'] = self.physical_space_name
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.model is not None:
            result['Model'] = self.model
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.login_type is not None:
            result['LoginType'] = self.login_type
        if self.login_username is not None:
            result['LoginUsername'] = self.login_username
        if self.login_password is not None:
            result['LoginPassword'] = self.login_password
        if self.snmp_account_version is not None:
            result['SnmpAccountVersion'] = self.snmp_account_version
        if self.snmp_community is not None:
            result['SnmpCommunity'] = self.snmp_community
        if self.snmp_account_type is not None:
            result['SnmpAccountType'] = self.snmp_account_type
        if self.snmp_security_level is not None:
            result['SnmpSecurityLevel'] = self.snmp_security_level
        if self.snmp_username is not None:
            result['SnmpUsername'] = self.snmp_username
        if self.snmp_auth_pass_phrase is not None:
            result['SnmpAuthPassPhrase'] = self.snmp_auth_pass_phrase
        if self.snmp_auth_protocol is not None:
            result['SnmpAuthProtocol'] = self.snmp_auth_protocol
        if self.snmp_privacy_passphase is not None:
            result['SnmpPrivacyPassphase'] = self.snmp_privacy_passphase
        if self.snmp_privacy_protocol is not None:
            result['SnmpPrivacyProtocol'] = self.snmp_privacy_protocol
        if self.ext_attributes is not None:
            result['ExtAttributes'] = self.ext_attributes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('PhysicalSpaceName') is not None:
            self.physical_space_name = m.get('PhysicalSpaceName')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('LoginType') is not None:
            self.login_type = m.get('LoginType')
        if m.get('LoginUsername') is not None:
            self.login_username = m.get('LoginUsername')
        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')
        if m.get('SnmpAccountVersion') is not None:
            self.snmp_account_version = m.get('SnmpAccountVersion')
        if m.get('SnmpCommunity') is not None:
            self.snmp_community = m.get('SnmpCommunity')
        if m.get('SnmpAccountType') is not None:
            self.snmp_account_type = m.get('SnmpAccountType')
        if m.get('SnmpSecurityLevel') is not None:
            self.snmp_security_level = m.get('SnmpSecurityLevel')
        if m.get('SnmpUsername') is not None:
            self.snmp_username = m.get('SnmpUsername')
        if m.get('SnmpAuthPassPhrase') is not None:
            self.snmp_auth_pass_phrase = m.get('SnmpAuthPassPhrase')
        if m.get('SnmpAuthProtocol') is not None:
            self.snmp_auth_protocol = m.get('SnmpAuthProtocol')
        if m.get('SnmpPrivacyPassphase') is not None:
            self.snmp_privacy_passphase = m.get('SnmpPrivacyPassphase')
        if m.get('SnmpPrivacyProtocol') is not None:
            self.snmp_privacy_protocol = m.get('SnmpPrivacyProtocol')
        if m.get('ExtAttributes') is not None:
            self.ext_attributes = m.get('ExtAttributes')
        return self


class ListDevicesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        next_token: int = None,
        devices: List[ListDevicesResponseBodyDevices] = None,
        max_results: int = None,
    ):
        # 总记录数。
        self.total_count = total_count
        # Id of the request
        self.request_id = request_id
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 数组，返回示例目录。
        self.devices = devices
        # 每页数量。
        self.max_results = max_results

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = ListDevicesResponseBodyDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceValuesRequest(TeaModel):
    def __init__(
        self,
        device_form_id: str = None,
        device_form_name: str = None,
        attribute_keyword: str = None,
        attribute_group: str = None,
        instance_id: str = None,
    ):
        # 设备形态ID
        self.device_form_id = device_form_id
        # 设备形态名称
        self.device_form_name = device_form_name
        # 查询属性主键
        self.attribute_keyword = attribute_keyword
        # 查询属性对应JSON中主键
        self.attribute_group = attribute_group
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.device_form_name is not None:
            result['DeviceFormName'] = self.device_form_name
        if self.attribute_keyword is not None:
            result['AttributeKeyword'] = self.attribute_keyword
        if self.attribute_group is not None:
            result['AttributeGroup'] = self.attribute_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('DeviceFormName') is not None:
            self.device_form_name = m.get('DeviceFormName')
        if m.get('AttributeKeyword') is not None:
            self.attribute_keyword = m.get('AttributeKeyword')
        if m.get('AttributeGroup') is not None:
            self.attribute_group = m.get('AttributeGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListDeviceValuesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_values: List[str] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 数组，返回示例目录。
        self.device_values = device_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_values is not None:
            result['DeviceValues'] = self.device_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceValues') is not None:
            self.device_values = m.get('DeviceValues')
        return self


class ListDeviceValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDeviceValuesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDeviceValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInspectionTasksRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        item_id: str = None,
        host_name: str = None,
        ip: str = None,
        task_status: str = None,
        instance_id: str = None,
    ):
        # 返回结果的最大个数。
        self.max_results = max_results
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 巡检项ID
        self.item_id = item_id
        # 主机名
        self.host_name = host_name
        # 设备IP
        self.ip = ip
        # 巡检状态
        self.task_status = task_status
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListInspectionTasksResponseBodyInspectionTasksInspectionAlarmRules(TeaModel):
    def __init__(
        self,
        alarm_expression: str = None,
        alarm_operator: str = None,
        alarm_value: str = None,
        actual_value: str = None,
        alarm_level: str = None,
    ):
        # 告警符号
        self.alarm_expression = alarm_expression
        # 告警变量
        self.alarm_operator = alarm_operator
        # 告警值
        self.alarm_value = alarm_value
        # 告警实际值
        self.actual_value = actual_value
        # 告警级别
        self.alarm_level = alarm_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_expression is not None:
            result['AlarmExpression'] = self.alarm_expression
        if self.alarm_operator is not None:
            result['AlarmOperator'] = self.alarm_operator
        if self.alarm_value is not None:
            result['AlarmValue'] = self.alarm_value
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value
        if self.alarm_level is not None:
            result['AlarmLevel'] = self.alarm_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmExpression') is not None:
            self.alarm_expression = m.get('AlarmExpression')
        if m.get('AlarmOperator') is not None:
            self.alarm_operator = m.get('AlarmOperator')
        if m.get('AlarmValue') is not None:
            self.alarm_value = m.get('AlarmValue')
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')
        if m.get('AlarmLevel') is not None:
            self.alarm_level = m.get('AlarmLevel')
        return self


class ListInspectionTasksResponseBodyInspectionTasks(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        item_id: str = None,
        execution_end_time: str = None,
        execution_begin_time: str = None,
        item_name: str = None,
        script_id: str = None,
        space: str = None,
        inspection_result: str = None,
        inspection_alarm_rules: List[ListInspectionTasksResponseBodyInspectionTasksInspectionAlarmRules] = None,
        ip: str = None,
        host_name: str = None,
        vendor: str = None,
        task_status: str = None,
        model: List[str] = None,
        error_code: str = None,
        inspection_message: str = None,
        task_id: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 巡检项ID
        self.item_id = item_id
        # 巡检结束时间
        self.execution_end_time = execution_end_time
        # 巡检开始时间
        self.execution_begin_time = execution_begin_time
        # 巡检项名字
        self.item_name = item_name
        # 模板ID
        self.script_id = script_id
        # 物理空间
        self.space = space
        # 巡检结果
        self.inspection_result = inspection_result
        # 告警规则
        self.inspection_alarm_rules = inspection_alarm_rules
        # IP地址
        self.ip = ip
        # 主机名
        self.host_name = host_name
        # 厂商
        self.vendor = vendor
        # 任务状态
        self.task_status = task_status
        # 型号
        self.model = model
        # 错误码
        self.error_code = error_code
        # 巡检信息
        self.inspection_message = inspection_message
        # 任务ID
        self.task_id = task_id

    def validate(self):
        if self.inspection_alarm_rules:
            for k in self.inspection_alarm_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.execution_end_time is not None:
            result['ExecutionEndTime'] = self.execution_end_time
        if self.execution_begin_time is not None:
            result['ExecutionBeginTime'] = self.execution_begin_time
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.space is not None:
            result['Space'] = self.space
        if self.inspection_result is not None:
            result['InspectionResult'] = self.inspection_result
        result['InspectionAlarmRules'] = []
        if self.inspection_alarm_rules is not None:
            for k in self.inspection_alarm_rules:
                result['InspectionAlarmRules'].append(k.to_map() if k else None)
        if self.ip is not None:
            result['IP'] = self.ip
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.model is not None:
            result['Model'] = self.model
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.inspection_message is not None:
            result['InspectionMessage'] = self.inspection_message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ExecutionEndTime') is not None:
            self.execution_end_time = m.get('ExecutionEndTime')
        if m.get('ExecutionBeginTime') is not None:
            self.execution_begin_time = m.get('ExecutionBeginTime')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('Space') is not None:
            self.space = m.get('Space')
        if m.get('InspectionResult') is not None:
            self.inspection_result = m.get('InspectionResult')
        self.inspection_alarm_rules = []
        if m.get('InspectionAlarmRules') is not None:
            for k in m.get('InspectionAlarmRules'):
                temp_model = ListInspectionTasksResponseBodyInspectionTasksInspectionAlarmRules()
                self.inspection_alarm_rules.append(temp_model.from_map(k))
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InspectionMessage') is not None:
            self.inspection_message = m.get('InspectionMessage')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListInspectionTasksResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        next_token: int = None,
        inspection_tasks: List[ListInspectionTasksResponseBodyInspectionTasks] = None,
    ):
        # 总记录数。
        self.total_count = total_count
        # 请求ID
        self.request_id = request_id
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 数组，返回示例目录。
        self.inspection_tasks = inspection_tasks

    def validate(self):
        if self.inspection_tasks:
            for k in self.inspection_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['InspectionTasks'] = []
        if self.inspection_tasks is not None:
            for k in self.inspection_tasks:
                result['InspectionTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.inspection_tasks = []
        if m.get('InspectionTasks') is not None:
            for k in m.get('InspectionTasks'):
                temp_model = ListInspectionTasksResponseBodyInspectionTasks()
                self.inspection_tasks.append(temp_model.from_map(k))
        return self


class ListInspectionTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInspectionTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInspectionTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        instance_spec: str = None,
        instance_open_date: str = None,
        instance_end_date: str = None,
        instance_device_max_count: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 实例名称
        self.instance_name = instance_name
        # 实例规格
        self.instance_spec = instance_spec
        # 实例开通时间
        self.instance_open_date = instance_open_date
        # 实例到期时间
        self.instance_end_date = instance_end_date
        # 最大纳管设备数量
        self.instance_device_max_count = instance_device_max_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.instance_open_date is not None:
            result['InstanceOpenDate'] = self.instance_open_date
        if self.instance_end_date is not None:
            result['InstanceEndDate'] = self.instance_end_date
        if self.instance_device_max_count is not None:
            result['InstanceDeviceMaxCount'] = self.instance_device_max_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('InstanceOpenDate') is not None:
            self.instance_open_date = m.get('InstanceOpenDate')
        if m.get('InstanceEndDate') is not None:
            self.instance_end_date = m.get('InstanceEndDate')
        if m.get('InstanceDeviceMaxCount') is not None:
            self.instance_device_max_count = m.get('InstanceDeviceMaxCount')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instances: List[ListInstancesResponseBodyInstances] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 实例列表
        self.instances = instances

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMonitorDataRequest(TeaModel):
    def __init__(
        self,
        start: int = None,
        end: int = None,
        data_type: str = None,
        data_item: str = None,
        monitor_item_id: str = None,
        device_id: str = None,
        key: str = None,
        aggregate_data_id: str = None,
        port_collection_id: str = None,
        dedicated_line_id: str = None,
        instance_id: str = None,
    ):
        # 开始时间
        self.start = start
        # 结束时间
        self.end = end
        # 数据类型
        self.data_type = data_type
        # 数据项
        self.data_item = data_item
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 设备ID
        self.device_id = device_id
        # key
        self.key = key
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 端口集ID
        self.port_collection_id = port_collection_id
        # 专线ID
        self.dedicated_line_id = dedicated_line_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start is not None:
            result['Start'] = self.start
        if self.end is not None:
            result['End'] = self.end
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.data_item is not None:
            result['DataItem'] = self.data_item
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.key is not None:
            result['Key'] = self.key
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.port_collection_id is not None:
            result['PortCollectionId'] = self.port_collection_id
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DataItem') is not None:
            self.data_item = m.get('DataItem')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('PortCollectionId') is not None:
            self.port_collection_id = m.get('PortCollectionId')
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListMonitorDataResponseBodyMonitorData(TeaModel):
    def __init__(
        self,
        timestamp: int = None,
        value: str = None,
        data_item: str = None,
        key: str = None,
    ):
        # 时间戳
        self.timestamp = timestamp
        # 数值
        self.value = value
        # 数据项
        self.data_item = data_item
        # key
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.value is not None:
            result['Value'] = self.value
        if self.data_item is not None:
            result['DataItem'] = self.data_item
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('DataItem') is not None:
            self.data_item = m.get('DataItem')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ListMonitorDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        monitor_data: List[ListMonitorDataResponseBodyMonitorData] = None,
    ):
        # Request Id
        self.request_id = request_id
        # 数据列表
        self.monitor_data = monitor_data

    def validate(self):
        if self.monitor_data:
            for k in self.monitor_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['MonitorData'] = []
        if self.monitor_data is not None:
            for k in self.monitor_data:
                result['MonitorData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.monitor_data = []
        if m.get('MonitorData') is not None:
            for k in m.get('MonitorData'):
                temp_model = ListMonitorDataResponseBodyMonitorData()
                self.monitor_data.append(temp_model.from_map(k))
        return self


class ListMonitorDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMonitorDataResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListMonitorDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNotificationHistoriesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        monitor_item_id: str = None,
        device_id: str = None,
        type: str = None,
        dedicated_line_id: str = None,
        aggregate_data_id: str = None,
        instance_id: str = None,
    ):
        # 标记当前开始读取的位置，置空表示从头开始
        self.next_token = next_token
        # 本次读取的最大数据记录数量
        self.max_results = max_results
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 设备ID
        self.device_id = device_id
        # 类型
        self.type = type
        # 专线ID
        self.dedicated_line_id = dedicated_line_id
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.type is not None:
            result['Type'] = self.type
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListNotificationHistoriesResponseBodyNotificationHistories(TeaModel):
    def __init__(
        self,
        time: str = None,
        notification_mode: str = None,
        status: str = None,
        output: str = None,
        message: str = None,
        device_id: str = None,
        monitor_item_id: str = None,
        notification_group_id: str = None,
        notification_group_name: str = None,
        dedicated_line_id: str = None,
        aggregate_data_id: str = None,
    ):
        # 发送时间
        self.time = time
        # 发送方式
        self.notification_mode = notification_mode
        # 发送状态
        self.status = status
        # 输出内容
        self.output = output
        # 发送内容
        self.message = message
        # 设备ID
        self.device_id = device_id
        # 监控项ID
        self.monitor_item_id = monitor_item_id
        # 通知组ID
        self.notification_group_id = notification_group_id
        # 通知组名称
        self.notification_group_name = notification_group_name
        # 专线ID
        self.dedicated_line_id = dedicated_line_id
        # 聚合数据ID
        self.aggregate_data_id = aggregate_data_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.notification_mode is not None:
            result['NotificationMode'] = self.notification_mode
        if self.status is not None:
            result['Status'] = self.status
        if self.output is not None:
            result['Output'] = self.output
        if self.message is not None:
            result['Message'] = self.message
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.monitor_item_id is not None:
            result['MonitorItemId'] = self.monitor_item_id
        if self.notification_group_id is not None:
            result['NotificationGroupId'] = self.notification_group_id
        if self.notification_group_name is not None:
            result['NotificationGroupName'] = self.notification_group_name
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.aggregate_data_id is not None:
            result['AggregateDataId'] = self.aggregate_data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('NotificationMode') is not None:
            self.notification_mode = m.get('NotificationMode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('MonitorItemId') is not None:
            self.monitor_item_id = m.get('MonitorItemId')
        if m.get('NotificationGroupId') is not None:
            self.notification_group_id = m.get('NotificationGroupId')
        if m.get('NotificationGroupName') is not None:
            self.notification_group_name = m.get('NotificationGroupName')
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('AggregateDataId') is not None:
            self.aggregate_data_id = m.get('AggregateDataId')
        return self


class ListNotificationHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        next_token: str = None,
        max_results: int = None,
        notification_histories: List[ListNotificationHistoriesResponseBodyNotificationHistories] = None,
    ):
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count
        # request Id
        self.request_id = request_id
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # MaxResults本次请求所返回的最大记录条数
        self.max_results = max_results
        # 数据列表
        self.notification_histories = notification_histories

    def validate(self):
        if self.notification_histories:
            for k in self.notification_histories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['NotificationHistories'] = []
        if self.notification_histories is not None:
            for k in self.notification_histories:
                result['NotificationHistories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.notification_histories = []
        if m.get('NotificationHistories') is not None:
            for k in m.get('NotificationHistories'):
                temp_model = ListNotificationHistoriesResponseBodyNotificationHistories()
                self.notification_histories.append(temp_model.from_map(k))
        return self


class ListNotificationHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNotificationHistoriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListNotificationHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPhysicalSpacesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        physical_space_ids: List[str] = None,
        physical_space_name: str = None,
        instance_id: str = None,
    ):
        # 返回结果的最大个数。
        self.max_results = max_results
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 物理空间ID
        self.physical_space_ids = physical_space_ids
        # 物理空间名称，支持模糊搜索。
        self.physical_space_name = physical_space_name
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.physical_space_ids is not None:
            result['PhysicalSpaceIds'] = self.physical_space_ids
        if self.physical_space_name is not None:
            result['PhysicalSpaceName'] = self.physical_space_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PhysicalSpaceIds') is not None:
            self.physical_space_ids = m.get('PhysicalSpaceIds')
        if m.get('PhysicalSpaceName') is not None:
            self.physical_space_name = m.get('PhysicalSpaceName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListPhysicalSpacesResponseBodyPhysicalSpaces(TeaModel):
    def __init__(
        self,
        physical_space_id: str = None,
        physical_space_name: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        address: str = None,
    ):
        # 物理空间ID
        self.physical_space_id = physical_space_id
        # 物理空间名称
        self.physical_space_name = physical_space_name
        # 所属国家
        self.country = country
        # 所属省份
        self.province = province
        # 所属城市
        self.city = city
        # 具体地址
        self.address = address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.physical_space_name is not None:
            result['PhysicalSpaceName'] = self.physical_space_name
        if self.country is not None:
            result['Country'] = self.country
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.address is not None:
            result['Address'] = self.address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('PhysicalSpaceName') is not None:
            self.physical_space_name = m.get('PhysicalSpaceName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        return self


class ListPhysicalSpacesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: int = None,
        physical_spaces: List[ListPhysicalSpacesResponseBodyPhysicalSpaces] = None,
        request_id: str = None,
        total_count: int = None,
        max_results: int = None,
    ):
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 数组，返回示例目录。
        self.physical_spaces = physical_spaces
        # Id of the request
        self.request_id = request_id
        # 总记录数。
        self.total_count = total_count
        # 每页数量。
        self.max_results = max_results

    def validate(self):
        if self.physical_spaces:
            for k in self.physical_spaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['PhysicalSpaces'] = []
        if self.physical_spaces is not None:
            for k in self.physical_spaces:
                result['PhysicalSpaces'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.physical_spaces = []
        if m.get('PhysicalSpaces') is not None:
            for k in m.get('PhysicalSpaces'):
                temp_model = ListPhysicalSpacesResponseBodyPhysicalSpaces()
                self.physical_spaces.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListPhysicalSpacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPhysicalSpacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListPhysicalSpacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        success: bool = None,
        message: str = None,
        code: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.data = data
        self.success = success
        self.message = message
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.success is not None:
            result['Success'] = self.success
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksHistoriesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        item_id: str = None,
        device_id: str = None,
        instance_id: str = None,
    ):
        # 返回结果的最大个数。
        self.max_results = max_results
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 巡检项ID
        self.item_id = item_id
        # 设备ID
        self.device_id = device_id
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListTasksHistoriesResponseBodyInspectionTasksInspectionAlarmRules(TeaModel):
    def __init__(
        self,
        alarm_expression: str = None,
        alarm_operator: str = None,
        alarm_value: str = None,
        actual_value: str = None,
        alarm_level: str = None,
    ):
        # 告警表达式
        self.alarm_expression = alarm_expression
        # 告警操作符
        self.alarm_operator = alarm_operator
        # 告警值
        self.alarm_value = alarm_value
        # 告警实际值
        self.actual_value = actual_value
        # 告警级别
        self.alarm_level = alarm_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_expression is not None:
            result['AlarmExpression'] = self.alarm_expression
        if self.alarm_operator is not None:
            result['AlarmOperator'] = self.alarm_operator
        if self.alarm_value is not None:
            result['AlarmValue'] = self.alarm_value
        if self.actual_value is not None:
            result['ActualValue'] = self.actual_value
        if self.alarm_level is not None:
            result['AlarmLevel'] = self.alarm_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmExpression') is not None:
            self.alarm_expression = m.get('AlarmExpression')
        if m.get('AlarmOperator') is not None:
            self.alarm_operator = m.get('AlarmOperator')
        if m.get('AlarmValue') is not None:
            self.alarm_value = m.get('AlarmValue')
        if m.get('ActualValue') is not None:
            self.actual_value = m.get('ActualValue')
        if m.get('AlarmLevel') is not None:
            self.alarm_level = m.get('AlarmLevel')
        return self


class ListTasksHistoriesResponseBodyInspectionTasks(TeaModel):
    def __init__(
        self,
        execution_end_time: str = None,
        execution_begin_time: str = None,
        inspection_result: str = None,
        inspection_alarm_rules: List[ListTasksHistoriesResponseBodyInspectionTasksInspectionAlarmRules] = None,
        task_id: str = None,
    ):
        # 巡检结束时间
        self.execution_end_time = execution_end_time
        # 巡检开始时间
        self.execution_begin_time = execution_begin_time
        # 巡检结果
        self.inspection_result = inspection_result
        # 告警规则
        self.inspection_alarm_rules = inspection_alarm_rules
        # 任务ID
        self.task_id = task_id

    def validate(self):
        if self.inspection_alarm_rules:
            for k in self.inspection_alarm_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_end_time is not None:
            result['ExecutionEndTime'] = self.execution_end_time
        if self.execution_begin_time is not None:
            result['ExecutionBeginTime'] = self.execution_begin_time
        if self.inspection_result is not None:
            result['InspectionResult'] = self.inspection_result
        result['InspectionAlarmRules'] = []
        if self.inspection_alarm_rules is not None:
            for k in self.inspection_alarm_rules:
                result['InspectionAlarmRules'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionEndTime') is not None:
            self.execution_end_time = m.get('ExecutionEndTime')
        if m.get('ExecutionBeginTime') is not None:
            self.execution_begin_time = m.get('ExecutionBeginTime')
        if m.get('InspectionResult') is not None:
            self.inspection_result = m.get('InspectionResult')
        self.inspection_alarm_rules = []
        if m.get('InspectionAlarmRules') is not None:
            for k in m.get('InspectionAlarmRules'):
                temp_model = ListTasksHistoriesResponseBodyInspectionTasksInspectionAlarmRules()
                self.inspection_alarm_rules.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListTasksHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        next_token: int = None,
        inspection_tasks: List[ListTasksHistoriesResponseBodyInspectionTasks] = None,
    ):
        # 总记录数。
        self.total_count = total_count
        # 请求ID
        self.request_id = request_id
        # 当总结果个数大于MaxResults时，用于翻页的token。
        self.next_token = next_token
        # 数组，返回示例目录。
        self.inspection_tasks = inspection_tasks

    def validate(self):
        if self.inspection_tasks:
            for k in self.inspection_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['InspectionTasks'] = []
        if self.inspection_tasks is not None:
            for k in self.inspection_tasks:
                result['InspectionTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.inspection_tasks = []
        if m.get('InspectionTasks') is not None:
            for k in m.get('InspectionTasks'):
                temp_model = ListTasksHistoriesResponseBodyInspectionTasks()
                self.inspection_tasks.append(temp_model.from_map(k))
        return self


class ListTasksHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTasksHistoriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTasksHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryTasksRequestRetryTasks(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        script_id: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 脚本ID
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        return self


class RetryTasksRequest(TeaModel):
    def __init__(
        self,
        retry_tasks: List[RetryTasksRequestRetryTasks] = None,
        instance_id: str = None,
    ):
        # 重执行任务的数组
        self.retry_tasks = retry_tasks
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        if self.retry_tasks:
            for k in self.retry_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RetryTasks'] = []
        if self.retry_tasks is not None:
            for k in self.retry_tasks:
                result['RetryTasks'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.retry_tasks = []
        if m.get('RetryTasks') is not None:
            for k in m.get('RetryTasks'):
                temp_model = RetryTasksRequestRetryTasks()
                self.retry_tasks.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RetryTasksShrinkRequest(TeaModel):
    def __init__(
        self,
        retry_tasks_shrink: str = None,
        instance_id: str = None,
    ):
        # 重执行任务的数组
        self.retry_tasks_shrink = retry_tasks_shrink
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.retry_tasks_shrink is not None:
            result['RetryTasks'] = self.retry_tasks_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetryTasks') is not None:
            self.retry_tasks_shrink = m.get('RetryTasks')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RetryTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RetryTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RetryTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RetryTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDedicatedLineRequest(TeaModel):
    def __init__(
        self,
        dedicated_line_id: str = None,
        isp: str = None,
        bandwidth: int = None,
        dedicated_line_ip: str = None,
        dedicated_line_gateway: str = None,
        dedicated_line_role: str = None,
        device_id: str = None,
        device_port: str = None,
        instance_id: str = None,
    ):
        # 实例 ID。
        self.dedicated_line_id = dedicated_line_id
        # 运营商
        self.isp = isp
        # 宽带（Mbps）
        self.bandwidth = bandwidth
        # 专线IP
        self.dedicated_line_ip = dedicated_line_ip
        # 专线网关
        self.dedicated_line_gateway = dedicated_line_gateway
        # 专线角色
        self.dedicated_line_role = dedicated_line_role
        # 关联设备ID
        self.device_id = device_id
        # 关联设备端口名称
        self.device_port = device_port
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_line_id is not None:
            result['DedicatedLineId'] = self.dedicated_line_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.dedicated_line_ip is not None:
            result['DedicatedLineIp'] = self.dedicated_line_ip
        if self.dedicated_line_gateway is not None:
            result['DedicatedLineGateway'] = self.dedicated_line_gateway
        if self.dedicated_line_role is not None:
            result['DedicatedLineRole'] = self.dedicated_line_role
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_port is not None:
            result['DevicePort'] = self.device_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedLineId') is not None:
            self.dedicated_line_id = m.get('DedicatedLineId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('DedicatedLineIp') is not None:
            self.dedicated_line_ip = m.get('DedicatedLineIp')
        if m.get('DedicatedLineGateway') is not None:
            self.dedicated_line_gateway = m.get('DedicatedLineGateway')
        if m.get('DedicatedLineRole') is not None:
            self.dedicated_line_role = m.get('DedicatedLineRole')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DevicePort') is not None:
            self.device_port = m.get('DevicePort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateDedicatedLineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDedicatedLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDedicatedLineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDedicatedLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeviceRequest(TeaModel):
    def __init__(
        self,
        device_id: str = None,
        physical_space_id: str = None,
        host_name: str = None,
        ip: str = None,
        sn: str = None,
        mac: str = None,
        vendor: str = None,
        model: str = None,
        service_status: str = None,
        security_domain: str = None,
        login_type: str = None,
        login_username: str = None,
        login_password: str = None,
        snmp_account_version: str = None,
        snmp_community: str = None,
        snmp_account_type: str = None,
        snmp_security_level: str = None,
        snmp_username: str = None,
        snmp_auth_passphrase: str = None,
        snmp_auth_protocol: str = None,
        snmp_privacy_passphase: str = None,
        snmp_privacy_protocol: str = None,
        ext_attributes: str = None,
        instance_id: str = None,
    ):
        # 设备ID
        self.device_id = device_id
        # 物理空间
        self.physical_space_id = physical_space_id
        # 主机名
        self.host_name = host_name
        # 设备IP
        self.ip = ip
        # 设备SN
        self.sn = sn
        # 设备MAC地址
        self.mac = mac
        # 设备厂商
        self.vendor = vendor
        # 设备型号
        self.model = model
        # 设备状态
        self.service_status = service_status
        # 设备安全域
        self.security_domain = security_domain
        # 登录类型
        self.login_type = login_type
        # 登录账号
        self.login_username = login_username
        # 登录密码
        self.login_password = login_password
        # SNMP 版本号
        self.snmp_account_version = snmp_account_version
        # SNMP Community
        self.snmp_community = snmp_community
        # SNMP 账号类型
        self.snmp_account_type = snmp_account_type
        # SNMP 安全级别
        self.snmp_security_level = snmp_security_level
        # SNMP 用户名
        self.snmp_username = snmp_username
        # SNMP Auth PassPhrase
        self.snmp_auth_passphrase = snmp_auth_passphrase
        # Auth Protocol
        self.snmp_auth_protocol = snmp_auth_protocol
        # Privacy Passphase
        self.snmp_privacy_passphase = snmp_privacy_passphase
        # Privacy Protocol
        self.snmp_privacy_protocol = snmp_privacy_protocol
        # 设备额外属性
        self.ext_attributes = ext_attributes
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.model is not None:
            result['Model'] = self.model
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.security_domain is not None:
            result['SecurityDomain'] = self.security_domain
        if self.login_type is not None:
            result['LoginType'] = self.login_type
        if self.login_username is not None:
            result['LoginUsername'] = self.login_username
        if self.login_password is not None:
            result['LoginPassword'] = self.login_password
        if self.snmp_account_version is not None:
            result['SnmpAccountVersion'] = self.snmp_account_version
        if self.snmp_community is not None:
            result['SnmpCommunity'] = self.snmp_community
        if self.snmp_account_type is not None:
            result['SnmpAccountType'] = self.snmp_account_type
        if self.snmp_security_level is not None:
            result['SnmpSecurityLevel'] = self.snmp_security_level
        if self.snmp_username is not None:
            result['SnmpUsername'] = self.snmp_username
        if self.snmp_auth_passphrase is not None:
            result['SnmpAuthPassphrase'] = self.snmp_auth_passphrase
        if self.snmp_auth_protocol is not None:
            result['SnmpAuthProtocol'] = self.snmp_auth_protocol
        if self.snmp_privacy_passphase is not None:
            result['SnmpPrivacyPassphase'] = self.snmp_privacy_passphase
        if self.snmp_privacy_protocol is not None:
            result['SnmpPrivacyProtocol'] = self.snmp_privacy_protocol
        if self.ext_attributes is not None:
            result['ExtAttributes'] = self.ext_attributes
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('SecurityDomain') is not None:
            self.security_domain = m.get('SecurityDomain')
        if m.get('LoginType') is not None:
            self.login_type = m.get('LoginType')
        if m.get('LoginUsername') is not None:
            self.login_username = m.get('LoginUsername')
        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')
        if m.get('SnmpAccountVersion') is not None:
            self.snmp_account_version = m.get('SnmpAccountVersion')
        if m.get('SnmpCommunity') is not None:
            self.snmp_community = m.get('SnmpCommunity')
        if m.get('SnmpAccountType') is not None:
            self.snmp_account_type = m.get('SnmpAccountType')
        if m.get('SnmpSecurityLevel') is not None:
            self.snmp_security_level = m.get('SnmpSecurityLevel')
        if m.get('SnmpUsername') is not None:
            self.snmp_username = m.get('SnmpUsername')
        if m.get('SnmpAuthPassphrase') is not None:
            self.snmp_auth_passphrase = m.get('SnmpAuthPassphrase')
        if m.get('SnmpAuthProtocol') is not None:
            self.snmp_auth_protocol = m.get('SnmpAuthProtocol')
        if m.get('SnmpPrivacyPassphase') is not None:
            self.snmp_privacy_passphase = m.get('SnmpPrivacyPassphase')
        if m.get('SnmpPrivacyProtocol') is not None:
            self.snmp_privacy_protocol = m.get('SnmpPrivacyProtocol')
        if m.get('ExtAttributes') is not None:
            self.ext_attributes = m.get('ExtAttributes')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeviceFormRequestAttributeList(TeaModel):
    def __init__(
        self,
        attribute_key: str = None,
        attribute_name: str = None,
        attribute_requirement: bool = None,
        attribute_uniqueness: bool = None,
        attribute_format: str = None,
        attribute_type: str = None,
        attribute_reference: str = None,
        attribute_table_display: bool = None,
        attribute_placeholder: str = None,
        attribute_query: bool = None,
        attribute_fuzzy_query: bool = None,
    ):
        # 设备形态属性主键
        self.attribute_key = attribute_key
        # 设备形态属性名称
        self.attribute_name = attribute_name
        # 设备形态属性是否必填
        self.attribute_requirement = attribute_requirement
        # 设备形态属性是否唯一
        self.attribute_uniqueness = attribute_uniqueness
        # 设备形态属性值格式
        self.attribute_format = attribute_format
        # 设备形态属性值类型
        self.attribute_type = attribute_type
        # 设备形态属性关联对象
        self.attribute_reference = attribute_reference
        # 设备形态属性是否表格可见
        self.attribute_table_display = attribute_table_display
        # 前端查询控件占位符
        self.attribute_placeholder = attribute_placeholder
        # 前端展示搜索控件
        self.attribute_query = attribute_query
        # 查询支持模糊搜索
        self.attribute_fuzzy_query = attribute_fuzzy_query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_requirement is not None:
            result['AttributeRequirement'] = self.attribute_requirement
        if self.attribute_uniqueness is not None:
            result['AttributeUniqueness'] = self.attribute_uniqueness
        if self.attribute_format is not None:
            result['AttributeFormat'] = self.attribute_format
        if self.attribute_type is not None:
            result['AttributeType'] = self.attribute_type
        if self.attribute_reference is not None:
            result['AttributeReference'] = self.attribute_reference
        if self.attribute_table_display is not None:
            result['AttributeTableDisplay'] = self.attribute_table_display
        if self.attribute_placeholder is not None:
            result['AttributePlaceholder'] = self.attribute_placeholder
        if self.attribute_query is not None:
            result['AttributeQuery'] = self.attribute_query
        if self.attribute_fuzzy_query is not None:
            result['AttributeFuzzyQuery'] = self.attribute_fuzzy_query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeRequirement') is not None:
            self.attribute_requirement = m.get('AttributeRequirement')
        if m.get('AttributeUniqueness') is not None:
            self.attribute_uniqueness = m.get('AttributeUniqueness')
        if m.get('AttributeFormat') is not None:
            self.attribute_format = m.get('AttributeFormat')
        if m.get('AttributeType') is not None:
            self.attribute_type = m.get('AttributeType')
        if m.get('AttributeReference') is not None:
            self.attribute_reference = m.get('AttributeReference')
        if m.get('AttributeTableDisplay') is not None:
            self.attribute_table_display = m.get('AttributeTableDisplay')
        if m.get('AttributePlaceholder') is not None:
            self.attribute_placeholder = m.get('AttributePlaceholder')
        if m.get('AttributeQuery') is not None:
            self.attribute_query = m.get('AttributeQuery')
        if m.get('AttributeFuzzyQuery') is not None:
            self.attribute_fuzzy_query = m.get('AttributeFuzzyQuery')
        return self


class UpdateDeviceFormRequest(TeaModel):
    def __init__(
        self,
        device_form_id: str = None,
        config_compare: bool = None,
        account_config: bool = None,
        attribute_list: List[UpdateDeviceFormRequestAttributeList] = None,
        detail_display: bool = None,
        instance_id: str = None,
    ):
        # 设备形态ID
        self.device_form_id = device_form_id
        # 是否支持配置生成
        self.config_compare = config_compare
        # 是否需要账号配置
        self.account_config = account_config
        # 设备形态属性列表
        self.attribute_list = attribute_list
        # 是否展示设备详情
        self.detail_display = detail_display
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        if self.attribute_list:
            for k in self.attribute_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.config_compare is not None:
            result['ConfigCompare'] = self.config_compare
        if self.account_config is not None:
            result['AccountConfig'] = self.account_config
        result['AttributeList'] = []
        if self.attribute_list is not None:
            for k in self.attribute_list:
                result['AttributeList'].append(k.to_map() if k else None)
        if self.detail_display is not None:
            result['DetailDisplay'] = self.detail_display
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('ConfigCompare') is not None:
            self.config_compare = m.get('ConfigCompare')
        if m.get('AccountConfig') is not None:
            self.account_config = m.get('AccountConfig')
        self.attribute_list = []
        if m.get('AttributeList') is not None:
            for k in m.get('AttributeList'):
                temp_model = UpdateDeviceFormRequestAttributeList()
                self.attribute_list.append(temp_model.from_map(k))
        if m.get('DetailDisplay') is not None:
            self.detail_display = m.get('DetailDisplay')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateDeviceFormShrinkRequest(TeaModel):
    def __init__(
        self,
        device_form_id: str = None,
        config_compare: bool = None,
        account_config: bool = None,
        attribute_list_shrink: str = None,
        detail_display: bool = None,
        instance_id: str = None,
    ):
        # 设备形态ID
        self.device_form_id = device_form_id
        # 是否支持配置生成
        self.config_compare = config_compare
        # 是否需要账号配置
        self.account_config = account_config
        # 设备形态属性列表
        self.attribute_list_shrink = attribute_list_shrink
        # 是否展示设备详情
        self.detail_display = detail_display
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_form_id is not None:
            result['DeviceFormId'] = self.device_form_id
        if self.config_compare is not None:
            result['ConfigCompare'] = self.config_compare
        if self.account_config is not None:
            result['AccountConfig'] = self.account_config
        if self.attribute_list_shrink is not None:
            result['AttributeList'] = self.attribute_list_shrink
        if self.detail_display is not None:
            result['DetailDisplay'] = self.detail_display
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceFormId') is not None:
            self.device_form_id = m.get('DeviceFormId')
        if m.get('ConfigCompare') is not None:
            self.config_compare = m.get('ConfigCompare')
        if m.get('AccountConfig') is not None:
            self.account_config = m.get('AccountConfig')
        if m.get('AttributeList') is not None:
            self.attribute_list_shrink = m.get('AttributeList')
        if m.get('DetailDisplay') is not None:
            self.detail_display = m.get('DetailDisplay')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateDeviceFormResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDeviceFormResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDeviceFormResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDeviceFormResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDevicePropertyRequest(TeaModel):
    def __init__(
        self,
        device_property_id: str = None,
        property_format: str = None,
        property_content: str = None,
        property_name: str = None,
        instance_id: str = None,
    ):
        # 实例 ID。
        self.device_property_id = device_property_id
        # 属性格式
        self.property_format = property_format
        # 属性内容
        self.property_content = property_content
        # 属性名称
        self.property_name = property_name
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_property_id is not None:
            result['DevicePropertyId'] = self.device_property_id
        if self.property_format is not None:
            result['PropertyFormat'] = self.property_format
        if self.property_content is not None:
            result['PropertyContent'] = self.property_content
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevicePropertyId') is not None:
            self.device_property_id = m.get('DevicePropertyId')
        if m.get('PropertyFormat') is not None:
            self.property_format = m.get('PropertyFormat')
        if m.get('PropertyContent') is not None:
            self.property_content = m.get('PropertyContent')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateDevicePropertyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDevicePropertyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDevicePropertyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDevicePropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDevicesRequest(TeaModel):
    def __init__(
        self,
        device_ids: List[str] = None,
        login_type: str = None,
        login_username: str = None,
        login_password: str = None,
        snmp_account_version: str = None,
        snmp_community: str = None,
        snmp_account_type: str = None,
        snmp_security_level: str = None,
        snmp_user_name: str = None,
        snmp_auth_passphrase: str = None,
        snmp_auth_protocol: str = None,
        snmp_privacy_passphase: str = None,
        snmp_privacy_protocol: str = None,
        instance_id: str = None,
    ):
        # 设备ID
        self.device_ids = device_ids
        # 登录类型
        self.login_type = login_type
        # 登录账号
        self.login_username = login_username
        # 登录密码
        self.login_password = login_password
        # SNMP 版本号
        self.snmp_account_version = snmp_account_version
        # SNMP Community
        self.snmp_community = snmp_community
        # SNMP 账号类型
        self.snmp_account_type = snmp_account_type
        # SNMP 安全级别
        self.snmp_security_level = snmp_security_level
        # SNMP 用户名
        self.snmp_user_name = snmp_user_name
        # SNMP Auth PassPhrase
        self.snmp_auth_passphrase = snmp_auth_passphrase
        # SNMP Auth Protocol
        self.snmp_auth_protocol = snmp_auth_protocol
        # SNMP Privacy Passphase
        self.snmp_privacy_passphase = snmp_privacy_passphase
        # SNMP Privacy Protocol
        self.snmp_privacy_protocol = snmp_privacy_protocol
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids
        if self.login_type is not None:
            result['LoginType'] = self.login_type
        if self.login_username is not None:
            result['LoginUsername'] = self.login_username
        if self.login_password is not None:
            result['LoginPassword'] = self.login_password
        if self.snmp_account_version is not None:
            result['SnmpAccountVersion'] = self.snmp_account_version
        if self.snmp_community is not None:
            result['SnmpCommunity'] = self.snmp_community
        if self.snmp_account_type is not None:
            result['SnmpAccountType'] = self.snmp_account_type
        if self.snmp_security_level is not None:
            result['SnmpSecurityLevel'] = self.snmp_security_level
        if self.snmp_user_name is not None:
            result['SnmpUserName'] = self.snmp_user_name
        if self.snmp_auth_passphrase is not None:
            result['SnmpAuthPassphrase'] = self.snmp_auth_passphrase
        if self.snmp_auth_protocol is not None:
            result['SnmpAuthProtocol'] = self.snmp_auth_protocol
        if self.snmp_privacy_passphase is not None:
            result['SnmpPrivacyPassphase'] = self.snmp_privacy_passphase
        if self.snmp_privacy_protocol is not None:
            result['SnmpPrivacyProtocol'] = self.snmp_privacy_protocol
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIds') is not None:
            self.device_ids = m.get('DeviceIds')
        if m.get('LoginType') is not None:
            self.login_type = m.get('LoginType')
        if m.get('LoginUsername') is not None:
            self.login_username = m.get('LoginUsername')
        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')
        if m.get('SnmpAccountVersion') is not None:
            self.snmp_account_version = m.get('SnmpAccountVersion')
        if m.get('SnmpCommunity') is not None:
            self.snmp_community = m.get('SnmpCommunity')
        if m.get('SnmpAccountType') is not None:
            self.snmp_account_type = m.get('SnmpAccountType')
        if m.get('SnmpSecurityLevel') is not None:
            self.snmp_security_level = m.get('SnmpSecurityLevel')
        if m.get('SnmpUserName') is not None:
            self.snmp_user_name = m.get('SnmpUserName')
        if m.get('SnmpAuthPassphrase') is not None:
            self.snmp_auth_passphrase = m.get('SnmpAuthPassphrase')
        if m.get('SnmpAuthProtocol') is not None:
            self.snmp_auth_protocol = m.get('SnmpAuthProtocol')
        if m.get('SnmpPrivacyPassphase') is not None:
            self.snmp_privacy_passphase = m.get('SnmpPrivacyPassphase')
        if m.get('SnmpPrivacyProtocol') is not None:
            self.snmp_privacy_protocol = m.get('SnmpPrivacyProtocol')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateDevicesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePhysicalSpaceRequest(TeaModel):
    def __init__(
        self,
        physical_space_id: str = None,
        physical_space_name: str = None,
        country: str = None,
        province: str = None,
        city: str = None,
        address: str = None,
        instance_id: str = None,
    ):
        # 实例 ID。
        self.physical_space_id = physical_space_id
        # 物理空间名称
        self.physical_space_name = physical_space_name
        # 所属国家
        self.country = country
        # 所属省份
        self.province = province
        # 所属城市
        self.city = city
        # 具体地址
        self.address = address
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.physical_space_id is not None:
            result['PhysicalSpaceId'] = self.physical_space_id
        if self.physical_space_name is not None:
            result['PhysicalSpaceName'] = self.physical_space_name
        if self.country is not None:
            result['Country'] = self.country
        if self.province is not None:
            result['Province'] = self.province
        if self.city is not None:
            result['City'] = self.city
        if self.address is not None:
            result['Address'] = self.address
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalSpaceId') is not None:
            self.physical_space_id = m.get('PhysicalSpaceId')
        if m.get('PhysicalSpaceName') is not None:
            self.physical_space_name = m.get('PhysicalSpaceName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdatePhysicalSpaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePhysicalSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePhysicalSpaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdatePhysicalSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


