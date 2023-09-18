# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AllocatePublicConnectionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        database_instance_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the Simple Database Service instance.
        self.database_instance_id = database_instance_id
        # The region ID of the Simple Database Service instance. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AllocatePublicConnectionResponseBody(TeaModel):
    def __init__(
        self,
        public_connection: str = None,
        request_id: str = None,
    ):
        # The public endpoint that is assigned to the Simple Database Service instance.
        self.public_connection = public_connection
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.public_connection is not None:
            result['PublicConnection'] = self.public_connection
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PublicConnection') is not None:
            self.public_connection = m.get('PublicConnection')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AllocatePublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AllocatePublicConnectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AllocatePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCommandRequest(TeaModel):
    def __init__(
        self,
        command_content: str = None,
        description: str = None,
        enable_parameter: bool = None,
        name: str = None,
        region_id: str = None,
        timeout: int = None,
        type: str = None,
        working_dir: str = None,
    ):
        self.command_content = command_content
        self.description = description
        self.enable_parameter = enable_parameter
        self.name = name
        self.region_id = region_id
        self.timeout = timeout
        self.type = type
        self.working_dir = working_dir

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.type is not None:
            result['Type'] = self.type
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class CreateCommandResponseBody(TeaModel):
    def __init__(
        self,
        command_id: str = None,
        request_id: str = None,
    ):
        self.command_id = command_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCommandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomImageRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        data_snapshot_id: str = None,
        description: str = None,
        image_name: str = None,
        instance_id: str = None,
        region_id: str = None,
        system_snapshot_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the data disk snapshot.
        self.data_snapshot_id = data_snapshot_id
        # The description of the custom image.
        self.description = description
        # The name of the custom image. The name must be 2 to 128 characters in length, and can contain letters, digits, colons (:), underscores (\_), and hyphens (-). The name must start with a letter or a digit. This parameter is empty by default.
        self.image_name = image_name
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the database. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the system disk snapshot.
        self.system_snapshot_id = system_snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_snapshot_id is not None:
            result['DataSnapshotId'] = self.data_snapshot_id
        if self.description is not None:
            result['Description'] = self.description
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.system_snapshot_id is not None:
            result['SystemSnapshotId'] = self.system_snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataSnapshotId') is not None:
            self.data_snapshot_id = m.get('DataSnapshotId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SystemSnapshotId') is not None:
            self.system_snapshot_id = m.get('SystemSnapshotId')
        return self


class CreateCustomImageResponseBody(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        request_id: str = None,
    ):
        # The custom image ID.
        self.image_id = image_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCustomImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateCustomImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFirewallRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        port: str = None,
        region_id: str = None,
        remark: str = None,
        rule_protocol: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The port range. Valid values: 165535. Specify a port range in the format of \<start port number>/\<end port number>. Example: 1024/1055, which indicates the port range of 10241055.
        self.port = port
        # The region ID of the simple application server.
        self.region_id = region_id
        # The remarks of the firewall rule.
        self.remark = remark
        # The transport layer protocol. Valid values:
        # 
        # *   TCP: the TCP protocol
        # *   UDP: the UDP protocol
        # *   TCP+UDP: the TCP and UDP protocols
        self.rule_protocol = rule_protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.rule_protocol is not None:
            result['RuleProtocol'] = self.rule_protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RuleProtocol') is not None:
            self.rule_protocol = m.get('RuleProtocol')
        return self


class CreateFirewallRuleResponseBody(TeaModel):
    def __init__(
        self,
        firewall_id: str = None,
        request_id: str = None,
    ):
        # The ID of the firewall rule.
        self.firewall_id = firewall_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFirewallRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFirewallRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateFirewallRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFirewallRulesRequestFirewallRules(TeaModel):
    def __init__(
        self,
        port: str = None,
        remark: str = None,
        rule_protocol: str = None,
        source_cidr_ip: str = None,
    ):
        self.port = port
        self.remark = remark
        self.rule_protocol = rule_protocol
        self.source_cidr_ip = source_cidr_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.rule_protocol is not None:
            result['RuleProtocol'] = self.rule_protocol
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RuleProtocol') is not None:
            self.rule_protocol = m.get('RuleProtocol')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        return self


class CreateFirewallRulesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        firewall_rules: List[CreateFirewallRulesRequestFirewallRules] = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The client token.
        self.client_token = client_token
        # The remarks of the firewall rule.
        self.firewall_rules = firewall_rules
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        if self.firewall_rules:
            for k in self.firewall_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['FirewallRules'] = []
        if self.firewall_rules is not None:
            for k in self.firewall_rules:
                result['FirewallRules'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.firewall_rules = []
        if m.get('FirewallRules') is not None:
            for k in m.get('FirewallRules'):
                temp_model = CreateFirewallRulesRequestFirewallRules()
                self.firewall_rules.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateFirewallRulesShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        firewall_rules_shrink: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The client token.
        self.client_token = client_token
        # The remarks of the firewall rule.
        self.firewall_rules_shrink = firewall_rules_shrink
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.firewall_rules_shrink is not None:
            result['FirewallRules'] = self.firewall_rules_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('FirewallRules') is not None:
            self.firewall_rules_shrink = m.get('FirewallRules')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateFirewallRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class CreateFirewallRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFirewallRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateFirewallRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceKeyPairRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        key_pair_name: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateInstanceKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        fingerprint: str = None,
        key_pair_name: str = None,
        private_key: str = None,
        request_id: str = None,
    ):
        # The fingerprint of the key pair.
        self.fingerprint = fingerprint
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # The private key.
        self.private_key = private_key
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceKeyPairResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateInstanceKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstancesRequest(TeaModel):
    def __init__(
        self,
        amount: int = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        charge_type: str = None,
        client_token: str = None,
        data_disk_size: int = None,
        image_id: str = None,
        period: int = None,
        plan_id: str = None,
        region_id: str = None,
    ):
        # The number of simple application servers that you want to create. Valid values: 1 to 20.
        # 
        # Default value: 1.
        self.amount = amount
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.auto_renew = auto_renew
        # The auto-renewal period. This parameter is required only when you set `AutoRenew` to true. Unit: months. Valid values: 1, 3, 6, 12, 24, and 36.
        self.auto_renew_period = auto_renew_period
        # The billing method of the simple application servers. Set the value to PrePaid, which indicates the subscription billing method.
        # 
        # Default value: PrePaid.
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The size of the data disk that is attached to the server. Unit: GB. Valid values: 0 to 16380. The value must be an integral multiple of 20.
        # 
        # *   A value of 0 indicates that no data disk is attached.
        # *   If the disk included in the specified plan is a standard SSD, the data disk must be 20 GB or larger in size.
        # 
        # Default value: 0.
        self.data_disk_size = data_disk_size
        # The image ID. You can call the [ListImages](~~189313~~) operation to query the available images in the specified region.
        self.image_id = image_id
        # The subscription period of the servers. Unit: months. Valid values: 1, 3, 6, 12, 24, and 36.
        self.period = period
        # The plan ID. You can call the [ListPlans](~~189314~~) operation to query all plans provided by Simple Application Server in the specified region.
        self.plan_id = plan_id
        # The region ID of the simple application servers. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.period is not None:
            result['Period'] = self.period
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        request_id: str = None,
    ):
        # The IDs of the simple application servers.
        self.instance_ids = instance_ids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSnapshotRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        disk_id: str = None,
        region_id: str = None,
        snapshot_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The disk ID.
        self.disk_id = disk_id
        # The region ID of the simple application server to which the disk is attached.
        self.region_id = region_id
        # The snapshot name. The name must be 2 to 50 characters in length. It must start with a letter but cannot start with `http://` or `https://`. The name can only contain letters, digits, colons (:), underscores (\_), periods (.), and hyphens (-).
        self.snapshot_name = snapshot_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        return self


class CreateSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        snapshot_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The snapshot ID.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class CreateSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCommandRequest(TeaModel):
    def __init__(
        self,
        command_id: str = None,
        region_id: str = None,
    ):
        self.command_id = command_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCommandResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class DeleteCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCommandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomImageRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        image_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The custom image ID.
        self.image_id = image_id
        # The region ID of the custom image. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteCustomImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteCustomImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteCustomImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFirewallRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        region_id: str = None,
        rule_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the simple application server.
        self.region_id = region_id
        # The ID of the firewall rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteFirewallRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteFirewallRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFirewallRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteFirewallRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceKeyPairRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteInstanceKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteInstanceKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstanceKeyPairResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteInstanceKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        snapshot_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The region ID of the snapshot.
        self.region_id = region_id
        # The snapshot ID.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class DeleteSnapshotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteSnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSnapshotResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteSnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSnapshotsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        snapshot_ids: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id
        # The snapshot IDs. The value can be a JSON array that consists of up to 100 snapshot IDs. Separate multiple snapshot IDs with commas (,).
        self.snapshot_ids = snapshot_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')
        return self


class DeleteSnapshotsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteSnapshotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSnapshotsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudAssistantStatusRequest(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The IDs of the simple application servers.
        self.instance_ids = instance_ids
        # The page number.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the simple application servers.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCloudAssistantStatusShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_ids_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The IDs of the simple application servers.
        self.instance_ids_shrink = instance_ids_shrink
        # The page number.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the simple application servers.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCloudAssistantStatusResponseBodyCloudAssistantStatus(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        status: bool = None,
    ):
        # The ID of the simple application server.
        self.instance_id = instance_id
        # Indicates whether the Cloud Assistant client is installed on the server.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCloudAssistantStatusResponseBody(TeaModel):
    def __init__(
        self,
        cloud_assistant_status: List[DescribeCloudAssistantStatusResponseBodyCloudAssistantStatus] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Indicates whether the Cloud Assistant client is installed on the server.
        self.cloud_assistant_status = cloud_assistant_status
        # The page number.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.cloud_assistant_status:
            for k in self.cloud_assistant_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CloudAssistantStatus'] = []
        if self.cloud_assistant_status is not None:
            for k in self.cloud_assistant_status:
                result['CloudAssistantStatus'].append(k.to_map() if k else None)
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
        self.cloud_assistant_status = []
        if m.get('CloudAssistantStatus') is not None:
            for k in m.get('CloudAssistantStatus'):
                temp_model = DescribeCloudAssistantStatusResponseBodyCloudAssistantStatus()
                self.cloud_assistant_status.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCloudAssistantStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCloudAssistantStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeCloudAssistantStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudMonitorAgentStatusesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_ids: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The IDs of the simple application servers. The value can be a JSON array that consists of up to 100 simple application server IDs. Separate multiple server IDs with commas (,).
        self.instance_ids = instance_ids
        # The region ID of the simple application servers. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCloudMonitorAgentStatusesResponseBodyInstanceStatusList(TeaModel):
    def __init__(
        self,
        auto_install: bool = None,
        instance_id: str = None,
        status: str = None,
    ):
        self.auto_install = auto_install
        self.instance_id = instance_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCloudMonitorAgentStatusesResponseBody(TeaModel):
    def __init__(
        self,
        instance_status_list: List[DescribeCloudMonitorAgentStatusesResponseBodyInstanceStatusList] = None,
        request_id: str = None,
    ):
        # Indicates whether the Cloud Monitor agent was automatically installed on the simple application server. Valid values:
        # 
        # *   true
        # *   false
        self.instance_status_list = instance_status_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_status_list:
            for k in self.instance_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceStatusList'] = []
        if self.instance_status_list is not None:
            for k in self.instance_status_list:
                result['InstanceStatusList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_status_list = []
        if m.get('InstanceStatusList') is not None:
            for k in m.get('InstanceStatusList'):
                temp_model = DescribeCloudMonitorAgentStatusesResponseBodyInstanceStatusList()
                self.instance_status_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCloudMonitorAgentStatusesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCloudMonitorAgentStatusesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeCloudMonitorAgentStatusesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCommandInvocationsRequest(TeaModel):
    def __init__(
        self,
        command_id: str = None,
        command_name: str = None,
        command_type: str = None,
        instance_id: str = None,
        invocation_status: str = None,
        invoke_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        self.command_id = command_id
        self.command_name = command_name
        self.command_type = command_type
        self.instance_id = instance_id
        self.invocation_status = invocation_status
        self.invoke_id = invoke_id
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.command_name is not None:
            result['CommandName'] = self.command_name
        if self.command_type is not None:
            result['CommandType'] = self.command_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeCommandInvocationsResponseBodyCommandInvocationsInvokeInstances(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_info: str = None,
        exit_code: int = None,
        finish_time: str = None,
        instance_id: str = None,
        invocation_status: str = None,
        output: str = None,
        start_time: str = None,
    ):
        self.error_code = error_code
        self.error_info = error_info
        self.exit_code = exit_code
        self.finish_time = finish_time
        self.instance_id = instance_id
        self.invocation_status = invocation_status
        self.output = output
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.output is not None:
            result['Output'] = self.output
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCommandInvocationsResponseBodyCommandInvocations(TeaModel):
    def __init__(
        self,
        command_content: str = None,
        command_description: str = None,
        command_id: str = None,
        command_name: str = None,
        command_type: str = None,
        creation_time: str = None,
        invocation_status: str = None,
        invoke_id: str = None,
        invoke_instances: List[DescribeCommandInvocationsResponseBodyCommandInvocationsInvokeInstances] = None,
        parameters: str = None,
        timeout: int = None,
        username: str = None,
        working_dir: str = None,
    ):
        self.command_content = command_content
        self.command_description = command_description
        self.command_id = command_id
        self.command_name = command_name
        self.command_type = command_type
        self.creation_time = creation_time
        self.invocation_status = invocation_status
        self.invoke_id = invoke_id
        self.invoke_instances = invoke_instances
        self.parameters = parameters
        self.timeout = timeout
        self.username = username
        self.working_dir = working_dir

    def validate(self):
        if self.invoke_instances:
            for k in self.invoke_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.command_description is not None:
            result['CommandDescription'] = self.command_description
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.command_name is not None:
            result['CommandName'] = self.command_name
        if self.command_type is not None:
            result['CommandType'] = self.command_type
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        result['InvokeInstances'] = []
        if self.invoke_instances is not None:
            for k in self.invoke_instances:
                result['InvokeInstances'].append(k.to_map() if k else None)
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.username is not None:
            result['Username'] = self.username
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('CommandDescription') is not None:
            self.command_description = m.get('CommandDescription')
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        self.invoke_instances = []
        if m.get('InvokeInstances') is not None:
            for k in m.get('InvokeInstances'):
                temp_model = DescribeCommandInvocationsResponseBodyCommandInvocationsInvokeInstances()
                self.invoke_instances.append(temp_model.from_map(k))
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class DescribeCommandInvocationsResponseBody(TeaModel):
    def __init__(
        self,
        command_invocations: List[DescribeCommandInvocationsResponseBodyCommandInvocations] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.command_invocations = command_invocations
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.command_invocations:
            for k in self.command_invocations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CommandInvocations'] = []
        if self.command_invocations is not None:
            for k in self.command_invocations:
                result['CommandInvocations'].append(k.to_map() if k else None)
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
        self.command_invocations = []
        if m.get('CommandInvocations') is not None:
            for k in m.get('CommandInvocations'):
                temp_model = DescribeCommandInvocationsResponseBodyCommandInvocations()
                self.command_invocations.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCommandInvocationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCommandInvocationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeCommandInvocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCommandsRequest(TeaModel):
    def __init__(
        self,
        command_id: str = None,
        name: str = None,
        page_number: str = None,
        page_size: str = None,
        provider: str = None,
        region_id: str = None,
        type: str = None,
    ):
        self.command_id = command_id
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.provider = provider
        self.region_id = region_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCommandsResponseBodyCommandsParameterDefinitions(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        parameter_name: str = None,
        possible_values: List[str] = None,
        required: bool = None,
    ):
        self.default_value = default_value
        self.description = description
        self.parameter_name = parameter_name
        self.possible_values = possible_values
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.description is not None:
            result['Description'] = self.description
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.possible_values is not None:
            result['PossibleValues'] = self.possible_values
        if self.required is not None:
            result['Required'] = self.required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('PossibleValues') is not None:
            self.possible_values = m.get('PossibleValues')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        return self


class DescribeCommandsResponseBodyCommands(TeaModel):
    def __init__(
        self,
        command_content: str = None,
        command_id: str = None,
        creation_time: str = None,
        description: str = None,
        enable_parameter: bool = None,
        name: str = None,
        parameter_definitions: List[DescribeCommandsResponseBodyCommandsParameterDefinitions] = None,
        parameter_names: List[str] = None,
        provider: str = None,
        timeout: int = None,
        type: str = None,
        working_dir: str = None,
    ):
        self.command_content = command_content
        self.command_id = command_id
        self.creation_time = creation_time
        self.description = description
        self.enable_parameter = enable_parameter
        self.name = name
        self.parameter_definitions = parameter_definitions
        self.parameter_names = parameter_names
        self.provider = provider
        self.timeout = timeout
        self.type = type
        self.working_dir = working_dir

    def validate(self):
        if self.parameter_definitions:
            for k in self.parameter_definitions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter
        if self.name is not None:
            result['Name'] = self.name
        result['ParameterDefinitions'] = []
        if self.parameter_definitions is not None:
            for k in self.parameter_definitions:
                result['ParameterDefinitions'].append(k.to_map() if k else None)
        if self.parameter_names is not None:
            result['ParameterNames'] = self.parameter_names
        if self.provider is not None:
            result['Provider'] = self.provider
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.type is not None:
            result['Type'] = self.type
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.parameter_definitions = []
        if m.get('ParameterDefinitions') is not None:
            for k in m.get('ParameterDefinitions'):
                temp_model = DescribeCommandsResponseBodyCommandsParameterDefinitions()
                self.parameter_definitions.append(temp_model.from_map(k))
        if m.get('ParameterNames') is not None:
            self.parameter_names = m.get('ParameterNames')
        if m.get('Provider') is not None:
            self.provider = m.get('Provider')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class DescribeCommandsResponseBody(TeaModel):
    def __init__(
        self,
        commands: List[DescribeCommandsResponseBodyCommands] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.commands = commands
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.commands:
            for k in self.commands:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Commands'] = []
        if self.commands is not None:
            for k in self.commands:
                result['Commands'].append(k.to_map() if k else None)
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
        self.commands = []
        if m.get('Commands') is not None:
            for k in m.get('Commands'):
                temp_model = DescribeCommandsResponseBodyCommands()
                self.commands.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCommandsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCommandsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeCommandsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDatabaseErrorLogsRequest(TeaModel):
    def __init__(
        self,
        database_instance_id: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The ID of the Simple Database Service instance.
        self.database_instance_id = database_instance_id
        # The end of the time range to query. Specify the time in the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC. The end time must be later than the start time.
        # 
        # > The time displayed in the Simple Application Server console is in the format of UTC+8.
        self.end_time = end_time
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID of the Simple Database Service instance.
        # 
        # You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        # 
        # > The time displayed in the Simple Application Server console is in the format of UTC+8.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDatabaseErrorLogsResponseBodyErrorLogs(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        error_info: str = None,
    ):
        self.create_time = create_time
        self.error_info = error_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        return self


class DescribeDatabaseErrorLogsResponseBody(TeaModel):
    def __init__(
        self,
        error_logs: List[DescribeDatabaseErrorLogsResponseBodyErrorLogs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The time when the error log entry was generated. The time follows the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        # 
        # > The time displayed in the Simple Application Server console is in the format of UTC+8.
        self.error_logs = error_logs
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.error_logs:
            for k in self.error_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ErrorLogs'] = []
        if self.error_logs is not None:
            for k in self.error_logs:
                result['ErrorLogs'].append(k.to_map() if k else None)
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
        self.error_logs = []
        if m.get('ErrorLogs') is not None:
            for k in m.get('ErrorLogs'):
                temp_model = DescribeDatabaseErrorLogsResponseBodyErrorLogs()
                self.error_logs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDatabaseErrorLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDatabaseErrorLogsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeDatabaseErrorLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDatabaseInstanceMetricDataRequest(TeaModel):
    def __init__(
        self,
        database_instance_id: str = None,
        end_time: str = None,
        metric_name: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The ID of the Simple Database Service instance.
        self.database_instance_id = database_instance_id
        # The end of the time range to query. Specify the time in the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        # 
        # > The time displayed in the Simple Application Server console is in the format of UTC+8.
        self.end_time = end_time
        # The name of the metric. Valid values:
        # 
        # *   MySQL_MemCpuUsage: The CPU utilization and memory usage of the instance within the entire operating system.
        # *   MySQL_DetailedSpaceUsage: The total space usage, data space, log space, temporary space, and system space of the instance.
        # *   MySQL_Sessions : The total number of active connections.
        # *   MySQL_IOPS: The IOPS of the instance.
        self.metric_name = metric_name
        # The region ID of the Simple Database Service instance. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        # 
        # > The time displayed in the Simple Application Server console is in the format of UTC+8.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDatabaseInstanceMetricDataResponseBody(TeaModel):
    def __init__(
        self,
        data_format: str = None,
        metric_data: str = None,
        metric_name: str = None,
        request_id: str = None,
        unit: str = None,
    ):
        # The data format. Valid values:
        # 
        # *   cpuusage\&memusage
        # *   active_session\&total_session
        # *   ins_size\&data_size\&log_size\&tmp_size\&other_size
        # *   io
        self.data_format = data_format
        # The monitoring data.
        self.metric_data = metric_data
        # The name of the metric. Valid values:
        # 
        # *   MySQL_MemCpuUsage: The CPU utilization and memory usage of the instance within the entire operating system.
        # *   MySQL_DetailedSpaceUsage: The total space usage, data space, log space, temporary space, and system space of the instance.
        # *   MySQL_Sessions : The total number of active connections.
        # *   MySQL_IOPS: The IOPS of the instance.
        self.metric_name = metric_name
        # The request ID.
        self.request_id = request_id
        # The unit of the monitoring metric.
        # 
        # *   %\
        # *   int
        # *   MB
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_format is not None:
            result['DataFormat'] = self.data_format
        if self.metric_data is not None:
            result['MetricData'] = self.metric_data
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFormat') is not None:
            self.data_format = m.get('DataFormat')
        if m.get('MetricData') is not None:
            self.metric_data = m.get('MetricData')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class DescribeDatabaseInstanceMetricDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDatabaseInstanceMetricDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeDatabaseInstanceMetricDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDatabaseInstanceParametersRequest(TeaModel):
    def __init__(
        self,
        database_instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the Simple Database Service instance.
        self.database_instance_id = database_instance_id
        # The region ID of the Simple Database Service instance. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDatabaseInstanceParametersResponseBodyConfigParameters(TeaModel):
    def __init__(
        self,
        checking_code: str = None,
        force_modify: str = None,
        force_restart: str = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.checking_code = checking_code
        self.force_modify = force_modify
        self.force_restart = force_restart
        self.parameter_description = parameter_description
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code
        if self.force_modify is not None:
            result['ForceModify'] = self.force_modify
        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')
        if m.get('ForceModify') is not None:
            self.force_modify = m.get('ForceModify')
        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class DescribeDatabaseInstanceParametersResponseBodyRunningParameters(TeaModel):
    def __init__(
        self,
        checking_code: str = None,
        force_modify: str = None,
        force_restart: str = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.checking_code = checking_code
        self.force_modify = force_modify
        self.force_restart = force_restart
        self.parameter_description = parameter_description
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code
        if self.force_modify is not None:
            result['ForceModify'] = self.force_modify
        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')
        if m.get('ForceModify') is not None:
            self.force_modify = m.get('ForceModify')
        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class DescribeDatabaseInstanceParametersResponseBody(TeaModel):
    def __init__(
        self,
        config_parameters: List[DescribeDatabaseInstanceParametersResponseBodyConfigParameters] = None,
        engine: str = None,
        engine_version: str = None,
        request_id: str = None,
        running_parameters: List[DescribeDatabaseInstanceParametersResponseBodyRunningParameters] = None,
    ):
        # The range of ParameterValue.
        # 
        # > The value of CheckingCode varies based on the value of ParameterName.
        self.config_parameters = config_parameters
        # The database engine that the instance runs. The value must be MySQL.
        self.engine = engine
        # The version of the database engine. Valid values:
        # 
        # *   5.7: MySQL 5.7.
        # *   8.0: MySQL 8.0.
        self.engine_version = engine_version
        # The request ID.
        self.request_id = request_id
        # The range of ParameterValue.
        # 
        # > The value of CheckingCode varies based on the value of ParameterName.
        self.running_parameters = running_parameters

    def validate(self):
        if self.config_parameters:
            for k in self.config_parameters:
                if k:
                    k.validate()
        if self.running_parameters:
            for k in self.running_parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigParameters'] = []
        if self.config_parameters is not None:
            for k in self.config_parameters:
                result['ConfigParameters'].append(k.to_map() if k else None)
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RunningParameters'] = []
        if self.running_parameters is not None:
            for k in self.running_parameters:
                result['RunningParameters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_parameters = []
        if m.get('ConfigParameters') is not None:
            for k in m.get('ConfigParameters'):
                temp_model = DescribeDatabaseInstanceParametersResponseBodyConfigParameters()
                self.config_parameters.append(temp_model.from_map(k))
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.running_parameters = []
        if m.get('RunningParameters') is not None:
            for k in m.get('RunningParameters'):
                temp_model = DescribeDatabaseInstanceParametersResponseBodyRunningParameters()
                self.running_parameters.append(temp_model.from_map(k))
        return self


class DescribeDatabaseInstanceParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDatabaseInstanceParametersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeDatabaseInstanceParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDatabaseInstancesRequest(TeaModel):
    def __init__(
        self,
        database_instance_ids: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The IDs of the Simple Database Service instances. The value can be a JSON array that consists of up to 100 Simple Database Service instance IDs. Separate multiple instance IDs with commas (,).
        self.database_instance_ids = database_instance_ids
        # The page number.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the Simple Database Service instances.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_instance_ids is not None:
            result['DatabaseInstanceIds'] = self.database_instance_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseInstanceIds') is not None:
            self.database_instance_ids = m.get('DatabaseInstanceIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDatabaseInstancesResponseBodyDatabaseInstances(TeaModel):
    def __init__(
        self,
        business_status: str = None,
        charge_type: str = None,
        cpu: str = None,
        creation_time: str = None,
        database_instance_edition: str = None,
        database_instance_id: str = None,
        database_instance_name: str = None,
        database_instance_status: str = None,
        database_version: str = None,
        expired_time: str = None,
        memory: str = None,
        private_connection: str = None,
        public_connection: str = None,
        region_id: str = None,
        storage: int = None,
        super_account_name: str = None,
    ):
        self.business_status = business_status
        self.charge_type = charge_type
        self.cpu = cpu
        self.creation_time = creation_time
        self.database_instance_edition = database_instance_edition
        self.database_instance_id = database_instance_id
        self.database_instance_name = database_instance_name
        self.database_instance_status = database_instance_status
        self.database_version = database_version
        self.expired_time = expired_time
        self.memory = memory
        self.private_connection = private_connection
        self.public_connection = public_connection
        self.region_id = region_id
        self.storage = storage
        self.super_account_name = super_account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.database_instance_edition is not None:
            result['DatabaseInstanceEdition'] = self.database_instance_edition
        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id
        if self.database_instance_name is not None:
            result['DatabaseInstanceName'] = self.database_instance_name
        if self.database_instance_status is not None:
            result['DatabaseInstanceStatus'] = self.database_instance_status
        if self.database_version is not None:
            result['DatabaseVersion'] = self.database_version
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.private_connection is not None:
            result['PrivateConnection'] = self.private_connection
        if self.public_connection is not None:
            result['PublicConnection'] = self.public_connection
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.super_account_name is not None:
            result['SuperAccountName'] = self.super_account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DatabaseInstanceEdition') is not None:
            self.database_instance_edition = m.get('DatabaseInstanceEdition')
        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')
        if m.get('DatabaseInstanceName') is not None:
            self.database_instance_name = m.get('DatabaseInstanceName')
        if m.get('DatabaseInstanceStatus') is not None:
            self.database_instance_status = m.get('DatabaseInstanceStatus')
        if m.get('DatabaseVersion') is not None:
            self.database_version = m.get('DatabaseVersion')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('PrivateConnection') is not None:
            self.private_connection = m.get('PrivateConnection')
        if m.get('PublicConnection') is not None:
            self.public_connection = m.get('PublicConnection')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('SuperAccountName') is not None:
            self.super_account_name = m.get('SuperAccountName')
        return self


class DescribeDatabaseInstancesResponseBody(TeaModel):
    def __init__(
        self,
        database_instances: List[DescribeDatabaseInstancesResponseBodyDatabaseInstances] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The name of the super administrator account of the Simple Database Service instance.
        self.database_instances = database_instances
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.database_instances:
            for k in self.database_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DatabaseInstances'] = []
        if self.database_instances is not None:
            for k in self.database_instances:
                result['DatabaseInstances'].append(k.to_map() if k else None)
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
        self.database_instances = []
        if m.get('DatabaseInstances') is not None:
            for k in m.get('DatabaseInstances'):
                temp_model = DescribeDatabaseInstancesResponseBodyDatabaseInstances()
                self.database_instances.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDatabaseInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDatabaseInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeDatabaseInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDatabaseSlowLogRecordsRequest(TeaModel):
    def __init__(
        self,
        acs_product: str = None,
        database_instance_id: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.acs_product = acs_product
        # The ID of the Simple Database Service instance.
        self.database_instance_id = database_instance_id
        # The end of the time range to query. The end time must be later than the start time. The interval between the start time and the end time must be less than 7 days.
        # 
        # Specify the time in the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The time displayed in the Simple Application Server console is in the format of UTC+8.
        self.end_time = end_time
        # The page number.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 30 to 100.
        # 
        # Default value: 30.
        self.page_size = page_size
        # The region ID of the Simple Database Service instance. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id
        # The beginning of the time range to query.
        # 
        # Specify the time in the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The time displayed in the Simple Application Server console is in the format of UTC+8.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acs_product is not None:
            result['AcsProduct'] = self.acs_product
        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcsProduct') is not None:
            self.acs_product = m.get('AcsProduct')
        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDatabaseSlowLogRecordsResponseBodySlowLogs(TeaModel):
    def __init__(
        self,
        dbname: str = None,
        execution_start_time: str = None,
        host_address: str = None,
        lock_times: int = None,
        parse_row_counts: int = None,
        query_time_ms: int = None,
        query_times: int = None,
        return_row_counts: int = None,
        sqltext: str = None,
    ):
        self.dbname = dbname
        self.execution_start_time = execution_start_time
        self.host_address = host_address
        self.lock_times = lock_times
        self.parse_row_counts = parse_row_counts
        self.query_time_ms = query_time_ms
        self.query_times = query_times
        self.return_row_counts = return_row_counts
        self.sqltext = sqltext

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbname is not None:
            result['DBName'] = self.dbname
        if self.execution_start_time is not None:
            result['ExecutionStartTime'] = self.execution_start_time
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.lock_times is not None:
            result['LockTimes'] = self.lock_times
        if self.parse_row_counts is not None:
            result['ParseRowCounts'] = self.parse_row_counts
        if self.query_time_ms is not None:
            result['QueryTimeMS'] = self.query_time_ms
        if self.query_times is not None:
            result['QueryTimes'] = self.query_times
        if self.return_row_counts is not None:
            result['ReturnRowCounts'] = self.return_row_counts
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')
        if m.get('ExecutionStartTime') is not None:
            self.execution_start_time = m.get('ExecutionStartTime')
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('LockTimes') is not None:
            self.lock_times = m.get('LockTimes')
        if m.get('ParseRowCounts') is not None:
            self.parse_row_counts = m.get('ParseRowCounts')
        if m.get('QueryTimeMS') is not None:
            self.query_time_ms = m.get('QueryTimeMS')
        if m.get('QueryTimes') is not None:
            self.query_times = m.get('QueryTimes')
        if m.get('ReturnRowCounts') is not None:
            self.return_row_counts = m.get('ReturnRowCounts')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        return self


class DescribeDatabaseSlowLogRecordsResponseBody(TeaModel):
    def __init__(
        self,
        engine: str = None,
        page_number: int = None,
        page_size: int = None,
        physical_ioread: int = None,
        request_id: str = None,
        slow_logs: List[DescribeDatabaseSlowLogRecordsResponseBodySlowLogs] = None,
        total_count: int = None,
    ):
        # The database engine that the instance runs.
        self.engine = engine
        # The page number.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 30 to 100.
        # 
        # Default value: 30.
        self.page_size = page_size
        # The number of logical reads.
        self.physical_ioread = physical_ioread
        # The request ID.
        self.request_id = request_id
        # The database name.
        self.slow_logs = slow_logs
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.slow_logs:
            for k in self.slow_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.physical_ioread is not None:
            result['PhysicalIORead'] = self.physical_ioread
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SlowLogs'] = []
        if self.slow_logs is not None:
            for k in self.slow_logs:
                result['SlowLogs'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhysicalIORead') is not None:
            self.physical_ioread = m.get('PhysicalIORead')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.slow_logs = []
        if m.get('SlowLogs') is not None:
            for k in m.get('SlowLogs'):
                temp_model = DescribeDatabaseSlowLogRecordsResponseBodySlowLogs()
                self.slow_logs.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDatabaseSlowLogRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDatabaseSlowLogRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeDatabaseSlowLogRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceKeyPairRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        fingerprint: str = None,
        key_pair_name: str = None,
        request_id: str = None,
    ):
        # The fingerprint of the key pair.
        self.fingerprint = fingerprint
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceKeyPairResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeInstanceKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancePasswordsSettingRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstancePasswordsSettingResponseBody(TeaModel):
    def __init__(
        self,
        instance_password_setting: bool = None,
        request_id: str = None,
        vnc_password_setting: bool = None,
    ):
        # Indicates whether a logon password is set for the simple application server.
        self.instance_password_setting = instance_password_setting
        # The request ID.
        self.request_id = request_id
        # Indicates whether a VNC connection password is set.
        self.vnc_password_setting = vnc_password_setting

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_password_setting is not None:
            result['InstancePasswordSetting'] = self.instance_password_setting
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vnc_password_setting is not None:
            result['VncPasswordSetting'] = self.vnc_password_setting
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstancePasswordSetting') is not None:
            self.instance_password_setting = m.get('InstancePasswordSetting')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VncPasswordSetting') is not None:
            self.vnc_password_setting = m.get('VncPasswordSetting')
        return self


class DescribeInstancePasswordsSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstancePasswordsSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeInstancePasswordsSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceVncUrlRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the simple application server.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceVncUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vnc_url: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The VNC connection address of the server.
        self.vnc_url = vnc_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vnc_url is not None:
            result['VncUrl'] = self.vnc_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VncUrl') is not None:
            self.vnc_url = m.get('VncUrl')
        return self


class DescribeInstanceVncUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceVncUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeInstanceVncUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInvocationResultRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        invoke_id: str = None,
        region_id: str = None,
    ):
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The execution ID. You can call the [DescribeInvocations](~~439368~~) operation to query execution IDs.
        self.invoke_id = invoke_id
        # The region ID of the simple application server. You can call the [DescribeRegions](~~25609~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInvocationResultResponseBodyInvocationResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_info: str = None,
        exit_code: int = None,
        finished_time: str = None,
        instance_id: str = None,
        invocation_status: str = None,
        invoke_id: str = None,
        invoke_record_status: str = None,
        invoke_user: str = None,
        output: str = None,
        start_time: str = None,
    ):
        # The error code that is returned if the command failed to be sent or executed.
        # 
        # *   If this parameter is empty, the command is executed normally.
        # *   InstanceNotExists: The specified server does not exist or is released.
        # *   InstanceReleased: The server was released while the command was being executed on the server.
        # *   InstanceNotRunning: The server is not in the Running state while the command is being executed.
        # *   CommandNotApplicable: The command is not applicable to the specified server.
        # *   AccountNotExists: The specified account does not exist.
        # *   DirectoryNotExists: The specified directory does not exist.
        # *   BadCronExpression: The specified cron expression for the execution schedule is invalid.
        # *   ClientNotRunning: The Cloud Assistant client is not running.
        # *   ClientNotResponse: The Cloud Assistant client does not respond.
        # *   ClientIsUpgrading: The Cloud Assistant client is being upgraded.
        # *   ClientNeedUpgrade: The Cloud Assistant client needs to be upgraded.
        # *   DeliveryTimeout: Command sending times out.
        # *   ExecutionTimeout: The execution times out.
        # *   ExecutionException: An exception occurs while the command is being executed.
        # *   ExecutionInterrupted: The execution is interrupted.
        # *   ExitCodeNonzero: The execution is complete, but the exit code is not 0.
        self.error_code = error_code
        # The error message returned when the command is not successfully sent or executed. Valid values:
        # 
        # *   If this parameter is empty, the command is executed normally.
        # *   the specified instance does not exists: The specified server does not exist or is released.
        # *   the instance has released when create task: The server was released while the command was being executed on the server.
        # *   the instance is not running when create task: The server is not in the Running state while the command is being executed.
        # *   the command is not applicable: The command is not applicable to the specified server.
        # *   the specified account does not exists: The specified account does not exist.
        # *   the specified directory does not exists: The specified directory does not exist.
        # *   the cron job expression is invalid: The specified cron expression is invalid.
        # *   the aliyun service is not running on the instance: The Cloud Assistance client is not running.
        # *   the aliyun service in the instance does not response: The Cloud Assistant client does not respond to your request.
        # *   the aliyun service in the instance is upgrading now: The Cloud Assistant client is being upgraded.
        # *   the aliyun service in the instance need upgrade: The Cloud Assistant client needs to be upgraded.
        # *   the command delivery has been timeout: Command sending times out.
        # *   the command execution has been timeout: The execution times out.
        # *   the command execution got an exception: An exception occurs while the command is being executed.
        # *   the command execution has been interrupted: The execution is interrupted.
        # *   the command execution exit code is not zero: The execution is complete, and the exit code is not 0.
        self.error_info = error_info
        # The exit code of the command.
        # 
        # *   For Linux instances, the exit code is the exit code of the shell command.
        # *   For Windows instances, the exit code is the exit code of the batch or PowerShell command.
        self.exit_code = exit_code
        # The time when the execution ended.
        self.finished_time = finished_time
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The status of the execution progress. Valid values:
        # 
        # *   Pending: The command is being verified or sent.
        # *   Invalid: The specified command type or parameter is invalid.
        # *   Aborted: The command fails to be sent to the server. To send a command to a server, make sure that the server is in the Running state and the command can be sent within 1 minute.
        # *   Running: The command is being executed on the server.
        # *   Success: The execution is completed, and the exit code is 0.
        # *   Failed: The execution is completed, and the exit code is not 0.
        # *   Error: The execution cannot proceed due to an exception.
        # *   Timeout: The execution times out.
        # *   Cancelled: The execution is canceled, and the command is not executed.
        # *   Stopping: The command in the Running state is being stopped.
        # *   Terminated: The command is terminated while it is being executed.
        self.invocation_status = invocation_status
        # The execution ID.
        self.invoke_id = invoke_id
        # The status of the execution. Valid values:
        # 
        # *   Running
        # *   Finished
        # *   Failed
        # *   Stopped
        self.invoke_record_status = invoke_record_status
        # The username who executes the command on the simple application server.
        self.invoke_user = invoke_user
        # The command output.
        self.output = output
        # The time when the execution started.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.invoke_record_status is not None:
            result['InvokeRecordStatus'] = self.invoke_record_status
        if self.invoke_user is not None:
            result['InvokeUser'] = self.invoke_user
        if self.output is not None:
            result['Output'] = self.output
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('InvokeRecordStatus') is not None:
            self.invoke_record_status = m.get('InvokeRecordStatus')
        if m.get('InvokeUser') is not None:
            self.invoke_user = m.get('InvokeUser')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeInvocationResultResponseBody(TeaModel):
    def __init__(
        self,
        invocation_result: DescribeInvocationResultResponseBodyInvocationResult = None,
        request_id: str = None,
    ):
        # The execution results.
        self.invocation_result = invocation_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.invocation_result:
            self.invocation_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invocation_result is not None:
            result['InvocationResult'] = self.invocation_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvocationResult') is not None:
            temp_model = DescribeInvocationResultResponseBodyInvocationResult()
            self.invocation_result = temp_model.from_map(m['InvocationResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInvocationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInvocationResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeInvocationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInvocationsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        invoke_status: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The status of the command execution. Valid values:
        # 
        # *   Running: The command is being executed.
        # *   Finished: The execution is complete.
        # *   Failed: The execution fails.
        self.invoke_status = invoke_status
        # The page number.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.invoke_status is not None:
            result['InvokeStatus'] = self.invoke_status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InvokeStatus') is not None:
            self.invoke_status = m.get('InvokeStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInvocationsResponseBodyInvocations(TeaModel):
    def __init__(
        self,
        command_content: str = None,
        command_name: str = None,
        command_type: str = None,
        creation_time: str = None,
        invocation_status: str = None,
        invoke_id: str = None,
        invoke_status: str = None,
        parameters: Dict[str, Any] = None,
    ):
        # The content of the command, which is Base64-encoded.
        self.command_content = command_content
        # The name of the command.
        self.command_name = command_name
        # The type of the command. Valid values:
        # 
        # *   RunBatScript: batch command (applicable to Windows instances).
        # *   RunPowerShellScript: PowerShell command (applicable to Windows instances).
        # *   RunShellScript: shell command (applicable to Linux instances).
        self.command_type = command_type
        # The time when the command was created.
        self.creation_time = creation_time
        # The status of the command. Valid values:
        # 
        # *   Pending: The command is being verified or sent.
        # *   Invalid: The specified command type or parameter is invalid.
        # *   Aborted: The command failed to be sent. To send a command to an instance, make sure that the instance is in the Running state and the command is sent to the instance within 1 minute.
        # *   Running: The command is being run on the instance.
        # *   Success: The command finishes running, and the exit code is 0.
        # *   Failed: The command finishes running, but the exit code is not 0.
        # *   Error: The running of the command cannot proceed due to an exception.
        # *   Timeout: The running of the command times out.
        # *   Cancelled: The running is canceled, and the command is not run.
        # *   Stopping: The command that is running is being stopped.
        # *   Terminated: The command is terminated while it is being run.
        self.invocation_status = invocation_status
        # The ID of the command task.
        self.invoke_id = invoke_id
        # The status of the command. Valid values:
        # 
        # *   Running: The command is running.
        # *   Finished: The command finishes running.
        # *   Failed: The running of the command failed.
        # *   Stopped: The running is stopped.
        self.invoke_status = invoke_status
        # The custom parameters in the command. If no custom parameter exists in the command, the default value is {}.
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.command_name is not None:
            result['CommandName'] = self.command_name
        if self.command_type is not None:
            result['CommandType'] = self.command_type
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.invoke_status is not None:
            result['InvokeStatus'] = self.invoke_status
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('InvokeStatus') is not None:
            self.invoke_status = m.get('InvokeStatus')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class DescribeInvocationsResponseBody(TeaModel):
    def __init__(
        self,
        invocations: List[DescribeInvocationsResponseBodyInvocations] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The command name.
        self.invocations = invocations
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.invocations:
            for k in self.invocations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Invocations'] = []
        if self.invocations is not None:
            for k in self.invocations:
                result['Invocations'].append(k.to_map() if k else None)
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
        self.invocations = []
        if m.get('Invocations') is not None:
            for k in m.get('Invocations'):
                temp_model = DescribeInvocationsResponseBodyInvocations()
                self.invocations.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInvocationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInvocationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeInvocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMonitorDataRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        end_time: str = None,
        instance_id: str = None,
        length: str = None,
        metric_name: str = None,
        next_token: str = None,
        period: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **token** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The end of the time range to query. The following formats are supported:
        # 
        # *   UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 January 1, 1970.
        # *   Time format: YYYY-MM-DDThh:mm:ssZ.
        # 
        # > The interval between the start time and the end time is less than or equal to 31 days.
        self.end_time = end_time
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The number of entries per page. Valid values: 1 to 1440.
        self.length = length
        # The metric name. Valid values:
        # 
        # *   MEMORY_ACTUALUSEDSPACE: the memory usage. Unit: bytes.
        # *   DISKUSAGE_USED: the disk usage. Unit: bytes.
        # *   CPU_UTILIZATION: the CPU utilization in percentage.
        # *   VPC_PUBLICIP_INTERNETOUT_RATE: the outbound bandwidth rate of the network. Unit: bits/s.
        # *   VPC_PUBLICIP_INTERNETIN_RATE: the inbound bandwidth rate of the network. Unit: bits/s.
        # *   DISK_READ_IOPS: the read IOPS of the disk. Unit: count/s.
        # *   DISK_WRITE_IOPS: the write IOPS of the disk. Unit: count/s.
        # *   FLOW_USED: the traffic usage. Unit: bytes.
        self.metric_name = metric_name
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The interval at which the monitoring data is queried. Valid values: 60, 300, and 900. Unit: seconds.
        # 
        # > 
        # 
        # If MetricName is set to FLOW_USED, Period is set to 3600 (one hour). In other cases, set Period based on your business requirements.
        # 
        # **\
        # 
        # ****\
        self.period = period
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id
        # The beginning of the time range to query. The following formats are supported:
        # 
        # *   UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 January 1, 1970.
        # *   Time format: YYYY-MM-DDThh:mm:ssZ.
        # 
        # > The specified time range includes the end time and excludes the start time. The start time must be earlier than the end time.
        # 
        # The interval between the start time and the end time is less than or equal to 31 days.
        # 
        # **\
        # 
        # ****\
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.length is not None:
            result['Length'] = self.length
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeMonitorDataResponseBody(TeaModel):
    def __init__(
        self,
        datapoints: str = None,
        next_token: str = None,
        period: str = None,
        request_id: str = None,
    ):
        # The monitoring data.
        self.datapoints = datapoints
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The interval at which the monitoring data is queried. Valid values: 60, 300, and 900. Unit: seconds.
        # 
        # > 
        # 
        # If MetricName is set to FLOW_USED, the value of Period is 3600 (one hour).
        # 
        # **\
        # 
        # ****\
        self.period = period
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.period is not None:
            result['Period'] = self.period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Datapoints') is not None:
            self.datapoints = m.get('Datapoints')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMonitorDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMonitorDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeMonitorDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityAgentStatusRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSecurityAgentStatusResponseBody(TeaModel):
    def __init__(
        self,
        client_status: str = None,
        request_id: str = None,
    ):
        # The status of the Security Center agent. Valid values:
        # 
        # *   pause: The Security Center agent suspends protection for your server.
        # *   online: The Security Center agent is protecting your server.
        # *   offline: The Security Center agent does not protect your server.
        self.client_status = client_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_status is not None:
            result['ClientStatus'] = self.client_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientStatus') is not None:
            self.client_status = m.get('ClientStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSecurityAgentStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSecurityAgentStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeSecurityAgentStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableFirewallRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        region_id: str = None,
        remark: str = None,
        rule_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id
        # The remarks of the firewall rule.
        self.remark = remark
        # The ID of the firewall rule. You can call the ListFirewallRules operation to query the ID of the firewall rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DisableFirewallRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DisableFirewallRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableFirewallRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DisableFirewallRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableFirewallRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        region_id: str = None,
        remark: str = None,
        rule_id: str = None,
        source_cidr_ip: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id
        # The remarks of the firewall rule.
        self.remark = remark
        # The ID of the firewall rule.
        self.rule_id = rule_id
        # The IP address or CIDR block that is allowed in the firewall policy.
        self.source_cidr_ip = source_cidr_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        return self


class EnableFirewallRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class EnableFirewallRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableFirewallRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = EnableFirewallRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallCloudAssistantRequest(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        region_id: str = None,
    ):
        # The IDs of the simple application servers.
        self.instance_ids = instance_ids
        # The region ID of the simple application servers. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class InstallCloudAssistantShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_ids_shrink: str = None,
        region_id: str = None,
    ):
        # The IDs of the simple application servers.
        self.instance_ids_shrink = instance_ids_shrink
        # The region ID of the simple application servers. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class InstallCloudAssistantResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class InstallCloudAssistantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstallCloudAssistantResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = InstallCloudAssistantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallCloudMonitorAgentRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        force: bool = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # Specifies whether to forcibly install the CloudMonitor agent. Valid values:
        # 
        # *   true (default value): forcibly installs the CloudMonitor agent.
        # *   false: does not forcibly install the CloudMonitor agent.
        self.force = force
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.force is not None:
            result['Force'] = self.force
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class InstallCloudMonitorAgentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class InstallCloudMonitorAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstallCloudMonitorAgentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = InstallCloudMonitorAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeCommandRequest(TeaModel):
    def __init__(
        self,
        command_id: str = None,
        instance_ids: str = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        username: str = None,
    ):
        self.command_id = command_id
        self.instance_ids = instance_ids
        self.parameters = parameters
        self.region_id = region_id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class InvokeCommandShrinkRequest(TeaModel):
    def __init__(
        self,
        command_id: str = None,
        instance_ids: str = None,
        parameters_shrink: str = None,
        region_id: str = None,
        username: str = None,
    ):
        self.command_id = command_id
        self.instance_ids = instance_ids
        self.parameters_shrink = parameters_shrink
        self.region_id = region_id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class InvokeCommandResponseBody(TeaModel):
    def __init__(
        self,
        invoke_id: str = None,
        request_id: str = None,
    ):
        self.invoke_id = invoke_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InvokeCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InvokeCommandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = InvokeCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomImagesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        data_snapshot_id: str = None,
        image_ids: str = None,
        image_names: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        system_snapshot_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the data disk snapshot.
        self.data_snapshot_id = data_snapshot_id
        # The image IDs of the simple application server. The value can be a JSON array that consists of up to 100 image IDs. Separate multiple image IDs with commas (,).
        self.image_ids = image_ids
        # The image names of the simple application servers. The value can be a JSON array that consists of up to 100 image names. Separate multiple image names with commas (,).
        self.image_names = image_names
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # *   Maximum value: 100.
        # *   Default value: 10.
        self.page_size = page_size
        # The region ID of the simple application servers corresponding to the custom images. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the system disk snapshot.
        self.system_snapshot_id = system_snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.data_snapshot_id is not None:
            result['DataSnapshotId'] = self.data_snapshot_id
        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids
        if self.image_names is not None:
            result['ImageNames'] = self.image_names
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.system_snapshot_id is not None:
            result['SystemSnapshotId'] = self.system_snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DataSnapshotId') is not None:
            self.data_snapshot_id = m.get('DataSnapshotId')
        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')
        if m.get('ImageNames') is not None:
            self.image_names = m.get('ImageNames')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SystemSnapshotId') is not None:
            self.system_snapshot_id = m.get('SystemSnapshotId')
        return self


class ListCustomImagesResponseBodyCustomImages(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        data_snapshot_id: str = None,
        data_snapshot_name: str = None,
        description: str = None,
        image_id: str = None,
        in_share: bool = None,
        instance_id: str = None,
        instance_name: str = None,
        name: str = None,
        region_id: str = None,
        status: str = None,
        system_snapshot_id: str = None,
        system_snapshot_name: str = None,
    ):
        # The time when the snapshot was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The ID of the data disk snapshot.
        self.data_snapshot_id = data_snapshot_id
        # The name of the data disk snapshot.
        self.data_snapshot_name = data_snapshot_name
        # The description of the custom image.
        self.description = description
        # The ID of the custom image.
        self.image_id = image_id
        # Indicates whether the custom image is shared with Elastic Compute Service (ECS).
        self.in_share = in_share
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The name of the simple application server.
        self.instance_name = instance_name
        # The name of the custom image.
        self.name = name
        # The region ID of the custom images.
        self.region_id = region_id
        # The status of the custom image.
        self.status = status
        # The ID of the system disk snapshot.
        self.system_snapshot_id = system_snapshot_id
        # The name of the system disk snapshot.
        self.system_snapshot_name = system_snapshot_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.data_snapshot_id is not None:
            result['DataSnapshotId'] = self.data_snapshot_id
        if self.data_snapshot_name is not None:
            result['DataSnapshotName'] = self.data_snapshot_name
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.in_share is not None:
            result['InShare'] = self.in_share
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.system_snapshot_id is not None:
            result['SystemSnapshotId'] = self.system_snapshot_id
        if self.system_snapshot_name is not None:
            result['SystemSnapshotName'] = self.system_snapshot_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DataSnapshotId') is not None:
            self.data_snapshot_id = m.get('DataSnapshotId')
        if m.get('DataSnapshotName') is not None:
            self.data_snapshot_name = m.get('DataSnapshotName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InShare') is not None:
            self.in_share = m.get('InShare')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SystemSnapshotId') is not None:
            self.system_snapshot_id = m.get('SystemSnapshotId')
        if m.get('SystemSnapshotName') is not None:
            self.system_snapshot_name = m.get('SystemSnapshotName')
        return self


class ListCustomImagesResponseBody(TeaModel):
    def __init__(
        self,
        custom_images: List[ListCustomImagesResponseBodyCustomImages] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The queried custom images.
        self.custom_images = custom_images
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.custom_images:
            for k in self.custom_images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomImages'] = []
        if self.custom_images is not None:
            for k in self.custom_images:
                result['CustomImages'].append(k.to_map() if k else None)
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
        self.custom_images = []
        if m.get('CustomImages') is not None:
            for k in m.get('CustomImages'):
                temp_model = ListCustomImagesResponseBodyCustomImages()
                self.custom_images.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomImagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListCustomImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDisksRequest(TeaModel):
    def __init__(
        self,
        disk_ids: str = None,
        disk_type: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The IDs of the disks. The value can be a JSON array that consists of up to 100 disk IDs. Separate multiple disk IDs with commas (,).
        self.disk_ids = disk_ids
        # The type of the disk. Valid values:
        # 
        # *   System: system disk.
        # *   Data: data disk.
        # 
        # By default, system disks and data disks are both queried.
        self.disk_type = disk_type
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The page number.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the disks.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListDisksResponseBodyDisks(TeaModel):
    def __init__(
        self,
        category: str = None,
        creation_time: str = None,
        device: str = None,
        disk_charge_type: str = None,
        disk_id: str = None,
        disk_name: str = None,
        disk_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
        remark: str = None,
        size: int = None,
        status: str = None,
    ):
        # The category of the disk. Valid values:
        # 
        # *   ESSD: an enhanced SSD (ESSD) at performance level 0 (PL0).
        # *   SSD: a standard SSD.
        self.category = category
        # The time when the disk was created. The time follows the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The device name of the disk on the simple application server.
        self.device = device
        # The billing method of the disk.
        self.disk_charge_type = disk_charge_type
        # The ID of the disk.
        self.disk_id = disk_id
        # The name of the disk.
        self.disk_name = disk_name
        # The type of the disk. Valid values:
        # 
        # *   System: system disk.
        # *   Data: data disk.
        self.disk_type = disk_type
        # The ID of the simple application server to which the disk is attached.
        self.instance_id = instance_id
        # Name of the simple application server.
        self.instance_name = instance_name
        # The region ID of the disks.
        self.region_id = region_id
        # Description about the disk.
        self.remark = remark
        # The size of the disk. Unit: GB.
        self.size = size
        # The status of the disk. Valid values:
        # 
        # *   ReIniting: The disk is being initialized.
        # *   Creating: The disk is being created.
        # *   In_Use: The disk is being used.
        # *   Available: The disk can be attached.
        # *   Attaching: The disk is being attached.
        # *   Detaching: The disk is being detached.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.device is not None:
            result['Device'] = self.device
        if self.disk_charge_type is not None:
            result['DiskChargeType'] = self.disk_charge_type
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('DiskChargeType') is not None:
            self.disk_charge_type = m.get('DiskChargeType')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDisksResponseBody(TeaModel):
    def __init__(
        self,
        disks: List[ListDisksResponseBodyDisks] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the disks.
        self.disks = disks
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
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
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = ListDisksResponseBodyDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDisksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDisksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListDisksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFirewallRulesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The page number.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the simple application server.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListFirewallRulesResponseBodyFirewallRules(TeaModel):
    def __init__(
        self,
        policy: str = None,
        port: str = None,
        remark: str = None,
        rule_id: str = None,
        rule_protocol: str = None,
        source_cidr_ip: str = None,
    ):
        # The firewall policy.
        # 
        # *   accept: Access is allowed.
        # *   drop: Access is refused.
        self.policy = policy
        # The port range.
        self.port = port
        # The remarks of the firewall rule.
        self.remark = remark
        # The ID of the firewall rule.
        self.rule_id = rule_id
        # The transport layer protocol. Valid values:
        # 
        # *   TCP: the TCP protocol.
        # *   UDP: the UDP protocol
        # *   TCP+UDP: the TCP and UDP protocols
        self.rule_protocol = rule_protocol
        # The IP address or CIDR block that is allowed by the firewall rule.
        self.source_cidr_ip = source_cidr_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.port is not None:
            result['Port'] = self.port
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_protocol is not None:
            result['RuleProtocol'] = self.rule_protocol
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleProtocol') is not None:
            self.rule_protocol = m.get('RuleProtocol')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        return self


class ListFirewallRulesResponseBody(TeaModel):
    def __init__(
        self,
        firewall_rules: List[ListFirewallRulesResponseBodyFirewallRules] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the firewall rules.
        self.firewall_rules = firewall_rules
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.firewall_rules:
            for k in self.firewall_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FirewallRules'] = []
        if self.firewall_rules is not None:
            for k in self.firewall_rules:
                result['FirewallRules'].append(k.to_map() if k else None)
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
        self.firewall_rules = []
        if m.get('FirewallRules') is not None:
            for k in m.get('FirewallRules'):
                temp_model = ListFirewallRulesResponseBodyFirewallRules()
                self.firewall_rules.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFirewallRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFirewallRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListFirewallRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesRequest(TeaModel):
    def __init__(
        self,
        image_ids: str = None,
        image_type: str = None,
        region_id: str = None,
    ):
        # The image IDs. The value can be a JSON array that consists of up to 50 image IDs. Format: `["xxx", "yyy", … "zzz"]`. Separate multiple image IDs with commas (,).
        self.image_ids = image_ids
        # The type of the images. Valid values:
        # 
        # *   system: OS images
        # *   app: application images
        # *   custom: custom images
        self.image_type = image_type
        # The region ID of the images. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        description: str = None,
        image_id: str = None,
        image_name: str = None,
        image_type: str = None,
        platform: str = None,
    ):
        # The description of the image.
        self.description = description
        # The ID of the image.
        self.image_id = image_id
        # The name of the image.
        self.image_name = image_name
        # The type of the image. Valid values:
        # 
        # *   system
        # *   app
        # *   custom
        self.image_type = image_type
        # The operating system type of the image. Valid values:
        # 
        # *   Linux
        # *   Windows
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(
        self,
        images: List[ListImagesResponseBodyImages] = None,
        request_id: str = None,
    ):
        # The OS type of the image. Valid values:
        # 
        # *   Linux
        # *   Windows
        self.images = images
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListImagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancePlansModificationRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListInstancePlansModificationResponseBodyPlans(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        core: int = None,
        currency: str = None,
        disk_size: int = None,
        disk_type: str = None,
        flow: int = None,
        memory: int = None,
        origin_price: float = None,
        plan_id: str = None,
        support_platform: str = None,
    ):
        # The peak bandwidth. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The number of vCPUs.
        self.core = core
        # The unit of the plan price. Valid values:
        # 
        # *   CNY
        # *   USD
        self.currency = currency
        # The disk size of the simple application server. Unit: GB.
        self.disk_size = disk_size
        # The category of the disk. Valid values:
        # 
        # *   SSD: standard SSD
        # *   ESSD: enhanced SSD
        self.disk_type = disk_type
        # The monthly data transfer quota. Unit: GB.
        self.flow = flow
        # The memory size. Unit: GB.
        self.memory = memory
        # The price of the plan.
        self.origin_price = origin_price
        # The ID of the plan.
        self.plan_id = plan_id
        # The operating system types supported by the plan.
        self.support_platform = support_platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.core is not None:
            result['Core'] = self.core
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.support_platform is not None:
            result['SupportPlatform'] = self.support_platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Core') is not None:
            self.core = m.get('Core')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('SupportPlatform') is not None:
            self.support_platform = m.get('SupportPlatform')
        return self


class ListInstancePlansModificationResponseBody(TeaModel):
    def __init__(
        self,
        plans: List[ListInstancePlansModificationResponseBodyPlans] = None,
        request_id: str = None,
    ):
        # The operating system types supported by the plan.
        self.plans = plans
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.plans:
            for k in self.plans:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Plans'] = []
        if self.plans is not None:
            for k in self.plans:
                result['Plans'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plans = []
        if m.get('Plans') is not None:
            for k in m.get('Plans'):
                temp_model = ListInstancePlansModificationResponseBodyPlans()
                self.plans.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstancePlansModificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancePlansModificationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListInstancePlansModificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        instance_ids: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The IDs of the simple application servers. The value can be a JSON array that consists of up to 100 simple application server IDs. Separate multiple server IDs with commas (,).
        self.instance_ids = instance_ids
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID of the simple application servers. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListInstanceStatusResponseBodyInstanceStatuses(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        status: str = None,
    ):
        self.instance_id = instance_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstanceStatusResponseBody(TeaModel):
    def __init__(
        self,
        instance_statuses: List[ListInstanceStatusResponseBodyInstanceStatuses] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The ID of the simple application server.
        self.instance_statuses = instance_statuses
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.instance_statuses:
            for k in self.instance_statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceStatuses'] = []
        if self.instance_statuses is not None:
            for k in self.instance_statuses:
                result['InstanceStatuses'].append(k.to_map() if k else None)
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
        self.instance_statuses = []
        if m.get('InstanceStatuses') is not None:
            for k in m.get('InstanceStatuses'):
                temp_model = ListInstanceStatusResponseBodyInstanceStatuses()
                self.instance_statuses.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        instance_ids: str = None,
        page_number: int = None,
        page_size: int = None,
        public_ip_addresses: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # The billing method of the simple application servers. Set the value to PrePaid, which indicates the subscription billing method.
        # 
        # Default value: PrePaid.
        self.charge_type = charge_type
        # The IDs of the simple application servers. The value can be a JSON array that consists of up to 100 simple application server IDs. Separate multiple server IDs with commas (,).
        # 
        # > If you specify both `InstanceIds` and `PublicIpAddresses`, make sure that the specified IDs and the specified public IP addresses belong to the same simple application servers. Otherwise, an empty result is returned.
        self.instance_ids = instance_ids
        # The page number.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The public IP addresses of the simple application servers. The value can be a JSON array that consists of up to 100 IP addresses. Separate multiple IP addresses with commas (,).
        # 
        # > If you specify both `InstanceIds` and `PublicIpAddresses`, make sure that the specified IDs and the specified public IP addresses belong to the same simple application servers. Otherwise, an empty result is returned.
        self.public_ip_addresses = public_ip_addresses
        # The region ID of the simple application servers.
        self.region_id = region_id
        # 实例状态，可能值：
        # 
        # - Pending：准备中
        # - Starting：启动中
        # - Running：运行中
        # - Stopping：停止中
        # - Stopped：停止
        # - Resetting：重置中
        # - Upgrading：升级中
        # - Disabled：不可用
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.public_ip_addresses is not None:
            result['PublicIpAddresses'] = self.public_ip_addresses
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PublicIpAddresses') is not None:
            self.public_ip_addresses = m.get('PublicIpAddresses')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstancesResponseBodyInstancesImage(TeaModel):
    def __init__(
        self,
        image_contact: str = None,
        image_icon_url: str = None,
        image_name: str = None,
        image_type: str = None,
        image_version: str = None,
        os_type: str = None,
    ):
        # The image provider.
        self.image_contact = image_contact
        # The URL of the image icon.
        self.image_icon_url = image_icon_url
        # The image name.
        self.image_name = image_name
        # The image type. Valid values:
        # 
        # *   system
        # *   app
        # *   custom
        self.image_type = image_type
        # The image tag.
        self.image_version = image_version
        # The OS.
        self.os_type = os_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_contact is not None:
            result['ImageContact'] = self.image_contact
        if self.image_icon_url is not None:
            result['ImageIconUrl'] = self.image_icon_url
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.os_type is not None:
            result['OsType'] = self.os_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageContact') is not None:
            self.image_contact = m.get('ImageContact')
        if m.get('ImageIconUrl') is not None:
            self.image_icon_url = m.get('ImageIconUrl')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        return self


class ListInstancesResponseBodyInstancesResourceSpec(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        cpu: int = None,
        disk_category: str = None,
        disk_size: int = None,
        flow: float = None,
        memory: float = None,
    ):
        # The bandwidth of the server.
        self.bandwidth = bandwidth
        # The number of vCPUs.
        self.cpu = cpu
        # The category of the disk. Valid values:
        # 
        # *   ESSD: an enhanced SSD (ESSD) at performance level 0 (PL0).
        # *   SSD: a standard SSD.
        # *   CLOUD_EFFICIENCY: an ultra disk.
        self.disk_category = disk_category
        # The disk size.
        self.disk_size = disk_size
        # The amount of the traffic.
        # 
        # *   A value of 0 indicates that the server is a bandwidth-based server.
        # *   A value of none-zero indicates that the server is a data transfer plan-based server.
        self.flow = flow
        # The memory size.
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        business_status: str = None,
        charge_type: str = None,
        combination: bool = None,
        combination_instance_id: str = None,
        creation_time: str = None,
        ddos_status: str = None,
        disable_reason: str = None,
        expired_time: str = None,
        image: ListInstancesResponseBodyInstancesImage = None,
        image_id: str = None,
        inner_ip_address: str = None,
        instance_id: str = None,
        instance_name: str = None,
        plan_id: str = None,
        public_ip_address: str = None,
        region_id: str = None,
        resource_spec: ListInstancesResponseBodyInstancesResourceSpec = None,
        status: str = None,
        uuid: str = None,
    ):
        # The status of the server. Valid values:
        # 
        # *   Normal: The server is normal.
        # *   Expired: The server expires.
        # *   Overdue: The payment of the server is overdue.
        self.business_status = business_status
        # The billing method of the simple application server.
        self.charge_type = charge_type
        # Indicates whether the plan is a bundle plan.
        self.combination = combination
        # The ID of the bundle plan.
        self.combination_instance_id = combination_instance_id
        # The time when the simple application server was created. The time follows the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The DDoS protection status of the server. Valid values:
        # 
        # *   Normal: The DDoS protection status of the server is normal.
        # *   BlackHole: The server is in blackhole filtering.
        # *   Defense: The server is being scrubbed.
        self.ddos_status = ddos_status
        # The reason why the server is disabled. Valid values:
        # 
        # *   FINANCIAL: The server is locked due to overdue payments.
        # *   SECURITY: The server is locked due to security reasons.
        # *   EXPIRED: The server has expired.
        self.disable_reason = disable_reason
        # The time when the server expires. The time follows the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.expired_time = expired_time
        # The description of the image.
        self.image = image
        # The ID of an image.
        self.image_id = image_id
        # The internal IP address of the simple application server.
        self.inner_ip_address = inner_ip_address
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The name of the server.
        self.instance_name = instance_name
        # The plan ID.
        self.plan_id = plan_id
        # The public IP address of the server.
        self.public_ip_address = public_ip_address
        # The region ID of the servers.
        self.region_id = region_id
        # The specifications of the resource.
        self.resource_spec = resource_spec
        # The status of the simple application server. Valid values:
        # 
        # *   Pending
        # *   Starting
        # *   Running
        # *   Stopping
        # *   Stopped
        # *   Resetting
        # *   Upgrading
        # *   Disabled
        self.status = status
        # The universally unique identifier (UUID) of the server.
        self.uuid = uuid

    def validate(self):
        if self.image:
            self.image.validate()
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.combination is not None:
            result['Combination'] = self.combination
        if self.combination_instance_id is not None:
            result['CombinationInstanceId'] = self.combination_instance_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.ddos_status is not None:
            result['DdosStatus'] = self.ddos_status
        if self.disable_reason is not None:
            result['DisableReason'] = self.disable_reason
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.inner_ip_address is not None:
            result['InnerIpAddress'] = self.inner_ip_address
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Combination') is not None:
            self.combination = m.get('Combination')
        if m.get('CombinationInstanceId') is not None:
            self.combination_instance_id = m.get('CombinationInstanceId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DdosStatus') is not None:
            self.ddos_status = m.get('DdosStatus')
        if m.get('DisableReason') is not None:
            self.disable_reason = m.get('DisableReason')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Image') is not None:
            temp_model = ListInstancesResponseBodyInstancesImage()
            self.image = temp_model.from_map(m['Image'])
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InnerIpAddress') is not None:
            self.inner_ip_address = m.get('InnerIpAddress')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceSpec') is not None:
            temp_model = ListInstancesResponseBodyInstancesResourceSpec()
            self.resource_spec = temp_model.from_map(m['ResourceSpec'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[ListInstancesResponseBodyInstances] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the simple application servers.
        self.instances = instances
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesTrafficPackagesRequest(TeaModel):
    def __init__(
        self,
        acs_product: str = None,
        instance_ids: str = None,
        region_id: str = None,
    ):
        self.acs_product = acs_product
        # The IDs of the simple application servers. The value can be a JSON array that consists of up to 100 simple application server IDs. Separate multiple server IDs with commas (,).
        self.instance_ids = instance_ids
        # The region ID of the simple application servers. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acs_product is not None:
            result['AcsProduct'] = self.acs_product
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcsProduct') is not None:
            self.acs_product = m.get('AcsProduct')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListInstancesTrafficPackagesResponseBodyInstanceTrafficPackageUsages(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        traffic_overflow: int = None,
        traffic_package_remaining: int = None,
        traffic_package_total: int = None,
        traffic_used: int = None,
    ):
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The data transfers that exceeds the quota of the data transfer plan in the current month. Unit: Byte.
        self.traffic_overflow = traffic_overflow
        # The unused quota of the data transfer plan in the current month. Unit: Byte.
        self.traffic_package_remaining = traffic_package_remaining
        # The quota of the data transfer plan in the current month. Unit: Byte.
        # 
        # >  TrafficPackageTotal = TrafficUsed + TrafficPackageRemaining
        self.traffic_package_total = traffic_package_total
        # The used quota of the data transfer plan in the current month. Unit: Byte.
        self.traffic_used = traffic_used

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.traffic_overflow is not None:
            result['TrafficOverflow'] = self.traffic_overflow
        if self.traffic_package_remaining is not None:
            result['TrafficPackageRemaining'] = self.traffic_package_remaining
        if self.traffic_package_total is not None:
            result['TrafficPackageTotal'] = self.traffic_package_total
        if self.traffic_used is not None:
            result['TrafficUsed'] = self.traffic_used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TrafficOverflow') is not None:
            self.traffic_overflow = m.get('TrafficOverflow')
        if m.get('TrafficPackageRemaining') is not None:
            self.traffic_package_remaining = m.get('TrafficPackageRemaining')
        if m.get('TrafficPackageTotal') is not None:
            self.traffic_package_total = m.get('TrafficPackageTotal')
        if m.get('TrafficUsed') is not None:
            self.traffic_used = m.get('TrafficUsed')
        return self


class ListInstancesTrafficPackagesResponseBody(TeaModel):
    def __init__(
        self,
        instance_traffic_package_usages: List[ListInstancesTrafficPackagesResponseBodyInstanceTrafficPackageUsages] = None,
        request_id: str = None,
    ):
        # The data transfers that exceed the quota of the data transfer plan in the current month. Unit: bytes.
        self.instance_traffic_package_usages = instance_traffic_package_usages
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_traffic_package_usages:
            for k in self.instance_traffic_package_usages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceTrafficPackageUsages'] = []
        if self.instance_traffic_package_usages is not None:
            for k in self.instance_traffic_package_usages:
                result['InstanceTrafficPackageUsages'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_traffic_package_usages = []
        if m.get('InstanceTrafficPackageUsages') is not None:
            for k in m.get('InstanceTrafficPackageUsages'):
                temp_model = ListInstancesTrafficPackagesResponseBodyInstanceTrafficPackageUsages()
                self.instance_traffic_package_usages.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstancesTrafficPackagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesTrafficPackagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListInstancesTrafficPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPlansRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region ID of the plans. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListPlansResponseBodyPlans(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        core: int = None,
        currency: str = None,
        disk_size: int = None,
        disk_type: str = None,
        flow: int = None,
        memory: int = None,
        origin_price: float = None,
        plan_id: str = None,
        support_platform: str = None,
    ):
        # The peak bandwidth. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The number of vCPUs.
        self.core = core
        # The unit of the plan price. Valid values:
        # 
        # *   CNY
        # *   USD
        # 
        # >  CNY is for the China site (aliyun.com). USD is for the international site (alibabacloud.com).
        self.currency = currency
        # The size of the disk. Unit: GB.
        self.disk_size = disk_size
        # The category of the disk. Valid values:
        # 
        # *   SSD: standard SSDs
        # *   ESSD: enhanced SSDs
        self.disk_type = disk_type
        # The monthly data transfer quota. Unit: GB.
        self.flow = flow
        # The memory size. Unit: GB.
        self.memory = memory
        # The monthly price of the plan.
        self.origin_price = origin_price
        # The ID of the plan.
        self.plan_id = plan_id
        # The operating system types supported by the plan.
        self.support_platform = support_platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.core is not None:
            result['Core'] = self.core
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.flow is not None:
            result['Flow'] = self.flow
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.origin_price is not None:
            result['OriginPrice'] = self.origin_price
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.support_platform is not None:
            result['SupportPlatform'] = self.support_platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Core') is not None:
            self.core = m.get('Core')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('OriginPrice') is not None:
            self.origin_price = m.get('OriginPrice')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('SupportPlatform') is not None:
            self.support_platform = m.get('SupportPlatform')
        return self


class ListPlansResponseBody(TeaModel):
    def __init__(
        self,
        plans: List[ListPlansResponseBodyPlans] = None,
        request_id: str = None,
    ):
        # The operating system types supported by the plan.
        self.plans = plans
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.plans:
            for k in self.plans:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Plans'] = []
        if self.plans is not None:
            for k in self.plans:
                result['Plans'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plans = []
        if m.get('Plans') is not None:
            for k in m.get('Plans'):
                temp_model = ListPlansResponseBodyPlans()
                self.plans.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPlansResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        # The name of the region.
        self.local_name = local_name
        # The endpoint of the region.
        self.region_endpoint = region_endpoint
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[ListRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        # The region ID.
        self.regions = regions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSnapshotsRequest(TeaModel):
    def __init__(
        self,
        acs_product: str = None,
        disk_id: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        snapshot_ids: str = None,
        source_disk_type: str = None,
    ):
        self.acs_product = acs_product
        # The disk ID.
        self.disk_id = disk_id
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The page number.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the simple application server that corresponds to the snapshots.
        self.region_id = region_id
        # The snapshot IDs. The value can be a JSON array that consists of up to 100 snapshot IDs. Separate multiple snapshot IDs with commas (,).
        self.snapshot_ids = snapshot_ids
        # The type of the source disk. Valid values:
        # 
        # *   system: system disk.
        # *   data: data disk.
        self.source_disk_type = source_disk_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acs_product is not None:
            result['AcsProduct'] = self.acs_product
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_ids is not None:
            result['SnapshotIds'] = self.snapshot_ids
        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcsProduct') is not None:
            self.acs_product = m.get('AcsProduct')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotIds') is not None:
            self.snapshot_ids = m.get('SnapshotIds')
        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')
        return self


class ListSnapshotsResponseBodySnapshots(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        instance_id: str = None,
        progress: str = None,
        region_id: str = None,
        remark: str = None,
        rollback_time: str = None,
        snapshot_id: str = None,
        snapshot_name: str = None,
        source_disk_id: str = None,
        source_disk_type: str = None,
        status: str = None,
    ):
        # The time when the snapshot was created. The time follows the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The ID of the simple application server.
        # 
        # Note: This parameter has a value for system disk snapshots. This parameter is left empty for data disk snapshots.
        self.instance_id = instance_id
        # The progress of snapshot creation.
        self.progress = progress
        # The region ID of the snapshots.
        self.region_id = region_id
        # The remarks of the snapshot.
        self.remark = remark
        # The time when the last disk rollback was performed.
        self.rollback_time = rollback_time
        # The snapshot ID.
        self.snapshot_id = snapshot_id
        # The name of the snapshot.
        self.snapshot_name = snapshot_name
        # The ID of the source disk based on which the snapshot is created. This parameter has a value even if the source disk is released.
        self.source_disk_id = source_disk_id
        # The type of the source disk. Valid values:
        # 
        # *   system: system disk.
        # *   data: data disk.
        self.source_disk_type = source_disk_type
        # The status of the snapshot. Valid values:
        # 
        # *   Progressing: The snapshot is being created.
        # *   Accomplished: The snapshot is created.
        # *   Failed: The snapshot failed to be created.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.rollback_time is not None:
            result['RollbackTime'] = self.rollback_time
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name
        if self.source_disk_id is not None:
            result['SourceDiskId'] = self.source_disk_id
        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RollbackTime') is not None:
            self.rollback_time = m.get('RollbackTime')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')
        if m.get('SourceDiskId') is not None:
            self.source_disk_id = m.get('SourceDiskId')
        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSnapshotsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        snapshots: List[ListSnapshotsResponseBodySnapshots] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Details about the snapshots.
        self.snapshots = snapshots
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.snapshots:
            for k in self.snapshots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Snapshots'] = []
        if self.snapshots is not None:
            for k in self.snapshots:
                result['Snapshots'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.snapshots = []
        if m.get('Snapshots') is not None:
            for k in m.get('Snapshots'):
                temp_model = ListSnapshotsResponseBodySnapshots()
                self.snapshots.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSnapshotsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSnapshotsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListSnapshotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LoginInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        password: str = None,
        region_id: str = None,
        username: str = None,
    ):
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The password that corresponds to the username.
        # 
        # *   For a Linux server, you do not need to enter a password.
        # *   For a Windows server, enter the password that you set. If you have not set a password for the simple application server, set a password. For more information, see [Reset the password](~~60055~~).
        self.password = password
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id
        # The username of the simple application server.
        # 
        # *   For a Linux server, you do not need to enter a username.
        # *   For a Windows server, the default username is `administrator`.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class LoginInstanceResponseBody(TeaModel):
    def __init__(
        self,
        redirect_url: str = None,
        request_id: str = None,
    ):
        # The URL that you use to log on to the server.
        self.redirect_url = redirect_url
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_url is not None:
            result['RedirectUrl'] = self.redirect_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUrl') is not None:
            self.redirect_url = m.get('RedirectUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LoginInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LoginInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = LoginInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDatabaseInstanceDescriptionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        database_instance_description: str = None,
        database_instance_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The description of the Simple Database Service instance.
        self.database_instance_description = database_instance_description
        # The ID of the Simple Database Service instance.
        self.database_instance_id = database_instance_id
        # The region ID of the Simple Database Service instance. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.database_instance_description is not None:
            result['DatabaseInstanceDescription'] = self.database_instance_description
        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DatabaseInstanceDescription') is not None:
            self.database_instance_description = m.get('DatabaseInstanceDescription')
        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDatabaseInstanceDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ModifyDatabaseInstanceDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDatabaseInstanceDescriptionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ModifyDatabaseInstanceDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDatabaseInstanceParameterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        database_instance_id: str = None,
        force_restart: bool = None,
        parameters: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the Simple Database Service instance.
        self.database_instance_id = database_instance_id
        # Specifies whether to forcibly restart the instance after parameters are modified. Valid values:
        # 
        # *   true: forcibly restarts the instance. If a new parameter value takes effect only after the instance restarts, you must set this parameter to true. Otherwise, the new parameter value cannot take effect.
        # *   false: does not forcibly restart the instance.
        # 
        # Default value: false.
        self.force_restart = force_restart
        # The JSON strings that consist of instance parameters and the values of the instance parameters. The parameter values are of the string type. Format: {"Parameter name 1":"Parameter value 1","Parameter name 2":"Parameter value 2"...}.
        self.parameters = parameters
        # The region ID of the Simple Database Service instance. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id
        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')
        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDatabaseInstanceParameterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ModifyDatabaseInstanceParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDatabaseInstanceParameterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ModifyDatabaseInstanceParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFirewallRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        port: str = None,
        region_id: str = None,
        remark: str = None,
        rule_id: str = None,
        rule_protocol: str = None,
        source_cidr_ip: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The port range. Valid values: 165535. Specify a port range in the format of \<start port number>/\<end port number>. Example: `1024/1055`, which indicates that the port range of 10241055.
        self.port = port
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id
        # The remarks of the firewall rule.
        self.remark = remark
        # The ID of the firewall rule.
        self.rule_id = rule_id
        # The transport layer protocol. Valid values:
        # 
        # *   TCP: the TCP protocol
        # *   UDP: the UDP protocol
        # *   TCP+UDP: the TCP and UDP protocols
        self.rule_protocol = rule_protocol
        # The IP address or CIDR block that is allowed in the firewall rule.
        self.source_cidr_ip = source_cidr_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_protocol is not None:
            result['RuleProtocol'] = self.rule_protocol
        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleProtocol') is not None:
            self.rule_protocol = m.get('RuleProtocol')
        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')
        return self


class ModifyFirewallRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ModifyFirewallRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFirewallRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ModifyFirewallRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyImageShareStatusRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        image_id: str = None,
        operation: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The image ID.
        self.image_id = image_id
        # Valid values:
        # 
        # *   Share
        # *   UnShare
        self.operation = operation
        # The region ID of the custom image. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyImageShareStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ModifyImageShareStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyImageShareStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ModifyImageShareStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceVncPasswordRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        region_id: str = None,
        vnc_password: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id
        # The existing VNC password.
        self.vnc_password = vnc_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vnc_password is not None:
            result['VncPassword'] = self.vnc_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VncPassword') is not None:
            self.vnc_password = m.get('VncPassword')
        return self


class ModifyInstanceVncPasswordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ModifyInstanceVncPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceVncPasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ModifyInstanceVncPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the simple application server.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RebootInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class RebootInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RebootInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RebootInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootInstancesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        force_reboot: bool = None,
        instance_ids: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # Specifies whether to forcibly restart the servers. Valid values:
        # 
        # *   true: forcibly restarts the servers. This operation is equivalent to the typical power-off operation. Cache data that is not written to storage devices on the server will be lost.
        # *   false: normally restarts the instance.
        # 
        # Default value: false
        self.force_reboot = force_reboot
        # The IDs of the simple application servers. The value can be a JSON array that consists of up to 100 simple application server IDs. Separate multiple server IDs with commas (,).
        self.instance_ids = instance_ids
        # The region ID of the simple application servers. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.force_reboot is not None:
            result['ForceReboot'] = self.force_reboot
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ForceReboot') is not None:
            self.force_reboot = m.get('ForceReboot')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RebootInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class RebootInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RebootInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RebootInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleasePublicConnectionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        database_instance_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the Simple Database Service instance.
        self.database_instance_id = database_instance_id
        # The region ID of the Simple Database Service instance. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ReleasePublicConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ReleasePublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleasePublicConnectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ReleasePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        period: int = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The renewal period. Unit: month. Valid values: 1, 3, 6, 12, 24, and 36.
        self.period = period
        # The region ID of the server.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class RenewInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetDatabaseAccountPasswordRequest(TeaModel):
    def __init__(
        self,
        account_password: str = None,
        client_token: str = None,
        database_instance_id: str = None,
        region_id: str = None,
    ):
        # The password of the database administrator account.
        self.account_password = account_password
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the Simple Database Service instance.
        self.database_instance_id = database_instance_id
        # The region ID of the Simple Database Service instance. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ResetDatabaseAccountPasswordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ResetDatabaseAccountPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetDatabaseAccountPasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ResetDatabaseAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetDiskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        disk_id: str = None,
        region_id: str = None,
        snapshot_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the disk to be rolled back.
        self.disk_id = disk_id
        # The region ID of the simple application server for which the snapshot is created.
        self.region_id = region_id
        # The snapshot ID.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class ResetDiskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ResetDiskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetDiskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ResetDiskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetSystemRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        image_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the image that is used to replace the image of the simple application server. If you do not specify this parameter, the current image of the simple application server is replaced by default.
        self.image_id = image_id
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ResetSystemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ResetSystemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetSystemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ResetSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDatabaseInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        database_instance_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the Simple Database Service instance.
        self.database_instance_id = database_instance_id
        # The region ID of the Simple Database Service instance. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RestartDatabaseInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class RestartDatabaseInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartDatabaseInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RestartDatabaseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCommandRequest(TeaModel):
    def __init__(
        self,
        command_content: str = None,
        enable_parameter: bool = None,
        instance_id: str = None,
        name: str = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        timeout: int = None,
        type: str = None,
        windows_password_name: str = None,
        working_dir: str = None,
        working_user: str = None,
    ):
        # The content of the command. Take note of the following items:
        # 
        # *   If you set `EnableParameter` to true, the custom parameter feature is enabled in the command content and you can configure custom parameters based on the following rules:
        # *   Define custom parameters in the {{}} format. Within `{{}}`, the spaces and line feeds before and after the parameter names are ignored.
        # *   The number of custom parameters cannot be greater than 20.
        # *   A custom parameter name can contain only letters, digits, underscores (\_), and hyphens (-). The name is case-insensitive.
        # *   Each custom parameter name cannot exceed 64 bytes in length.
        self.command_content = command_content
        # Specifies whether to enable the custom parameter feature.
        # 
        # Default value: false.
        self.enable_parameter = enable_parameter
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The name of the command.
        self.name = name
        # The custom parameters in the key-value pair format that are to be passed in when the command includes custom parameters. For example, if the command content is `echo {{name}}`, you can use `Parameters` to pass in the `{"name":"Jack"}` key-value pair. The `name` key of the custom parameter is automatically replaced with the paired Jack value to generate a new command. As a result, the `echo Jack` command is executed.
        # 
        # Number of custom parameters ranges from 0 to 20. Take note of the following items:
        # 
        # *   The key cannot be an empty string. It can be up to 64 characters in length.
        # *   The value can be an empty string.
        # *   After custom parameters and original command content are encoded in Base64, the command cannot exceed 16 KB in size.
        # *   The custom parameter names that are specified by Parameters must be included in the custom parameter names that you specified when you created the command. You can use empty strings to represent the parameters that are not passed in.
        # 
        # This parameter is empty by default, which indicates to disable the custom parameter feature.
        self.parameters = parameters
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id
        # The timeout period of the command on the server.
        # 
        # If a command execution task times out, Command Assistant forcibly terminates the task process. Valid values: 10 to 86400. Unit: seconds. The period of 86400 seconds is equal to 24 hours.
        # 
        # Default value: 60.
        self.timeout = timeout
        # The language type of the command. Valid values:
        # 
        # *   RunBatScript: batch commands (applicable to Windows servers).
        # *   RunPowerShellScript: PowerShell commands (applicable to Windows servers).
        # *   RunShellScript: shell commands (applicable to Linux servers).
        self.type = type
        # The name of the password to be used to run the command on a Windows server.
        # 
        # If you want to use a username other than the default "system" username to run the command on a Windows server, you must specify both the WindowsPasswordName and WorkingUser parameters. To mitigate the risk of password leaks, the password is stored in plaintext in Operation Orchestration Service (OOS) Parameter Store, and only the name of the password is passed in by using WindowsPasswordName.
        self.windows_password_name = windows_password_name
        # The execution path of the command. You can specify a value for the parameter. Default execution paths vary based on the operating systems of the servers.
        # 
        # *   For Linux servers, the default execution path is the /home directory of the root user.
        # *   For Windows servers, the default execution path is C:\Windows\system32.
        self.working_dir = working_dir
        # A user of the server who runs the command. We recommend that you run the command as a regular user to reduce security risks. Default values:
        # 
        # *   For Linux servers, the default value is root.
        # *   For Windows servers, the default value is system.
        self.working_user = working_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.type is not None:
            result['Type'] = self.type
        if self.windows_password_name is not None:
            result['WindowsPasswordName'] = self.windows_password_name
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        if self.working_user is not None:
            result['WorkingUser'] = self.working_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WindowsPasswordName') is not None:
            self.windows_password_name = m.get('WindowsPasswordName')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        if m.get('WorkingUser') is not None:
            self.working_user = m.get('WorkingUser')
        return self


class RunCommandShrinkRequest(TeaModel):
    def __init__(
        self,
        command_content: str = None,
        enable_parameter: bool = None,
        instance_id: str = None,
        name: str = None,
        parameters_shrink: str = None,
        region_id: str = None,
        timeout: int = None,
        type: str = None,
        windows_password_name: str = None,
        working_dir: str = None,
        working_user: str = None,
    ):
        # The content of the command. Take note of the following items:
        # 
        # *   If you set `EnableParameter` to true, the custom parameter feature is enabled in the command content and you can configure custom parameters based on the following rules:
        # *   Define custom parameters in the {{}} format. Within `{{}}`, the spaces and line feeds before and after the parameter names are ignored.
        # *   The number of custom parameters cannot be greater than 20.
        # *   A custom parameter name can contain only letters, digits, underscores (\_), and hyphens (-). The name is case-insensitive.
        # *   Each custom parameter name cannot exceed 64 bytes in length.
        self.command_content = command_content
        # Specifies whether to enable the custom parameter feature.
        # 
        # Default value: false.
        self.enable_parameter = enable_parameter
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The name of the command.
        self.name = name
        # The custom parameters in the key-value pair format that are to be passed in when the command includes custom parameters. For example, if the command content is `echo {{name}}`, you can use `Parameters` to pass in the `{"name":"Jack"}` key-value pair. The `name` key of the custom parameter is automatically replaced with the paired Jack value to generate a new command. As a result, the `echo Jack` command is executed.
        # 
        # Number of custom parameters ranges from 0 to 20. Take note of the following items:
        # 
        # *   The key cannot be an empty string. It can be up to 64 characters in length.
        # *   The value can be an empty string.
        # *   After custom parameters and original command content are encoded in Base64, the command cannot exceed 16 KB in size.
        # *   The custom parameter names that are specified by Parameters must be included in the custom parameter names that you specified when you created the command. You can use empty strings to represent the parameters that are not passed in.
        # 
        # This parameter is empty by default, which indicates to disable the custom parameter feature.
        self.parameters_shrink = parameters_shrink
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id
        # The timeout period of the command on the server.
        # 
        # If a command execution task times out, Command Assistant forcibly terminates the task process. Valid values: 10 to 86400. Unit: seconds. The period of 86400 seconds is equal to 24 hours.
        # 
        # Default value: 60.
        self.timeout = timeout
        # The language type of the command. Valid values:
        # 
        # *   RunBatScript: batch commands (applicable to Windows servers).
        # *   RunPowerShellScript: PowerShell commands (applicable to Windows servers).
        # *   RunShellScript: shell commands (applicable to Linux servers).
        self.type = type
        # The name of the password to be used to run the command on a Windows server.
        # 
        # If you want to use a username other than the default "system" username to run the command on a Windows server, you must specify both the WindowsPasswordName and WorkingUser parameters. To mitigate the risk of password leaks, the password is stored in plaintext in Operation Orchestration Service (OOS) Parameter Store, and only the name of the password is passed in by using WindowsPasswordName.
        self.windows_password_name = windows_password_name
        # The execution path of the command. You can specify a value for the parameter. Default execution paths vary based on the operating systems of the servers.
        # 
        # *   For Linux servers, the default execution path is the /home directory of the root user.
        # *   For Windows servers, the default execution path is C:\Windows\system32.
        self.working_dir = working_dir
        # A user of the server who runs the command. We recommend that you run the command as a regular user to reduce security risks. Default values:
        # 
        # *   For Linux servers, the default value is root.
        # *   For Windows servers, the default value is system.
        self.working_user = working_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.type is not None:
            result['Type'] = self.type
        if self.windows_password_name is not None:
            result['WindowsPasswordName'] = self.windows_password_name
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        if self.working_user is not None:
            result['WorkingUser'] = self.working_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WindowsPasswordName') is not None:
            self.windows_password_name = m.get('WindowsPasswordName')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        if m.get('WorkingUser') is not None:
            self.working_user = m.get('WorkingUser')
        return self


class RunCommandResponseBody(TeaModel):
    def __init__(
        self,
        invoke_id: str = None,
        request_id: str = None,
    ):
        # The execution ID.
        self.invoke_id = invoke_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunCommandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RunCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDatabaseInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        database_instance_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the Simple Database Service instance.
        self.database_instance_id = database_instance_id
        # The region ID of the Simple Database Service instance. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartDatabaseInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class StartDatabaseInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartDatabaseInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StartDatabaseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the server.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstancesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_ids: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The IDs of the simple application servers. The value can be a JSON array that consists of up to 100 simple application server IDs. Separate multiple server IDs with commas (,).
        self.instance_ids = instance_ids
        # The region ID of the simple application servers. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class StartInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StartInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTerminalSessionRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartTerminalSessionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_token: str = None,
        session_id: str = None,
        web_socket_url: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The security token included in the WebSocket request header. The system uses this token to authenticate the request.
        self.security_token = security_token
        # The session ID.
        self.session_id = session_id
        # The URL of the WebSocket session that is used to connect to the server. The URL contains the session ID (`SessionId`) and the authentication token (`SecurityToken`).
        self.web_socket_url = web_socket_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.web_socket_url is not None:
            result['WebSocketUrl'] = self.web_socket_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('WebSocketUrl') is not None:
            self.web_socket_url = m.get('WebSocketUrl')
        return self


class StartTerminalSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartTerminalSessionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StartTerminalSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDatabaseInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        database_instance_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the Simple Database Service instance.
        self.database_instance_id = database_instance_id
        # The region ID of the Simple Database Service instance. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.database_instance_id is not None:
            result['DatabaseInstanceId'] = self.database_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DatabaseInstanceId') is not None:
            self.database_instance_id = m.get('DatabaseInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopDatabaseInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class StopDatabaseInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopDatabaseInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StopDatabaseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The region ID of the server.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class StopInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstancesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        force_stop: bool = None,
        instance_ids: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # Specifies whether to forcibly stop the servers.
        # 
        # *   **true**: forcibly stops the servers.
        # *   **false**: normally stops the servers. This is the default value.
        self.force_stop = force_stop
        # The IDs of the simple application servers. The value can be a JSON array that consists of up to 100 simple application server IDs. Separate multiple server IDs with commas (,).
        self.instance_ids = instance_ids
        # The region ID of the simple application servers. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class StopInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = StopInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCommandAttributeRequest(TeaModel):
    def __init__(
        self,
        command_id: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        timeout: int = None,
        working_dir: str = None,
    ):
        self.command_id = command_id
        self.description = description
        self.name = name
        self.region_id = region_id
        self.timeout = timeout
        self.working_dir = working_dir

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class UpdateCommandAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class UpdateCommandAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCommandAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateCommandAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDiskAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        disk_id: str = None,
        region_id: str = None,
        remark: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The disk ID. You can call the ListDisks operation to query the ID of data disk.
        self.disk_id = disk_id
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id
        # The remarks of the data disk.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class UpdateDiskAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpdateDiskAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDiskAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateDiskAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        instance_name: str = None,
        password: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The name of the simple application server. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with `http://` or `https://`. The name can only contain letters, digits, colons (:), underscores (\_), periods (.), and hyphens (-).
        self.instance_name = instance_name
        # The new password of the simple application server. The password must be 8 to 30 characters in length. It must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Only the following special characters are supported:
        # 
        # `()~!@#$%^&*-+=|{}[]:;<>,.?/`
        self.password = password
        # The region ID of the simple application server.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpdateInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSnapshotAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        remark: str = None,
        snapshot_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id
        # The remarks of the snapshot of the simple application server.
        self.remark = remark
        # The snapshot ID. You can call the ListSnapshots operation to query the snapshot ID.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')
        return self


class UpdateSnapshotAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpdateSnapshotAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSnapshotAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateSnapshotAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        plan_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The ID of the new plan. You can call the [ListPlans](~~189314~~) operation to query the plans provided by Simple Application Server.
        self.plan_id = plan_id
        # The region ID of the simple application server.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpgradeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpgradeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpgradeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadInstanceKeyPairRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        key_pair_name: str = None,
        public_key: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token
        # The ID of the simple application server.
        self.instance_id = instance_id
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # The public key.
        self.public_key = public_key
        # The region ID of the simple application server. You can call the [ListRegions](~~189315~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UploadInstanceKeyPairResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UploadInstanceKeyPairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadInstanceKeyPairResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UploadInstanceKeyPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


