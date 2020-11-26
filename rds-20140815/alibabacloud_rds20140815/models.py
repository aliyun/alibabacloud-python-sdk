# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List, Dict, Any
except ImportError:
    pass


class GetDbProxyInstanceSslRequest(TeaModel):
    def __init__(self, region_id=None, db_instance_id=None):
        self.region_id = region_id      # type: str
        self.db_instance_id = db_instance_id  # type: str

    def validate(self):
        self.validate_required(self.db_instance_id, 'db_instance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DbInstanceId'] = self.db_instance_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.db_instance_id = map.get('DbInstanceId')
        return self


class GetDbProxyInstanceSslResponse(TeaModel):
    def __init__(self, request_id=None, db_proxy_cert_list_items=None):
        self.request_id = request_id    # type: str
        self.db_proxy_cert_list_items = db_proxy_cert_list_items  # type: GetDbProxyInstanceSslResponseDbProxyCertListItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.db_proxy_cert_list_items, 'db_proxy_cert_list_items')
        if self.db_proxy_cert_list_items:
            self.db_proxy_cert_list_items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.db_proxy_cert_list_items is not None:
            result['DbProxyCertListItems'] = self.db_proxy_cert_list_items.to_map()
        else:
            result['DbProxyCertListItems'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('DbProxyCertListItems') is not None:
            temp_model = GetDbProxyInstanceSslResponseDbProxyCertListItems()
            self.db_proxy_cert_list_items = temp_model.from_map(map['DbProxyCertListItems'])
        else:
            self.db_proxy_cert_list_items = None
        return self


class GetDbProxyInstanceSslResponseDbProxyCertListItemsDbProxyCertListItems(TeaModel):
    def __init__(self, db_instance_name=None, endpoint_name=None, endpoint_type=None, cert_common_name=None,
                 ssl_expired_time=None):
        self.db_instance_name = db_instance_name  # type: str
        self.endpoint_name = endpoint_name  # type: str
        self.endpoint_type = endpoint_type  # type: str
        self.cert_common_name = cert_common_name  # type: str
        self.ssl_expired_time = ssl_expired_time  # type: str

    def validate(self):
        self.validate_required(self.db_instance_name, 'db_instance_name')
        self.validate_required(self.endpoint_name, 'endpoint_name')
        self.validate_required(self.endpoint_type, 'endpoint_type')
        self.validate_required(self.cert_common_name, 'cert_common_name')
        self.validate_required(self.ssl_expired_time, 'ssl_expired_time')

    def to_map(self):
        result = {}
        result['DbInstanceName'] = self.db_instance_name
        result['EndpointName'] = self.endpoint_name
        result['EndpointType'] = self.endpoint_type
        result['CertCommonName'] = self.cert_common_name
        result['SslExpiredTime'] = self.ssl_expired_time
        return result

    def from_map(self, map={}):
        self.db_instance_name = map.get('DbInstanceName')
        self.endpoint_name = map.get('EndpointName')
        self.endpoint_type = map.get('EndpointType')
        self.cert_common_name = map.get('CertCommonName')
        self.ssl_expired_time = map.get('SslExpiredTime')
        return self


class GetDbProxyInstanceSslResponseDbProxyCertListItems(TeaModel):
    def __init__(self, db_proxy_cert_list_items=None):
        self.db_proxy_cert_list_items = db_proxy_cert_list_items  # type: List[GetDbProxyInstanceSslResponseDbProxyCertListItemsDbProxyCertListItems]

    def validate(self):
        self.validate_required(self.db_proxy_cert_list_items, 'db_proxy_cert_list_items')
        if self.db_proxy_cert_list_items:
            for k in self.db_proxy_cert_list_items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DbProxyCertListItems'] = []
        if self.db_proxy_cert_list_items is not None:
            for k in self.db_proxy_cert_list_items:
                result['DbProxyCertListItems'].append(k.to_map() if k else None)
        else:
            result['DbProxyCertListItems'] = None
        return result

    def from_map(self, map={}):
        self.db_proxy_cert_list_items = []
        if map.get('DbProxyCertListItems') is not None:
            for k in map.get('DbProxyCertListItems'):
                temp_model = GetDbProxyInstanceSslResponseDbProxyCertListItemsDbProxyCertListItems()
                self.db_proxy_cert_list_items.append(temp_model.from_map(k))
        else:
            self.db_proxy_cert_list_items = None
        return self


class ModifyDbProxyInstanceSslRequest(TeaModel):
    def __init__(self, region_id=None, db_instance_id=None, db_proxy_endpoint_id=None,
                 db_proxy_connect_string=None, db_proxy_ssl_enabled=None):
        self.region_id = region_id      # type: str
        self.db_instance_id = db_instance_id  # type: str
        self.db_proxy_endpoint_id = db_proxy_endpoint_id  # type: str
        self.db_proxy_connect_string = db_proxy_connect_string  # type: str
        self.db_proxy_ssl_enabled = db_proxy_ssl_enabled  # type: str

    def validate(self):
        self.validate_required(self.db_instance_id, 'db_instance_id')
        self.validate_required(self.db_proxy_endpoint_id, 'db_proxy_endpoint_id')
        self.validate_required(self.db_proxy_connect_string, 'db_proxy_connect_string')
        self.validate_required(self.db_proxy_ssl_enabled, 'db_proxy_ssl_enabled')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DbInstanceId'] = self.db_instance_id
        result['DbProxyEndpointId'] = self.db_proxy_endpoint_id
        result['DbProxyConnectString'] = self.db_proxy_connect_string
        result['DbProxySslEnabled'] = self.db_proxy_ssl_enabled
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.db_instance_id = map.get('DbInstanceId')
        self.db_proxy_endpoint_id = map.get('DbProxyEndpointId')
        self.db_proxy_connect_string = map.get('DbProxyConnectString')
        self.db_proxy_ssl_enabled = map.get('DbProxySslEnabled')
        return self


class ModifyDbProxyInstanceSslResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class MigrateConnectionToOtherZoneRequest(TeaModel):
    def __init__(self, dbinstance_id=None, connection_string=None, zone_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.connection_string = connection_string  # type: str
        self.zone_id = zone_id          # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.connection_string, 'connection_string')
        self.validate_required(self.zone_id, 'zone_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['ConnectionString'] = self.connection_string
        result['ZoneId'] = self.zone_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.connection_string = map.get('ConnectionString')
        self.zone_id = map.get('ZoneId')
        return self


class MigrateConnectionToOtherZoneResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        return self


class GetDBInstanceTopologyRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class GetDBInstanceTopologyResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.data = data                # type: GetDBInstanceTopologyResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = GetDBInstanceTopologyResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetDBInstanceTopologyResponseDataConnections(TeaModel):
    def __init__(self, net_type=None, connection_string=None, zone_id=None):
        self.net_type = net_type        # type: str
        self.connection_string = connection_string  # type: str
        self.zone_id = zone_id          # type: str

    def validate(self):
        self.validate_required(self.net_type, 'net_type')
        self.validate_required(self.connection_string, 'connection_string')
        self.validate_required(self.zone_id, 'zone_id')

    def to_map(self):
        result = {}
        result['NetType'] = self.net_type
        result['ConnectionString'] = self.connection_string
        result['ZoneId'] = self.zone_id
        return result

    def from_map(self, map={}):
        self.net_type = map.get('NetType')
        self.connection_string = map.get('ConnectionString')
        self.zone_id = map.get('ZoneId')
        return self


class GetDBInstanceTopologyResponseDataNodes(TeaModel):
    def __init__(self, role=None, dedicated_host_id=None, zone_id=None, dedicated_host_group_id=None):
        self.role = role                # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.zone_id = zone_id          # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str

    def validate(self):
        self.validate_required(self.role, 'role')
        self.validate_required(self.dedicated_host_id, 'dedicated_host_id')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.dedicated_host_group_id, 'dedicated_host_group_id')

    def to_map(self):
        result = {}
        result['Role'] = self.role
        result['DedicatedHostId'] = self.dedicated_host_id
        result['ZoneId'] = self.zone_id
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        return result

    def from_map(self, map={}):
        self.role = map.get('Role')
        self.dedicated_host_id = map.get('DedicatedHostId')
        self.zone_id = map.get('ZoneId')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        return self


class GetDBInstanceTopologyResponseData(TeaModel):
    def __init__(self, dbinstance_name=None, connections=None, nodes=None):
        self.dbinstance_name = dbinstance_name  # type: str
        self.connections = connections  # type: List[GetDBInstanceTopologyResponseDataConnections]
        self.nodes = nodes              # type: List[GetDBInstanceTopologyResponseDataNodes]

    def validate(self):
        self.validate_required(self.dbinstance_name, 'dbinstance_name')
        self.validate_required(self.connections, 'connections')
        if self.connections:
            for k in self.connections:
                if k:
                    k.validate()
        self.validate_required(self.nodes, 'nodes')
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DBInstanceName'] = self.dbinstance_name
        result['Connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['Connections'].append(k.to_map() if k else None)
        else:
            result['Connections'] = None
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        else:
            result['Nodes'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_name = map.get('DBInstanceName')
        self.connections = []
        if map.get('Connections') is not None:
            for k in map.get('Connections'):
                temp_model = GetDBInstanceTopologyResponseDataConnections()
                self.connections.append(temp_model.from_map(k))
        else:
            self.connections = None
        self.nodes = []
        if map.get('Nodes') is not None:
            for k in map.get('Nodes'):
                temp_model = GetDBInstanceTopologyResponseDataNodes()
                self.nodes.append(temp_model.from_map(k))
        else:
            self.nodes = None
        return self


class CheckRegionSupportBackupEncryptionRequest(TeaModel):
    def __init__(self, region_id=None, dbinstance_id=None):
        self.region_id = region_id      # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DBInstanceID'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dbinstance_id = map.get('DBInstanceID')
        return self


class CheckRegionSupportBackupEncryptionResponse(TeaModel):
    def __init__(self, request_id=None, support_backup_encryption=None):
        self.request_id = request_id    # type: str
        self.support_backup_encryption = support_backup_encryption  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.support_backup_encryption, 'support_backup_encryption')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['SupportBackupEncryption'] = self.support_backup_encryption
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.support_backup_encryption = map.get('SupportBackupEncryption')
        return self


class DescribeDBInstanceDetailRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeDBInstanceDetailResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, region_id=None, license_type=None,
                 activation_state=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id      # type: str
        self.license_type = license_type  # type: str
        self.activation_state = activation_state  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.license_type, 'license_type')
        self.validate_required(self.activation_state, 'activation_state')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['RegionId'] = self.region_id
        result['LicenseType'] = self.license_type
        result['ActivationState'] = self.activation_state
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.region_id = map.get('RegionId')
        self.license_type = map.get('LicenseType')
        self.activation_state = map.get('ActivationState')
        return self


class ModifyLicenseInfoRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, license=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.license = license          # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.license, 'license')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['License'] = self.license
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.license = map.get('License')
        return self


class ModifyLicenseInfoResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteDBProxyEndpointAddressRequest(TeaModel):
    def __init__(self, region_id=None, dbinstance_id=None, dbproxy_endpoint_id=None,
                 dbproxy_connect_string_net_type=None):
        self.region_id = region_id      # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbproxy_endpoint_id = dbproxy_endpoint_id  # type: str
        self.dbproxy_connect_string_net_type = dbproxy_connect_string_net_type  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbproxy_endpoint_id, 'dbproxy_endpoint_id')
        self.validate_required(self.dbproxy_connect_string_net_type, 'dbproxy_connect_string_net_type')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DBInstanceId'] = self.dbinstance_id
        result['DBProxyEndpointId'] = self.dbproxy_endpoint_id
        result['DBProxyConnectStringNetType'] = self.dbproxy_connect_string_net_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbproxy_endpoint_id = map.get('DBProxyEndpointId')
        self.dbproxy_connect_string_net_type = map.get('DBProxyConnectStringNetType')
        return self


class DeleteDBProxyEndpointAddressResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateDBProxyEndpointAddressRequest(TeaModel):
    def __init__(self, region_id=None, dbinstance_id=None, dbproxy_endpoint_id=None, connection_string_prefix=None,
                 dbproxy_new_connect_string_port=None, dbproxy_connect_string_net_type=None, vpcid=None, v_switch_id=None):
        self.region_id = region_id      # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbproxy_endpoint_id = dbproxy_endpoint_id  # type: str
        self.connection_string_prefix = connection_string_prefix  # type: str
        self.dbproxy_new_connect_string_port = dbproxy_new_connect_string_port  # type: str
        self.dbproxy_connect_string_net_type = dbproxy_connect_string_net_type  # type: str
        self.vpcid = vpcid              # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbproxy_endpoint_id, 'dbproxy_endpoint_id')
        self.validate_required(self.connection_string_prefix, 'connection_string_prefix')
        self.validate_required(self.dbproxy_connect_string_net_type, 'dbproxy_connect_string_net_type')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DBInstanceId'] = self.dbinstance_id
        result['DBProxyEndpointId'] = self.dbproxy_endpoint_id
        result['ConnectionStringPrefix'] = self.connection_string_prefix
        result['DBProxyNewConnectStringPort'] = self.dbproxy_new_connect_string_port
        result['DBProxyConnectStringNetType'] = self.dbproxy_connect_string_net_type
        result['VPCId'] = self.vpcid
        result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbproxy_endpoint_id = map.get('DBProxyEndpointId')
        self.connection_string_prefix = map.get('ConnectionStringPrefix')
        self.dbproxy_new_connect_string_port = map.get('DBProxyNewConnectStringPort')
        self.dbproxy_connect_string_net_type = map.get('DBProxyConnectStringNetType')
        self.vpcid = map.get('VPCId')
        self.v_switch_id = map.get('VSwitchId')
        return self


class CreateDBProxyEndpointAddressResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeDasInstanceConfigRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeDasInstanceConfigResponse(TeaModel):
    def __init__(self, request_id=None, data=None, storage_upper_bound=None, max_storage_upper_bound=None,
                 dbinstance_id=None, storage_threshold=None, storage_auto_scale=None, dbtype=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: str
        self.storage_upper_bound = storage_upper_bound  # type: int
        self.max_storage_upper_bound = max_storage_upper_bound  # type: int
        self.dbinstance_id = dbinstance_id  # type: str
        self.storage_threshold = storage_threshold  # type: int
        self.storage_auto_scale = storage_auto_scale  # type: bool
        self.dbtype = dbtype            # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        self.validate_required(self.storage_upper_bound, 'storage_upper_bound')
        self.validate_required(self.max_storage_upper_bound, 'max_storage_upper_bound')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.storage_threshold, 'storage_threshold')
        self.validate_required(self.storage_auto_scale, 'storage_auto_scale')
        self.validate_required(self.dbtype, 'dbtype')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        result['StorageUpperBound'] = self.storage_upper_bound
        result['MaxStorageUpperBound'] = self.max_storage_upper_bound
        result['DBInstanceId'] = self.dbinstance_id
        result['StorageThreshold'] = self.storage_threshold
        result['StorageAutoScale'] = self.storage_auto_scale
        result['DBType'] = self.dbtype
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        self.storage_upper_bound = map.get('StorageUpperBound')
        self.max_storage_upper_bound = map.get('MaxStorageUpperBound')
        self.dbinstance_id = map.get('DBInstanceId')
        self.storage_threshold = map.get('StorageThreshold')
        self.storage_auto_scale = map.get('StorageAutoScale')
        self.dbtype = map.get('DBType')
        return self


class ModifyDasInstanceConfigRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, storage_auto_scale=None, storage_threshold=None,
                 storage_upper_bound=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.storage_auto_scale = storage_auto_scale  # type: str
        self.storage_threshold = storage_threshold  # type: int
        self.storage_upper_bound = storage_upper_bound  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.storage_auto_scale, 'storage_auto_scale')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['StorageAutoScale'] = self.storage_auto_scale
        result['StorageThreshold'] = self.storage_threshold
        result['StorageUpperBound'] = self.storage_upper_bound
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.storage_auto_scale = map.get('StorageAutoScale')
        self.storage_threshold = map.get('StorageThreshold')
        self.storage_upper_bound = map.get('StorageUpperBound')
        return self


class ModifyDasInstanceConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeRdsResourceSettingsRequest(TeaModel):
    def __init__(self, resource_niche=None):
        self.resource_niche = resource_niche  # type: str

    def validate(self):
        self.validate_required(self.resource_niche, 'resource_niche')

    def to_map(self):
        result = {}
        result['ResourceNiche'] = self.resource_niche
        return result

    def from_map(self, map={}):
        self.resource_niche = map.get('ResourceNiche')
        return self


class DescribeRdsResourceSettingsResponse(TeaModel):
    def __init__(self, request_id=None, rds_instance_resource_settings=None):
        self.request_id = request_id    # type: str
        self.rds_instance_resource_settings = rds_instance_resource_settings  # type: DescribeRdsResourceSettingsResponseRdsInstanceResourceSettings

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.rds_instance_resource_settings, 'rds_instance_resource_settings')
        if self.rds_instance_resource_settings:
            self.rds_instance_resource_settings.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.rds_instance_resource_settings is not None:
            result['RdsInstanceResourceSettings'] = self.rds_instance_resource_settings.to_map()
        else:
            result['RdsInstanceResourceSettings'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('RdsInstanceResourceSettings') is not None:
            temp_model = DescribeRdsResourceSettingsResponseRdsInstanceResourceSettings()
            self.rds_instance_resource_settings = temp_model.from_map(map['RdsInstanceResourceSettings'])
        else:
            self.rds_instance_resource_settings = None
        return self


class DescribeRdsResourceSettingsResponseRdsInstanceResourceSettingsRdsInstanceResourceSetting(TeaModel):
    def __init__(self, start_date=None, end_date=None, resource_niche=None, notice_bar_content=None,
                 popped_up_button_text=None, popped_up_button_type=None, popped_up_button_url=None, popped_up_content=None, is_top=None):
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str
        self.resource_niche = resource_niche  # type: str
        self.notice_bar_content = notice_bar_content  # type: str
        self.popped_up_button_text = popped_up_button_text  # type: str
        self.popped_up_button_type = popped_up_button_type  # type: str
        self.popped_up_button_url = popped_up_button_url  # type: str
        self.popped_up_content = popped_up_content  # type: str
        self.is_top = is_top            # type: str

    def validate(self):
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')
        self.validate_required(self.resource_niche, 'resource_niche')
        self.validate_required(self.notice_bar_content, 'notice_bar_content')
        self.validate_required(self.popped_up_button_text, 'popped_up_button_text')
        self.validate_required(self.popped_up_button_type, 'popped_up_button_type')
        self.validate_required(self.popped_up_button_url, 'popped_up_button_url')
        self.validate_required(self.popped_up_content, 'popped_up_content')
        self.validate_required(self.is_top, 'is_top')

    def to_map(self):
        result = {}
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        result['ResourceNiche'] = self.resource_niche
        result['NoticeBarContent'] = self.notice_bar_content
        result['PoppedUpButtonText'] = self.popped_up_button_text
        result['PoppedUpButtonType'] = self.popped_up_button_type
        result['PoppedUpButtonUrl'] = self.popped_up_button_url
        result['PoppedUpContent'] = self.popped_up_content
        result['IsTop'] = self.is_top
        return result

    def from_map(self, map={}):
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        self.resource_niche = map.get('ResourceNiche')
        self.notice_bar_content = map.get('NoticeBarContent')
        self.popped_up_button_text = map.get('PoppedUpButtonText')
        self.popped_up_button_type = map.get('PoppedUpButtonType')
        self.popped_up_button_url = map.get('PoppedUpButtonUrl')
        self.popped_up_content = map.get('PoppedUpContent')
        self.is_top = map.get('IsTop')
        return self


class DescribeRdsResourceSettingsResponseRdsInstanceResourceSettings(TeaModel):
    def __init__(self, rds_instance_resource_setting=None):
        self.rds_instance_resource_setting = rds_instance_resource_setting  # type: List[DescribeRdsResourceSettingsResponseRdsInstanceResourceSettingsRdsInstanceResourceSetting]

    def validate(self):
        self.validate_required(self.rds_instance_resource_setting, 'rds_instance_resource_setting')
        if self.rds_instance_resource_setting:
            for k in self.rds_instance_resource_setting:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RdsInstanceResourceSetting'] = []
        if self.rds_instance_resource_setting is not None:
            for k in self.rds_instance_resource_setting:
                result['RdsInstanceResourceSetting'].append(k.to_map() if k else None)
        else:
            result['RdsInstanceResourceSetting'] = None
        return result

    def from_map(self, map={}):
        self.rds_instance_resource_setting = []
        if map.get('RdsInstanceResourceSetting') is not None:
            for k in map.get('RdsInstanceResourceSetting'):
                temp_model = DescribeRdsResourceSettingsResponseRdsInstanceResourceSettingsRdsInstanceResourceSetting()
                self.rds_instance_resource_setting.append(temp_model.from_map(k))
        else:
            self.rds_instance_resource_setting = None
        return self


class DeleteHostAccountRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, account_name=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.account_name, 'account_name')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['AccountName'] = self.account_name
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.account_name = map.get('AccountName')
        return self


class DeleteHostAccountResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeHostAccountsRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeHostAccountsResponse(TeaModel):
    def __init__(self, request_id=None, accounts=None):
        self.request_id = request_id    # type: str
        self.accounts = accounts        # type: DescribeHostAccountsResponseAccounts

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.accounts, 'accounts')
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        else:
            result['Accounts'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Accounts') is not None:
            temp_model = DescribeHostAccountsResponseAccounts()
            self.accounts = temp_model.from_map(map['Accounts'])
        else:
            self.accounts = None
        return self


class DescribeHostAccountsResponseAccountsAccounts(TeaModel):
    def __init__(self, account_name=None, account_type=None, account_description=None, account_status=None,
                 dbinstance_id=None):
        self.account_name = account_name  # type: str
        self.account_type = account_type  # type: str
        self.account_description = account_description  # type: str
        self.account_status = account_status  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.account_type, 'account_type')
        self.validate_required(self.account_description, 'account_description')
        self.validate_required(self.account_status, 'account_status')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['AccountName'] = self.account_name
        result['AccountType'] = self.account_type
        result['AccountDescription'] = self.account_description
        result['AccountStatus'] = self.account_status
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.account_name = map.get('AccountName')
        self.account_type = map.get('AccountType')
        self.account_description = map.get('AccountDescription')
        self.account_status = map.get('AccountStatus')
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeHostAccountsResponseAccounts(TeaModel):
    def __init__(self, accounts=None):
        self.accounts = accounts        # type: List[DescribeHostAccountsResponseAccountsAccounts]

    def validate(self):
        self.validate_required(self.accounts, 'accounts')
        if self.accounts:
            for k in self.accounts:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Accounts'] = []
        if self.accounts is not None:
            for k in self.accounts:
                result['Accounts'].append(k.to_map() if k else None)
        else:
            result['Accounts'] = None
        return result

    def from_map(self, map={}):
        self.accounts = []
        if map.get('Accounts') is not None:
            for k in map.get('Accounts'):
                temp_model = DescribeHostAccountsResponseAccountsAccounts()
                self.accounts.append(temp_model.from_map(k))
        else:
            self.accounts = None
        return self


class ResetHostAccountPasswordRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, account_name=None, account_password=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.account_password, 'account_password')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['AccountName'] = self.account_name
        result['AccountPassword'] = self.account_password
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.account_name = map.get('AccountName')
        self.account_password = map.get('AccountPassword')
        return self


class ResetHostAccountPasswordResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateHostAccountRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, account_name=None, account_type=None,
                 account_password=None, account_description=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.account_name = account_name  # type: str
        self.account_type = account_type  # type: str
        self.account_password = account_password  # type: str
        self.account_description = account_description  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.account_password, 'account_password')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['AccountName'] = self.account_name
        result['AccountType'] = self.account_type
        result['AccountPassword'] = self.account_password
        result['AccountDescription'] = self.account_description
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.account_name = map.get('AccountName')
        self.account_type = map.get('AccountType')
        self.account_password = map.get('AccountPassword')
        self.account_description = map.get('AccountDescription')
        return self


class CreateHostAccountResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeDedicatedHostImageCategoriesRequest(TeaModel):
    def __init__(self, region_id=None, host_group=None):
        self.region_id = region_id      # type: str
        self.host_group = host_group    # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.host_group, 'host_group')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['HostGroup'] = self.host_group
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.host_group = map.get('HostGroup')
        return self


class DescribeDedicatedHostImageCategoriesResponse(TeaModel):
    def __init__(self, request_id=None, images=None):
        self.request_id = request_id    # type: str
        self.images = images            # type: DescribeDedicatedHostImageCategoriesResponseImages

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.images, 'images')
        if self.images:
            self.images.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.images is not None:
            result['Images'] = self.images.to_map()
        else:
            result['Images'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Images') is not None:
            temp_model = DescribeDedicatedHostImageCategoriesResponseImages()
            self.images = temp_model.from_map(map['Images'])
        else:
            self.images = None
        return self


class DescribeDedicatedHostImageCategoriesResponseImagesImages(TeaModel):
    def __init__(self, image_name=None, image_code=None):
        self.image_name = image_name    # type: str
        self.image_code = image_code    # type: str

    def validate(self):
        self.validate_required(self.image_name, 'image_name')
        self.validate_required(self.image_code, 'image_code')

    def to_map(self):
        result = {}
        result['ImageName'] = self.image_name
        result['ImageCode'] = self.image_code
        return result

    def from_map(self, map={}):
        self.image_name = map.get('ImageName')
        self.image_code = map.get('ImageCode')
        return self


class DescribeDedicatedHostImageCategoriesResponseImages(TeaModel):
    def __init__(self, images=None):
        self.images = images            # type: List[DescribeDedicatedHostImageCategoriesResponseImagesImages]

    def validate(self):
        self.validate_required(self.images, 'images')
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        else:
            result['Images'] = None
        return result

    def from_map(self, map={}):
        self.images = []
        if map.get('Images') is not None:
            for k in map.get('Images'):
                temp_model = DescribeDedicatedHostImageCategoriesResponseImagesImages()
                self.images.append(temp_model.from_map(k))
        else:
            self.images = None
        return self


class DescribeCrossBackupMetaListRequest(TeaModel):
    def __init__(self, backup_set_id=None, get_db_name=None, pattern=None, page_size=None, page_index=None,
                 region=None):
        self.backup_set_id = backup_set_id  # type: str
        self.get_db_name = get_db_name  # type: str
        self.pattern = pattern          # type: str
        self.page_size = page_size      # type: str
        self.page_index = page_index    # type: str
        self.region = region            # type: str

    def validate(self):
        self.validate_required(self.backup_set_id, 'backup_set_id')

    def to_map(self):
        result = {}
        result['BackupSetId'] = self.backup_set_id
        result['GetDbName'] = self.get_db_name
        result['Pattern'] = self.pattern
        result['PageSize'] = self.page_size
        result['PageIndex'] = self.page_index
        result['Region'] = self.region
        return result

    def from_map(self, map={}):
        self.backup_set_id = map.get('BackupSetId')
        self.get_db_name = map.get('GetDbName')
        self.pattern = map.get('Pattern')
        self.page_size = map.get('PageSize')
        self.page_index = map.get('PageIndex')
        self.region = map.get('Region')
        return self


class DescribeCrossBackupMetaListResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_name=None, page_number=None, page_record_count=None,
                 total_record_count=None, total_page_count=None, items=None):
        self.request_id = request_id    # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.total_record_count = total_record_count  # type: int
        self.total_page_count = total_page_count  # type: int
        self.items = items              # type: DescribeCrossBackupMetaListResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_name, 'dbinstance_name')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.total_page_count, 'total_page_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceName'] = self.dbinstance_name
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        result['TotalRecordCount'] = self.total_record_count
        result['TotalPageCount'] = self.total_page_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_name = map.get('DBInstanceName')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        self.total_record_count = map.get('TotalRecordCount')
        self.total_page_count = map.get('TotalPageCount')
        if map.get('Items') is not None:
            temp_model = DescribeCrossBackupMetaListResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeCrossBackupMetaListResponseItemsMeta(TeaModel):
    def __init__(self, database=None, tables=None, size=None):
        self.database = database        # type: str
        self.tables = tables            # type: str
        self.size = size                # type: str

    def validate(self):
        self.validate_required(self.database, 'database')
        self.validate_required(self.tables, 'tables')
        self.validate_required(self.size, 'size')

    def to_map(self):
        result = {}
        result['Database'] = self.database
        result['Tables'] = self.tables
        result['Size'] = self.size
        return result

    def from_map(self, map={}):
        self.database = map.get('Database')
        self.tables = map.get('Tables')
        self.size = map.get('Size')
        return self


class DescribeCrossBackupMetaListResponseItems(TeaModel):
    def __init__(self, meta=None):
        self.meta = meta                # type: List[DescribeCrossBackupMetaListResponseItemsMeta]

    def validate(self):
        self.validate_required(self.meta, 'meta')
        if self.meta:
            for k in self.meta:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Meta'] = []
        if self.meta is not None:
            for k in self.meta:
                result['Meta'].append(k.to_map() if k else None)
        else:
            result['Meta'] = None
        return result

    def from_map(self, map={}):
        self.meta = []
        if map.get('Meta') is not None:
            for k in map.get('Meta'):
                temp_model = DescribeCrossBackupMetaListResponseItemsMeta()
                self.meta.append(temp_model.from_map(k))
        else:
            self.meta = None
        return self


class RestoreDdrTableRequest(TeaModel):
    def __init__(self, dbinstance_id=None, region_id=None, client_token=None, restore_type=None, backup_id=None,
                 restore_time=None, source_region=None, source_dbinstance_name=None, table_meta=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id      # type: str
        self.client_token = client_token  # type: str
        self.restore_type = restore_type  # type: str
        self.backup_id = backup_id      # type: str
        self.restore_time = restore_time  # type: str
        self.source_region = source_region  # type: str
        self.source_dbinstance_name = source_dbinstance_name  # type: str
        self.table_meta = table_meta    # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.restore_type, 'restore_type')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['RestoreType'] = self.restore_type
        result['BackupId'] = self.backup_id
        result['RestoreTime'] = self.restore_time
        result['SourceRegion'] = self.source_region
        result['SourceDBInstanceName'] = self.source_dbinstance_name
        result['TableMeta'] = self.table_meta
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.restore_type = map.get('RestoreType')
        self.backup_id = map.get('BackupId')
        self.restore_time = map.get('RestoreTime')
        self.source_region = map.get('SourceRegion')
        self.source_dbinstance_name = map.get('SourceDBInstanceName')
        self.table_meta = map.get('TableMeta')
        return self


class RestoreDdrTableResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyDBProxyEndpointAddressRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbproxy_endpoint_id=None, dbproxy_new_connect_string=None,
                 dbproxy_new_connect_string_port=None, dbproxy_connect_string_net_type=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbproxy_endpoint_id = dbproxy_endpoint_id  # type: str
        self.dbproxy_new_connect_string = dbproxy_new_connect_string  # type: str
        self.dbproxy_new_connect_string_port = dbproxy_new_connect_string_port  # type: str
        self.dbproxy_connect_string_net_type = dbproxy_connect_string_net_type  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbproxy_endpoint_id, 'dbproxy_endpoint_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBProxyEndpointId'] = self.dbproxy_endpoint_id
        result['DBProxyNewConnectString'] = self.dbproxy_new_connect_string
        result['DBProxyNewConnectStringPort'] = self.dbproxy_new_connect_string_port
        result['DBProxyConnectStringNetType'] = self.dbproxy_connect_string_net_type
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbproxy_endpoint_id = map.get('DBProxyEndpointId')
        self.dbproxy_new_connect_string = map.get('DBProxyNewConnectString')
        self.dbproxy_new_connect_string_port = map.get('DBProxyNewConnectStringPort')
        self.dbproxy_connect_string_net_type = map.get('DBProxyConnectStringNetType')
        return self


class ModifyDBProxyEndpointAddressResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class TerminateMigrateTaskRequest(TeaModel):
    def __init__(self, dbinstance_id=None, migrate_task_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.migrate_task_id = migrate_task_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.migrate_task_id, 'migrate_task_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['MigrateTaskId'] = self.migrate_task_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.migrate_task_id = map.get('MigrateTaskId')
        return self


class TerminateMigrateTaskResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLocalAvailableRecoveryTimeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, region=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.region = region            # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['Region'] = self.region
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.region = map.get('Region')
        return self


class DescribeLocalAvailableRecoveryTimeResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, recovery_begin_time=None, recovery_end_time=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.recovery_begin_time = recovery_begin_time  # type: str
        self.recovery_end_time = recovery_end_time  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.recovery_begin_time, 'recovery_begin_time')
        self.validate_required(self.recovery_end_time, 'recovery_end_time')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['RecoveryBeginTime'] = self.recovery_begin_time
        result['RecoveryEndTime'] = self.recovery_end_time
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.recovery_begin_time = map.get('RecoveryBeginTime')
        self.recovery_end_time = map.get('RecoveryEndTime')
        return self


class DescribeAvailableZonesRequest(TeaModel):
    def __init__(self, region_id=None, engine=None, zone_id=None, engine_version=None, instance_charge_type=None,
                 commodity_code=None, dispense_mode=None):
        self.region_id = region_id      # type: str
        self.engine = engine            # type: str
        self.zone_id = zone_id          # type: str
        self.engine_version = engine_version  # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.commodity_code = commodity_code  # type: str
        self.dispense_mode = dispense_mode  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.engine, 'engine')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Engine'] = self.engine
        result['ZoneId'] = self.zone_id
        result['EngineVersion'] = self.engine_version
        result['InstanceChargeType'] = self.instance_charge_type
        result['CommodityCode'] = self.commodity_code
        result['DispenseMode'] = self.dispense_mode
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.engine = map.get('Engine')
        self.zone_id = map.get('ZoneId')
        self.engine_version = map.get('EngineVersion')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.commodity_code = map.get('CommodityCode')
        self.dispense_mode = map.get('DispenseMode')
        return self


class DescribeAvailableZonesResponse(TeaModel):
    def __init__(self, request_id=None, available_zones=None):
        self.request_id = request_id    # type: str
        self.available_zones = available_zones  # type: List[DescribeAvailableZonesResponseAvailableZones]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.available_zones, 'available_zones')
        if self.available_zones:
            for k in self.available_zones:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['AvailableZones'] = []
        if self.available_zones is not None:
            for k in self.available_zones:
                result['AvailableZones'].append(k.to_map() if k else None)
        else:
            result['AvailableZones'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.available_zones = []
        if map.get('AvailableZones') is not None:
            for k in map.get('AvailableZones'):
                temp_model = DescribeAvailableZonesResponseAvailableZones()
                self.available_zones.append(temp_model.from_map(k))
        else:
            self.available_zones = None
        return self


class DescribeAvailableZonesResponseAvailableZonesSupportedEnginesSupportedEngineVersionsSupportedCategorysSupportedStorageTypes(TeaModel):
    def __init__(self, storage_type=None):
        self.storage_type = storage_type  # type: str

    def validate(self):
        self.validate_required(self.storage_type, 'storage_type')

    def to_map(self):
        result = {}
        result['StorageType'] = self.storage_type
        return result

    def from_map(self, map={}):
        self.storage_type = map.get('StorageType')
        return self


class DescribeAvailableZonesResponseAvailableZonesSupportedEnginesSupportedEngineVersionsSupportedCategorys(TeaModel):
    def __init__(self, category=None, supported_storage_types=None):
        self.category = category        # type: str
        self.supported_storage_types = supported_storage_types  # type: List[DescribeAvailableZonesResponseAvailableZonesSupportedEnginesSupportedEngineVersionsSupportedCategorysSupportedStorageTypes]

    def validate(self):
        self.validate_required(self.category, 'category')
        self.validate_required(self.supported_storage_types, 'supported_storage_types')
        if self.supported_storage_types:
            for k in self.supported_storage_types:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Category'] = self.category
        result['SupportedStorageTypes'] = []
        if self.supported_storage_types is not None:
            for k in self.supported_storage_types:
                result['SupportedStorageTypes'].append(k.to_map() if k else None)
        else:
            result['SupportedStorageTypes'] = None
        return result

    def from_map(self, map={}):
        self.category = map.get('Category')
        self.supported_storage_types = []
        if map.get('SupportedStorageTypes') is not None:
            for k in map.get('SupportedStorageTypes'):
                temp_model = DescribeAvailableZonesResponseAvailableZonesSupportedEnginesSupportedEngineVersionsSupportedCategorysSupportedStorageTypes()
                self.supported_storage_types.append(temp_model.from_map(k))
        else:
            self.supported_storage_types = None
        return self


class DescribeAvailableZonesResponseAvailableZonesSupportedEnginesSupportedEngineVersions(TeaModel):
    def __init__(self, version=None, supported_categorys=None):
        self.version = version          # type: str
        self.supported_categorys = supported_categorys  # type: List[DescribeAvailableZonesResponseAvailableZonesSupportedEnginesSupportedEngineVersionsSupportedCategorys]

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.supported_categorys, 'supported_categorys')
        if self.supported_categorys:
            for k in self.supported_categorys:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['SupportedCategorys'] = []
        if self.supported_categorys is not None:
            for k in self.supported_categorys:
                result['SupportedCategorys'].append(k.to_map() if k else None)
        else:
            result['SupportedCategorys'] = None
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.supported_categorys = []
        if map.get('SupportedCategorys') is not None:
            for k in map.get('SupportedCategorys'):
                temp_model = DescribeAvailableZonesResponseAvailableZonesSupportedEnginesSupportedEngineVersionsSupportedCategorys()
                self.supported_categorys.append(temp_model.from_map(k))
        else:
            self.supported_categorys = None
        return self


class DescribeAvailableZonesResponseAvailableZonesSupportedEngines(TeaModel):
    def __init__(self, engine=None, supported_engine_versions=None):
        self.engine = engine            # type: str
        self.supported_engine_versions = supported_engine_versions  # type: List[DescribeAvailableZonesResponseAvailableZonesSupportedEnginesSupportedEngineVersions]

    def validate(self):
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.supported_engine_versions, 'supported_engine_versions')
        if self.supported_engine_versions:
            for k in self.supported_engine_versions:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Engine'] = self.engine
        result['SupportedEngineVersions'] = []
        if self.supported_engine_versions is not None:
            for k in self.supported_engine_versions:
                result['SupportedEngineVersions'].append(k.to_map() if k else None)
        else:
            result['SupportedEngineVersions'] = None
        return result

    def from_map(self, map={}):
        self.engine = map.get('Engine')
        self.supported_engine_versions = []
        if map.get('SupportedEngineVersions') is not None:
            for k in map.get('SupportedEngineVersions'):
                temp_model = DescribeAvailableZonesResponseAvailableZonesSupportedEnginesSupportedEngineVersions()
                self.supported_engine_versions.append(temp_model.from_map(k))
        else:
            self.supported_engine_versions = None
        return self


class DescribeAvailableZonesResponseAvailableZones(TeaModel):
    def __init__(self, region_id=None, zone_id=None, supported_engines=None):
        self.region_id = region_id      # type: str
        self.zone_id = zone_id          # type: str
        self.supported_engines = supported_engines  # type: List[DescribeAvailableZonesResponseAvailableZonesSupportedEngines]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.supported_engines, 'supported_engines')
        if self.supported_engines:
            for k in self.supported_engines:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ZoneId'] = self.zone_id
        result['SupportedEngines'] = []
        if self.supported_engines is not None:
            for k in self.supported_engines:
                result['SupportedEngines'].append(k.to_map() if k else None)
        else:
            result['SupportedEngines'] = None
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.zone_id = map.get('ZoneId')
        self.supported_engines = []
        if map.get('SupportedEngines') is not None:
            for k in map.get('SupportedEngines'):
                temp_model = DescribeAvailableZonesResponseAvailableZonesSupportedEngines()
                self.supported_engines.append(temp_model.from_map(k))
        else:
            self.supported_engines = None
        return self


class DescribeAvailableClassesRequest(TeaModel):
    def __init__(self, region_id=None, zone_id=None, instance_charge_type=None, engine=None, engine_version=None,
                 dbinstance_id=None, order_type=None, dbinstance_storage_type=None, category=None, commodity_code=None,
                 dispense_mode=None):
        self.region_id = region_id      # type: str
        self.zone_id = zone_id          # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.engine = engine            # type: str
        self.engine_version = engine_version  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.order_type = order_type    # type: str
        self.dbinstance_storage_type = dbinstance_storage_type  # type: str
        self.category = category        # type: str
        self.commodity_code = commodity_code  # type: str
        self.dispense_mode = dispense_mode  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.dbinstance_storage_type, 'dbinstance_storage_type')
        self.validate_required(self.category, 'category')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ZoneId'] = self.zone_id
        result['InstanceChargeType'] = self.instance_charge_type
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        result['DBInstanceId'] = self.dbinstance_id
        result['OrderType'] = self.order_type
        result['DBInstanceStorageType'] = self.dbinstance_storage_type
        result['Category'] = self.category
        result['CommodityCode'] = self.commodity_code
        result['DispenseMode'] = self.dispense_mode
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.zone_id = map.get('ZoneId')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        self.dbinstance_id = map.get('DBInstanceId')
        self.order_type = map.get('OrderType')
        self.dbinstance_storage_type = map.get('DBInstanceStorageType')
        self.category = map.get('Category')
        self.commodity_code = map.get('CommodityCode')
        self.dispense_mode = map.get('DispenseMode')
        return self


class DescribeAvailableClassesResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_classes=None):
        self.request_id = request_id    # type: str
        self.dbinstance_classes = dbinstance_classes  # type: List[DescribeAvailableClassesResponseDBInstanceClasses]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_classes, 'dbinstance_classes')
        if self.dbinstance_classes:
            for k in self.dbinstance_classes:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceClasses'] = []
        if self.dbinstance_classes is not None:
            for k in self.dbinstance_classes:
                result['DBInstanceClasses'].append(k.to_map() if k else None)
        else:
            result['DBInstanceClasses'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_classes = []
        if map.get('DBInstanceClasses') is not None:
            for k in map.get('DBInstanceClasses'):
                temp_model = DescribeAvailableClassesResponseDBInstanceClasses()
                self.dbinstance_classes.append(temp_model.from_map(k))
        else:
            self.dbinstance_classes = None
        return self


class DescribeAvailableClassesResponseDBInstanceClassesDBInstanceStorageRange(TeaModel):
    def __init__(self, max_value=None, min_value=None, step=None):
        self.max_value = max_value      # type: int
        self.min_value = min_value      # type: int
        self.step = step                # type: int

    def validate(self):
        self.validate_required(self.max_value, 'max_value')
        self.validate_required(self.min_value, 'min_value')
        self.validate_required(self.step, 'step')

    def to_map(self):
        result = {}
        result['MaxValue'] = self.max_value
        result['MinValue'] = self.min_value
        result['Step'] = self.step
        return result

    def from_map(self, map={}):
        self.max_value = map.get('MaxValue')
        self.min_value = map.get('MinValue')
        self.step = map.get('Step')
        return self


class DescribeAvailableClassesResponseDBInstanceClasses(TeaModel):
    def __init__(self, dbinstance_class=None, storage_range=None, dbinstance_storage_range=None):
        self.dbinstance_class = dbinstance_class  # type: str
        self.storage_range = storage_range  # type: str
        self.dbinstance_storage_range = dbinstance_storage_range  # type: DescribeAvailableClassesResponseDBInstanceClassesDBInstanceStorageRange

    def validate(self):
        self.validate_required(self.dbinstance_class, 'dbinstance_class')
        self.validate_required(self.storage_range, 'storage_range')
        self.validate_required(self.dbinstance_storage_range, 'dbinstance_storage_range')
        if self.dbinstance_storage_range:
            self.dbinstance_storage_range.validate()

    def to_map(self):
        result = {}
        result['DBInstanceClass'] = self.dbinstance_class
        result['StorageRange'] = self.storage_range
        if self.dbinstance_storage_range is not None:
            result['DBInstanceStorageRange'] = self.dbinstance_storage_range.to_map()
        else:
            result['DBInstanceStorageRange'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_class = map.get('DBInstanceClass')
        self.storage_range = map.get('StorageRange')
        if map.get('DBInstanceStorageRange') is not None:
            temp_model = DescribeAvailableClassesResponseDBInstanceClassesDBInstanceStorageRange()
            self.dbinstance_storage_range = temp_model.from_map(map['DBInstanceStorageRange'])
        else:
            self.dbinstance_storage_range = None
        return self


class CreateDedicatedHostAccountRequest(TeaModel):
    def __init__(self, dedicated_host_id=None, account_name=None, account_password=None, region_id=None):
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_id, 'dedicated_host_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.account_password, 'account_password')

    def to_map(self):
        result = {}
        result['DedicatedHostId'] = self.dedicated_host_id
        result['AccountName'] = self.account_name
        result['AccountPassword'] = self.account_password
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.dedicated_host_id = map.get('DedicatedHostId')
        self.account_name = map.get('AccountName')
        self.account_password = map.get('AccountPassword')
        self.region_id = map.get('RegionId')
        return self


class CreateDedicatedHostAccountResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteDedicatedHostAccountRequest(TeaModel):
    def __init__(self, dedicated_host_id=None, account_name=None, region_id=None):
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.account_name = account_name  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_id, 'dedicated_host_id')
        self.validate_required(self.account_name, 'account_name')

    def to_map(self):
        result = {}
        result['DedicatedHostId'] = self.dedicated_host_id
        result['AccountName'] = self.account_name
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.dedicated_host_id = map.get('DedicatedHostId')
        self.account_name = map.get('AccountName')
        self.region_id = map.get('RegionId')
        return self


class DeleteDedicatedHostAccountResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyDedicatedHostAccountRequest(TeaModel):
    def __init__(self, dedicated_host_id=None, account_name=None, account_password=None, region_id=None):
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_id, 'dedicated_host_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.account_password, 'account_password')

    def to_map(self):
        result = {}
        result['DedicatedHostId'] = self.dedicated_host_id
        result['AccountName'] = self.account_name
        result['AccountPassword'] = self.account_password
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.dedicated_host_id = map.get('DedicatedHostId')
        self.account_name = map.get('AccountName')
        self.account_password = map.get('AccountPassword')
        self.region_id = map.get('RegionId')
        return self


class ModifyDedicatedHostAccountResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class TransformDBInstancePayTypeRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, used_time=None, pay_type=None, period=None,
                 business_info=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.used_time = used_time      # type: int
        self.pay_type = pay_type        # type: str
        self.period = period            # type: str
        self.business_info = business_info  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.pay_type, 'pay_type')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['UsedTime'] = self.used_time
        result['PayType'] = self.pay_type
        result['Period'] = self.period
        result['BusinessInfo'] = self.business_info
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.used_time = map.get('UsedTime')
        self.pay_type = map.get('PayType')
        self.period = map.get('Period')
        self.business_info = map.get('BusinessInfo')
        return self


class TransformDBInstancePayTypeResponse(TeaModel):
    def __init__(self, request_id=None, order_id=None, charge_type=None, expired_time=None, dbinstance_id=None):
        self.request_id = request_id    # type: str
        self.order_id = order_id        # type: int
        self.charge_type = charge_type  # type: str
        self.expired_time = expired_time  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.charge_type, 'charge_type')
        self.validate_required(self.expired_time, 'expired_time')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['OrderId'] = self.order_id
        result['ChargeType'] = self.charge_type
        result['ExpiredTime'] = self.expired_time
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.order_id = map.get('OrderId')
        self.charge_type = map.get('ChargeType')
        self.expired_time = map.get('ExpiredTime')
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class CreateDedicatedHostUserRequest(TeaModel):
    def __init__(self, dedicated_host_name=None, user_name=None, user_password=None, region_id=None):
        self.dedicated_host_name = dedicated_host_name  # type: str
        self.user_name = user_name      # type: str
        self.user_password = user_password  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_name, 'dedicated_host_name')
        self.validate_required(self.user_name, 'user_name')
        self.validate_required(self.user_password, 'user_password')

    def to_map(self):
        result = {}
        result['DedicatedHostName'] = self.dedicated_host_name
        result['UserName'] = self.user_name
        result['UserPassword'] = self.user_password
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.dedicated_host_name = map.get('DedicatedHostName')
        self.user_name = map.get('UserName')
        self.user_password = map.get('UserPassword')
        self.region_id = map.get('RegionId')
        return self


class CreateDedicatedHostUserResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyDedicatedHostUserRequest(TeaModel):
    def __init__(self, dedicated_host_name=None, user_name=None, old_password=None, new_password=None,
                 region_id=None):
        self.dedicated_host_name = dedicated_host_name  # type: str
        self.user_name = user_name      # type: str
        self.old_password = old_password  # type: str
        self.new_password = new_password  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_name, 'dedicated_host_name')
        self.validate_required(self.user_name, 'user_name')
        self.validate_required(self.old_password, 'old_password')
        self.validate_required(self.new_password, 'new_password')

    def to_map(self):
        result = {}
        result['DedicatedHostName'] = self.dedicated_host_name
        result['UserName'] = self.user_name
        result['OldPassword'] = self.old_password
        result['NewPassword'] = self.new_password
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.dedicated_host_name = map.get('DedicatedHostName')
        self.user_name = map.get('UserName')
        self.old_password = map.get('OldPassword')
        self.new_password = map.get('NewPassword')
        self.region_id = map.get('RegionId')
        return self


class ModifyDedicatedHostUserResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DropDedicatedHostUserRequest(TeaModel):
    def __init__(self, dedicated_host_name=None, user_name=None, region_id=None):
        self.dedicated_host_name = dedicated_host_name  # type: str
        self.user_name = user_name      # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_name, 'dedicated_host_name')
        self.validate_required(self.user_name, 'user_name')

    def to_map(self):
        result = {}
        result['DedicatedHostName'] = self.dedicated_host_name
        result['UserName'] = self.user_name
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.dedicated_host_name = map.get('DedicatedHostName')
        self.user_name = map.get('UserName')
        self.region_id = map.get('RegionId')
        return self


class DropDedicatedHostUserResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class UpgradeDBProxyInstanceKernelVersionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, upgrade_time=None, switch_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.upgrade_time = upgrade_time  # type: str
        self.switch_time = switch_time  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['UpgradeTime'] = self.upgrade_time
        result['SwitchTime'] = self.switch_time
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.upgrade_time = map.get('UpgradeTime')
        self.switch_time = map.get('SwitchTime')
        return self


class UpgradeDBProxyInstanceKernelVersionResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_name=None, task_id=None, target_minor_version=None):
        self.request_id = request_id    # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.task_id = task_id          # type: str
        self.target_minor_version = target_minor_version  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_name, 'dbinstance_name')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.target_minor_version, 'target_minor_version')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceName'] = self.dbinstance_name
        result['TaskId'] = self.task_id
        result['TargetMinorVersion'] = self.target_minor_version
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_name = map.get('DBInstanceName')
        self.task_id = map.get('TaskId')
        self.target_minor_version = map.get('TargetMinorVersion')
        return self


class StopDBInstanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, region_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.region_id = map.get('RegionId')
        return self


class StopDBInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class StartDBInstanceRequest(TeaModel):
    def __init__(self, region_id=None, dedicated_host_group_id=None, dbinstance_id=None,
                 target_dedicated_host_id_for_master=None, target_dedicated_host_id_for_slave=None, target_dedicated_host_id_for_log=None,
                 effective_time=None, specified_time=None, target_dbinstance_class=None, engine_version=None,
                 dbinstance_trans_type=None, storage=None, v_switch_id=None, zone_id=None):
        self.region_id = region_id      # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.target_dedicated_host_id_for_master = target_dedicated_host_id_for_master  # type: str
        self.target_dedicated_host_id_for_slave = target_dedicated_host_id_for_slave  # type: str
        self.target_dedicated_host_id_for_log = target_dedicated_host_id_for_log  # type: str
        self.effective_time = effective_time  # type: str
        self.specified_time = specified_time  # type: str
        self.target_dbinstance_class = target_dbinstance_class  # type: str
        self.engine_version = engine_version  # type: str
        self.dbinstance_trans_type = dbinstance_trans_type  # type: int
        self.storage = storage          # type: int
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id          # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_group_id, 'dedicated_host_group_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['DBInstanceId'] = self.dbinstance_id
        result['TargetDedicatedHostIdForMaster'] = self.target_dedicated_host_id_for_master
        result['TargetDedicatedHostIdForSlave'] = self.target_dedicated_host_id_for_slave
        result['TargetDedicatedHostIdForLog'] = self.target_dedicated_host_id_for_log
        result['EffectiveTime'] = self.effective_time
        result['SpecifiedTime'] = self.specified_time
        result['TargetDBInstanceClass'] = self.target_dbinstance_class
        result['EngineVersion'] = self.engine_version
        result['DBInstanceTransType'] = self.dbinstance_trans_type
        result['Storage'] = self.storage
        result['VSwitchId'] = self.v_switch_id
        result['ZoneId'] = self.zone_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.target_dedicated_host_id_for_master = map.get('TargetDedicatedHostIdForMaster')
        self.target_dedicated_host_id_for_slave = map.get('TargetDedicatedHostIdForSlave')
        self.target_dedicated_host_id_for_log = map.get('TargetDedicatedHostIdForLog')
        self.effective_time = map.get('EffectiveTime')
        self.specified_time = map.get('SpecifiedTime')
        self.target_dbinstance_class = map.get('TargetDBInstanceClass')
        self.engine_version = map.get('EngineVersion')
        self.dbinstance_trans_type = map.get('DBInstanceTransType')
        self.storage = map.get('Storage')
        self.v_switch_id = map.get('VSwitchId')
        self.zone_id = map.get('ZoneId')
        return self


class StartDBInstanceResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None, migration_id=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: int
        self.migration_id = migration_id  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.migration_id, 'migration_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        result['MigrationId'] = self.migration_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        self.migration_id = map.get('MigrationId')
        return self


class DescribeSignedEventActionsRequest(TeaModel):
    def __init__(self, region_id=None, begin_event_id=None, page_size=None):
        self.region_id = region_id      # type: str
        self.begin_event_id = begin_event_id  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BeginEventId'] = self.begin_event_id
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.begin_event_id = map.get('BeginEventId')
        self.page_size = map.get('PageSize')
        return self


class DescribeSignedEventActionsResponse(TeaModel):
    def __init__(self, request_id=None, next_page_event_id=None, page_record_count=None, from_begin=None,
                 to_end=None, event_items=None):
        self.request_id = request_id    # type: str
        self.next_page_event_id = next_page_event_id  # type: int
        self.page_record_count = page_record_count  # type: int
        self.from_begin = from_begin    # type: bool
        self.to_end = to_end            # type: bool
        self.event_items = event_items  # type: DescribeSignedEventActionsResponseEventItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_page_event_id, 'next_page_event_id')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.from_begin, 'from_begin')
        self.validate_required(self.to_end, 'to_end')
        self.validate_required(self.event_items, 'event_items')
        if self.event_items:
            self.event_items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['NextPageEventId'] = self.next_page_event_id
        result['PageRecordCount'] = self.page_record_count
        result['FromBegin'] = self.from_begin
        result['ToEnd'] = self.to_end
        if self.event_items is not None:
            result['EventItems'] = self.event_items.to_map()
        else:
            result['EventItems'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.next_page_event_id = map.get('NextPageEventId')
        self.page_record_count = map.get('PageRecordCount')
        self.from_begin = map.get('FromBegin')
        self.to_end = map.get('ToEnd')
        if map.get('EventItems') is not None:
            temp_model = DescribeSignedEventActionsResponseEventItems()
            self.event_items = temp_model.from_map(map['EventItems'])
        else:
            self.event_items = None
        return self


class DescribeSignedEventActionsResponseEventItemsEventItems(TeaModel):
    def __init__(self, event_id=None, event_content=None, event_sig=None, event_rcpt=None):
        self.event_id = event_id        # type: int
        self.event_content = event_content  # type: str
        self.event_sig = event_sig      # type: str
        self.event_rcpt = event_rcpt    # type: str

    def validate(self):
        self.validate_required(self.event_id, 'event_id')
        self.validate_required(self.event_content, 'event_content')
        self.validate_required(self.event_sig, 'event_sig')
        self.validate_required(self.event_rcpt, 'event_rcpt')

    def to_map(self):
        result = {}
        result['EventId'] = self.event_id
        result['EventContent'] = self.event_content
        result['EventSig'] = self.event_sig
        result['EventRcpt'] = self.event_rcpt
        return result

    def from_map(self, map={}):
        self.event_id = map.get('EventId')
        self.event_content = map.get('EventContent')
        self.event_sig = map.get('EventSig')
        self.event_rcpt = map.get('EventRcpt')
        return self


class DescribeSignedEventActionsResponseEventItems(TeaModel):
    def __init__(self, event_items=None):
        self.event_items = event_items  # type: List[DescribeSignedEventActionsResponseEventItemsEventItems]

    def validate(self):
        self.validate_required(self.event_items, 'event_items')
        if self.event_items:
            for k in self.event_items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EventItems'] = []
        if self.event_items is not None:
            for k in self.event_items:
                result['EventItems'].append(k.to_map() if k else None)
        else:
            result['EventItems'] = None
        return result

    def from_map(self, map={}):
        self.event_items = []
        if map.get('EventItems') is not None:
            for k in map.get('EventItems'):
                temp_model = DescribeSignedEventActionsResponseEventItemsEventItems()
                self.event_items.append(temp_model.from_map(k))
        else:
            self.event_items = None
        return self


class SignEventActionRequest(TeaModel):
    def __init__(self, region_id=None, event_id=None, event_sig=None):
        self.region_id = region_id      # type: str
        self.event_id = event_id        # type: int
        self.event_sig = event_sig      # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.event_id, 'event_id')
        self.validate_required(self.event_sig, 'event_sig')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['EventId'] = self.event_id
        result['EventSig'] = self.event_sig
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.event_id = map.get('EventId')
        self.event_sig = map.get('EventSig')
        return self


class SignEventActionResponse(TeaModel):
    def __init__(self, request_id=None, event_id=None, event_rcpt=None):
        self.request_id = request_id    # type: str
        self.event_id = event_id        # type: str
        self.event_rcpt = event_rcpt    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.event_id, 'event_id')
        self.validate_required(self.event_rcpt, 'event_rcpt')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['EventId'] = self.event_id
        result['EventRcpt'] = self.event_rcpt
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.event_id = map.get('EventId')
        self.event_rcpt = map.get('EventRcpt')
        return self


class DescribeNextEventForSignRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        return self


class DescribeNextEventForSignResponse(TeaModel):
    def __init__(self, request_id=None, event_items=None):
        self.request_id = request_id    # type: str
        self.event_items = event_items  # type: DescribeNextEventForSignResponseEventItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.event_items, 'event_items')
        if self.event_items:
            self.event_items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.event_items is not None:
            result['EventItems'] = self.event_items.to_map()
        else:
            result['EventItems'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('EventItems') is not None:
            temp_model = DescribeNextEventForSignResponseEventItems()
            self.event_items = temp_model.from_map(map['EventItems'])
        else:
            self.event_items = None
        return self


class DescribeNextEventForSignResponseEventItemsEventItems(TeaModel):
    def __init__(self, event_id=None, event_content=None):
        self.event_id = event_id        # type: int
        self.event_content = event_content  # type: str

    def validate(self):
        self.validate_required(self.event_id, 'event_id')
        self.validate_required(self.event_content, 'event_content')

    def to_map(self):
        result = {}
        result['EventId'] = self.event_id
        result['EventContent'] = self.event_content
        return result

    def from_map(self, map={}):
        self.event_id = map.get('EventId')
        self.event_content = map.get('EventContent')
        return self


class DescribeNextEventForSignResponseEventItems(TeaModel):
    def __init__(self, event_items=None):
        self.event_items = event_items  # type: List[DescribeNextEventForSignResponseEventItemsEventItems]

    def validate(self):
        self.validate_required(self.event_items, 'event_items')
        if self.event_items:
            for k in self.event_items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EventItems'] = []
        if self.event_items is not None:
            for k in self.event_items:
                result['EventItems'].append(k.to_map() if k else None)
        else:
            result['EventItems'] = None
        return result

    def from_map(self, map={}):
        self.event_items = []
        if map.get('EventItems') is not None:
            for k in map.get('EventItems'):
                temp_model = DescribeNextEventForSignResponseEventItemsEventItems()
                self.event_items.append(temp_model.from_map(k))
        else:
            self.event_items = None
        return self


class ModifyActionEventVerifyPolicyRequest(TeaModel):
    def __init__(self, region_id=None, user_public_key=None):
        self.region_id = region_id      # type: str
        self.user_public_key = user_public_key  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.user_public_key, 'user_public_key')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['UserPublicKey'] = self.user_public_key
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.user_public_key = map.get('UserPublicKey')
        return self


class ModifyActionEventVerifyPolicyResponse(TeaModel):
    def __init__(self, request_id=None, region_id=None, server_public_key=None):
        self.request_id = request_id    # type: str
        self.region_id = region_id      # type: str
        self.server_public_key = server_public_key  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.server_public_key, 'server_public_key')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RegionId'] = self.region_id
        result['ServerPublicKey'] = self.server_public_key
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.region_id = map.get('RegionId')
        self.server_public_key = map.get('ServerPublicKey')
        return self


class DescribeDBInstancesOverviewRequest(TeaModel):
    def __init__(self, client_token=None, proxy_id=None, engine=None, zone_id=None, expired=None, dbinstance_id=None,
                 region_id=None, resource_group_id=None):
        self.client_token = client_token  # type: str
        self.proxy_id = proxy_id        # type: str
        self.engine = engine            # type: str
        self.zone_id = zone_id          # type: str
        self.expired = expired          # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id      # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['ProxyId'] = self.proxy_id
        result['Engine'] = self.engine
        result['ZoneId'] = self.zone_id
        result['Expired'] = self.expired
        result['DBInstanceId'] = self.dbinstance_id
        result['RegionId'] = self.region_id
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.proxy_id = map.get('ProxyId')
        self.engine = map.get('Engine')
        self.zone_id = map.get('ZoneId')
        self.expired = map.get('Expired')
        self.dbinstance_id = map.get('DBInstanceId')
        self.region_id = map.get('RegionId')
        self.resource_group_id = map.get('ResourceGroupId')
        return self


class DescribeDBInstancesOverviewResponse(TeaModel):
    def __init__(self, request_id=None, regions=None):
        self.request_id = request_id    # type: str
        self.regions = regions          # type: DescribeDBInstancesOverviewResponseRegions

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.regions, 'regions')
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        else:
            result['Regions'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Regions') is not None:
            temp_model = DescribeDBInstancesOverviewResponseRegions()
            self.regions = temp_model.from_map(map['Regions'])
        else:
            self.regions = None
        return self


class DescribeDBInstancesOverviewResponseRegionsRegionModelTypeModelsTypeModelInstanceModelsInstanceModel(TeaModel):
    def __init__(self, dbinstance_id=None, region=None, zone_id=None, engine=None, pay_type=None, created_time=None,
                 expire_time=None, lock_mode=None, dbinstance_status=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.region = region            # type: str
        self.zone_id = zone_id          # type: str
        self.engine = engine            # type: str
        self.pay_type = pay_type        # type: str
        self.created_time = created_time  # type: str
        self.expire_time = expire_time  # type: str
        self.lock_mode = lock_mode      # type: str
        self.dbinstance_status = dbinstance_status  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.region, 'region')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.pay_type, 'pay_type')
        self.validate_required(self.created_time, 'created_time')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.lock_mode, 'lock_mode')
        self.validate_required(self.dbinstance_status, 'dbinstance_status')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['Region'] = self.region
        result['ZoneId'] = self.zone_id
        result['Engine'] = self.engine
        result['PayType'] = self.pay_type
        result['CreatedTime'] = self.created_time
        result['ExpireTime'] = self.expire_time
        result['LockMode'] = self.lock_mode
        result['DBInstanceStatus'] = self.dbinstance_status
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.region = map.get('Region')
        self.zone_id = map.get('ZoneId')
        self.engine = map.get('Engine')
        self.pay_type = map.get('PayType')
        self.created_time = map.get('CreatedTime')
        self.expire_time = map.get('ExpireTime')
        self.lock_mode = map.get('LockMode')
        self.dbinstance_status = map.get('DBInstanceStatus')
        return self


class DescribeDBInstancesOverviewResponseRegionsRegionModelTypeModelsTypeModelInstanceModels(TeaModel):
    def __init__(self, instance_model=None):
        self.instance_model = instance_model  # type: List[DescribeDBInstancesOverviewResponseRegionsRegionModelTypeModelsTypeModelInstanceModelsInstanceModel]

    def validate(self):
        self.validate_required(self.instance_model, 'instance_model')
        if self.instance_model:
            for k in self.instance_model:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['InstanceModel'] = []
        if self.instance_model is not None:
            for k in self.instance_model:
                result['InstanceModel'].append(k.to_map() if k else None)
        else:
            result['InstanceModel'] = None
        return result

    def from_map(self, map={}):
        self.instance_model = []
        if map.get('InstanceModel') is not None:
            for k in map.get('InstanceModel'):
                temp_model = DescribeDBInstancesOverviewResponseRegionsRegionModelTypeModelsTypeModelInstanceModelsInstanceModel()
                self.instance_model.append(temp_model.from_map(k))
        else:
            self.instance_model = None
        return self


class DescribeDBInstancesOverviewResponseRegionsRegionModelTypeModelsTypeModel(TeaModel):
    def __init__(self, instance_date_type=None, count=None, instance_models=None):
        self.instance_date_type = instance_date_type  # type: str
        self.count = count              # type: int
        self.instance_models = instance_models  # type: DescribeDBInstancesOverviewResponseRegionsRegionModelTypeModelsTypeModelInstanceModels

    def validate(self):
        self.validate_required(self.instance_date_type, 'instance_date_type')
        self.validate_required(self.count, 'count')
        self.validate_required(self.instance_models, 'instance_models')
        if self.instance_models:
            self.instance_models.validate()

    def to_map(self):
        result = {}
        result['InstanceDateType'] = self.instance_date_type
        result['Count'] = self.count
        if self.instance_models is not None:
            result['InstanceModels'] = self.instance_models.to_map()
        else:
            result['InstanceModels'] = None
        return result

    def from_map(self, map={}):
        self.instance_date_type = map.get('InstanceDateType')
        self.count = map.get('Count')
        if map.get('InstanceModels') is not None:
            temp_model = DescribeDBInstancesOverviewResponseRegionsRegionModelTypeModelsTypeModelInstanceModels()
            self.instance_models = temp_model.from_map(map['InstanceModels'])
        else:
            self.instance_models = None
        return self


class DescribeDBInstancesOverviewResponseRegionsRegionModelTypeModels(TeaModel):
    def __init__(self, type_model=None):
        self.type_model = type_model    # type: List[DescribeDBInstancesOverviewResponseRegionsRegionModelTypeModelsTypeModel]

    def validate(self):
        self.validate_required(self.type_model, 'type_model')
        if self.type_model:
            for k in self.type_model:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TypeModel'] = []
        if self.type_model is not None:
            for k in self.type_model:
                result['TypeModel'].append(k.to_map() if k else None)
        else:
            result['TypeModel'] = None
        return result

    def from_map(self, map={}):
        self.type_model = []
        if map.get('TypeModel') is not None:
            for k in map.get('TypeModel'):
                temp_model = DescribeDBInstancesOverviewResponseRegionsRegionModelTypeModelsTypeModel()
                self.type_model.append(temp_model.from_map(k))
        else:
            self.type_model = None
        return self


class DescribeDBInstancesOverviewResponseRegionsRegionModel(TeaModel):
    def __init__(self, region=None, engine_count=None, total_count=None, type_models=None):
        self.region = region            # type: str
        self.engine_count = engine_count  # type: str
        self.total_count = total_count  # type: int
        self.type_models = type_models  # type: DescribeDBInstancesOverviewResponseRegionsRegionModelTypeModels

    def validate(self):
        self.validate_required(self.region, 'region')
        self.validate_required(self.engine_count, 'engine_count')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.type_models, 'type_models')
        if self.type_models:
            self.type_models.validate()

    def to_map(self):
        result = {}
        result['Region'] = self.region
        result['EngineCount'] = self.engine_count
        result['TotalCount'] = self.total_count
        if self.type_models is not None:
            result['TypeModels'] = self.type_models.to_map()
        else:
            result['TypeModels'] = None
        return result

    def from_map(self, map={}):
        self.region = map.get('Region')
        self.engine_count = map.get('EngineCount')
        self.total_count = map.get('TotalCount')
        if map.get('TypeModels') is not None:
            temp_model = DescribeDBInstancesOverviewResponseRegionsRegionModelTypeModels()
            self.type_models = temp_model.from_map(map['TypeModels'])
        else:
            self.type_models = None
        return self


class DescribeDBInstancesOverviewResponseRegions(TeaModel):
    def __init__(self, region_model=None):
        self.region_model = region_model  # type: List[DescribeDBInstancesOverviewResponseRegionsRegionModel]

    def validate(self):
        self.validate_required(self.region_model, 'region_model')
        if self.region_model:
            for k in self.region_model:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RegionModel'] = []
        if self.region_model is not None:
            for k in self.region_model:
                result['RegionModel'].append(k.to_map() if k else None)
        else:
            result['RegionModel'] = None
        return result

    def from_map(self, map={}):
        self.region_model = []
        if map.get('RegionModel') is not None:
            for k in map.get('RegionModel'):
                temp_model = DescribeDBInstancesOverviewResponseRegionsRegionModel()
                self.region_model.append(temp_model.from_map(k))
        else:
            self.region_model = None
        return self


class DescribeMigrateTaskByIdRequest(TeaModel):
    def __init__(self, dbinstance_id=None, migrate_task_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.migrate_task_id = migrate_task_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.migrate_task_id, 'migrate_task_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['MigrateTaskId'] = self.migrate_task_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.migrate_task_id = map.get('MigrateTaskId')
        return self


class DescribeMigrateTaskByIdResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_name=None, dbname=None, migrate_task_id=None, create_time=None,
                 end_time=None, backup_mode=None, status=None, is_dbreplaced=None, description=None):
        self.request_id = request_id    # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.dbname = dbname            # type: str
        self.migrate_task_id = migrate_task_id  # type: str
        self.create_time = create_time  # type: str
        self.end_time = end_time        # type: str
        self.backup_mode = backup_mode  # type: str
        self.status = status            # type: str
        self.is_dbreplaced = is_dbreplaced  # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_name, 'dbinstance_name')
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.migrate_task_id, 'migrate_task_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.backup_mode, 'backup_mode')
        self.validate_required(self.status, 'status')
        self.validate_required(self.is_dbreplaced, 'is_dbreplaced')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceName'] = self.dbinstance_name
        result['DBName'] = self.dbname
        result['MigrateTaskId'] = self.migrate_task_id
        result['CreateTime'] = self.create_time
        result['EndTime'] = self.end_time
        result['BackupMode'] = self.backup_mode
        result['Status'] = self.status
        result['IsDBReplaced'] = self.is_dbreplaced
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_name = map.get('DBInstanceName')
        self.dbname = map.get('DBName')
        self.migrate_task_id = map.get('MigrateTaskId')
        self.create_time = map.get('CreateTime')
        self.end_time = map.get('EndTime')
        self.backup_mode = map.get('BackupMode')
        self.status = map.get('Status')
        self.is_dbreplaced = map.get('IsDBReplaced')
        self.description = map.get('Description')
        return self


class DeleteBackupFileRequest(TeaModel):
    def __init__(self, region_id=None, dbinstance_id=None, backup_id=None, dbname=None, backup_time=None):
        self.region_id = region_id      # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.backup_id = backup_id      # type: str
        self.dbname = dbname            # type: str
        self.backup_time = backup_time  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DBInstanceId'] = self.dbinstance_id
        result['BackupId'] = self.backup_id
        result['DBName'] = self.dbname
        result['BackupTime'] = self.backup_time
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.backup_id = map.get('BackupId')
        self.dbname = map.get('DBName')
        self.backup_time = map.get('BackupTime')
        return self


class DeleteBackupFileResponse(TeaModel):
    def __init__(self, request_id=None, deleted_bakset_ids=None):
        self.request_id = request_id    # type: str
        self.deleted_bakset_ids = deleted_bakset_ids  # type: DeleteBackupFileResponseDeletedBaksetIds

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.deleted_bakset_ids, 'deleted_bakset_ids')
        if self.deleted_bakset_ids:
            self.deleted_bakset_ids.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.deleted_bakset_ids is not None:
            result['DeletedBaksetIds'] = self.deleted_bakset_ids.to_map()
        else:
            result['DeletedBaksetIds'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('DeletedBaksetIds') is not None:
            temp_model = DeleteBackupFileResponseDeletedBaksetIds()
            self.deleted_bakset_ids = temp_model.from_map(map['DeletedBaksetIds'])
        else:
            self.deleted_bakset_ids = None
        return self


class DeleteBackupFileResponseDeletedBaksetIds(TeaModel):
    def __init__(self, deleted_bakset_ids=None):
        self.deleted_bakset_ids = deleted_bakset_ids  # type: List[int]

    def validate(self):
        self.validate_required(self.deleted_bakset_ids, 'deleted_bakset_ids')

    def to_map(self):
        result = {}
        result['DeletedBaksetIds'] = self.deleted_bakset_ids
        return result

    def from_map(self, map={}):
        self.deleted_bakset_ids = map.get('DeletedBaksetIds')
        return self


class DescribeDetachedBackupsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, backup_id=None, backup_status=None, backup_mode=None, start_time=None,
                 end_time=None, page_size=None, page_number=None, region=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.backup_id = backup_id      # type: str
        self.backup_status = backup_status  # type: str
        self.backup_mode = backup_mode  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.region = region            # type: str

    def validate(self):
        self.validate_required(self.region, 'region')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['BackupId'] = self.backup_id
        result['BackupStatus'] = self.backup_status
        result['BackupMode'] = self.backup_mode
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['Region'] = self.region
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.backup_id = map.get('BackupId')
        self.backup_status = map.get('BackupStatus')
        self.backup_mode = map.get('BackupMode')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.region = map.get('Region')
        return self


class DescribeDetachedBackupsResponse(TeaModel):
    def __init__(self, request_id=None, total_record_count=None, page_number=None, page_record_count=None,
                 items=None):
        self.request_id = request_id    # type: str
        self.total_record_count = total_record_count  # type: str
        self.page_number = page_number  # type: str
        self.page_record_count = page_record_count  # type: str
        self.items = items              # type: DescribeDetachedBackupsResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalRecordCount'] = self.total_record_count
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeDetachedBackupsResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeDetachedBackupsResponseItemsBackup(TeaModel):
    def __init__(self, backup_id=None, dbinstance_id=None, backup_status=None, backup_start_time=None,
                 backup_end_time=None, backup_type=None, backup_mode=None, backup_method=None, backup_download_url=None,
                 backup_intranet_download_url=None, backup_size=None, host_instance_id=None, store_status=None, meta_status=None,
                 consistent_time=None, is_avail=None):
        self.backup_id = backup_id      # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.backup_status = backup_status  # type: str
        self.backup_start_time = backup_start_time  # type: str
        self.backup_end_time = backup_end_time  # type: str
        self.backup_type = backup_type  # type: str
        self.backup_mode = backup_mode  # type: str
        self.backup_method = backup_method  # type: str
        self.backup_download_url = backup_download_url  # type: str
        self.backup_intranet_download_url = backup_intranet_download_url  # type: str
        self.backup_size = backup_size  # type: int
        self.host_instance_id = host_instance_id  # type: str
        self.store_status = store_status  # type: str
        self.meta_status = meta_status  # type: str
        self.consistent_time = consistent_time  # type: int
        self.is_avail = is_avail        # type: int

    def validate(self):
        self.validate_required(self.backup_id, 'backup_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.backup_status, 'backup_status')
        self.validate_required(self.backup_start_time, 'backup_start_time')
        self.validate_required(self.backup_end_time, 'backup_end_time')
        self.validate_required(self.backup_type, 'backup_type')
        self.validate_required(self.backup_mode, 'backup_mode')
        self.validate_required(self.backup_method, 'backup_method')
        self.validate_required(self.backup_download_url, 'backup_download_url')
        self.validate_required(self.backup_intranet_download_url, 'backup_intranet_download_url')
        self.validate_required(self.backup_size, 'backup_size')
        self.validate_required(self.host_instance_id, 'host_instance_id')
        self.validate_required(self.store_status, 'store_status')
        self.validate_required(self.meta_status, 'meta_status')
        self.validate_required(self.consistent_time, 'consistent_time')
        self.validate_required(self.is_avail, 'is_avail')

    def to_map(self):
        result = {}
        result['BackupId'] = self.backup_id
        result['DBInstanceId'] = self.dbinstance_id
        result['BackupStatus'] = self.backup_status
        result['BackupStartTime'] = self.backup_start_time
        result['BackupEndTime'] = self.backup_end_time
        result['BackupType'] = self.backup_type
        result['BackupMode'] = self.backup_mode
        result['BackupMethod'] = self.backup_method
        result['BackupDownloadURL'] = self.backup_download_url
        result['BackupIntranetDownloadURL'] = self.backup_intranet_download_url
        result['BackupSize'] = self.backup_size
        result['HostInstanceID'] = self.host_instance_id
        result['StoreStatus'] = self.store_status
        result['MetaStatus'] = self.meta_status
        result['ConsistentTime'] = self.consistent_time
        result['IsAvail'] = self.is_avail
        return result

    def from_map(self, map={}):
        self.backup_id = map.get('BackupId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.backup_status = map.get('BackupStatus')
        self.backup_start_time = map.get('BackupStartTime')
        self.backup_end_time = map.get('BackupEndTime')
        self.backup_type = map.get('BackupType')
        self.backup_mode = map.get('BackupMode')
        self.backup_method = map.get('BackupMethod')
        self.backup_download_url = map.get('BackupDownloadURL')
        self.backup_intranet_download_url = map.get('BackupIntranetDownloadURL')
        self.backup_size = map.get('BackupSize')
        self.host_instance_id = map.get('HostInstanceID')
        self.store_status = map.get('StoreStatus')
        self.meta_status = map.get('MetaStatus')
        self.consistent_time = map.get('ConsistentTime')
        self.is_avail = map.get('IsAvail')
        return self


class DescribeDetachedBackupsResponseItems(TeaModel):
    def __init__(self, backup=None):
        self.backup = backup            # type: List[DescribeDetachedBackupsResponseItemsBackup]

    def validate(self):
        self.validate_required(self.backup, 'backup')
        if self.backup:
            for k in self.backup:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Backup'] = []
        if self.backup is not None:
            for k in self.backup:
                result['Backup'].append(k.to_map() if k else None)
        else:
            result['Backup'] = None
        return result

    def from_map(self, map={}):
        self.backup = []
        if map.get('Backup') is not None:
            for k in map.get('Backup'):
                temp_model = DescribeDetachedBackupsResponseItemsBackup()
                self.backup.append(temp_model.from_map(k))
        else:
            self.backup = None
        return self


class EvaluateDedicatedHostInstanceResourceRequest(TeaModel):
    def __init__(self, region_id=None, dedicated_host_group_id=None, disk_type=None, disk_size=None,
                 instance_class_names=None, engine=None, engine_version=None):
        self.region_id = region_id      # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.disk_type = disk_type      # type: str
        self.disk_size = disk_size      # type: str
        self.instance_class_names = instance_class_names  # type: str
        self.engine = engine            # type: str
        self.engine_version = engine_version  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.dedicated_host_group_id, 'dedicated_host_group_id')
        self.validate_required(self.instance_class_names, 'instance_class_names')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['DiskType'] = self.disk_type
        result['DiskSize'] = self.disk_size
        result['InstanceClassNames'] = self.instance_class_names
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.disk_type = map.get('DiskType')
        self.disk_size = map.get('DiskSize')
        self.instance_class_names = map.get('InstanceClassNames')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        return self


class EvaluateDedicatedHostInstanceResourceResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_class=None, available=None):
        self.request_id = request_id    # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.available = available      # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_class, 'dbinstance_class')
        self.validate_required(self.available, 'available')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceClass'] = self.dbinstance_class
        result['Available'] = self.available
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_class = map.get('DBInstanceClass')
        self.available = map.get('Available')
        return self


class DescribeAvailableDedicatedHostClassesRequest(TeaModel):
    def __init__(self, region_id=None, zone_id=None, storage_type=None):
        self.region_id = region_id      # type: str
        self.zone_id = zone_id          # type: str
        self.storage_type = storage_type  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.zone_id, 'zone_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ZoneId'] = self.zone_id
        result['StorageType'] = self.storage_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.zone_id = map.get('ZoneId')
        self.storage_type = map.get('StorageType')
        return self


class DescribeAvailableDedicatedHostClassesResponse(TeaModel):
    def __init__(self, request_id=None, host_classes=None):
        self.request_id = request_id    # type: str
        self.host_classes = host_classes  # type: DescribeAvailableDedicatedHostClassesResponseHostClasses

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.host_classes, 'host_classes')
        if self.host_classes:
            self.host_classes.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.host_classes is not None:
            result['HostClasses'] = self.host_classes.to_map()
        else:
            result['HostClasses'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('HostClasses') is not None:
            temp_model = DescribeAvailableDedicatedHostClassesResponseHostClasses()
            self.host_classes = temp_model.from_map(map['HostClasses'])
        else:
            self.host_classes = None
        return self


class DescribeAvailableDedicatedHostClassesResponseHostClassesHostClasses(TeaModel):
    def __init__(self, host_class_name=None, description=None):
        self.host_class_name = host_class_name  # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.host_class_name, 'host_class_name')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        result['HostClassName'] = self.host_class_name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.host_class_name = map.get('HostClassName')
        self.description = map.get('Description')
        return self


class DescribeAvailableDedicatedHostClassesResponseHostClasses(TeaModel):
    def __init__(self, host_classes=None):
        self.host_classes = host_classes  # type: List[DescribeAvailableDedicatedHostClassesResponseHostClassesHostClasses]

    def validate(self):
        self.validate_required(self.host_classes, 'host_classes')
        if self.host_classes:
            for k in self.host_classes:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['HostClasses'] = []
        if self.host_classes is not None:
            for k in self.host_classes:
                result['HostClasses'].append(k.to_map() if k else None)
        else:
            result['HostClasses'] = None
        return result

    def from_map(self, map={}):
        self.host_classes = []
        if map.get('HostClasses') is not None:
            for k in map.get('HostClasses'):
                temp_model = DescribeAvailableDedicatedHostClassesResponseHostClassesHostClasses()
                self.host_classes.append(temp_model.from_map(k))
        else:
            self.host_classes = None
        return self


class DescribeAvailableDedicatedHostZonesRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        return self


class DescribeAvailableDedicatedHostZonesResponse(TeaModel):
    def __init__(self, request_id=None, zones=None):
        self.request_id = request_id    # type: str
        self.zones = zones              # type: DescribeAvailableDedicatedHostZonesResponseZones

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.zones, 'zones')
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        else:
            result['Zones'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Zones') is not None:
            temp_model = DescribeAvailableDedicatedHostZonesResponseZones()
            self.zones = temp_model.from_map(map['Zones'])
        else:
            self.zones = None
        return self


class DescribeAvailableDedicatedHostZonesResponseZonesDedicatedHostZones(TeaModel):
    def __init__(self, zone_id=None, description=None):
        self.zone_id = zone_id          # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        result['ZoneId'] = self.zone_id
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.zone_id = map.get('ZoneId')
        self.description = map.get('Description')
        return self


class DescribeAvailableDedicatedHostZonesResponseZones(TeaModel):
    def __init__(self, dedicated_host_zones=None):
        self.dedicated_host_zones = dedicated_host_zones  # type: List[DescribeAvailableDedicatedHostZonesResponseZonesDedicatedHostZones]

    def validate(self):
        self.validate_required(self.dedicated_host_zones, 'dedicated_host_zones')
        if self.dedicated_host_zones:
            for k in self.dedicated_host_zones:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DedicatedHostZones'] = []
        if self.dedicated_host_zones is not None:
            for k in self.dedicated_host_zones:
                result['DedicatedHostZones'].append(k.to_map() if k else None)
        else:
            result['DedicatedHostZones'] = None
        return result

    def from_map(self, map={}):
        self.dedicated_host_zones = []
        if map.get('DedicatedHostZones') is not None:
            for k in map.get('DedicatedHostZones'):
                temp_model = DescribeAvailableDedicatedHostZonesResponseZonesDedicatedHostZones()
                self.dedicated_host_zones.append(temp_model.from_map(k))
        else:
            self.dedicated_host_zones = None
        return self


class ReleaseInstanceConnectionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, current_connection_string=None, instance_network_type=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.current_connection_string = current_connection_string  # type: str
        self.instance_network_type = instance_network_type  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.current_connection_string, 'current_connection_string')
        self.validate_required(self.instance_network_type, 'instance_network_type')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['CurrentConnectionString'] = self.current_connection_string
        result['InstanceNetworkType'] = self.instance_network_type
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.current_connection_string = map.get('CurrentConnectionString')
        self.instance_network_type = map.get('InstanceNetworkType')
        return self


class ReleaseInstanceConnectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class UnlockAccountRequest(TeaModel):
    def __init__(self, dbinstance_id=None, account_name=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.account_name, 'account_name')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['AccountName'] = self.account_name
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.account_name = map.get('AccountName')
        return self


class UnlockAccountResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class LockAccountRequest(TeaModel):
    def __init__(self, dbinstance_id=None, account_name=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.account_name, 'account_name')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['AccountName'] = self.account_name
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.account_name = map.get('AccountName')
        return self


class LockAccountResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, next_token=None, resource_id=None, tag=None):
        self.region_id = region_id      # type: str
        self.resource_type = resource_type  # type: str
        self.next_token = next_token    # type: str
        self.resource_id = resource_id  # type: List[str]
        self.tag = tag                  # type: List[ListTagResourcesRequestTag]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ResourceType'] = self.resource_type
        result['NextToken'] = self.next_token
        result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.resource_type = map.get('ResourceType')
        self.next_token = map.get('NextToken')
        self.resource_id = map.get('ResourceId')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, request_id=None, next_token=None, tag_resources=None):
        self.request_id = request_id    # type: str
        self.next_token = next_token    # type: str
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseTagResources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.tag_resources, 'tag_resources')
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['NextToken'] = self.next_token
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        else:
            result['TagResources'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.next_token = map.get('NextToken')
        if map.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseTagResources()
            self.tag_resources = temp_model.from_map(map['TagResources'])
        else:
            self.tag_resources = None
        return self


class ListTagResourcesResponseTagResourcesTagResource(TeaModel):
    def __init__(self, tag_key=None, tag_value=None, resource_type=None, resource_id=None):
        self.tag_key = tag_key          # type: str
        self.tag_value = tag_value      # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['TagKey'] = self.tag_key
        result['TagValue'] = self.tag_value
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.tag_key = map.get('TagKey')
        self.tag_value = map.get('TagValue')
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        return self


class ListTagResourcesResponseTagResources(TeaModel):
    def __init__(self, tag_resource=None):
        self.tag_resource = tag_resource  # type: List[ListTagResourcesResponseTagResourcesTagResource]

    def validate(self):
        self.validate_required(self.tag_resource, 'tag_resource')
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        else:
            result['TagResource'] = None
        return result

    def from_map(self, map={}):
        self.tag_resource = []
        if map.get('TagResource') is not None:
            for k in map.get('TagResource'):
                temp_model = ListTagResourcesResponseTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        else:
            self.tag_resource = None
        return self


class TagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, resource_id=None, tag=None):
        self.region_id = region_id      # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: List[str]
        self.tag = tag                  # type: List[TagResourcesRequestTag]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        self.validate_required(self.key, 'key')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, all=None, resource_id=None, tag_key=None):
        self.region_id = region_id      # type: str
        self.resource_type = resource_type  # type: str
        self.all = all                  # type: bool
        self.resource_id = resource_id  # type: List[str]
        self.tag_key = tag_key          # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ResourceType'] = self.resource_type
        result['All'] = self.all
        result['ResourceId'] = self.resource_id
        result['TagKey'] = self.tag_key
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.resource_type = map.get('ResourceType')
        self.all = map.get('All')
        self.resource_id = map.get('ResourceId')
        self.tag_key = map.get('TagKey')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeDedicatedHostGroupsRequest(TeaModel):
    def __init__(self, region_id=None, dedicated_host_group_id=None, image_category=None):
        self.region_id = region_id      # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.image_category = image_category  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['ImageCategory'] = self.image_category
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.image_category = map.get('ImageCategory')
        return self


class DescribeDedicatedHostGroupsResponse(TeaModel):
    def __init__(self, request_id=None, dedicated_host_groups=None):
        self.request_id = request_id    # type: str
        self.dedicated_host_groups = dedicated_host_groups  # type: DescribeDedicatedHostGroupsResponseDedicatedHostGroups

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dedicated_host_groups, 'dedicated_host_groups')
        if self.dedicated_host_groups:
            self.dedicated_host_groups.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.dedicated_host_groups is not None:
            result['DedicatedHostGroups'] = self.dedicated_host_groups.to_map()
        else:
            result['DedicatedHostGroups'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('DedicatedHostGroups') is not None:
            temp_model = DescribeDedicatedHostGroupsResponseDedicatedHostGroups()
            self.dedicated_host_groups = temp_model.from_map(map['DedicatedHostGroups'])
        else:
            self.dedicated_host_groups = None
        return self


class DescribeDedicatedHostGroupsResponseDedicatedHostGroupsDedicatedHostGroupsZoneIDList(TeaModel):
    def __init__(self, zone_idlist=None):
        # ZoneIDList
        self.zone_idlist = zone_idlist  # type: List[str]

    def validate(self):
        self.validate_required(self.zone_idlist, 'zone_idlist')

    def to_map(self):
        result = {}
        result['ZoneIDList'] = self.zone_idlist
        return result

    def from_map(self, map={}):
        self.zone_idlist = map.get('ZoneIDList')
        return self


class DescribeDedicatedHostGroupsResponseDedicatedHostGroupsDedicatedHostGroups(TeaModel):
    def __init__(self, dedicated_host_group_id=None, dedicated_host_group_desc=None, cpu_allocation_ratio=None,
                 mem_allocation_ratio=None, disk_allocation_ratio=None, allocation_policy=None, host_replace_policy=None,
                 create_time=None, vpcid=None, host_number=None, instance_number=None, engine=None, text=None,
                 dedicated_host_count_group_by_host_type=None, bastion_instance_id=None, open_permission=None, mem_utility=None, mem_used_amount=None,
                 disk_utility=None, disk_used_amount=None, cpu_allocate_ration=None, cpu_allocated_amount=None,
                 mem_allocate_ration=None, mem_allocated_amount=None, disk_allocate_ration=None, disk_allocated_amount=None,
                 zone_idlist=None):
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.dedicated_host_group_desc = dedicated_host_group_desc  # type: str
        self.cpu_allocation_ratio = cpu_allocation_ratio  # type: int
        self.mem_allocation_ratio = mem_allocation_ratio  # type: int
        self.disk_allocation_ratio = disk_allocation_ratio  # type: int
        self.allocation_policy = allocation_policy  # type: str
        self.host_replace_policy = host_replace_policy  # type: str
        self.create_time = create_time  # type: str
        self.vpcid = vpcid              # type: str
        self.host_number = host_number  # type: int
        self.instance_number = instance_number  # type: int
        self.engine = engine            # type: str
        self.text = text                # type: str
        self.dedicated_host_count_group_by_host_type = dedicated_host_count_group_by_host_type  # type: Dict[str, Any]
        self.bastion_instance_id = bastion_instance_id  # type: str
        self.open_permission = open_permission  # type: str
        self.mem_utility = mem_utility  # type: float
        self.mem_used_amount = mem_used_amount  # type: float
        self.disk_utility = disk_utility  # type: float
        self.disk_used_amount = disk_used_amount  # type: float
        self.cpu_allocate_ration = cpu_allocate_ration  # type: float
        self.cpu_allocated_amount = cpu_allocated_amount  # type: float
        self.mem_allocate_ration = mem_allocate_ration  # type: float
        self.mem_allocated_amount = mem_allocated_amount  # type: float
        self.disk_allocate_ration = disk_allocate_ration  # type: float
        self.disk_allocated_amount = disk_allocated_amount  # type: float
        self.zone_idlist = zone_idlist  # type: DescribeDedicatedHostGroupsResponseDedicatedHostGroupsDedicatedHostGroupsZoneIDList

    def validate(self):
        self.validate_required(self.dedicated_host_group_id, 'dedicated_host_group_id')
        self.validate_required(self.dedicated_host_group_desc, 'dedicated_host_group_desc')
        self.validate_required(self.cpu_allocation_ratio, 'cpu_allocation_ratio')
        self.validate_required(self.mem_allocation_ratio, 'mem_allocation_ratio')
        self.validate_required(self.disk_allocation_ratio, 'disk_allocation_ratio')
        self.validate_required(self.allocation_policy, 'allocation_policy')
        self.validate_required(self.host_replace_policy, 'host_replace_policy')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.vpcid, 'vpcid')
        self.validate_required(self.host_number, 'host_number')
        self.validate_required(self.instance_number, 'instance_number')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.text, 'text')
        self.validate_required(self.dedicated_host_count_group_by_host_type, 'dedicated_host_count_group_by_host_type')
        self.validate_required(self.bastion_instance_id, 'bastion_instance_id')
        self.validate_required(self.open_permission, 'open_permission')
        self.validate_required(self.mem_utility, 'mem_utility')
        self.validate_required(self.mem_used_amount, 'mem_used_amount')
        self.validate_required(self.disk_utility, 'disk_utility')
        self.validate_required(self.disk_used_amount, 'disk_used_amount')
        self.validate_required(self.cpu_allocate_ration, 'cpu_allocate_ration')
        self.validate_required(self.cpu_allocated_amount, 'cpu_allocated_amount')
        self.validate_required(self.mem_allocate_ration, 'mem_allocate_ration')
        self.validate_required(self.mem_allocated_amount, 'mem_allocated_amount')
        self.validate_required(self.disk_allocate_ration, 'disk_allocate_ration')
        self.validate_required(self.disk_allocated_amount, 'disk_allocated_amount')
        self.validate_required(self.zone_idlist, 'zone_idlist')
        if self.zone_idlist:
            self.zone_idlist.validate()

    def to_map(self):
        result = {}
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['DedicatedHostGroupDesc'] = self.dedicated_host_group_desc
        result['CpuAllocationRatio'] = self.cpu_allocation_ratio
        result['MemAllocationRatio'] = self.mem_allocation_ratio
        result['DiskAllocationRatio'] = self.disk_allocation_ratio
        result['AllocationPolicy'] = self.allocation_policy
        result['HostReplacePolicy'] = self.host_replace_policy
        result['CreateTime'] = self.create_time
        result['VPCId'] = self.vpcid
        result['HostNumber'] = self.host_number
        result['InstanceNumber'] = self.instance_number
        result['Engine'] = self.engine
        result['Text'] = self.text
        result['DedicatedHostCountGroupByHostType'] = self.dedicated_host_count_group_by_host_type
        result['BastionInstanceId'] = self.bastion_instance_id
        result['OpenPermission'] = self.open_permission
        result['MemUtility'] = self.mem_utility
        result['MemUsedAmount'] = self.mem_used_amount
        result['DiskUtility'] = self.disk_utility
        result['DiskUsedAmount'] = self.disk_used_amount
        result['CpuAllocateRation'] = self.cpu_allocate_ration
        result['CpuAllocatedAmount'] = self.cpu_allocated_amount
        result['MemAllocateRation'] = self.mem_allocate_ration
        result['MemAllocatedAmount'] = self.mem_allocated_amount
        result['DiskAllocateRation'] = self.disk_allocate_ration
        result['DiskAllocatedAmount'] = self.disk_allocated_amount
        if self.zone_idlist is not None:
            result['ZoneIDList'] = self.zone_idlist.to_map()
        else:
            result['ZoneIDList'] = None
        return result

    def from_map(self, map={}):
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.dedicated_host_group_desc = map.get('DedicatedHostGroupDesc')
        self.cpu_allocation_ratio = map.get('CpuAllocationRatio')
        self.mem_allocation_ratio = map.get('MemAllocationRatio')
        self.disk_allocation_ratio = map.get('DiskAllocationRatio')
        self.allocation_policy = map.get('AllocationPolicy')
        self.host_replace_policy = map.get('HostReplacePolicy')
        self.create_time = map.get('CreateTime')
        self.vpcid = map.get('VPCId')
        self.host_number = map.get('HostNumber')
        self.instance_number = map.get('InstanceNumber')
        self.engine = map.get('Engine')
        self.text = map.get('Text')
        self.dedicated_host_count_group_by_host_type = map.get('DedicatedHostCountGroupByHostType')
        self.bastion_instance_id = map.get('BastionInstanceId')
        self.open_permission = map.get('OpenPermission')
        self.mem_utility = map.get('MemUtility')
        self.mem_used_amount = map.get('MemUsedAmount')
        self.disk_utility = map.get('DiskUtility')
        self.disk_used_amount = map.get('DiskUsedAmount')
        self.cpu_allocate_ration = map.get('CpuAllocateRation')
        self.cpu_allocated_amount = map.get('CpuAllocatedAmount')
        self.mem_allocate_ration = map.get('MemAllocateRation')
        self.mem_allocated_amount = map.get('MemAllocatedAmount')
        self.disk_allocate_ration = map.get('DiskAllocateRation')
        self.disk_allocated_amount = map.get('DiskAllocatedAmount')
        if map.get('ZoneIDList') is not None:
            temp_model = DescribeDedicatedHostGroupsResponseDedicatedHostGroupsDedicatedHostGroupsZoneIDList()
            self.zone_idlist = temp_model.from_map(map['ZoneIDList'])
        else:
            self.zone_idlist = None
        return self


class DescribeDedicatedHostGroupsResponseDedicatedHostGroups(TeaModel):
    def __init__(self, dedicated_host_groups=None):
        self.dedicated_host_groups = dedicated_host_groups  # type: List[DescribeDedicatedHostGroupsResponseDedicatedHostGroupsDedicatedHostGroups]

    def validate(self):
        self.validate_required(self.dedicated_host_groups, 'dedicated_host_groups')
        if self.dedicated_host_groups:
            for k in self.dedicated_host_groups:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DedicatedHostGroups'] = []
        if self.dedicated_host_groups is not None:
            for k in self.dedicated_host_groups:
                result['DedicatedHostGroups'].append(k.to_map() if k else None)
        else:
            result['DedicatedHostGroups'] = None
        return result

    def from_map(self, map={}):
        self.dedicated_host_groups = []
        if map.get('DedicatedHostGroups') is not None:
            for k in map.get('DedicatedHostGroups'):
                temp_model = DescribeDedicatedHostGroupsResponseDedicatedHostGroupsDedicatedHostGroups()
                self.dedicated_host_groups.append(temp_model.from_map(k))
        else:
            self.dedicated_host_groups = None
        return self


class CreateDedicatedHostGroupRequest(TeaModel):
    def __init__(self, region_id=None, engine=None, cpu_allocation_ratio=None, mem_allocation_ratio=None,
                 disk_allocation_ratio=None, allocation_policy=None, vpcid=None, host_replace_policy=None, client_token=None,
                 open_permission=None):
        self.region_id = region_id      # type: str
        self.engine = engine            # type: str
        self.cpu_allocation_ratio = cpu_allocation_ratio  # type: int
        self.mem_allocation_ratio = mem_allocation_ratio  # type: int
        self.disk_allocation_ratio = disk_allocation_ratio  # type: int
        self.allocation_policy = allocation_policy  # type: str
        self.vpcid = vpcid              # type: str
        self.host_replace_policy = host_replace_policy  # type: str
        self.client_token = client_token  # type: str
        self.open_permission = open_permission  # type: int

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.vpcid, 'vpcid')
        self.validate_required(self.client_token, 'client_token')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Engine'] = self.engine
        result['CpuAllocationRatio'] = self.cpu_allocation_ratio
        result['MemAllocationRatio'] = self.mem_allocation_ratio
        result['DiskAllocationRatio'] = self.disk_allocation_ratio
        result['AllocationPolicy'] = self.allocation_policy
        result['VPCId'] = self.vpcid
        result['HostReplacePolicy'] = self.host_replace_policy
        result['ClientToken'] = self.client_token
        result['OpenPermission'] = self.open_permission
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.engine = map.get('Engine')
        self.cpu_allocation_ratio = map.get('CpuAllocationRatio')
        self.mem_allocation_ratio = map.get('MemAllocationRatio')
        self.disk_allocation_ratio = map.get('DiskAllocationRatio')
        self.allocation_policy = map.get('AllocationPolicy')
        self.vpcid = map.get('VPCId')
        self.host_replace_policy = map.get('HostReplacePolicy')
        self.client_token = map.get('ClientToken')
        self.open_permission = map.get('OpenPermission')
        return self


class CreateDedicatedHostGroupResponse(TeaModel):
    def __init__(self, request_id=None, dedicated_host_group_id=None):
        self.request_id = request_id    # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dedicated_host_group_id, 'dedicated_host_group_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        return self


class DeleteDedicatedHostGroupRequest(TeaModel):
    def __init__(self, dedicated_host_group_id=None, region_id=None):
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_group_id, 'dedicated_host_group_id')

    def to_map(self):
        result = {}
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.region_id = map.get('RegionId')
        return self


class DeleteDedicatedHostGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyDedicatedHostGroupAttributeRequest(TeaModel):
    def __init__(self, region_id=None, dedicated_host_group_id=None, dedicated_host_group_desc=None,
                 cpu_allocation_ratio=None, mem_allocation_ratio=None, disk_allocation_ratio=None, allocation_policy=None,
                 host_replace_policy=None):
        self.region_id = region_id      # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.dedicated_host_group_desc = dedicated_host_group_desc  # type: str
        self.cpu_allocation_ratio = cpu_allocation_ratio  # type: int
        self.mem_allocation_ratio = mem_allocation_ratio  # type: int
        self.disk_allocation_ratio = disk_allocation_ratio  # type: int
        self.allocation_policy = allocation_policy  # type: str
        self.host_replace_policy = host_replace_policy  # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_group_id, 'dedicated_host_group_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['DedicatedHostGroupDesc'] = self.dedicated_host_group_desc
        result['CpuAllocationRatio'] = self.cpu_allocation_ratio
        result['MemAllocationRatio'] = self.mem_allocation_ratio
        result['DiskAllocationRatio'] = self.disk_allocation_ratio
        result['AllocationPolicy'] = self.allocation_policy
        result['HostReplacePolicy'] = self.host_replace_policy
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.dedicated_host_group_desc = map.get('DedicatedHostGroupDesc')
        self.cpu_allocation_ratio = map.get('CpuAllocationRatio')
        self.mem_allocation_ratio = map.get('MemAllocationRatio')
        self.disk_allocation_ratio = map.get('DiskAllocationRatio')
        self.allocation_policy = map.get('AllocationPolicy')
        self.host_replace_policy = map.get('HostReplacePolicy')
        return self


class ModifyDedicatedHostGroupAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class RestartDedicatedHostRequest(TeaModel):
    def __init__(self, region_id=None, dedicated_host_id=None, failover_mode=None):
        self.region_id = region_id      # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.failover_mode = failover_mode  # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_id, 'dedicated_host_id')
        self.validate_required(self.failover_mode, 'failover_mode')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DedicatedHostId'] = self.dedicated_host_id
        result['FailoverMode'] = self.failover_mode
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dedicated_host_id = map.get('DedicatedHostId')
        self.failover_mode = map.get('FailoverMode')
        return self


class RestartDedicatedHostResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None, dedicated_host_id=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: int
        self.dedicated_host_id = dedicated_host_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.dedicated_host_id, 'dedicated_host_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        result['DedicatedHostId'] = self.dedicated_host_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        self.dedicated_host_id = map.get('DedicatedHostId')
        return self


class ReplaceDedicatedHostRequest(TeaModel):
    def __init__(self, region_id=None, dedicated_host_id=None, failover_mode=None):
        self.region_id = region_id      # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.failover_mode = failover_mode  # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_id, 'dedicated_host_id')
        self.validate_required(self.failover_mode, 'failover_mode')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DedicatedHostId'] = self.dedicated_host_id
        result['FailoverMode'] = self.failover_mode
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dedicated_host_id = map.get('DedicatedHostId')
        self.failover_mode = map.get('FailoverMode')
        return self


class ReplaceDedicatedHostResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None, dedicated_host_id=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: int
        self.dedicated_host_id = dedicated_host_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.dedicated_host_id, 'dedicated_host_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        result['DedicatedHostId'] = self.dedicated_host_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        self.dedicated_host_id = map.get('DedicatedHostId')
        return self


class DescribeDedicatedHostsRequest(TeaModel):
    def __init__(self, region_id=None, dedicated_host_group_id=None, order_id=None, host_type=None,
                 host_status=None, allocation_status=None, zone_id=None, dedicated_host_id=None):
        self.region_id = region_id      # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.order_id = order_id        # type: int
        self.host_type = host_type      # type: str
        self.host_status = host_status  # type: str
        self.allocation_status = allocation_status  # type: str
        self.zone_id = zone_id          # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['OrderId'] = self.order_id
        result['HostType'] = self.host_type
        result['HostStatus'] = self.host_status
        result['AllocationStatus'] = self.allocation_status
        result['ZoneId'] = self.zone_id
        result['DedicatedHostId'] = self.dedicated_host_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.order_id = map.get('OrderId')
        self.host_type = map.get('HostType')
        self.host_status = map.get('HostStatus')
        self.allocation_status = map.get('AllocationStatus')
        self.zone_id = map.get('ZoneId')
        self.dedicated_host_id = map.get('DedicatedHostId')
        return self


class DescribeDedicatedHostsResponse(TeaModel):
    def __init__(self, request_id=None, dedicated_host_group_id=None, dedicated_hosts=None):
        self.request_id = request_id    # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.dedicated_hosts = dedicated_hosts  # type: DescribeDedicatedHostsResponseDedicatedHosts

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dedicated_host_group_id, 'dedicated_host_group_id')
        self.validate_required(self.dedicated_hosts, 'dedicated_hosts')
        if self.dedicated_hosts:
            self.dedicated_hosts.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_hosts is not None:
            result['DedicatedHosts'] = self.dedicated_hosts.to_map()
        else:
            result['DedicatedHosts'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        if map.get('DedicatedHosts') is not None:
            temp_model = DescribeDedicatedHostsResponseDedicatedHosts()
            self.dedicated_hosts = temp_model.from_map(map['DedicatedHosts'])
        else:
            self.dedicated_hosts = None
        return self


class DescribeDedicatedHostsResponseDedicatedHostsDedicatedHosts(TeaModel):
    def __init__(self, host_name=None, host_status=None, instance_number=None, cpuallocation_ratio=None,
                 mem_allocation_ratio=None, disk_allocation_ratio=None, vpcid=None, v_switch_id=None, zone_id=None, ipaddress=None,
                 host_class=None, created_time=None, dedicated_host_id=None, allocation_status=None, end_time=None,
                 host_type=None, bastion_instance_id=None, open_permission=None, account_name=None, host_cpu=None,
                 host_mem=None, host_storage=None, cpu_used=None, memory_used=None, storage_used=None, image_category=None,
                 dedicated_host_group_id=None, engine=None):
        self.host_name = host_name      # type: str
        self.host_status = host_status  # type: str
        self.instance_number = instance_number  # type: str
        self.cpuallocation_ratio = cpuallocation_ratio  # type: str
        self.mem_allocation_ratio = mem_allocation_ratio  # type: str
        self.disk_allocation_ratio = disk_allocation_ratio  # type: str
        self.vpcid = vpcid              # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.zone_id = zone_id          # type: str
        self.ipaddress = ipaddress      # type: str
        self.host_class = host_class    # type: str
        self.created_time = created_time  # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.allocation_status = allocation_status  # type: str
        self.end_time = end_time        # type: str
        self.host_type = host_type      # type: str
        self.bastion_instance_id = bastion_instance_id  # type: str
        self.open_permission = open_permission  # type: str
        self.account_name = account_name  # type: str
        self.host_cpu = host_cpu        # type: str
        self.host_mem = host_mem        # type: str
        self.host_storage = host_storage  # type: str
        self.cpu_used = cpu_used        # type: str
        self.memory_used = memory_used  # type: str
        self.storage_used = storage_used  # type: str
        self.image_category = image_category  # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.engine = engine            # type: str

    def validate(self):
        self.validate_required(self.host_name, 'host_name')
        self.validate_required(self.host_status, 'host_status')
        self.validate_required(self.instance_number, 'instance_number')
        self.validate_required(self.cpuallocation_ratio, 'cpuallocation_ratio')
        self.validate_required(self.mem_allocation_ratio, 'mem_allocation_ratio')
        self.validate_required(self.disk_allocation_ratio, 'disk_allocation_ratio')
        self.validate_required(self.vpcid, 'vpcid')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.ipaddress, 'ipaddress')
        self.validate_required(self.host_class, 'host_class')
        self.validate_required(self.created_time, 'created_time')
        self.validate_required(self.dedicated_host_id, 'dedicated_host_id')
        self.validate_required(self.allocation_status, 'allocation_status')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.host_type, 'host_type')
        self.validate_required(self.bastion_instance_id, 'bastion_instance_id')
        self.validate_required(self.open_permission, 'open_permission')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.host_cpu, 'host_cpu')
        self.validate_required(self.host_mem, 'host_mem')
        self.validate_required(self.host_storage, 'host_storage')
        self.validate_required(self.cpu_used, 'cpu_used')
        self.validate_required(self.memory_used, 'memory_used')
        self.validate_required(self.storage_used, 'storage_used')
        self.validate_required(self.image_category, 'image_category')
        self.validate_required(self.dedicated_host_group_id, 'dedicated_host_group_id')
        self.validate_required(self.engine, 'engine')

    def to_map(self):
        result = {}
        result['HostName'] = self.host_name
        result['HostStatus'] = self.host_status
        result['InstanceNumber'] = self.instance_number
        result['CPUAllocationRatio'] = self.cpuallocation_ratio
        result['MemAllocationRatio'] = self.mem_allocation_ratio
        result['DiskAllocationRatio'] = self.disk_allocation_ratio
        result['VPCId'] = self.vpcid
        result['VSwitchId'] = self.v_switch_id
        result['ZoneId'] = self.zone_id
        result['IPAddress'] = self.ipaddress
        result['HostClass'] = self.host_class
        result['CreatedTime'] = self.created_time
        result['DedicatedHostId'] = self.dedicated_host_id
        result['AllocationStatus'] = self.allocation_status
        result['EndTime'] = self.end_time
        result['HostType'] = self.host_type
        result['BastionInstanceId'] = self.bastion_instance_id
        result['OpenPermission'] = self.open_permission
        result['AccountName'] = self.account_name
        result['HostCPU'] = self.host_cpu
        result['HostMem'] = self.host_mem
        result['HostStorage'] = self.host_storage
        result['CpuUsed'] = self.cpu_used
        result['MemoryUsed'] = self.memory_used
        result['StorageUsed'] = self.storage_used
        result['ImageCategory'] = self.image_category
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['Engine'] = self.engine
        return result

    def from_map(self, map={}):
        self.host_name = map.get('HostName')
        self.host_status = map.get('HostStatus')
        self.instance_number = map.get('InstanceNumber')
        self.cpuallocation_ratio = map.get('CPUAllocationRatio')
        self.mem_allocation_ratio = map.get('MemAllocationRatio')
        self.disk_allocation_ratio = map.get('DiskAllocationRatio')
        self.vpcid = map.get('VPCId')
        self.v_switch_id = map.get('VSwitchId')
        self.zone_id = map.get('ZoneId')
        self.ipaddress = map.get('IPAddress')
        self.host_class = map.get('HostClass')
        self.created_time = map.get('CreatedTime')
        self.dedicated_host_id = map.get('DedicatedHostId')
        self.allocation_status = map.get('AllocationStatus')
        self.end_time = map.get('EndTime')
        self.host_type = map.get('HostType')
        self.bastion_instance_id = map.get('BastionInstanceId')
        self.open_permission = map.get('OpenPermission')
        self.account_name = map.get('AccountName')
        self.host_cpu = map.get('HostCPU')
        self.host_mem = map.get('HostMem')
        self.host_storage = map.get('HostStorage')
        self.cpu_used = map.get('CpuUsed')
        self.memory_used = map.get('MemoryUsed')
        self.storage_used = map.get('StorageUsed')
        self.image_category = map.get('ImageCategory')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.engine = map.get('Engine')
        return self


class DescribeDedicatedHostsResponseDedicatedHosts(TeaModel):
    def __init__(self, dedicated_hosts=None):
        self.dedicated_hosts = dedicated_hosts  # type: List[DescribeDedicatedHostsResponseDedicatedHostsDedicatedHosts]

    def validate(self):
        self.validate_required(self.dedicated_hosts, 'dedicated_hosts')
        if self.dedicated_hosts:
            for k in self.dedicated_hosts:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DedicatedHosts'] = []
        if self.dedicated_hosts is not None:
            for k in self.dedicated_hosts:
                result['DedicatedHosts'].append(k.to_map() if k else None)
        else:
            result['DedicatedHosts'] = None
        return result

    def from_map(self, map={}):
        self.dedicated_hosts = []
        if map.get('DedicatedHosts') is not None:
            for k in map.get('DedicatedHosts'):
                temp_model = DescribeDedicatedHostsResponseDedicatedHostsDedicatedHosts()
                self.dedicated_hosts.append(temp_model.from_map(k))
        else:
            self.dedicated_hosts = None
        return self


class DescribeDedicatedHostAttributeRequest(TeaModel):
    def __init__(self, region_id=None, dedicated_host_id=None, dedicated_host_group_id=None):
        self.region_id = region_id      # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_id, 'dedicated_host_id')
        self.validate_required(self.dedicated_host_group_id, 'dedicated_host_group_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DedicatedHostId'] = self.dedicated_host_id
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dedicated_host_id = map.get('DedicatedHostId')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        return self


class DescribeDedicatedHostAttributeResponse(TeaModel):
    def __init__(self, request_id=None, dedicated_host_group_id=None, dedicated_host_id=None, region_id=None,
                 zone_id=None, vpcid=None, v_switch_id=None, ipaddress=None, host_name=None, host_status=None,
                 host_class=None, host_cpu=None, host_mem=None, host_storage=None, cpuallocation_ratio=None,
                 mem_allocation_ratio=None, disk_allocation_ratio=None, instance_number=None, instance_number_master=None,
                 instance_number_slave=None, instance_number_romaster=None, instance_number_roslave=None, created_time=None,
                 expired_time=None, auto_renew=None, allocation_status=None, cpu_used=None, memory_used=None, storage_used=None,
                 host_type=None, account_name=None, open_permission=None, image_category=None):
        self.request_id = request_id    # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.region_id = region_id      # type: str
        self.zone_id = zone_id          # type: str
        self.vpcid = vpcid              # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.ipaddress = ipaddress      # type: str
        self.host_name = host_name      # type: str
        self.host_status = host_status  # type: str
        self.host_class = host_class    # type: str
        self.host_cpu = host_cpu        # type: int
        self.host_mem = host_mem        # type: int
        self.host_storage = host_storage  # type: int
        self.cpuallocation_ratio = cpuallocation_ratio  # type: str
        self.mem_allocation_ratio = mem_allocation_ratio  # type: str
        self.disk_allocation_ratio = disk_allocation_ratio  # type: str
        self.instance_number = instance_number  # type: int
        self.instance_number_master = instance_number_master  # type: int
        self.instance_number_slave = instance_number_slave  # type: int
        self.instance_number_romaster = instance_number_romaster  # type: int
        self.instance_number_roslave = instance_number_roslave  # type: int
        self.created_time = created_time  # type: str
        self.expired_time = expired_time  # type: str
        self.auto_renew = auto_renew    # type: str
        self.allocation_status = allocation_status  # type: str
        self.cpu_used = cpu_used        # type: str
        self.memory_used = memory_used  # type: str
        self.storage_used = storage_used  # type: str
        self.host_type = host_type      # type: str
        self.account_name = account_name  # type: str
        self.open_permission = open_permission  # type: str
        self.image_category = image_category  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dedicated_host_group_id, 'dedicated_host_group_id')
        self.validate_required(self.dedicated_host_id, 'dedicated_host_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.vpcid, 'vpcid')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.ipaddress, 'ipaddress')
        self.validate_required(self.host_name, 'host_name')
        self.validate_required(self.host_status, 'host_status')
        self.validate_required(self.host_class, 'host_class')
        self.validate_required(self.host_cpu, 'host_cpu')
        self.validate_required(self.host_mem, 'host_mem')
        self.validate_required(self.host_storage, 'host_storage')
        self.validate_required(self.cpuallocation_ratio, 'cpuallocation_ratio')
        self.validate_required(self.mem_allocation_ratio, 'mem_allocation_ratio')
        self.validate_required(self.disk_allocation_ratio, 'disk_allocation_ratio')
        self.validate_required(self.instance_number, 'instance_number')
        self.validate_required(self.instance_number_master, 'instance_number_master')
        self.validate_required(self.instance_number_slave, 'instance_number_slave')
        self.validate_required(self.instance_number_romaster, 'instance_number_romaster')
        self.validate_required(self.instance_number_roslave, 'instance_number_roslave')
        self.validate_required(self.created_time, 'created_time')
        self.validate_required(self.expired_time, 'expired_time')
        self.validate_required(self.auto_renew, 'auto_renew')
        self.validate_required(self.allocation_status, 'allocation_status')
        self.validate_required(self.cpu_used, 'cpu_used')
        self.validate_required(self.memory_used, 'memory_used')
        self.validate_required(self.storage_used, 'storage_used')
        self.validate_required(self.host_type, 'host_type')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.open_permission, 'open_permission')
        self.validate_required(self.image_category, 'image_category')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['DedicatedHostId'] = self.dedicated_host_id
        result['RegionId'] = self.region_id
        result['ZoneId'] = self.zone_id
        result['VPCId'] = self.vpcid
        result['VSwitchId'] = self.v_switch_id
        result['IPAddress'] = self.ipaddress
        result['HostName'] = self.host_name
        result['HostStatus'] = self.host_status
        result['HostClass'] = self.host_class
        result['HostCPU'] = self.host_cpu
        result['HostMem'] = self.host_mem
        result['HostStorage'] = self.host_storage
        result['CPUAllocationRatio'] = self.cpuallocation_ratio
        result['MemAllocationRatio'] = self.mem_allocation_ratio
        result['DiskAllocationRatio'] = self.disk_allocation_ratio
        result['InstanceNumber'] = self.instance_number
        result['InstanceNumberMaster'] = self.instance_number_master
        result['InstanceNumberSlave'] = self.instance_number_slave
        result['InstanceNumberROMaster'] = self.instance_number_romaster
        result['InstanceNumberROSlave'] = self.instance_number_roslave
        result['CreatedTime'] = self.created_time
        result['ExpiredTime'] = self.expired_time
        result['AutoRenew'] = self.auto_renew
        result['AllocationStatus'] = self.allocation_status
        result['CpuUsed'] = self.cpu_used
        result['MemoryUsed'] = self.memory_used
        result['StorageUsed'] = self.storage_used
        result['HostType'] = self.host_type
        result['AccountName'] = self.account_name
        result['OpenPermission'] = self.open_permission
        result['ImageCategory'] = self.image_category
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.dedicated_host_id = map.get('DedicatedHostId')
        self.region_id = map.get('RegionId')
        self.zone_id = map.get('ZoneId')
        self.vpcid = map.get('VPCId')
        self.v_switch_id = map.get('VSwitchId')
        self.ipaddress = map.get('IPAddress')
        self.host_name = map.get('HostName')
        self.host_status = map.get('HostStatus')
        self.host_class = map.get('HostClass')
        self.host_cpu = map.get('HostCPU')
        self.host_mem = map.get('HostMem')
        self.host_storage = map.get('HostStorage')
        self.cpuallocation_ratio = map.get('CPUAllocationRatio')
        self.mem_allocation_ratio = map.get('MemAllocationRatio')
        self.disk_allocation_ratio = map.get('DiskAllocationRatio')
        self.instance_number = map.get('InstanceNumber')
        self.instance_number_master = map.get('InstanceNumberMaster')
        self.instance_number_slave = map.get('InstanceNumberSlave')
        self.instance_number_romaster = map.get('InstanceNumberROMaster')
        self.instance_number_roslave = map.get('InstanceNumberROSlave')
        self.created_time = map.get('CreatedTime')
        self.expired_time = map.get('ExpiredTime')
        self.auto_renew = map.get('AutoRenew')
        self.allocation_status = map.get('AllocationStatus')
        self.cpu_used = map.get('CpuUsed')
        self.memory_used = map.get('MemoryUsed')
        self.storage_used = map.get('StorageUsed')
        self.host_type = map.get('HostType')
        self.account_name = map.get('AccountName')
        self.open_permission = map.get('OpenPermission')
        self.image_category = map.get('ImageCategory')
        return self


class ClearDedicatedHostRequest(TeaModel):
    def __init__(self, region_id=None, dedicated_host_id=None, failover_mode=None):
        self.region_id = region_id      # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.failover_mode = failover_mode  # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_id, 'dedicated_host_id')
        self.validate_required(self.failover_mode, 'failover_mode')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DedicatedHostId'] = self.dedicated_host_id
        result['FailoverMode'] = self.failover_mode
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dedicated_host_id = map.get('DedicatedHostId')
        self.failover_mode = map.get('FailoverMode')
        return self


class ClearDedicatedHostResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None, dedicated_host_id=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.dedicated_host_id, 'dedicated_host_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        result['DedicatedHostId'] = self.dedicated_host_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        self.dedicated_host_id = map.get('DedicatedHostId')
        return self


class ModifyDedicatedHostAttributeRequest(TeaModel):
    def __init__(self, region_id=None, dedicated_host_id=None, host_name=None, allocation_status=None):
        self.region_id = region_id      # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.host_name = host_name      # type: str
        self.allocation_status = allocation_status  # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_id, 'dedicated_host_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DedicatedHostId'] = self.dedicated_host_id
        result['HostName'] = self.host_name
        result['AllocationStatus'] = self.allocation_status
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dedicated_host_id = map.get('DedicatedHostId')
        self.host_name = map.get('HostName')
        self.allocation_status = map.get('AllocationStatus')
        return self


class ModifyDedicatedHostAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class MigrateDBInstanceRequest(TeaModel):
    def __init__(self, region_id=None, dedicated_host_group_id=None, dbinstance_id=None,
                 target_dedicated_host_id_for_master=None, target_dedicated_host_id_for_slave=None, effective_time=None, specified_time=None,
                 zone_id_for_log=None, zone_id_for_follower=None):
        self.region_id = region_id      # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.target_dedicated_host_id_for_master = target_dedicated_host_id_for_master  # type: str
        self.target_dedicated_host_id_for_slave = target_dedicated_host_id_for_slave  # type: str
        self.effective_time = effective_time  # type: str
        self.specified_time = specified_time  # type: str
        self.zone_id_for_log = zone_id_for_log  # type: str
        self.zone_id_for_follower = zone_id_for_follower  # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_group_id, 'dedicated_host_group_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['DBInstanceId'] = self.dbinstance_id
        result['TargetDedicatedHostIdForMaster'] = self.target_dedicated_host_id_for_master
        result['TargetDedicatedHostIdForSlave'] = self.target_dedicated_host_id_for_slave
        result['EffectiveTime'] = self.effective_time
        result['SpecifiedTime'] = self.specified_time
        result['ZoneIdForLog'] = self.zone_id_for_log
        result['ZoneIdForFollower'] = self.zone_id_for_follower
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.target_dedicated_host_id_for_master = map.get('TargetDedicatedHostIdForMaster')
        self.target_dedicated_host_id_for_slave = map.get('TargetDedicatedHostIdForSlave')
        self.effective_time = map.get('EffectiveTime')
        self.specified_time = map.get('SpecifiedTime')
        self.zone_id_for_log = map.get('ZoneIdForLog')
        self.zone_id_for_follower = map.get('ZoneIdForFollower')
        return self


class MigrateDBInstanceResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None, migration_id=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: int
        self.migration_id = migration_id  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.migration_id, 'migration_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        result['MigrationId'] = self.migration_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        self.migration_id = map.get('MigrationId')
        return self


class CreateDedicatedHostRequest(TeaModel):
    def __init__(self, region_id=None, dedicated_host_group_id=None, host_name=None, zone_id=None, v_switch_id=None,
                 host_class=None, pay_type=None, period=None, used_time=None, client_token=None, auto_renew=None):
        self.region_id = region_id      # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.host_name = host_name      # type: str
        self.zone_id = zone_id          # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.host_class = host_class    # type: str
        self.pay_type = pay_type        # type: str
        self.period = period            # type: str
        self.used_time = used_time      # type: str
        self.client_token = client_token  # type: str
        self.auto_renew = auto_renew    # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_group_id, 'dedicated_host_group_id')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.host_class, 'host_class')
        self.validate_required(self.pay_type, 'pay_type')
        self.validate_required(self.client_token, 'client_token')
        self.validate_required(self.auto_renew, 'auto_renew')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['HostName'] = self.host_name
        result['ZoneId'] = self.zone_id
        result['VSwitchId'] = self.v_switch_id
        result['HostClass'] = self.host_class
        result['PayType'] = self.pay_type
        result['Period'] = self.period
        result['UsedTime'] = self.used_time
        result['ClientToken'] = self.client_token
        result['AutoRenew'] = self.auto_renew
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.host_name = map.get('HostName')
        self.zone_id = map.get('ZoneId')
        self.v_switch_id = map.get('VSwitchId')
        self.host_class = map.get('HostClass')
        self.pay_type = map.get('PayType')
        self.period = map.get('Period')
        self.used_time = map.get('UsedTime')
        self.client_token = map.get('ClientToken')
        self.auto_renew = map.get('AutoRenew')
        return self


class CreateDedicatedHostResponse(TeaModel):
    def __init__(self, request_id=None, order_id=None, dedicate_host_list=None):
        self.request_id = request_id    # type: str
        self.order_id = order_id        # type: int
        self.dedicate_host_list = dedicate_host_list  # type: CreateDedicatedHostResponseDedicateHostList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.dedicate_host_list, 'dedicate_host_list')
        if self.dedicate_host_list:
            self.dedicate_host_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['OrderId'] = self.order_id
        if self.dedicate_host_list is not None:
            result['DedicateHostList'] = self.dedicate_host_list.to_map()
        else:
            result['DedicateHostList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.order_id = map.get('OrderId')
        if map.get('DedicateHostList') is not None:
            temp_model = CreateDedicatedHostResponseDedicateHostList()
            self.dedicate_host_list = temp_model.from_map(map['DedicateHostList'])
        else:
            self.dedicate_host_list = None
        return self


class CreateDedicatedHostResponseDedicateHostListDedicateHostList(TeaModel):
    def __init__(self, dedicated_host_id=None):
        self.dedicated_host_id = dedicated_host_id  # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_id, 'dedicated_host_id')

    def to_map(self):
        result = {}
        result['DedicatedHostId'] = self.dedicated_host_id
        return result

    def from_map(self, map={}):
        self.dedicated_host_id = map.get('DedicatedHostId')
        return self


class CreateDedicatedHostResponseDedicateHostList(TeaModel):
    def __init__(self, dedicate_host_list=None):
        self.dedicate_host_list = dedicate_host_list  # type: List[CreateDedicatedHostResponseDedicateHostListDedicateHostList]

    def validate(self):
        self.validate_required(self.dedicate_host_list, 'dedicate_host_list')
        if self.dedicate_host_list:
            for k in self.dedicate_host_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DedicateHostList'] = []
        if self.dedicate_host_list is not None:
            for k in self.dedicate_host_list:
                result['DedicateHostList'].append(k.to_map() if k else None)
        else:
            result['DedicateHostList'] = None
        return result

    def from_map(self, map={}):
        self.dedicate_host_list = []
        if map.get('DedicateHostList') is not None:
            for k in map.get('DedicateHostList'):
                temp_model = CreateDedicatedHostResponseDedicateHostListDedicateHostList()
                self.dedicate_host_list.append(temp_model.from_map(k))
        else:
            self.dedicate_host_list = None
        return self


class RebuildDBInstanceRequest(TeaModel):
    def __init__(self, region_id=None, dedicated_host_group_id=None, dbinstance_id=None, dedicated_host_id=None,
                 rebuild_node_type=None):
        self.region_id = region_id      # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.rebuild_node_type = rebuild_node_type  # type: str

    def validate(self):
        self.validate_required(self.dedicated_host_group_id, 'dedicated_host_group_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['DBInstanceId'] = self.dbinstance_id
        result['DedicatedHostId'] = self.dedicated_host_id
        result['RebuildNodeType'] = self.rebuild_node_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.dedicated_host_id = map.get('DedicatedHostId')
        self.rebuild_node_type = map.get('RebuildNodeType')
        return self


class RebuildDBInstanceResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None, migration_id=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: int
        self.migration_id = migration_id  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.migration_id, 'migration_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        result['MigrationId'] = self.migration_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        self.migration_id = map.get('MigrationId')
        return self


class DescribeDBProxyEndpointRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbproxy_endpoint_id=None, dbproxy_connect_string=None, region_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbproxy_endpoint_id = dbproxy_endpoint_id  # type: str
        self.dbproxy_connect_string = dbproxy_connect_string  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBProxyEndpointId'] = self.dbproxy_endpoint_id
        result['DBProxyConnectString'] = self.dbproxy_connect_string
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbproxy_endpoint_id = map.get('DBProxyEndpointId')
        self.dbproxy_connect_string = map.get('DBProxyConnectString')
        self.region_id = map.get('RegionId')
        return self


class DescribeDBProxyEndpointResponse(TeaModel):
    def __init__(self, request_id=None, dbproxy_endpoint_id=None, dbproxy_connect_string=None,
                 dbproxy_connect_string_port=None, dbproxy_connect_string_net_type=None, dbproxy_features=None,
                 read_only_instance_max_delay_time=None, read_only_instance_distribution_type=None, read_only_instance_weight=None):
        self.request_id = request_id    # type: str
        self.dbproxy_endpoint_id = dbproxy_endpoint_id  # type: str
        self.dbproxy_connect_string = dbproxy_connect_string  # type: str
        self.dbproxy_connect_string_port = dbproxy_connect_string_port  # type: str
        self.dbproxy_connect_string_net_type = dbproxy_connect_string_net_type  # type: str
        self.dbproxy_features = dbproxy_features  # type: str
        self.read_only_instance_max_delay_time = read_only_instance_max_delay_time  # type: str
        self.read_only_instance_distribution_type = read_only_instance_distribution_type  # type: str
        self.read_only_instance_weight = read_only_instance_weight  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbproxy_endpoint_id, 'dbproxy_endpoint_id')
        self.validate_required(self.dbproxy_connect_string, 'dbproxy_connect_string')
        self.validate_required(self.dbproxy_connect_string_port, 'dbproxy_connect_string_port')
        self.validate_required(self.dbproxy_connect_string_net_type, 'dbproxy_connect_string_net_type')
        self.validate_required(self.dbproxy_features, 'dbproxy_features')
        self.validate_required(self.read_only_instance_max_delay_time, 'read_only_instance_max_delay_time')
        self.validate_required(self.read_only_instance_distribution_type, 'read_only_instance_distribution_type')
        self.validate_required(self.read_only_instance_weight, 'read_only_instance_weight')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBProxyEndpointId'] = self.dbproxy_endpoint_id
        result['DBProxyConnectString'] = self.dbproxy_connect_string
        result['DBProxyConnectStringPort'] = self.dbproxy_connect_string_port
        result['DBProxyConnectStringNetType'] = self.dbproxy_connect_string_net_type
        result['DBProxyFeatures'] = self.dbproxy_features
        result['ReadOnlyInstanceMaxDelayTime'] = self.read_only_instance_max_delay_time
        result['ReadOnlyInstanceDistributionType'] = self.read_only_instance_distribution_type
        result['ReadOnlyInstanceWeight'] = self.read_only_instance_weight
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbproxy_endpoint_id = map.get('DBProxyEndpointId')
        self.dbproxy_connect_string = map.get('DBProxyConnectString')
        self.dbproxy_connect_string_port = map.get('DBProxyConnectStringPort')
        self.dbproxy_connect_string_net_type = map.get('DBProxyConnectStringNetType')
        self.dbproxy_features = map.get('DBProxyFeatures')
        self.read_only_instance_max_delay_time = map.get('ReadOnlyInstanceMaxDelayTime')
        self.read_only_instance_distribution_type = map.get('ReadOnlyInstanceDistributionType')
        self.read_only_instance_weight = map.get('ReadOnlyInstanceWeight')
        return self


class DescribeDBProxyPerformanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbproxy_instance_type=None, start_time=None, end_time=None,
                 region_id=None, metrics_name=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbproxy_instance_type = dbproxy_instance_type  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.region_id = region_id      # type: str
        self.metrics_name = metrics_name  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.metrics_name, 'metrics_name')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBProxyInstanceType'] = self.dbproxy_instance_type
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['RegionId'] = self.region_id
        result['MetricsName'] = self.metrics_name
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbproxy_instance_type = map.get('DBProxyInstanceType')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.region_id = map.get('RegionId')
        self.metrics_name = map.get('MetricsName')
        return self


class DescribeDBProxyPerformanceResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, start_time=None, end_time=None, performance_keys=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.performance_keys = performance_keys  # type: DescribeDBProxyPerformanceResponsePerformanceKeys

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.performance_keys, 'performance_keys')
        if self.performance_keys:
            self.performance_keys.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        if self.performance_keys is not None:
            result['PerformanceKeys'] = self.performance_keys.to_map()
        else:
            result['PerformanceKeys'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        if map.get('PerformanceKeys') is not None:
            temp_model = DescribeDBProxyPerformanceResponsePerformanceKeys()
            self.performance_keys = temp_model.from_map(map['PerformanceKeys'])
        else:
            self.performance_keys = None
        return self


class DescribeDBProxyPerformanceResponsePerformanceKeysPerformanceKeyValuesPerformanceValue(TeaModel):
    def __init__(self, value=None, date=None):
        self.value = value              # type: str
        self.date = date                # type: str

    def validate(self):
        self.validate_required(self.value, 'value')
        self.validate_required(self.date, 'date')

    def to_map(self):
        result = {}
        result['Value'] = self.value
        result['Date'] = self.date
        return result

    def from_map(self, map={}):
        self.value = map.get('Value')
        self.date = map.get('Date')
        return self


class DescribeDBProxyPerformanceResponsePerformanceKeysPerformanceKeyValues(TeaModel):
    def __init__(self, performance_value=None):
        self.performance_value = performance_value  # type: List[DescribeDBProxyPerformanceResponsePerformanceKeysPerformanceKeyValuesPerformanceValue]

    def validate(self):
        self.validate_required(self.performance_value, 'performance_value')
        if self.performance_value:
            for k in self.performance_value:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PerformanceValue'] = []
        if self.performance_value is not None:
            for k in self.performance_value:
                result['PerformanceValue'].append(k.to_map() if k else None)
        else:
            result['PerformanceValue'] = None
        return result

    def from_map(self, map={}):
        self.performance_value = []
        if map.get('PerformanceValue') is not None:
            for k in map.get('PerformanceValue'):
                temp_model = DescribeDBProxyPerformanceResponsePerformanceKeysPerformanceKeyValuesPerformanceValue()
                self.performance_value.append(temp_model.from_map(k))
        else:
            self.performance_value = None
        return self


class DescribeDBProxyPerformanceResponsePerformanceKeysPerformanceKey(TeaModel):
    def __init__(self, key=None, value_format=None, values=None):
        self.key = key                  # type: str
        self.value_format = value_format  # type: str
        self.values = values            # type: DescribeDBProxyPerformanceResponsePerformanceKeysPerformanceKeyValues

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value_format, 'value_format')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['ValueFormat'] = self.value_format
        if self.values is not None:
            result['Values'] = self.values.to_map()
        else:
            result['Values'] = None
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value_format = map.get('ValueFormat')
        if map.get('Values') is not None:
            temp_model = DescribeDBProxyPerformanceResponsePerformanceKeysPerformanceKeyValues()
            self.values = temp_model.from_map(map['Values'])
        else:
            self.values = None
        return self


class DescribeDBProxyPerformanceResponsePerformanceKeys(TeaModel):
    def __init__(self, performance_key=None):
        self.performance_key = performance_key  # type: List[DescribeDBProxyPerformanceResponsePerformanceKeysPerformanceKey]

    def validate(self):
        self.validate_required(self.performance_key, 'performance_key')
        if self.performance_key:
            for k in self.performance_key:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PerformanceKey'] = []
        if self.performance_key is not None:
            for k in self.performance_key:
                result['PerformanceKey'].append(k.to_map() if k else None)
        else:
            result['PerformanceKey'] = None
        return result

    def from_map(self, map={}):
        self.performance_key = []
        if map.get('PerformanceKey') is not None:
            for k in map.get('PerformanceKey'):
                temp_model = DescribeDBProxyPerformanceResponsePerformanceKeysPerformanceKey()
                self.performance_key.append(temp_model.from_map(k))
        else:
            self.performance_key = None
        return self


class DescribeDBProxyRequest(TeaModel):
    def __init__(self, dbinstance_id=None, region_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.region_id = map.get('RegionId')
        return self


class DescribeDBProxyResponse(TeaModel):
    def __init__(self, request_id=None, dbproxy_service_status=None, dbproxy_instance_type=None,
                 dbproxy_instance_num=None, dbproxy_instance_status=None, dbproxy_instance_current_minor_version=None,
                 dbproxy_instance_latest_minor_version=None, dbproxy_instance_name=None, dbproxy_connect_string_items=None):
        self.request_id = request_id    # type: str
        self.dbproxy_service_status = dbproxy_service_status  # type: str
        self.dbproxy_instance_type = dbproxy_instance_type  # type: str
        self.dbproxy_instance_num = dbproxy_instance_num  # type: int
        self.dbproxy_instance_status = dbproxy_instance_status  # type: str
        self.dbproxy_instance_current_minor_version = dbproxy_instance_current_minor_version  # type: str
        self.dbproxy_instance_latest_minor_version = dbproxy_instance_latest_minor_version  # type: str
        self.dbproxy_instance_name = dbproxy_instance_name  # type: str
        self.dbproxy_connect_string_items = dbproxy_connect_string_items  # type: DescribeDBProxyResponseDBProxyConnectStringItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbproxy_service_status, 'dbproxy_service_status')
        self.validate_required(self.dbproxy_instance_type, 'dbproxy_instance_type')
        self.validate_required(self.dbproxy_instance_num, 'dbproxy_instance_num')
        self.validate_required(self.dbproxy_instance_status, 'dbproxy_instance_status')
        self.validate_required(self.dbproxy_instance_current_minor_version, 'dbproxy_instance_current_minor_version')
        self.validate_required(self.dbproxy_instance_latest_minor_version, 'dbproxy_instance_latest_minor_version')
        self.validate_required(self.dbproxy_instance_name, 'dbproxy_instance_name')
        self.validate_required(self.dbproxy_connect_string_items, 'dbproxy_connect_string_items')
        if self.dbproxy_connect_string_items:
            self.dbproxy_connect_string_items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBProxyServiceStatus'] = self.dbproxy_service_status
        result['DBProxyInstanceType'] = self.dbproxy_instance_type
        result['DBProxyInstanceNum'] = self.dbproxy_instance_num
        result['DBProxyInstanceStatus'] = self.dbproxy_instance_status
        result['DBProxyInstanceCurrentMinorVersion'] = self.dbproxy_instance_current_minor_version
        result['DBProxyInstanceLatestMinorVersion'] = self.dbproxy_instance_latest_minor_version
        result['DBProxyInstanceName'] = self.dbproxy_instance_name
        if self.dbproxy_connect_string_items is not None:
            result['DBProxyConnectStringItems'] = self.dbproxy_connect_string_items.to_map()
        else:
            result['DBProxyConnectStringItems'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbproxy_service_status = map.get('DBProxyServiceStatus')
        self.dbproxy_instance_type = map.get('DBProxyInstanceType')
        self.dbproxy_instance_num = map.get('DBProxyInstanceNum')
        self.dbproxy_instance_status = map.get('DBProxyInstanceStatus')
        self.dbproxy_instance_current_minor_version = map.get('DBProxyInstanceCurrentMinorVersion')
        self.dbproxy_instance_latest_minor_version = map.get('DBProxyInstanceLatestMinorVersion')
        self.dbproxy_instance_name = map.get('DBProxyInstanceName')
        if map.get('DBProxyConnectStringItems') is not None:
            temp_model = DescribeDBProxyResponseDBProxyConnectStringItems()
            self.dbproxy_connect_string_items = temp_model.from_map(map['DBProxyConnectStringItems'])
        else:
            self.dbproxy_connect_string_items = None
        return self


class DescribeDBProxyResponseDBProxyConnectStringItemsDBProxyConnectStringItems(TeaModel):
    def __init__(self, dbproxy_endpoint_id=None, dbproxy_connect_string=None, dbproxy_connect_string_port=None,
                 dbproxy_connect_string_net_type=None, dbproxy_vpc_instance_id=None, dbproxy_endpoint_name=None,
                 dbproxy_connect_string_net_work_type=None):
        self.dbproxy_endpoint_id = dbproxy_endpoint_id  # type: str
        self.dbproxy_connect_string = dbproxy_connect_string  # type: str
        self.dbproxy_connect_string_port = dbproxy_connect_string_port  # type: str
        self.dbproxy_connect_string_net_type = dbproxy_connect_string_net_type  # type: str
        self.dbproxy_vpc_instance_id = dbproxy_vpc_instance_id  # type: str
        self.dbproxy_endpoint_name = dbproxy_endpoint_name  # type: str
        self.dbproxy_connect_string_net_work_type = dbproxy_connect_string_net_work_type  # type: str

    def validate(self):
        self.validate_required(self.dbproxy_endpoint_id, 'dbproxy_endpoint_id')
        self.validate_required(self.dbproxy_connect_string, 'dbproxy_connect_string')
        self.validate_required(self.dbproxy_connect_string_port, 'dbproxy_connect_string_port')
        self.validate_required(self.dbproxy_connect_string_net_type, 'dbproxy_connect_string_net_type')
        self.validate_required(self.dbproxy_vpc_instance_id, 'dbproxy_vpc_instance_id')
        self.validate_required(self.dbproxy_endpoint_name, 'dbproxy_endpoint_name')
        self.validate_required(self.dbproxy_connect_string_net_work_type, 'dbproxy_connect_string_net_work_type')

    def to_map(self):
        result = {}
        result['DBProxyEndpointId'] = self.dbproxy_endpoint_id
        result['DBProxyConnectString'] = self.dbproxy_connect_string
        result['DBProxyConnectStringPort'] = self.dbproxy_connect_string_port
        result['DBProxyConnectStringNetType'] = self.dbproxy_connect_string_net_type
        result['DBProxyVpcInstanceId'] = self.dbproxy_vpc_instance_id
        result['DBProxyEndpointName'] = self.dbproxy_endpoint_name
        result['DBProxyConnectStringNetWorkType'] = self.dbproxy_connect_string_net_work_type
        return result

    def from_map(self, map={}):
        self.dbproxy_endpoint_id = map.get('DBProxyEndpointId')
        self.dbproxy_connect_string = map.get('DBProxyConnectString')
        self.dbproxy_connect_string_port = map.get('DBProxyConnectStringPort')
        self.dbproxy_connect_string_net_type = map.get('DBProxyConnectStringNetType')
        self.dbproxy_vpc_instance_id = map.get('DBProxyVpcInstanceId')
        self.dbproxy_endpoint_name = map.get('DBProxyEndpointName')
        self.dbproxy_connect_string_net_work_type = map.get('DBProxyConnectStringNetWorkType')
        return self


class DescribeDBProxyResponseDBProxyConnectStringItems(TeaModel):
    def __init__(self, dbproxy_connect_string_items=None):
        self.dbproxy_connect_string_items = dbproxy_connect_string_items  # type: List[DescribeDBProxyResponseDBProxyConnectStringItemsDBProxyConnectStringItems]

    def validate(self):
        self.validate_required(self.dbproxy_connect_string_items, 'dbproxy_connect_string_items')
        if self.dbproxy_connect_string_items:
            for k in self.dbproxy_connect_string_items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DBProxyConnectStringItems'] = []
        if self.dbproxy_connect_string_items is not None:
            for k in self.dbproxy_connect_string_items:
                result['DBProxyConnectStringItems'].append(k.to_map() if k else None)
        else:
            result['DBProxyConnectStringItems'] = None
        return result

    def from_map(self, map={}):
        self.dbproxy_connect_string_items = []
        if map.get('DBProxyConnectStringItems') is not None:
            for k in map.get('DBProxyConnectStringItems'):
                temp_model = DescribeDBProxyResponseDBProxyConnectStringItemsDBProxyConnectStringItems()
                self.dbproxy_connect_string_items.append(temp_model.from_map(k))
        else:
            self.dbproxy_connect_string_items = None
        return self


class ModifyDBProxyEndpointRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbproxy_endpoint_id=None, config_dbproxy_features=None, region_id=None,
                 read_only_instance_max_delay_time=None, read_only_instance_distribution_type=None, read_only_instance_weight=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbproxy_endpoint_id = dbproxy_endpoint_id  # type: str
        self.config_dbproxy_features = config_dbproxy_features  # type: str
        self.region_id = region_id      # type: str
        self.read_only_instance_max_delay_time = read_only_instance_max_delay_time  # type: str
        self.read_only_instance_distribution_type = read_only_instance_distribution_type  # type: str
        self.read_only_instance_weight = read_only_instance_weight  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbproxy_endpoint_id, 'dbproxy_endpoint_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBProxyEndpointId'] = self.dbproxy_endpoint_id
        result['ConfigDBProxyFeatures'] = self.config_dbproxy_features
        result['RegionId'] = self.region_id
        result['ReadOnlyInstanceMaxDelayTime'] = self.read_only_instance_max_delay_time
        result['ReadOnlyInstanceDistributionType'] = self.read_only_instance_distribution_type
        result['ReadOnlyInstanceWeight'] = self.read_only_instance_weight
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbproxy_endpoint_id = map.get('DBProxyEndpointId')
        self.config_dbproxy_features = map.get('ConfigDBProxyFeatures')
        self.region_id = map.get('RegionId')
        self.read_only_instance_max_delay_time = map.get('ReadOnlyInstanceMaxDelayTime')
        self.read_only_instance_distribution_type = map.get('ReadOnlyInstanceDistributionType')
        self.read_only_instance_weight = map.get('ReadOnlyInstanceWeight')
        return self


class ModifyDBProxyEndpointResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyDBProxyInstanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbproxy_instance_type=None, dbproxy_instance_num=None,
                 effective_time=None, effective_specific_time=None, region_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbproxy_instance_type = dbproxy_instance_type  # type: str
        self.dbproxy_instance_num = dbproxy_instance_num  # type: str
        self.effective_time = effective_time  # type: str
        self.effective_specific_time = effective_specific_time  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbproxy_instance_type, 'dbproxy_instance_type')
        self.validate_required(self.dbproxy_instance_num, 'dbproxy_instance_num')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBProxyInstanceType'] = self.dbproxy_instance_type
        result['DBProxyInstanceNum'] = self.dbproxy_instance_num
        result['EffectiveTime'] = self.effective_time
        result['EffectiveSpecificTime'] = self.effective_specific_time
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbproxy_instance_type = map.get('DBProxyInstanceType')
        self.dbproxy_instance_num = map.get('DBProxyInstanceNum')
        self.effective_time = map.get('EffectiveTime')
        self.effective_specific_time = map.get('EffectiveSpecificTime')
        self.region_id = map.get('RegionId')
        return self


class ModifyDBProxyInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyDBProxyRequest(TeaModel):
    def __init__(self, dbinstance_id=None, config_dbproxy_service=None, dbproxy_instance_num=None, region_id=None,
                 instance_network_type=None, vpcid=None, v_switch_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.config_dbproxy_service = config_dbproxy_service  # type: str
        self.dbproxy_instance_num = dbproxy_instance_num  # type: str
        self.region_id = region_id      # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.vpcid = vpcid              # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.config_dbproxy_service, 'config_dbproxy_service')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['ConfigDBProxyService'] = self.config_dbproxy_service
        result['DBProxyInstanceNum'] = self.dbproxy_instance_num
        result['RegionId'] = self.region_id
        result['InstanceNetworkType'] = self.instance_network_type
        result['VPCId'] = self.vpcid
        result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.config_dbproxy_service = map.get('ConfigDBProxyService')
        self.dbproxy_instance_num = map.get('DBProxyInstanceNum')
        self.region_id = map.get('RegionId')
        self.instance_network_type = map.get('InstanceNetworkType')
        self.vpcid = map.get('VPCId')
        self.v_switch_id = map.get('VSwitchId')
        return self


class ModifyDBProxyResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyHASwitchConfigRequest(TeaModel):
    def __init__(self, dbinstance_id=None, haconfig=None, manual_hatime=None, region_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.haconfig = haconfig        # type: str
        self.manual_hatime = manual_hatime  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['HAConfig'] = self.haconfig
        result['ManualHATime'] = self.manual_hatime
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.haconfig = map.get('HAConfig')
        self.manual_hatime = map.get('ManualHATime')
        self.region_id = map.get('RegionId')
        return self


class ModifyHASwitchConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeHASwitchConfigRequest(TeaModel):
    def __init__(self, dbinstance_id=None, region_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.region_id = map.get('RegionId')
        return self


class DescribeHASwitchConfigResponse(TeaModel):
    def __init__(self, request_id=None, haconfig=None, manual_hatime=None):
        self.request_id = request_id    # type: str
        self.haconfig = haconfig        # type: str
        self.manual_hatime = manual_hatime  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.haconfig, 'haconfig')
        self.validate_required(self.manual_hatime, 'manual_hatime')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['HAConfig'] = self.haconfig
        result['ManualHATime'] = self.manual_hatime
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.haconfig = map.get('HAConfig')
        self.manual_hatime = map.get('ManualHATime')
        return self


class ModifyActionEventPolicyRequest(TeaModel):
    def __init__(self, region_id=None, enable_event_log=None):
        self.region_id = region_id      # type: str
        self.enable_event_log = enable_event_log  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.enable_event_log, 'enable_event_log')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['EnableEventLog'] = self.enable_event_log
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.enable_event_log = map.get('EnableEventLog')
        return self


class ModifyActionEventPolicyResponse(TeaModel):
    def __init__(self, request_id=None, region_id=None, enable_event_log=None):
        self.request_id = request_id    # type: str
        self.region_id = region_id      # type: str
        self.enable_event_log = enable_event_log  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.enable_event_log, 'enable_event_log')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RegionId'] = self.region_id
        result['EnableEventLog'] = self.enable_event_log
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.region_id = map.get('RegionId')
        self.enable_event_log = map.get('EnableEventLog')
        return self


class DescribeActionEventPolicyRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        return self


class DescribeActionEventPolicyResponse(TeaModel):
    def __init__(self, request_id=None, region_id=None, enable_event_log=None):
        self.request_id = request_id    # type: str
        self.region_id = region_id      # type: str
        self.enable_event_log = enable_event_log  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.enable_event_log, 'enable_event_log')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RegionId'] = self.region_id
        result['EnableEventLog'] = self.enable_event_log
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.region_id = map.get('RegionId')
        self.enable_event_log = map.get('EnableEventLog')
        return self


class DescribeEventsRequest(TeaModel):
    def __init__(self, region_id=None, start_time=None, end_time=None, page_size=None, page_number=None):
        self.region_id = region_id      # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeEventsResponse(TeaModel):
    def __init__(self, request_id=None, total_record_count=None, page_size=None, page_number=None, event_items=None):
        self.request_id = request_id    # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.event_items = event_items  # type: DescribeEventsResponseEventItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.event_items, 'event_items')
        if self.event_items:
            self.event_items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalRecordCount'] = self.total_record_count
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        if self.event_items is not None:
            result['EventItems'] = self.event_items.to_map()
        else:
            result['EventItems'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        if map.get('EventItems') is not None:
            temp_model = DescribeEventsResponseEventItems()
            self.event_items = temp_model.from_map(map['EventItems'])
        else:
            self.event_items = None
        return self


class DescribeEventsResponseEventItemsEventItems(TeaModel):
    def __init__(self, event_id=None, event_type=None, event_name=None, event_time=None, resource_type=None,
                 resource_name=None, region_id=None, event_user_type=None, event_reason=None, event_payload=None,
                 event_record_time=None):
        self.event_id = event_id        # type: int
        self.event_type = event_type    # type: str
        self.event_name = event_name    # type: str
        self.event_time = event_time    # type: str
        self.resource_type = resource_type  # type: str
        self.resource_name = resource_name  # type: str
        self.region_id = region_id      # type: str
        self.event_user_type = event_user_type  # type: str
        self.event_reason = event_reason  # type: str
        self.event_payload = event_payload  # type: str
        self.event_record_time = event_record_time  # type: str

    def validate(self):
        self.validate_required(self.event_id, 'event_id')
        self.validate_required(self.event_type, 'event_type')
        self.validate_required(self.event_name, 'event_name')
        self.validate_required(self.event_time, 'event_time')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_name, 'resource_name')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.event_user_type, 'event_user_type')
        self.validate_required(self.event_reason, 'event_reason')
        self.validate_required(self.event_payload, 'event_payload')
        self.validate_required(self.event_record_time, 'event_record_time')

    def to_map(self):
        result = {}
        result['EventId'] = self.event_id
        result['EventType'] = self.event_type
        result['EventName'] = self.event_name
        result['EventTime'] = self.event_time
        result['ResourceType'] = self.resource_type
        result['ResourceName'] = self.resource_name
        result['RegionId'] = self.region_id
        result['EventUserType'] = self.event_user_type
        result['EventReason'] = self.event_reason
        result['EventPayload'] = self.event_payload
        result['EventRecordTime'] = self.event_record_time
        return result

    def from_map(self, map={}):
        self.event_id = map.get('EventId')
        self.event_type = map.get('EventType')
        self.event_name = map.get('EventName')
        self.event_time = map.get('EventTime')
        self.resource_type = map.get('ResourceType')
        self.resource_name = map.get('ResourceName')
        self.region_id = map.get('RegionId')
        self.event_user_type = map.get('EventUserType')
        self.event_reason = map.get('EventReason')
        self.event_payload = map.get('EventPayload')
        self.event_record_time = map.get('EventRecordTime')
        return self


class DescribeEventsResponseEventItems(TeaModel):
    def __init__(self, event_items=None):
        self.event_items = event_items  # type: List[DescribeEventsResponseEventItemsEventItems]

    def validate(self):
        self.validate_required(self.event_items, 'event_items')
        if self.event_items:
            for k in self.event_items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EventItems'] = []
        if self.event_items is not None:
            for k in self.event_items:
                result['EventItems'].append(k.to_map() if k else None)
        else:
            result['EventItems'] = None
        return result

    def from_map(self, map={}):
        self.event_items = []
        if map.get('EventItems') is not None:
            for k in map.get('EventItems'):
                temp_model = DescribeEventsResponseEventItemsEventItems()
                self.event_items.append(temp_model.from_map(k))
        else:
            self.event_items = None
        return self


class DescribeDBInstancesForCloneRequest(TeaModel):
    def __init__(self, client_token=None, proxy_id=None, engine=None, zone_id=None, dbinstance_status=None,
                 expired=None, search_key=None, dbinstance_id=None, dbinstance_type=None, region_id=None, page_size=None,
                 page_number=None, instance_network_type=None, vpc_id=None, v_switch_id=None, dbinstance_class=None,
                 engine_version=None, node_type=None, pay_type=None, connection_mode=None, current_instance_id=None):
        self.client_token = client_token  # type: str
        self.proxy_id = proxy_id        # type: str
        self.engine = engine            # type: str
        self.zone_id = zone_id          # type: str
        self.dbinstance_status = dbinstance_status  # type: str
        self.expired = expired          # type: str
        self.search_key = search_key    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_type = dbinstance_type  # type: str
        self.region_id = region_id      # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.instance_network_type = instance_network_type  # type: str
        self.vpc_id = vpc_id            # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.engine_version = engine_version  # type: str
        self.node_type = node_type      # type: str
        self.pay_type = pay_type        # type: str
        self.connection_mode = connection_mode  # type: str
        self.current_instance_id = current_instance_id  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['proxyId'] = self.proxy_id
        result['Engine'] = self.engine
        result['ZoneId'] = self.zone_id
        result['DBInstanceStatus'] = self.dbinstance_status
        result['Expired'] = self.expired
        result['SearchKey'] = self.search_key
        result['DBInstanceId'] = self.dbinstance_id
        result['DBInstanceType'] = self.dbinstance_type
        result['RegionId'] = self.region_id
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['InstanceNetworkType'] = self.instance_network_type
        result['VpcId'] = self.vpc_id
        result['VSwitchId'] = self.v_switch_id
        result['DBInstanceClass'] = self.dbinstance_class
        result['EngineVersion'] = self.engine_version
        result['NodeType'] = self.node_type
        result['PayType'] = self.pay_type
        result['ConnectionMode'] = self.connection_mode
        result['CurrentInstanceId'] = self.current_instance_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.proxy_id = map.get('proxyId')
        self.engine = map.get('Engine')
        self.zone_id = map.get('ZoneId')
        self.dbinstance_status = map.get('DBInstanceStatus')
        self.expired = map.get('Expired')
        self.search_key = map.get('SearchKey')
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbinstance_type = map.get('DBInstanceType')
        self.region_id = map.get('RegionId')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.instance_network_type = map.get('InstanceNetworkType')
        self.vpc_id = map.get('VpcId')
        self.v_switch_id = map.get('VSwitchId')
        self.dbinstance_class = map.get('DBInstanceClass')
        self.engine_version = map.get('EngineVersion')
        self.node_type = map.get('NodeType')
        self.pay_type = map.get('PayType')
        self.connection_mode = map.get('ConnectionMode')
        self.current_instance_id = map.get('CurrentInstanceId')
        return self


class DescribeDBInstancesForCloneResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, total_record_count=None, page_record_count=None,
                 items=None):
        self.request_id = request_id    # type: str
        self.page_number = page_number  # type: int
        self.total_record_count = total_record_count  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items              # type: DescribeDBInstancesForCloneResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNumber'] = self.page_number
        result['TotalRecordCount'] = self.total_record_count
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_number = map.get('PageNumber')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeDBInstancesForCloneResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeDBInstancesForCloneResponseItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeDBInstancesForCloneResponseItemsDBInstanceReadOnlyDBInstanceIds(TeaModel):
    def __init__(self, read_only_dbinstance_id=None):
        self.read_only_dbinstance_id = read_only_dbinstance_id  # type: List[DescribeDBInstancesForCloneResponseItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId]

    def validate(self):
        self.validate_required(self.read_only_dbinstance_id, 'read_only_dbinstance_id')
        if self.read_only_dbinstance_id:
            for k in self.read_only_dbinstance_id:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ReadOnlyDBInstanceId'] = []
        if self.read_only_dbinstance_id is not None:
            for k in self.read_only_dbinstance_id:
                result['ReadOnlyDBInstanceId'].append(k.to_map() if k else None)
        else:
            result['ReadOnlyDBInstanceId'] = None
        return result

    def from_map(self, map={}):
        self.read_only_dbinstance_id = []
        if map.get('ReadOnlyDBInstanceId') is not None:
            for k in map.get('ReadOnlyDBInstanceId'):
                temp_model = DescribeDBInstancesForCloneResponseItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId()
                self.read_only_dbinstance_id.append(temp_model.from_map(k))
        else:
            self.read_only_dbinstance_id = None
        return self


class DescribeDBInstancesForCloneResponseItemsDBInstance(TeaModel):
    def __init__(self, ins_id=None, dbinstance_id=None, dbinstance_description=None, pay_type=None,
                 dbinstance_type=None, region_id=None, expire_time=None, destroy_time=None, dbinstance_status=None, engine=None,
                 dbinstance_net_type=None, connection_mode=None, lock_mode=None, category=None, dbinstance_storage_type=None,
                 dbinstance_class=None, instance_network_type=None, vpc_cloud_instance_id=None, lock_reason=None, zone_id=None,
                 mutri_orsignle=None, create_time=None, engine_version=None, guard_dbinstance_id=None, temp_dbinstance_id=None,
                 master_instance_id=None, vpc_id=None, v_switch_id=None, replicate_id=None, resource_group_id=None,
                 read_only_dbinstance_ids=None):
        self.ins_id = ins_id            # type: int
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.pay_type = pay_type        # type: str
        self.dbinstance_type = dbinstance_type  # type: str
        self.region_id = region_id      # type: str
        self.expire_time = expire_time  # type: str
        self.destroy_time = destroy_time  # type: str
        self.dbinstance_status = dbinstance_status  # type: str
        self.engine = engine            # type: str
        self.dbinstance_net_type = dbinstance_net_type  # type: str
        self.connection_mode = connection_mode  # type: str
        self.lock_mode = lock_mode      # type: str
        self.category = category        # type: str
        self.dbinstance_storage_type = dbinstance_storage_type  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.vpc_cloud_instance_id = vpc_cloud_instance_id  # type: str
        self.lock_reason = lock_reason  # type: str
        self.zone_id = zone_id          # type: str
        self.mutri_orsignle = mutri_orsignle  # type: bool
        self.create_time = create_time  # type: str
        self.engine_version = engine_version  # type: str
        self.guard_dbinstance_id = guard_dbinstance_id  # type: str
        self.temp_dbinstance_id = temp_dbinstance_id  # type: str
        self.master_instance_id = master_instance_id  # type: str
        self.vpc_id = vpc_id            # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.replicate_id = replicate_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.read_only_dbinstance_ids = read_only_dbinstance_ids  # type: DescribeDBInstancesForCloneResponseItemsDBInstanceReadOnlyDBInstanceIds

    def validate(self):
        self.validate_required(self.ins_id, 'ins_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbinstance_description, 'dbinstance_description')
        self.validate_required(self.pay_type, 'pay_type')
        self.validate_required(self.dbinstance_type, 'dbinstance_type')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.destroy_time, 'destroy_time')
        self.validate_required(self.dbinstance_status, 'dbinstance_status')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.dbinstance_net_type, 'dbinstance_net_type')
        self.validate_required(self.connection_mode, 'connection_mode')
        self.validate_required(self.lock_mode, 'lock_mode')
        self.validate_required(self.category, 'category')
        self.validate_required(self.dbinstance_storage_type, 'dbinstance_storage_type')
        self.validate_required(self.dbinstance_class, 'dbinstance_class')
        self.validate_required(self.instance_network_type, 'instance_network_type')
        self.validate_required(self.vpc_cloud_instance_id, 'vpc_cloud_instance_id')
        self.validate_required(self.lock_reason, 'lock_reason')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.mutri_orsignle, 'mutri_orsignle')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.guard_dbinstance_id, 'guard_dbinstance_id')
        self.validate_required(self.temp_dbinstance_id, 'temp_dbinstance_id')
        self.validate_required(self.master_instance_id, 'master_instance_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.replicate_id, 'replicate_id')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.read_only_dbinstance_ids, 'read_only_dbinstance_ids')
        if self.read_only_dbinstance_ids:
            self.read_only_dbinstance_ids.validate()

    def to_map(self):
        result = {}
        result['InsId'] = self.ins_id
        result['DBInstanceId'] = self.dbinstance_id
        result['DBInstanceDescription'] = self.dbinstance_description
        result['PayType'] = self.pay_type
        result['DBInstanceType'] = self.dbinstance_type
        result['RegionId'] = self.region_id
        result['ExpireTime'] = self.expire_time
        result['DestroyTime'] = self.destroy_time
        result['DBInstanceStatus'] = self.dbinstance_status
        result['Engine'] = self.engine
        result['DBInstanceNetType'] = self.dbinstance_net_type
        result['ConnectionMode'] = self.connection_mode
        result['LockMode'] = self.lock_mode
        result['Category'] = self.category
        result['DBInstanceStorageType'] = self.dbinstance_storage_type
        result['DBInstanceClass'] = self.dbinstance_class
        result['InstanceNetworkType'] = self.instance_network_type
        result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        result['LockReason'] = self.lock_reason
        result['ZoneId'] = self.zone_id
        result['MutriORsignle'] = self.mutri_orsignle
        result['CreateTime'] = self.create_time
        result['EngineVersion'] = self.engine_version
        result['GuardDBInstanceId'] = self.guard_dbinstance_id
        result['TempDBInstanceId'] = self.temp_dbinstance_id
        result['MasterInstanceId'] = self.master_instance_id
        result['VpcId'] = self.vpc_id
        result['VSwitchId'] = self.v_switch_id
        result['ReplicateId'] = self.replicate_id
        result['ResourceGroupId'] = self.resource_group_id
        if self.read_only_dbinstance_ids is not None:
            result['ReadOnlyDBInstanceIds'] = self.read_only_dbinstance_ids.to_map()
        else:
            result['ReadOnlyDBInstanceIds'] = None
        return result

    def from_map(self, map={}):
        self.ins_id = map.get('InsId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbinstance_description = map.get('DBInstanceDescription')
        self.pay_type = map.get('PayType')
        self.dbinstance_type = map.get('DBInstanceType')
        self.region_id = map.get('RegionId')
        self.expire_time = map.get('ExpireTime')
        self.destroy_time = map.get('DestroyTime')
        self.dbinstance_status = map.get('DBInstanceStatus')
        self.engine = map.get('Engine')
        self.dbinstance_net_type = map.get('DBInstanceNetType')
        self.connection_mode = map.get('ConnectionMode')
        self.lock_mode = map.get('LockMode')
        self.category = map.get('Category')
        self.dbinstance_storage_type = map.get('DBInstanceStorageType')
        self.dbinstance_class = map.get('DBInstanceClass')
        self.instance_network_type = map.get('InstanceNetworkType')
        self.vpc_cloud_instance_id = map.get('VpcCloudInstanceId')
        self.lock_reason = map.get('LockReason')
        self.zone_id = map.get('ZoneId')
        self.mutri_orsignle = map.get('MutriORsignle')
        self.create_time = map.get('CreateTime')
        self.engine_version = map.get('EngineVersion')
        self.guard_dbinstance_id = map.get('GuardDBInstanceId')
        self.temp_dbinstance_id = map.get('TempDBInstanceId')
        self.master_instance_id = map.get('MasterInstanceId')
        self.vpc_id = map.get('VpcId')
        self.v_switch_id = map.get('VSwitchId')
        self.replicate_id = map.get('ReplicateId')
        self.resource_group_id = map.get('ResourceGroupId')
        if map.get('ReadOnlyDBInstanceIds') is not None:
            temp_model = DescribeDBInstancesForCloneResponseItemsDBInstanceReadOnlyDBInstanceIds()
            self.read_only_dbinstance_ids = temp_model.from_map(map['ReadOnlyDBInstanceIds'])
        else:
            self.read_only_dbinstance_ids = None
        return self


class DescribeDBInstancesForCloneResponseItems(TeaModel):
    def __init__(self, dbinstance=None):
        self.dbinstance = dbinstance    # type: List[DescribeDBInstancesForCloneResponseItemsDBInstance]

    def validate(self):
        self.validate_required(self.dbinstance, 'dbinstance')
        if self.dbinstance:
            for k in self.dbinstance:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DBInstance'] = []
        if self.dbinstance is not None:
            for k in self.dbinstance:
                result['DBInstance'].append(k.to_map() if k else None)
        else:
            result['DBInstance'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance = []
        if map.get('DBInstance') is not None:
            for k in map.get('DBInstance'):
                temp_model = DescribeDBInstancesForCloneResponseItemsDBInstance()
                self.dbinstance.append(temp_model.from_map(k))
        else:
            self.dbinstance = None
        return self


class DescribeDTCSecurityIpHostsForSQLServerRequest(TeaModel):
    def __init__(self, security_token=None, dbinstance_id=None, region_id=None):
        self.security_token = security_token  # type: str
        # description: 实例ID。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: 地域ID，可以通过接口[DescribeRegions](~~26243~~)查看。; 
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DBInstanceId'] = self.dbinstance_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.region_id = map.get('RegionId')
        return self


class DescribeDTCSecurityIpHostsForSQLServerResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, ip_host_pair_num=None, items=None):
        # description: 请求ID。; 
        self.request_id = request_id    # type: str
        # description: 实例ID。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: 分布式事务白名单条目数。; 
        self.ip_host_pair_num = ip_host_pair_num  # type: str
        # description: 分布式事务白名单分组列表。
        self.items = items              # type: DescribeDTCSecurityIpHostsForSQLServerResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.ip_host_pair_num, 'ip_host_pair_num')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['IpHostPairNum'] = self.ip_host_pair_num
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.ip_host_pair_num = map.get('IpHostPairNum')
        if map.get('Items') is not None:
            temp_model = DescribeDTCSecurityIpHostsForSQLServerResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeDTCSecurityIpHostsForSQLServerResponseItemsWhiteListGroups(TeaModel):
    def __init__(self, security_ip_hosts=None, whitelist_group_name=None):
        # description: ECS实例的IP地址和Windows系统的计算机名。格式：ip,hostname。多个实例之间以英文分号（;）隔开。; 
        self.security_ip_hosts = security_ip_hosts  # type: str
        # description: 分布式事务白名单分组名称。; 
        self.whitelist_group_name = whitelist_group_name  # type: str

    def validate(self):
        self.validate_required(self.security_ip_hosts, 'security_ip_hosts')
        self.validate_required(self.whitelist_group_name, 'whitelist_group_name')

    def to_map(self):
        result = {}
        result['SecurityIpHosts'] = self.security_ip_hosts
        result['WhitelistGroupName'] = self.whitelist_group_name
        return result

    def from_map(self, map={}):
        self.security_ip_hosts = map.get('SecurityIpHosts')
        self.whitelist_group_name = map.get('WhitelistGroupName')
        return self


class DescribeDTCSecurityIpHostsForSQLServerResponseItems(TeaModel):
    def __init__(self, white_list_groups=None):
        self.white_list_groups = white_list_groups  # type: List[DescribeDTCSecurityIpHostsForSQLServerResponseItemsWhiteListGroups]

    def validate(self):
        self.validate_required(self.white_list_groups, 'white_list_groups')
        if self.white_list_groups:
            for k in self.white_list_groups:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['WhiteListGroups'] = []
        if self.white_list_groups is not None:
            for k in self.white_list_groups:
                result['WhiteListGroups'].append(k.to_map() if k else None)
        else:
            result['WhiteListGroups'] = None
        return result

    def from_map(self, map={}):
        self.white_list_groups = []
        if map.get('WhiteListGroups') is not None:
            for k in map.get('WhiteListGroups'):
                temp_model = DescribeDTCSecurityIpHostsForSQLServerResponseItemsWhiteListGroups()
                self.white_list_groups.append(temp_model.from_map(k))
        else:
            self.white_list_groups = None
        return self


class ModifyDTCSecurityIpHostsForSQLServerRequest(TeaModel):
    def __init__(self, security_token=None, dbinstance_id=None, security_ip_hosts=None, white_list_group_name=None,
                 region_id=None):
        self.security_token = security_token  # type: str
        # description: RDS实例ID。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: ECS实例的IP地址和Windows系统的计算机名。格式：ip,hostname。多个实例之间以英文分号（;）隔开。>计算机名查看方式请参见[设置分布式事务白名单](~~124321~~)。; 
        self.security_ip_hosts = security_ip_hosts  # type: str
        # description: 白名单分组名称。; 
        self.white_list_group_name = white_list_group_name  # type: str
        # description: RDS实例的地域ID，可以通过接口[DescribeRegions](~~26243~~)查看。; 
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.security_ip_hosts, 'security_ip_hosts')
        self.validate_required(self.white_list_group_name, 'white_list_group_name')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DBInstanceId'] = self.dbinstance_id
        result['SecurityIpHosts'] = self.security_ip_hosts
        result['WhiteListGroupName'] = self.white_list_group_name
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.security_ip_hosts = map.get('SecurityIpHosts')
        self.white_list_group_name = map.get('WhiteListGroupName')
        self.region_id = map.get('RegionId')
        return self


class ModifyDTCSecurityIpHostsForSQLServerResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, dtcset_result=None, task_id=None):
        # description: 请求ID。; 
        self.request_id = request_id    # type: str
        # description: RDS实例ID。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: 设置白名单的结果，取值：* **Success**：设置成功；* **Fail**：设置失败。; 
        self.dtcset_result = dtcset_result  # type: str
        # description: 设置任务ID。; 
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dtcset_result, 'dtcset_result')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['DTCSetResult'] = self.dtcset_result
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.dtcset_result = map.get('DTCSetResult')
        self.task_id = map.get('TaskId')
        return self


class DescribeDBInstanceIpHostnameRequest(TeaModel):
    def __init__(self, security_token=None, dbinstance_id=None, region_id=None):
        self.security_token = security_token  # type: str
        # description: RDS实例ID。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: RDS实例的地域ID，可以通过接口[DescribeRegions](~~26243~~)查看。; 
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DBInstanceId'] = self.dbinstance_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.region_id = map.get('RegionId')
        return self


class DescribeDBInstanceIpHostnameResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, ip_hostname_infos=None):
        # description: 请求ID。; 
        self.request_id = request_id    # type: str
        # description: 实例ID。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: RDS实例所在ECS实例的内网IP和ECS主机名，包含主备实例。格式：ip1,hostname1;ip2,hostname2。; 
        self.ip_hostname_infos = ip_hostname_infos  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.ip_hostname_infos, 'ip_hostname_infos')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['IpHostnameInfos'] = self.ip_hostname_infos
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.ip_hostname_infos = map.get('IpHostnameInfos')
        return self


class ModifyDBInstanceAutoUpgradeMinorVersionRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, auto_upgrade_minor_version=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.auto_upgrade_minor_version = auto_upgrade_minor_version  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.auto_upgrade_minor_version, 'auto_upgrade_minor_version')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['AutoUpgradeMinorVersion'] = self.auto_upgrade_minor_version
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.auto_upgrade_minor_version = map.get('AutoUpgradeMinorVersion')
        return self


class ModifyDBInstanceAutoUpgradeMinorVersionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeAvailableCrossRegionRequest(TeaModel):
    def __init__(self, region_id=None):
        # description: 地域ID。可以通过接口[DescribeRegions](~~26243~~)查看地域ID。; 
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        return self


class DescribeAvailableCrossRegionResponse(TeaModel):
    def __init__(self, request_id=None, regions=None):
        # description: 请求ID。; 
        self.request_id = request_id    # type: str
        self.regions = regions          # type: DescribeAvailableCrossRegionResponseRegions

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.regions, 'regions')
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        else:
            result['Regions'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Regions') is not None:
            temp_model = DescribeAvailableCrossRegionResponseRegions()
            self.regions = temp_model.from_map(map['Regions'])
        else:
            self.regions = None
        return self


class DescribeAvailableCrossRegionResponseRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region            # type: List[str]

    def validate(self):
        self.validate_required(self.region, 'region')

    def to_map(self):
        result = {}
        result['Region'] = self.region
        return result

    def from_map(self, map={}):
        self.region = map.get('Region')
        return self


class CheckCreateDdrDBInstanceRequest(TeaModel):
    def __init__(self, region_id=None, engine=None, engine_version=None, dbinstance_class=None,
                 dbinstance_storage=None, restore_type=None, backup_set_id=None, restore_time=None, source_region=None,
                 source_dbinstance_name=None, binlog_name=None, binlog_position=None, binlog_role=None):
        self.region_id = region_id      # type: str
        self.engine = engine            # type: str
        self.engine_version = engine_version  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_storage = dbinstance_storage  # type: int
        self.restore_type = restore_type  # type: str
        self.backup_set_id = backup_set_id  # type: str
        self.restore_time = restore_time  # type: str
        self.source_region = source_region  # type: str
        self.source_dbinstance_name = source_dbinstance_name  # type: str
        self.binlog_name = binlog_name  # type: str
        self.binlog_position = binlog_position  # type: str
        self.binlog_role = binlog_role  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.dbinstance_class, 'dbinstance_class')
        self.validate_required(self.dbinstance_storage, 'dbinstance_storage')
        self.validate_required(self.restore_type, 'restore_type')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        result['DBInstanceClass'] = self.dbinstance_class
        result['DBInstanceStorage'] = self.dbinstance_storage
        result['RestoreType'] = self.restore_type
        result['BackupSetId'] = self.backup_set_id
        result['RestoreTime'] = self.restore_time
        result['SourceRegion'] = self.source_region
        result['SourceDBInstanceName'] = self.source_dbinstance_name
        result['BinlogName'] = self.binlog_name
        result['BinlogPosition'] = self.binlog_position
        result['BinlogRole'] = self.binlog_role
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        self.dbinstance_class = map.get('DBInstanceClass')
        self.dbinstance_storage = map.get('DBInstanceStorage')
        self.restore_type = map.get('RestoreType')
        self.backup_set_id = map.get('BackupSetId')
        self.restore_time = map.get('RestoreTime')
        self.source_region = map.get('SourceRegion')
        self.source_dbinstance_name = map.get('SourceDBInstanceName')
        self.binlog_name = map.get('BinlogName')
        self.binlog_position = map.get('BinlogPosition')
        self.binlog_role = map.get('BinlogRole')
        return self


class CheckCreateDdrDBInstanceResponse(TeaModel):
    def __init__(self, request_id=None, is_valid=None):
        self.request_id = request_id    # type: str
        self.is_valid = is_valid        # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_valid, 'is_valid')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['IsValid'] = self.is_valid
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.is_valid = map.get('IsValid')
        return self


class DescribeAvailableRecoveryTimeRequest(TeaModel):
    def __init__(self, cross_backup_id=None, region_id=None):
        # description: 跨地域备份文件ID。可以通过接口[DescribeCrossRegionBackups](~~121733~~)查看备份集ID。; 
        self.cross_backup_id = cross_backup_id  # type: int
        # description: 地域ID。; 
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.cross_backup_id, 'cross_backup_id')

    def to_map(self):
        result = {}
        result['CrossBackupId'] = self.cross_backup_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.cross_backup_id = map.get('CrossBackupId')
        self.region_id = map.get('RegionId')
        return self


class DescribeAvailableRecoveryTimeResponse(TeaModel):
    def __init__(self, request_id=None, recovery_begin_time=None, recovery_end_time=None, region_id=None,
                 cross_backup_id=None):
        # description: 请求ID。; 
        self.request_id = request_id    # type: str
        # description: 跨地域备份文件可恢复的起始时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z（UTC时间）。; 
        self.recovery_begin_time = recovery_begin_time  # type: str
        # description: 跨地域备份文件可恢复的结束时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z（UTC时间）。; 
        self.recovery_end_time = recovery_end_time  # type: str
        # description: 源实例所在地域ID。; 
        self.region_id = region_id      # type: str
        # description: 跨地域备份文件ID。; 
        self.cross_backup_id = cross_backup_id  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.recovery_begin_time, 'recovery_begin_time')
        self.validate_required(self.recovery_end_time, 'recovery_end_time')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.cross_backup_id, 'cross_backup_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RecoveryBeginTime'] = self.recovery_begin_time
        result['RecoveryEndTime'] = self.recovery_end_time
        result['RegionId'] = self.region_id
        result['CrossBackupId'] = self.cross_backup_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.recovery_begin_time = map.get('RecoveryBeginTime')
        self.recovery_end_time = map.get('RecoveryEndTime')
        self.region_id = map.get('RegionId')
        self.cross_backup_id = map.get('CrossBackupId')
        return self


class DescribeCrossRegionLogBackupFilesRequest(TeaModel):
    def __init__(self, dbinstance_id=None, region_id=None, cross_backup_region=None, start_time=None, end_time=None,
                 page_size=None, page_number=None):
        # description: 实例ID。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: 实例所在地域ID。可以通过接口[DescribeRegions](~~26243~~)查看地域ID。; 
        self.region_id = region_id      # type: str
        # description: 跨地域备份目的地域ID。可以通过接口[DescribeCrossRegionBackupDBInstance](~~121737~~)查看地域ID。; 
        self.cross_backup_region = cross_backup_region  # type: str
        # description: 查询开始时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm</i>Z（UTC时间）。; 
        self.start_time = start_time    # type: str
        # description: 查询结束时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm</i>Z（UTC时间）。; 
        self.end_time = end_time        # type: str
        # description: 每页记录数，取值：* **30**；* **50**；* **100**。默认值：30。; 
        self.page_size = page_size      # type: int
        # description: 页码，取值：大于0且不超过Integer的最大值。默认值：**1**。; 
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['RegionId'] = self.region_id
        result['CrossBackupRegion'] = self.cross_backup_region
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.region_id = map.get('RegionId')
        self.cross_backup_region = map.get('CrossBackupRegion')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeCrossRegionLogBackupFilesResponse(TeaModel):
    def __init__(self, request_id=None, region_id=None, dbinstance_id=None, start_time=None, end_time=None,
                 total_record_count=None, page_record_count=None, page_number=None, items=None):
        # description: 请求ID。; 
        self.request_id = request_id    # type: str
        # description: 实例所在地域ID。; 
        self.region_id = region_id      # type: str
        # description: 实例ID。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: 查询开始时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm</i>Z（UTC时间）。; 
        self.start_time = start_time    # type: str
        # description: 查询结束时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm</i>Z（UTC时间）。; 
        self.end_time = end_time        # type: str
        # description: 总记录数。; 
        self.total_record_count = total_record_count  # type: int
        # description: 本页备份文件个数。; 
        self.page_record_count = page_record_count  # type: int
        # description: 页码，取值：大于0且不超过Integer的最大值。默认值：**1**。; 
        self.page_number = page_number  # type: int
        # description: 跨地域日志备份列表。
        self.items = items              # type: DescribeCrossRegionLogBackupFilesResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RegionId'] = self.region_id
        result['DBInstanceId'] = self.dbinstance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['TotalRecordCount'] = self.total_record_count
        result['PageRecordCount'] = self.page_record_count
        result['PageNumber'] = self.page_number
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.region_id = map.get('RegionId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_record_count = map.get('PageRecordCount')
        self.page_number = map.get('PageNumber')
        if map.get('Items') is not None:
            temp_model = DescribeCrossRegionLogBackupFilesResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeCrossRegionLogBackupFilesResponseItemsItem(TeaModel):
    def __init__(self, cross_log_backup_id=None, cross_backup_region=None, cross_log_backup_size=None,
                 log_begin_time=None, log_end_time=None, cross_download_link=None, cross_intranet_download_link=None,
                 link_expired_time=None, log_file_name=None, instance_id=None):
        # description: 跨地域日志备份文件ID。; 
        self.cross_log_backup_id = cross_log_backup_id  # type: int
        # description: 跨地域备份目的地域ID。; 
        self.cross_backup_region = cross_backup_region  # type: str
        # description: 跨地域日志备份文件大小，单位：Byte。; 
        self.cross_log_backup_size = cross_log_backup_size  # type: int
        # description: 跨地域日志备份文件记录的开始时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm</i>Z（UTC时间）。; 
        self.log_begin_time = log_begin_time  # type: str
        # description: 跨地域日志备份文件记录的结束时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm</i>Z（UTC时间）。; 
        self.log_end_time = log_end_time  # type: str
        # description: 跨地域日志备份外网下载链接。; 
        self.cross_download_link = cross_download_link  # type: str
        # description: 跨地域日志备份内网下载链接。; 
        self.cross_intranet_download_link = cross_intranet_download_link  # type: str
        # description: 下载链接过期时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z（UTC时间）。; 
        self.link_expired_time = link_expired_time  # type: str
        # description: 跨地域日志备份文件名称。; 
        self.log_file_name = log_file_name  # type: str
        # description: 实例编号。; 
        self.instance_id = instance_id  # type: int

    def validate(self):
        self.validate_required(self.cross_log_backup_id, 'cross_log_backup_id')
        self.validate_required(self.cross_backup_region, 'cross_backup_region')
        self.validate_required(self.cross_log_backup_size, 'cross_log_backup_size')
        self.validate_required(self.log_begin_time, 'log_begin_time')
        self.validate_required(self.log_end_time, 'log_end_time')
        self.validate_required(self.cross_download_link, 'cross_download_link')
        self.validate_required(self.cross_intranet_download_link, 'cross_intranet_download_link')
        self.validate_required(self.link_expired_time, 'link_expired_time')
        self.validate_required(self.log_file_name, 'log_file_name')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['CrossLogBackupId'] = self.cross_log_backup_id
        result['CrossBackupRegion'] = self.cross_backup_region
        result['CrossLogBackupSize'] = self.cross_log_backup_size
        result['LogBeginTime'] = self.log_begin_time
        result['LogEndTime'] = self.log_end_time
        result['CrossDownloadLink'] = self.cross_download_link
        result['CrossIntranetDownloadLink'] = self.cross_intranet_download_link
        result['LinkExpiredTime'] = self.link_expired_time
        result['LogFileName'] = self.log_file_name
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.cross_log_backup_id = map.get('CrossLogBackupId')
        self.cross_backup_region = map.get('CrossBackupRegion')
        self.cross_log_backup_size = map.get('CrossLogBackupSize')
        self.log_begin_time = map.get('LogBeginTime')
        self.log_end_time = map.get('LogEndTime')
        self.cross_download_link = map.get('CrossDownloadLink')
        self.cross_intranet_download_link = map.get('CrossIntranetDownloadLink')
        self.link_expired_time = map.get('LinkExpiredTime')
        self.log_file_name = map.get('LogFileName')
        self.instance_id = map.get('InstanceId')
        return self


class DescribeCrossRegionLogBackupFilesResponseItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[DescribeCrossRegionLogBackupFilesResponseItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = DescribeCrossRegionLogBackupFilesResponseItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class ModifyInstanceCrossBackupPolicyRequest(TeaModel):
    def __init__(self, dbinstance_id=None, region_id=None, cross_backup_type=None, log_backup_enabled=None,
                 backup_enabled=None, cross_backup_region=None, retent_type=None, retention=None):
        # description: 实例ID。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: 源实例地域ID，可以通过接口[DescribeRegions](~~26243~~)查看地域ID。; 
        self.region_id = region_id      # type: str
        # description: 跨地域备份保存类型。默认值：**1**，表示每个备份都保存。; 
        self.cross_backup_type = cross_backup_type  # type: str
        # description: 跨地域日志备份开关，取值：* **0**：关闭；* **1**：开启。; 
        self.log_backup_enabled = log_backup_enabled  # type: str
        # description: 跨地域备份总开关（数据备份+日志备份），取值：* **0**：关闭；* **1**：开启。; 
        self.backup_enabled = backup_enabled  # type: str
        # description: 跨地域备份的目的地域ID。; 
        self.cross_backup_region = cross_backup_region  # type: str
        # description: 跨地域备份保留方式。默认值：**1**，表示按时长保留。; 
        self.retent_type = retent_type  # type: int
        # description: 跨地域备份保留天数，取值：**7~1825**。; 
        self.retention = retention      # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['RegionId'] = self.region_id
        result['CrossBackupType'] = self.cross_backup_type
        result['LogBackupEnabled'] = self.log_backup_enabled
        result['BackupEnabled'] = self.backup_enabled
        result['CrossBackupRegion'] = self.cross_backup_region
        result['RetentType'] = self.retent_type
        result['Retention'] = self.retention
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.region_id = map.get('RegionId')
        self.cross_backup_type = map.get('CrossBackupType')
        self.log_backup_enabled = map.get('LogBackupEnabled')
        self.backup_enabled = map.get('BackupEnabled')
        self.cross_backup_region = map.get('CrossBackupRegion')
        self.retent_type = map.get('RetentType')
        self.retention = map.get('Retention')
        return self


class ModifyInstanceCrossBackupPolicyResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, region_id=None, cross_backup_region=None,
                 cross_backup_type=None, backup_enabled=None, log_backup_enabled=None, retent_type=None, retention=None):
        # description: 请求ID。; 
        self.request_id = request_id    # type: str
        # description: 实例ID。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: 源实例地域ID，可以通过接口[DescribeRegions](~~26243~~)查看地域ID。; 
        self.region_id = region_id      # type: str
        # description: 跨地域备份的目的地域ID。; 
        self.cross_backup_region = cross_backup_region  # type: str
        # description: 跨地域备份保存类型。默认值：**1**，表示每个备份都保存。; 
        self.cross_backup_type = cross_backup_type  # type: str
        # description: 跨地域备份总开关，取值：* **0**：关闭；* **1**：开启。; 
        self.backup_enabled = backup_enabled  # type: str
        # description: 跨地域日志备份开关，取值：* **0**：关闭；* **1**：开启。; 
        self.log_backup_enabled = log_backup_enabled  # type: str
        # description: 跨地域备份保留方式。默认值：**1**，表示按时长保留。; 
        self.retent_type = retent_type  # type: int
        # description: 跨地域备份保留天数，取值：**7~1825**。; 
        self.retention = retention      # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.cross_backup_region, 'cross_backup_region')
        self.validate_required(self.cross_backup_type, 'cross_backup_type')
        self.validate_required(self.backup_enabled, 'backup_enabled')
        self.validate_required(self.log_backup_enabled, 'log_backup_enabled')
        self.validate_required(self.retent_type, 'retent_type')
        self.validate_required(self.retention, 'retention')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['RegionId'] = self.region_id
        result['CrossBackupRegion'] = self.cross_backup_region
        result['CrossBackupType'] = self.cross_backup_type
        result['BackupEnabled'] = self.backup_enabled
        result['LogBackupEnabled'] = self.log_backup_enabled
        result['RetentType'] = self.retent_type
        result['Retention'] = self.retention
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.region_id = map.get('RegionId')
        self.cross_backup_region = map.get('CrossBackupRegion')
        self.cross_backup_type = map.get('CrossBackupType')
        self.backup_enabled = map.get('BackupEnabled')
        self.log_backup_enabled = map.get('LogBackupEnabled')
        self.retent_type = map.get('RetentType')
        self.retention = map.get('Retention')
        return self


class CreateDdrInstanceRequest(TeaModel):
    def __init__(self, region_id=None, engine=None, engine_version=None, dbinstance_class=None,
                 dbinstance_storage=None, system_dbcharset=None, dbinstance_net_type=None, dbinstance_description=None,
                 security_iplist=None, client_token=None, pay_type=None, zone_id=None, instance_network_type=None,
                 connection_mode=None, vpcid=None, v_switch_id=None, private_ip_address=None, used_time=None, period=None,
                 resource_group_id=None, restore_type=None, backup_set_id=None, restore_time=None, source_region=None,
                 source_dbinstance_name=None, dbinstance_storage_type=None, binlog_name=None, binlog_position=None, binlog_role=None):
        # description: 目的地域ID，可以通过接口[DescribeRegions](~~26243~~)查看地域ID。; 
        self.region_id = region_id      # type: str
        # description: 目的数据库类型，取值：**MySQL**。; 
        self.engine = engine            # type: str
        # description: 目的数据库版本，取值：* **5.6**；* **5.7**。; 
        self.engine_version = engine_version  # type: str
        # description: 目的实例规格，详见[实例规格表](~~26312~~)。; 
        self.dbinstance_class = dbinstance_class  # type: str
        # description: 目的实例存储空间，取值： **5~2000**。每5G进行递增，单位：GB。详见[实例规格表](~~26312~~)。; 
        self.dbinstance_storage = dbinstance_storage  # type: int
        # description: 目的实例的字符集，取值：* **utf8**；* **gbk**；* **latin1**；* **utf8mb4**。; 
        self.system_dbcharset = system_dbcharset  # type: str
        # description: 目的实例的网络连接类型，取值：* **Internet**：公网连接；* **Intranet**：内网连接。; 
        self.dbinstance_net_type = dbinstance_net_type  # type: str
        # description: 目的实例名称，长度为2~256个字符。以中文、英文字母开头，可以包含数字、中文、英文、下划线（_）、短横线（-）。>不能以 http:// 和 https:// 开头。; 
        self.dbinstance_description = dbinstance_description  # type: str
        # description: 目的实例的[IP白名单](~~43185~~)，多个IP地址请以英文逗号（,）隔开，不可重复，最多1000个。支持如下两种格式：* IP地址形式，例如：10.23.12.24；* CIDR形式，例如：10.23.12.24/24（无类域间路由，24表示了地址中前缀的长度，范围为1~32）。; 
        self.security_iplist = security_iplist  # type: str
        # description: 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII字符，且该参数值中不能包含非ASCII字符。; 
        self.client_token = client_token  # type: str
        # description: 目的实例的付费类型，取值：* **Postpaid**：后付费（按量付费）；* **Prepaid**：预付费（包年包月）。; 
        self.pay_type = pay_type        # type: str
        # description: 目的实例的可用区ID。多可用区用英文冒号（:）分隔。> 指定了VPC和交换机时，为匹配交换机对应的可用区，该参数必填。; 
        self.zone_id = zone_id          # type: str
        # description: 目的实例的网络类型，取值：* **VPC**：VPC网络；* **Classic**：经典网络。默认创建经典网络类型的实例。>当本参数值为 **VPC**时，还需要传入参数**VpcId**、**VSwitchId**。; 
        self.instance_network_type = instance_network_type  # type: str
        # description: 目的实例的访问模式，取值：* **Standard**：标准访问模式；* **Safe**：数据库代理模式。默认值：**Standard**。; 
        self.connection_mode = connection_mode  # type: str
        # description: 目的实例的VPC ID。当**InstanceNetworkType**=**VPC**时，本参数可用。>如果传入此参数，您还需要传入参数**ZoneId**。; 
        self.vpcid = vpcid              # type: str
        # description: 目的实例的VSwitch ID，多个值用英文逗号（,）隔开。当**InstanceNetworkType**=**VPC**时，本参数可用。>如果传入此参数，您还需要传入参数**ZoneId**。; 
        self.v_switch_id = v_switch_id  # type: str
        # description: 设置目的实例的内网IP，需要在指定交换机的IP地址范围内。系统默认通过**VPCId**和**VSwitchId**自动分配。; 
        self.private_ip_address = private_ip_address  # type: str
        # description: 指定购买时长，取值：* 当参数**Period**为**Year**时，UsedTime取值为**1~3**；* 当参数**Period**为**Month**时，UsedTime取值为**1~9**。> 若付费类型为**Prepaid**则该参数必须传入。; 
        self.used_time = used_time      # type: str
        # description: 指定预付费目的实例为包年或者包月类型，取值：* **Year**：包年；* **Month**：包月。> 若付费类型为**Prepaid**则该参数必须传入。; 
        self.period = period            # type: str
        # description: 资源组ID。; 
        self.resource_group_id = resource_group_id  # type: str
        # description: 恢复方式，取值：* **0**：基于备份集恢复，您还需要传入参数**BackupSetID**；* **1**：基于时间点恢复，您还需要传入参数**RestoreTime**、**SourceRegion**、**SourceDBInstanceName**。; 
        self.restore_type = restore_type  # type: str
        # description: 基于备份集恢复时，使用的备份集的ID。可以通过接口[DescribeCrossRegionBackups](~~121733~~)查看备份集ID。>**RestoreTyp**e=**0**时必传。; 
        self.backup_set_id = backup_set_id  # type: str
        # description: 基于时间点恢复时，要恢复的时间节点，需要早于当前时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z（UTC时间）。>**RestoreType**=**1**时必传 。; 
        self.restore_time = restore_time  # type: str
        # description: 基于时间点恢复时，源地域的ID。>**RestoreType**=**1**时必传。; 
        self.source_region = source_region  # type: str
        # description: 基于时间点恢复时，源实例的ID。>**RestoreType**=**1**时必传。; 
        self.source_dbinstance_name = source_dbinstance_name  # type: str
        # description: 目的实例存储类型，当前仅支持SSD本地盘，默认值：**local_ssd**。; 
        self.dbinstance_storage_type = dbinstance_storage_type  # type: str
        self.binlog_name = binlog_name  # type: str
        self.binlog_position = binlog_position  # type: str
        self.binlog_role = binlog_role  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.dbinstance_class, 'dbinstance_class')
        self.validate_required(self.dbinstance_storage, 'dbinstance_storage')
        self.validate_required(self.dbinstance_net_type, 'dbinstance_net_type')
        self.validate_required(self.security_iplist, 'security_iplist')
        self.validate_required(self.pay_type, 'pay_type')
        self.validate_required(self.restore_type, 'restore_type')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        result['DBInstanceClass'] = self.dbinstance_class
        result['DBInstanceStorage'] = self.dbinstance_storage
        result['SystemDBCharset'] = self.system_dbcharset
        result['DBInstanceNetType'] = self.dbinstance_net_type
        result['DBInstanceDescription'] = self.dbinstance_description
        result['SecurityIPList'] = self.security_iplist
        result['ClientToken'] = self.client_token
        result['PayType'] = self.pay_type
        result['ZoneId'] = self.zone_id
        result['InstanceNetworkType'] = self.instance_network_type
        result['ConnectionMode'] = self.connection_mode
        result['VPCId'] = self.vpcid
        result['VSwitchId'] = self.v_switch_id
        result['PrivateIpAddress'] = self.private_ip_address
        result['UsedTime'] = self.used_time
        result['Period'] = self.period
        result['ResourceGroupId'] = self.resource_group_id
        result['RestoreType'] = self.restore_type
        result['BackupSetId'] = self.backup_set_id
        result['RestoreTime'] = self.restore_time
        result['SourceRegion'] = self.source_region
        result['SourceDBInstanceName'] = self.source_dbinstance_name
        result['DBInstanceStorageType'] = self.dbinstance_storage_type
        result['BinlogName'] = self.binlog_name
        result['BinlogPosition'] = self.binlog_position
        result['BinlogRole'] = self.binlog_role
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        self.dbinstance_class = map.get('DBInstanceClass')
        self.dbinstance_storage = map.get('DBInstanceStorage')
        self.system_dbcharset = map.get('SystemDBCharset')
        self.dbinstance_net_type = map.get('DBInstanceNetType')
        self.dbinstance_description = map.get('DBInstanceDescription')
        self.security_iplist = map.get('SecurityIPList')
        self.client_token = map.get('ClientToken')
        self.pay_type = map.get('PayType')
        self.zone_id = map.get('ZoneId')
        self.instance_network_type = map.get('InstanceNetworkType')
        self.connection_mode = map.get('ConnectionMode')
        self.vpcid = map.get('VPCId')
        self.v_switch_id = map.get('VSwitchId')
        self.private_ip_address = map.get('PrivateIpAddress')
        self.used_time = map.get('UsedTime')
        self.period = map.get('Period')
        self.resource_group_id = map.get('ResourceGroupId')
        self.restore_type = map.get('RestoreType')
        self.backup_set_id = map.get('BackupSetId')
        self.restore_time = map.get('RestoreTime')
        self.source_region = map.get('SourceRegion')
        self.source_dbinstance_name = map.get('SourceDBInstanceName')
        self.dbinstance_storage_type = map.get('DBInstanceStorageType')
        self.binlog_name = map.get('BinlogName')
        self.binlog_position = map.get('BinlogPosition')
        self.binlog_role = map.get('BinlogRole')
        return self


class CreateDdrInstanceResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, order_id=None, connection_string=None, port=None):
        # description: 请求ID。; 
        self.request_id = request_id    # type: str
        # description: 新实例ID。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: 订单ID。; 
        self.order_id = order_id        # type: str
        # description: 新实例连接地址。>参数**DBInstanceNetType**决定该地址为内网或外网。; 
        self.connection_string = connection_string  # type: str
        # description: 新实例连接端口。>参数**DBInstanceNetType**决定该端口为内网端口或外网端口。; 
        self.port = port                # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.connection_string, 'connection_string')
        self.validate_required(self.port, 'port')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['OrderId'] = self.order_id
        result['ConnectionString'] = self.connection_string
        result['Port'] = self.port
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.order_id = map.get('OrderId')
        self.connection_string = map.get('ConnectionString')
        self.port = map.get('Port')
        return self


class DescribeCrossRegionBackupDBInstanceRequest(TeaModel):
    def __init__(self, region_id=None, dbinstance_id=None, page_size=None, page_number=None):
        self.region_id = region_id      # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DBInstanceId'] = self.dbinstance_id
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeCrossRegionBackupDBInstanceResponse(TeaModel):
    def __init__(self, request_id=None, region_id=None, total_records=None, page_size=None, page_number=None,
                 items_numbers=None, items=None):
        self.request_id = request_id    # type: str
        self.region_id = region_id      # type: str
        self.total_records = total_records  # type: int
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.items_numbers = items_numbers  # type: int
        self.items = items              # type: DescribeCrossRegionBackupDBInstanceResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.total_records, 'total_records')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.items_numbers, 'items_numbers')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RegionId'] = self.region_id
        result['TotalRecords'] = self.total_records
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['ItemsNumbers'] = self.items_numbers
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.region_id = map.get('RegionId')
        self.total_records = map.get('TotalRecords')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.items_numbers = map.get('ItemsNumbers')
        if map.get('Items') is not None:
            temp_model = DescribeCrossRegionBackupDBInstanceResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeCrossRegionBackupDBInstanceResponseItemsItem(TeaModel):
    def __init__(self, dbinstance_id=None, dbinstance_description=None, dbinstance_status=None, engine=None,
                 engine_version=None, cross_backup_region=None, cross_backup_type=None, backup_enabled=None,
                 log_backup_enabled=None, log_backup_enabled_time=None, backup_enabled_time=None, retent_type=None, retention=None,
                 lock_mode=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.dbinstance_status = dbinstance_status  # type: str
        self.engine = engine            # type: str
        self.engine_version = engine_version  # type: str
        self.cross_backup_region = cross_backup_region  # type: str
        self.cross_backup_type = cross_backup_type  # type: str
        self.backup_enabled = backup_enabled  # type: str
        self.log_backup_enabled = log_backup_enabled  # type: str
        self.log_backup_enabled_time = log_backup_enabled_time  # type: str
        self.backup_enabled_time = backup_enabled_time  # type: str
        self.retent_type = retent_type  # type: int
        self.retention = retention      # type: int
        self.lock_mode = lock_mode      # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbinstance_description, 'dbinstance_description')
        self.validate_required(self.dbinstance_status, 'dbinstance_status')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.cross_backup_region, 'cross_backup_region')
        self.validate_required(self.cross_backup_type, 'cross_backup_type')
        self.validate_required(self.backup_enabled, 'backup_enabled')
        self.validate_required(self.log_backup_enabled, 'log_backup_enabled')
        self.validate_required(self.log_backup_enabled_time, 'log_backup_enabled_time')
        self.validate_required(self.backup_enabled_time, 'backup_enabled_time')
        self.validate_required(self.retent_type, 'retent_type')
        self.validate_required(self.retention, 'retention')
        self.validate_required(self.lock_mode, 'lock_mode')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBInstanceDescription'] = self.dbinstance_description
        result['DBInstanceStatus'] = self.dbinstance_status
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        result['CrossBackupRegion'] = self.cross_backup_region
        result['CrossBackupType'] = self.cross_backup_type
        result['BackupEnabled'] = self.backup_enabled
        result['LogBackupEnabled'] = self.log_backup_enabled
        result['LogBackupEnabledTime'] = self.log_backup_enabled_time
        result['BackupEnabledTime'] = self.backup_enabled_time
        result['RetentType'] = self.retent_type
        result['Retention'] = self.retention
        result['LockMode'] = self.lock_mode
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbinstance_description = map.get('DBInstanceDescription')
        self.dbinstance_status = map.get('DBInstanceStatus')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        self.cross_backup_region = map.get('CrossBackupRegion')
        self.cross_backup_type = map.get('CrossBackupType')
        self.backup_enabled = map.get('BackupEnabled')
        self.log_backup_enabled = map.get('LogBackupEnabled')
        self.log_backup_enabled_time = map.get('LogBackupEnabledTime')
        self.backup_enabled_time = map.get('BackupEnabledTime')
        self.retent_type = map.get('RetentType')
        self.retention = map.get('Retention')
        self.lock_mode = map.get('LockMode')
        return self


class DescribeCrossRegionBackupDBInstanceResponseItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[DescribeCrossRegionBackupDBInstanceResponseItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = DescribeCrossRegionBackupDBInstanceResponseItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class DescribeInstanceCrossBackupPolicyRequest(TeaModel):
    def __init__(self, dbinstance_id=None, region_id=None):
        # description: 实例ID。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: 地域ID，可以通过接口[DescribeRegions](~~26243~~)查看地域ID。; 
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.region_id = map.get('RegionId')
        return self


class DescribeInstanceCrossBackupPolicyResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, dbinstance_description=None, dbinstance_status=None,
                 engine=None, engine_version=None, region_id=None, cross_backup_region=None, cross_backup_type=None,
                 backup_enabled_time=None, backup_enabled=None, log_backup_enabled=None, log_backup_enabled_time=None,
                 retent_type=None, retention=None, lock_mode=None):
        # description: 请求ID。; 
        self.request_id = request_id    # type: str
        # description: 实例ID。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: 实例名称，长度为2~256个字符。以中文、英文字母开头，可以包含数字、中文、英文、下划线（_）、短横线（-）。>不能以 http:// 和 https:// 开头。; 
        self.dbinstance_description = dbinstance_description  # type: str
        # description: 实例状态。详情请参见[实例状态表](~~26315~~)。; 
        self.dbinstance_status = dbinstance_status  # type: str
        # description: 数据库类型。; 
        self.engine = engine            # type: str
        # description: 数据库版本。; 
        self.engine_version = engine_version  # type: str
        # description: 实例所在地域ID。; 
        self.region_id = region_id      # type: str
        # description: 跨地域备份的目的地域ID。; 
        self.cross_backup_region = cross_backup_region  # type: str
        # description: 跨地域备份保存类型。默认值：**1**，表示每个备份都保存。; 
        self.cross_backup_type = cross_backup_type  # type: str
        # description: 跨地域备份开启时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z（UTC时间）。; 
        self.backup_enabled_time = backup_enabled_time  # type: str
        # description: 跨地域备份总开关，取值：* **Disable**：关闭；* **Enable**：开启。; 
        self.backup_enabled = backup_enabled  # type: str
        # description: 跨地域日志备份开关，取值：* **Disable**：关闭；* **Enable**：开启。; 
        self.log_backup_enabled = log_backup_enabled  # type: str
        # description: 跨地域日志备份开启时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z（UTC时间）。; 
        self.log_backup_enabled_time = log_backup_enabled_time  # type: str
        # description: 跨地域备份保留方式。默认值：**1**，表示按时长保留。; 
        self.retent_type = retent_type  # type: int
        # description: 跨地域备份保留天数，取值：**7~1825**。; 
        self.retention = retention      # type: int
        # description: 实例锁定状态，取值：* **Unlock**：正常，没有锁定；* **ManualLock**：手动触发锁定；* **LockByExpiration**：实例过期自动锁定；* **LockByRestoration**：实例回滚前的自动锁定；* **LockByDiskQuota**：实例空间满自动锁定，不可访问实例。; 
        self.lock_mode = lock_mode      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbinstance_description, 'dbinstance_description')
        self.validate_required(self.dbinstance_status, 'dbinstance_status')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.cross_backup_region, 'cross_backup_region')
        self.validate_required(self.cross_backup_type, 'cross_backup_type')
        self.validate_required(self.backup_enabled_time, 'backup_enabled_time')
        self.validate_required(self.backup_enabled, 'backup_enabled')
        self.validate_required(self.log_backup_enabled, 'log_backup_enabled')
        self.validate_required(self.log_backup_enabled_time, 'log_backup_enabled_time')
        self.validate_required(self.retent_type, 'retent_type')
        self.validate_required(self.retention, 'retention')
        self.validate_required(self.lock_mode, 'lock_mode')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['DBInstanceDescription'] = self.dbinstance_description
        result['DBInstanceStatus'] = self.dbinstance_status
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        result['RegionId'] = self.region_id
        result['CrossBackupRegion'] = self.cross_backup_region
        result['CrossBackupType'] = self.cross_backup_type
        result['BackupEnabledTime'] = self.backup_enabled_time
        result['BackupEnabled'] = self.backup_enabled
        result['LogBackupEnabled'] = self.log_backup_enabled
        result['LogBackupEnabledTime'] = self.log_backup_enabled_time
        result['RetentType'] = self.retent_type
        result['Retention'] = self.retention
        result['LockMode'] = self.lock_mode
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbinstance_description = map.get('DBInstanceDescription')
        self.dbinstance_status = map.get('DBInstanceStatus')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        self.region_id = map.get('RegionId')
        self.cross_backup_region = map.get('CrossBackupRegion')
        self.cross_backup_type = map.get('CrossBackupType')
        self.backup_enabled_time = map.get('BackupEnabledTime')
        self.backup_enabled = map.get('BackupEnabled')
        self.log_backup_enabled = map.get('LogBackupEnabled')
        self.log_backup_enabled_time = map.get('LogBackupEnabledTime')
        self.retent_type = map.get('RetentType')
        self.retention = map.get('Retention')
        self.lock_mode = map.get('LockMode')
        return self


class DescribeCrossRegionBackupsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, region_id=None, cross_backup_region=None, cross_backup_id=None,
                 start_time=None, end_time=None, page_size=None, page_number=None, backup_id=None):
        # description: 实例ID。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: 实例所在地域ID。; 
        self.region_id = region_id      # type: str
        # description: 跨地域备份目的地域ID。; 
        self.cross_backup_region = cross_backup_region  # type: str
        # description: 跨地域备份文件ID。>**CrossBackupId**和起止时间参数（**StartTime**、**EndTime**）必须传入其中一组。; 
        self.cross_backup_id = cross_backup_id  # type: int
        # description: 查询开始时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm</i>Z（UTC时间）。; 
        self.start_time = start_time    # type: str
        # description: 查询结束时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm</i>Z（UTC时间）。; 
        self.end_time = end_time        # type: str
        # description: 每页记录数，取值：* **30**；* **50**；* **100**。默认值：30。; 
        self.page_size = page_size      # type: int
        # description: 页码，取值：大于0且不超过Integer的最大值。默认值：**1**。; 
        self.page_number = page_number  # type: int
        self.backup_id = backup_id      # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['RegionId'] = self.region_id
        result['CrossBackupRegion'] = self.cross_backup_region
        result['CrossBackupId'] = self.cross_backup_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['BackupId'] = self.backup_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.region_id = map.get('RegionId')
        self.cross_backup_region = map.get('CrossBackupRegion')
        self.cross_backup_id = map.get('CrossBackupId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.backup_id = map.get('BackupId')
        return self


class DescribeCrossRegionBackupsResponse(TeaModel):
    def __init__(self, request_id=None, region_id=None, start_time=None, end_time=None, total_record_count=None,
                 page_record_count=None, page_number=None, items=None):
        # description: 请求ID。; 
        self.request_id = request_id    # type: str
        # description: 实例所在地域ID。; 
        self.region_id = region_id      # type: str
        # description: 查询开始时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm</i>Z（UTC时间）。; 
        self.start_time = start_time    # type: str
        # description: 查询结束时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm</i>Z（UTC时间）。; 
        self.end_time = end_time        # type: str
        # description: 总记录数。; 
        self.total_record_count = total_record_count  # type: int
        # description: 本页备份文件个数。; 
        self.page_record_count = page_record_count  # type: int
        # description: 页码，取值：大于0且不超过Integer的最大值。默认值：**1**。; 
        self.page_number = page_number  # type: int
        # description: 跨地域备份列表。
        self.items = items              # type: DescribeCrossRegionBackupsResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RegionId'] = self.region_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['TotalRecordCount'] = self.total_record_count
        result['PageRecordCount'] = self.page_record_count
        result['PageNumber'] = self.page_number
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.region_id = map.get('RegionId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_record_count = map.get('PageRecordCount')
        self.page_number = map.get('PageNumber')
        if map.get('Items') is not None:
            temp_model = DescribeCrossRegionBackupsResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeCrossRegionBackupsResponseItemsItemRestoreRegions(TeaModel):
    def __init__(self, restore_region=None):
        # RestoreRegion
        self.restore_region = restore_region  # type: List[str]

    def validate(self):
        self.validate_required(self.restore_region, 'restore_region')

    def to_map(self):
        result = {}
        result['RestoreRegion'] = self.restore_region
        return result

    def from_map(self, map={}):
        self.restore_region = map.get('RestoreRegion')
        return self


class DescribeCrossRegionBackupsResponseItemsItem(TeaModel):
    def __init__(self, cross_backup_id=None, cross_backup_region=None, backup_set_status=None,
                 backup_start_time=None, backup_end_time=None, backup_type=None, backup_method=None, cross_backup_set_size=None,
                 cross_backup_set_file=None, cross_backup_download_link=None, engine=None, engine_version=None,
                 cross_backup_set_location=None, backup_set_scale=None, instance_id=None, dbinstance_storage_type=None, category=None,
                 consistent_time=None, restore_regions=None):
        # description: 跨地域备份文件ID。; 
        self.cross_backup_id = cross_backup_id  # type: int
        # description: 跨地域备份的目的地域ID。; 
        self.cross_backup_region = cross_backup_region  # type: str
        # description: 备份文件状态，取值：* **0**：完成备份；* **1**：备份失败。; 
        self.backup_set_status = backup_set_status  # type: int
        # description: 跨地域备份开始时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm</i>Z（UTC时间）。; 
        self.backup_start_time = backup_start_time  # type: str
        # description: 跨地域备份结束时间。格式：<i>yyyy-MM-dd</i>T<i>HH:mm</i>Z（UTC时间）。; 
        self.backup_end_time = backup_end_time  # type: str
        # description: 跨地域备份类型，取值：* **F**：全量；* **I**：增量。; 
        self.backup_type = backup_type  # type: str
        # description: 跨地域备份方式，取值：* **L**：逻辑备份；* **P**：物理备份。; 
        self.backup_method = backup_method  # type: str
        # description: 跨地域备份文件大小，单位：Byte。; 
        self.cross_backup_set_size = cross_backup_set_size  # type: int
        # description: 跨地域备份文件压缩包名称。; 
        self.cross_backup_set_file = cross_backup_set_file  # type: str
        # description: 跨地域备份文件外网下载链接。; 
        self.cross_backup_download_link = cross_backup_download_link  # type: str
        # description: 数据库类型。; 
        self.engine = engine            # type: str
        # description: 数据库版本。; 
        self.engine_version = engine_version  # type: str
        # description: 备份文件存储位置。; 
        self.cross_backup_set_location = cross_backup_set_location  # type: str
        # description: 备份文件的备份策略，取值：* **0**：实例备份；* **1**：单库备份。; 
        self.backup_set_scale = backup_set_scale  # type: int
        # description: 实例编号。用于区分该备份集产生于主实例或备实例。; 
        self.instance_id = instance_id  # type: int
        # description: 存储类型。; 
        self.dbinstance_storage_type = dbinstance_storage_type  # type: str
        # description: 实例系列，取值：* **Basic**：基础版；* **HighAvailability**：高可用版；* **Finance**：金融版（仅中国站支持）。; 
        self.category = category        # type: str
        # description: 备份文件里数据的时间点。; 
        self.consistent_time = consistent_time  # type: str
        self.restore_regions = restore_regions  # type: DescribeCrossRegionBackupsResponseItemsItemRestoreRegions

    def validate(self):
        self.validate_required(self.cross_backup_id, 'cross_backup_id')
        self.validate_required(self.cross_backup_region, 'cross_backup_region')
        self.validate_required(self.backup_set_status, 'backup_set_status')
        self.validate_required(self.backup_start_time, 'backup_start_time')
        self.validate_required(self.backup_end_time, 'backup_end_time')
        self.validate_required(self.backup_type, 'backup_type')
        self.validate_required(self.backup_method, 'backup_method')
        self.validate_required(self.cross_backup_set_size, 'cross_backup_set_size')
        self.validate_required(self.cross_backup_set_file, 'cross_backup_set_file')
        self.validate_required(self.cross_backup_download_link, 'cross_backup_download_link')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.cross_backup_set_location, 'cross_backup_set_location')
        self.validate_required(self.backup_set_scale, 'backup_set_scale')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.dbinstance_storage_type, 'dbinstance_storage_type')
        self.validate_required(self.category, 'category')
        self.validate_required(self.consistent_time, 'consistent_time')
        self.validate_required(self.restore_regions, 'restore_regions')
        if self.restore_regions:
            self.restore_regions.validate()

    def to_map(self):
        result = {}
        result['CrossBackupId'] = self.cross_backup_id
        result['CrossBackupRegion'] = self.cross_backup_region
        result['BackupSetStatus'] = self.backup_set_status
        result['BackupStartTime'] = self.backup_start_time
        result['BackupEndTime'] = self.backup_end_time
        result['BackupType'] = self.backup_type
        result['BackupMethod'] = self.backup_method
        result['CrossBackupSetSize'] = self.cross_backup_set_size
        result['CrossBackupSetFile'] = self.cross_backup_set_file
        result['CrossBackupDownloadLink'] = self.cross_backup_download_link
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        result['CrossBackupSetLocation'] = self.cross_backup_set_location
        result['BackupSetScale'] = self.backup_set_scale
        result['InstanceId'] = self.instance_id
        result['DBInstanceStorageType'] = self.dbinstance_storage_type
        result['Category'] = self.category
        result['ConsistentTime'] = self.consistent_time
        if self.restore_regions is not None:
            result['RestoreRegions'] = self.restore_regions.to_map()
        else:
            result['RestoreRegions'] = None
        return result

    def from_map(self, map={}):
        self.cross_backup_id = map.get('CrossBackupId')
        self.cross_backup_region = map.get('CrossBackupRegion')
        self.backup_set_status = map.get('BackupSetStatus')
        self.backup_start_time = map.get('BackupStartTime')
        self.backup_end_time = map.get('BackupEndTime')
        self.backup_type = map.get('BackupType')
        self.backup_method = map.get('BackupMethod')
        self.cross_backup_set_size = map.get('CrossBackupSetSize')
        self.cross_backup_set_file = map.get('CrossBackupSetFile')
        self.cross_backup_download_link = map.get('CrossBackupDownloadLink')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        self.cross_backup_set_location = map.get('CrossBackupSetLocation')
        self.backup_set_scale = map.get('BackupSetScale')
        self.instance_id = map.get('InstanceId')
        self.dbinstance_storage_type = map.get('DBInstanceStorageType')
        self.category = map.get('Category')
        self.consistent_time = map.get('ConsistentTime')
        if map.get('RestoreRegions') is not None:
            temp_model = DescribeCrossRegionBackupsResponseItemsItemRestoreRegions()
            self.restore_regions = temp_model.from_map(map['RestoreRegions'])
        else:
            self.restore_regions = None
        return self


class DescribeCrossRegionBackupsResponseItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[DescribeCrossRegionBackupsResponseItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = DescribeCrossRegionBackupsResponseItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class CheckCloudResourceAuthorizedRequest(TeaModel):
    def __init__(self, security_token=None, region_id=None, dbinstance_id=None, target_region_id=None):
        self.security_token = security_token  # type: str
        self.region_id = region_id      # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.target_region_id = target_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['RegionId'] = self.region_id
        result['DBInstanceId'] = self.dbinstance_id
        result['TargetRegionId'] = self.target_region_id
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.region_id = map.get('RegionId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.target_region_id = map.get('TargetRegionId')
        return self


class CheckCloudResourceAuthorizedResponse(TeaModel):
    def __init__(self, request_id=None, authorization_state=None, role_arn=None):
        self.request_id = request_id    # type: str
        self.authorization_state = authorization_state  # type: int
        self.role_arn = role_arn        # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.authorization_state, 'authorization_state')
        self.validate_required(self.role_arn, 'role_arn')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['AuthorizationState'] = self.authorization_state
        result['RoleArn'] = self.role_arn
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.authorization_state = map.get('AuthorizationState')
        self.role_arn = map.get('RoleArn')
        return self


class DescribeReadDBInstanceDelayRequest(TeaModel):
    def __init__(self, security_token=None, dbinstance_id=None, read_instance_id=None):
        self.security_token = security_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.read_instance_id = read_instance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.read_instance_id, 'read_instance_id')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DBInstanceId'] = self.dbinstance_id
        result['ReadInstanceId'] = self.read_instance_id
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.read_instance_id = map.get('ReadInstanceId')
        return self


class DescribeReadDBInstanceDelayResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, read_dbinstance_id=None, delay_time=None, items=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.read_dbinstance_id = read_dbinstance_id  # type: str
        self.delay_time = delay_time    # type: int
        self.items = items              # type: DescribeReadDBInstanceDelayResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.read_dbinstance_id, 'read_dbinstance_id')
        self.validate_required(self.delay_time, 'delay_time')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['ReadDBInstanceId'] = self.read_dbinstance_id
        result['DelayTime'] = self.delay_time
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.read_dbinstance_id = map.get('ReadDBInstanceId')
        self.delay_time = map.get('DelayTime')
        if map.get('Items') is not None:
            temp_model = DescribeReadDBInstanceDelayResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeReadDBInstanceDelayResponseItemsItemsReadonlyInstanceDelayReadonlyInstanceDelay(TeaModel):
    def __init__(self, replay_latency=None, flush_lag=None, flush_latency=None, send_latency=None, write_lag=None,
                 replay_lag=None, write_latency=None, read_dbinstance_name=None):
        self.replay_latency = replay_latency  # type: str
        self.flush_lag = flush_lag      # type: str
        self.flush_latency = flush_latency  # type: str
        self.send_latency = send_latency  # type: str
        self.write_lag = write_lag      # type: str
        self.replay_lag = replay_lag    # type: str
        self.write_latency = write_latency  # type: str
        self.read_dbinstance_name = read_dbinstance_name  # type: str

    def validate(self):
        self.validate_required(self.replay_latency, 'replay_latency')
        self.validate_required(self.flush_lag, 'flush_lag')
        self.validate_required(self.flush_latency, 'flush_latency')
        self.validate_required(self.send_latency, 'send_latency')
        self.validate_required(self.write_lag, 'write_lag')
        self.validate_required(self.replay_lag, 'replay_lag')
        self.validate_required(self.write_latency, 'write_latency')
        self.validate_required(self.read_dbinstance_name, 'read_dbinstance_name')

    def to_map(self):
        result = {}
        result['ReplayLatency'] = self.replay_latency
        result['FlushLag'] = self.flush_lag
        result['FlushLatency'] = self.flush_latency
        result['SendLatency'] = self.send_latency
        result['WriteLag'] = self.write_lag
        result['ReplayLag'] = self.replay_lag
        result['WriteLatency'] = self.write_latency
        result['ReadDBInstanceName'] = self.read_dbinstance_name
        return result

    def from_map(self, map={}):
        self.replay_latency = map.get('ReplayLatency')
        self.flush_lag = map.get('FlushLag')
        self.flush_latency = map.get('FlushLatency')
        self.send_latency = map.get('SendLatency')
        self.write_lag = map.get('WriteLag')
        self.replay_lag = map.get('ReplayLag')
        self.write_latency = map.get('WriteLatency')
        self.read_dbinstance_name = map.get('ReadDBInstanceName')
        return self


class DescribeReadDBInstanceDelayResponseItemsItemsReadonlyInstanceDelay(TeaModel):
    def __init__(self, readonly_instance_delay=None):
        self.readonly_instance_delay = readonly_instance_delay  # type: List[DescribeReadDBInstanceDelayResponseItemsItemsReadonlyInstanceDelayReadonlyInstanceDelay]

    def validate(self):
        self.validate_required(self.readonly_instance_delay, 'readonly_instance_delay')
        if self.readonly_instance_delay:
            for k in self.readonly_instance_delay:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ReadonlyInstanceDelay'] = []
        if self.readonly_instance_delay is not None:
            for k in self.readonly_instance_delay:
                result['ReadonlyInstanceDelay'].append(k.to_map() if k else None)
        else:
            result['ReadonlyInstanceDelay'] = None
        return result

    def from_map(self, map={}):
        self.readonly_instance_delay = []
        if map.get('ReadonlyInstanceDelay') is not None:
            for k in map.get('ReadonlyInstanceDelay'):
                temp_model = DescribeReadDBInstanceDelayResponseItemsItemsReadonlyInstanceDelayReadonlyInstanceDelay()
                self.readonly_instance_delay.append(temp_model.from_map(k))
        else:
            self.readonly_instance_delay = None
        return self


class DescribeReadDBInstanceDelayResponseItemsItemsReadDBInstanceNames(TeaModel):
    def __init__(self, read_dbinstance_name=None):
        # ReadDBInstanceName
        self.read_dbinstance_name = read_dbinstance_name  # type: List[str]

    def validate(self):
        self.validate_required(self.read_dbinstance_name, 'read_dbinstance_name')

    def to_map(self):
        result = {}
        result['ReadDBInstanceName'] = self.read_dbinstance_name
        return result

    def from_map(self, map={}):
        self.read_dbinstance_name = map.get('ReadDBInstanceName')
        return self


class DescribeReadDBInstanceDelayResponseItemsItemsReadDelayTimes(TeaModel):
    def __init__(self, read_delay_time=None):
        # ReadDelayTime
        self.read_delay_time = read_delay_time  # type: List[str]

    def validate(self):
        self.validate_required(self.read_delay_time, 'read_delay_time')

    def to_map(self):
        result = {}
        result['ReadDelayTime'] = self.read_delay_time
        return result

    def from_map(self, map={}):
        self.read_delay_time = map.get('ReadDelayTime')
        return self


class DescribeReadDBInstanceDelayResponseItemsItems(TeaModel):
    def __init__(self, dbinstance_id=None, readonly_instance_delay=None, read_dbinstance_names=None,
                 read_delay_times=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.readonly_instance_delay = readonly_instance_delay  # type: DescribeReadDBInstanceDelayResponseItemsItemsReadonlyInstanceDelay
        self.read_dbinstance_names = read_dbinstance_names  # type: DescribeReadDBInstanceDelayResponseItemsItemsReadDBInstanceNames
        self.read_delay_times = read_delay_times  # type: DescribeReadDBInstanceDelayResponseItemsItemsReadDelayTimes

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.readonly_instance_delay, 'readonly_instance_delay')
        if self.readonly_instance_delay:
            self.readonly_instance_delay.validate()
        self.validate_required(self.read_dbinstance_names, 'read_dbinstance_names')
        if self.read_dbinstance_names:
            self.read_dbinstance_names.validate()
        self.validate_required(self.read_delay_times, 'read_delay_times')
        if self.read_delay_times:
            self.read_delay_times.validate()

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        if self.readonly_instance_delay is not None:
            result['ReadonlyInstanceDelay'] = self.readonly_instance_delay.to_map()
        else:
            result['ReadonlyInstanceDelay'] = None
        if self.read_dbinstance_names is not None:
            result['ReadDBInstanceNames'] = self.read_dbinstance_names.to_map()
        else:
            result['ReadDBInstanceNames'] = None
        if self.read_delay_times is not None:
            result['ReadDelayTimes'] = self.read_delay_times.to_map()
        else:
            result['ReadDelayTimes'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        if map.get('ReadonlyInstanceDelay') is not None:
            temp_model = DescribeReadDBInstanceDelayResponseItemsItemsReadonlyInstanceDelay()
            self.readonly_instance_delay = temp_model.from_map(map['ReadonlyInstanceDelay'])
        else:
            self.readonly_instance_delay = None
        if map.get('ReadDBInstanceNames') is not None:
            temp_model = DescribeReadDBInstanceDelayResponseItemsItemsReadDBInstanceNames()
            self.read_dbinstance_names = temp_model.from_map(map['ReadDBInstanceNames'])
        else:
            self.read_dbinstance_names = None
        if map.get('ReadDelayTimes') is not None:
            temp_model = DescribeReadDBInstanceDelayResponseItemsItemsReadDelayTimes()
            self.read_delay_times = temp_model.from_map(map['ReadDelayTimes'])
        else:
            self.read_delay_times = None
        return self


class DescribeReadDBInstanceDelayResponseItems(TeaModel):
    def __init__(self, items=None):
        self.items = items              # type: List[DescribeReadDBInstanceDelayResponseItemsItems]

    def validate(self):
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('Items') is not None:
            for k in map.get('Items'):
                temp_model = DescribeReadDBInstanceDelayResponseItemsItems()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        return self


class RestoreTableRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, backup_id=None, restore_time=None, table_meta=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.backup_id = backup_id      # type: str
        self.restore_time = restore_time  # type: str
        self.table_meta = table_meta    # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.table_meta, 'table_meta')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['BackupId'] = self.backup_id
        result['RestoreTime'] = self.restore_time
        result['TableMeta'] = self.table_meta
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.backup_id = map.get('BackupId')
        self.restore_time = map.get('RestoreTime')
        self.table_meta = map.get('TableMeta')
        return self


class RestoreTableResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateParameterGroupRequest(TeaModel):
    def __init__(self, region_id=None, parameter_group_name=None, engine=None, engine_version=None, parameters=None,
                 parameter_group_desc=None):
        self.region_id = region_id      # type: str
        self.parameter_group_name = parameter_group_name  # type: str
        self.engine = engine            # type: str
        self.engine_version = engine_version  # type: str
        self.parameters = parameters    # type: str
        self.parameter_group_desc = parameter_group_desc  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.parameter_group_name, 'parameter_group_name')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.parameters, 'parameters')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ParameterGroupName'] = self.parameter_group_name
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        result['Parameters'] = self.parameters
        result['ParameterGroupDesc'] = self.parameter_group_desc
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.parameter_group_name = map.get('ParameterGroupName')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        self.parameters = map.get('Parameters')
        self.parameter_group_desc = map.get('ParameterGroupDesc')
        return self


class CreateParameterGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeParameterGroupsRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        return self


class DescribeParameterGroupsResponse(TeaModel):
    def __init__(self, request_id=None, signal_for_optimize_params=None, parameter_groups=None):
        self.request_id = request_id    # type: str
        self.signal_for_optimize_params = signal_for_optimize_params  # type: bool
        self.parameter_groups = parameter_groups  # type: DescribeParameterGroupsResponseParameterGroups

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.signal_for_optimize_params, 'signal_for_optimize_params')
        self.validate_required(self.parameter_groups, 'parameter_groups')
        if self.parameter_groups:
            self.parameter_groups.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['SignalForOptimizeParams'] = self.signal_for_optimize_params
        if self.parameter_groups is not None:
            result['ParameterGroups'] = self.parameter_groups.to_map()
        else:
            result['ParameterGroups'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.signal_for_optimize_params = map.get('SignalForOptimizeParams')
        if map.get('ParameterGroups') is not None:
            temp_model = DescribeParameterGroupsResponseParameterGroups()
            self.parameter_groups = temp_model.from_map(map['ParameterGroups'])
        else:
            self.parameter_groups = None
        return self


class DescribeParameterGroupsResponseParameterGroupsParameterGroup(TeaModel):
    def __init__(self, parameter_group_type=None, parameter_group_name=None, param_counts=None,
                 parameter_group_desc=None, force_restart=None, engine=None, engine_version=None, create_time=None, update_time=None,
                 parameter_group_id=None):
        self.parameter_group_type = parameter_group_type  # type: int
        self.parameter_group_name = parameter_group_name  # type: str
        self.param_counts = param_counts  # type: int
        self.parameter_group_desc = parameter_group_desc  # type: str
        self.force_restart = force_restart  # type: int
        self.engine = engine            # type: str
        self.engine_version = engine_version  # type: str
        self.create_time = create_time  # type: str
        self.update_time = update_time  # type: str
        self.parameter_group_id = parameter_group_id  # type: str

    def validate(self):
        self.validate_required(self.parameter_group_type, 'parameter_group_type')
        self.validate_required(self.parameter_group_name, 'parameter_group_name')
        self.validate_required(self.param_counts, 'param_counts')
        self.validate_required(self.parameter_group_desc, 'parameter_group_desc')
        self.validate_required(self.force_restart, 'force_restart')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.parameter_group_id, 'parameter_group_id')

    def to_map(self):
        result = {}
        result['ParameterGroupType'] = self.parameter_group_type
        result['ParameterGroupName'] = self.parameter_group_name
        result['ParamCounts'] = self.param_counts
        result['ParameterGroupDesc'] = self.parameter_group_desc
        result['ForceRestart'] = self.force_restart
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        result['CreateTime'] = self.create_time
        result['UpdateTime'] = self.update_time
        result['ParameterGroupId'] = self.parameter_group_id
        return result

    def from_map(self, map={}):
        self.parameter_group_type = map.get('ParameterGroupType')
        self.parameter_group_name = map.get('ParameterGroupName')
        self.param_counts = map.get('ParamCounts')
        self.parameter_group_desc = map.get('ParameterGroupDesc')
        self.force_restart = map.get('ForceRestart')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        self.create_time = map.get('CreateTime')
        self.update_time = map.get('UpdateTime')
        self.parameter_group_id = map.get('ParameterGroupId')
        return self


class DescribeParameterGroupsResponseParameterGroups(TeaModel):
    def __init__(self, parameter_group=None):
        self.parameter_group = parameter_group  # type: List[DescribeParameterGroupsResponseParameterGroupsParameterGroup]

    def validate(self):
        self.validate_required(self.parameter_group, 'parameter_group')
        if self.parameter_group:
            for k in self.parameter_group:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ParameterGroup'] = []
        if self.parameter_group is not None:
            for k in self.parameter_group:
                result['ParameterGroup'].append(k.to_map() if k else None)
        else:
            result['ParameterGroup'] = None
        return result

    def from_map(self, map={}):
        self.parameter_group = []
        if map.get('ParameterGroup') is not None:
            for k in map.get('ParameterGroup'):
                temp_model = DescribeParameterGroupsResponseParameterGroupsParameterGroup()
                self.parameter_group.append(temp_model.from_map(k))
        else:
            self.parameter_group = None
        return self


class CloneParameterGroupRequest(TeaModel):
    def __init__(self, region_id=None, target_region_id=None, parameter_group_id=None, parameter_group_name=None,
                 parameter_group_desc=None):
        self.region_id = region_id      # type: str
        self.target_region_id = target_region_id  # type: str
        self.parameter_group_id = parameter_group_id  # type: str
        self.parameter_group_name = parameter_group_name  # type: str
        self.parameter_group_desc = parameter_group_desc  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.target_region_id, 'target_region_id')
        self.validate_required(self.parameter_group_id, 'parameter_group_id')
        self.validate_required(self.parameter_group_name, 'parameter_group_name')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['TargetRegionId'] = self.target_region_id
        result['ParameterGroupId'] = self.parameter_group_id
        result['ParameterGroupName'] = self.parameter_group_name
        result['ParameterGroupDesc'] = self.parameter_group_desc
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.target_region_id = map.get('TargetRegionId')
        self.parameter_group_id = map.get('ParameterGroupId')
        self.parameter_group_name = map.get('ParameterGroupName')
        self.parameter_group_desc = map.get('ParameterGroupDesc')
        return self


class CloneParameterGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeParameterGroupRequest(TeaModel):
    def __init__(self, parameter_group_id=None, region_id=None):
        self.parameter_group_id = parameter_group_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.parameter_group_id, 'parameter_group_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ParameterGroupId'] = self.parameter_group_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.parameter_group_id = map.get('ParameterGroupId')
        self.region_id = map.get('RegionId')
        return self


class DescribeParameterGroupResponse(TeaModel):
    def __init__(self, request_id=None, param_group=None):
        self.request_id = request_id    # type: str
        self.param_group = param_group  # type: DescribeParameterGroupResponseParamGroup

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.param_group, 'param_group')
        if self.param_group:
            self.param_group.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.param_group is not None:
            result['ParamGroup'] = self.param_group.to_map()
        else:
            result['ParamGroup'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('ParamGroup') is not None:
            temp_model = DescribeParameterGroupResponseParamGroup()
            self.param_group = temp_model.from_map(map['ParamGroup'])
        else:
            self.param_group = None
        return self


class DescribeParameterGroupResponseParamGroupParameterGroupParamDetailParameterDetail(TeaModel):
    def __init__(self, param_name=None, param_value=None):
        self.param_name = param_name    # type: str
        self.param_value = param_value  # type: str

    def validate(self):
        self.validate_required(self.param_name, 'param_name')
        self.validate_required(self.param_value, 'param_value')

    def to_map(self):
        result = {}
        result['ParamName'] = self.param_name
        result['ParamValue'] = self.param_value
        return result

    def from_map(self, map={}):
        self.param_name = map.get('ParamName')
        self.param_value = map.get('ParamValue')
        return self


class DescribeParameterGroupResponseParamGroupParameterGroupParamDetail(TeaModel):
    def __init__(self, parameter_detail=None):
        self.parameter_detail = parameter_detail  # type: List[DescribeParameterGroupResponseParamGroupParameterGroupParamDetailParameterDetail]

    def validate(self):
        self.validate_required(self.parameter_detail, 'parameter_detail')
        if self.parameter_detail:
            for k in self.parameter_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ParameterDetail'] = []
        if self.parameter_detail is not None:
            for k in self.parameter_detail:
                result['ParameterDetail'].append(k.to_map() if k else None)
        else:
            result['ParameterDetail'] = None
        return result

    def from_map(self, map={}):
        self.parameter_detail = []
        if map.get('ParameterDetail') is not None:
            for k in map.get('ParameterDetail'):
                temp_model = DescribeParameterGroupResponseParamGroupParameterGroupParamDetailParameterDetail()
                self.parameter_detail.append(temp_model.from_map(k))
        else:
            self.parameter_detail = None
        return self


class DescribeParameterGroupResponseParamGroupParameterGroup(TeaModel):
    def __init__(self, parameter_group_type=None, parameter_group_name=None, param_counts=None,
                 parameter_group_desc=None, force_restart=None, engine=None, engine_version=None, parameter_group_id=None,
                 create_time=None, update_time=None, param_detail=None):
        self.parameter_group_type = parameter_group_type  # type: int
        self.parameter_group_name = parameter_group_name  # type: str
        self.param_counts = param_counts  # type: int
        self.parameter_group_desc = parameter_group_desc  # type: str
        self.force_restart = force_restart  # type: int
        self.engine = engine            # type: str
        self.engine_version = engine_version  # type: str
        self.parameter_group_id = parameter_group_id  # type: str
        self.create_time = create_time  # type: str
        self.update_time = update_time  # type: str
        self.param_detail = param_detail  # type: DescribeParameterGroupResponseParamGroupParameterGroupParamDetail

    def validate(self):
        self.validate_required(self.parameter_group_type, 'parameter_group_type')
        self.validate_required(self.parameter_group_name, 'parameter_group_name')
        self.validate_required(self.param_counts, 'param_counts')
        self.validate_required(self.parameter_group_desc, 'parameter_group_desc')
        self.validate_required(self.force_restart, 'force_restart')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.parameter_group_id, 'parameter_group_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.param_detail, 'param_detail')
        if self.param_detail:
            self.param_detail.validate()

    def to_map(self):
        result = {}
        result['ParameterGroupType'] = self.parameter_group_type
        result['ParameterGroupName'] = self.parameter_group_name
        result['ParamCounts'] = self.param_counts
        result['ParameterGroupDesc'] = self.parameter_group_desc
        result['ForceRestart'] = self.force_restart
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        result['ParameterGroupId'] = self.parameter_group_id
        result['CreateTime'] = self.create_time
        result['UpdateTime'] = self.update_time
        if self.param_detail is not None:
            result['ParamDetail'] = self.param_detail.to_map()
        else:
            result['ParamDetail'] = None
        return result

    def from_map(self, map={}):
        self.parameter_group_type = map.get('ParameterGroupType')
        self.parameter_group_name = map.get('ParameterGroupName')
        self.param_counts = map.get('ParamCounts')
        self.parameter_group_desc = map.get('ParameterGroupDesc')
        self.force_restart = map.get('ForceRestart')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        self.parameter_group_id = map.get('ParameterGroupId')
        self.create_time = map.get('CreateTime')
        self.update_time = map.get('UpdateTime')
        if map.get('ParamDetail') is not None:
            temp_model = DescribeParameterGroupResponseParamGroupParameterGroupParamDetail()
            self.param_detail = temp_model.from_map(map['ParamDetail'])
        else:
            self.param_detail = None
        return self


class DescribeParameterGroupResponseParamGroup(TeaModel):
    def __init__(self, parameter_group=None):
        self.parameter_group = parameter_group  # type: List[DescribeParameterGroupResponseParamGroupParameterGroup]

    def validate(self):
        self.validate_required(self.parameter_group, 'parameter_group')
        if self.parameter_group:
            for k in self.parameter_group:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ParameterGroup'] = []
        if self.parameter_group is not None:
            for k in self.parameter_group:
                result['ParameterGroup'].append(k.to_map() if k else None)
        else:
            result['ParameterGroup'] = None
        return result

    def from_map(self, map={}):
        self.parameter_group = []
        if map.get('ParameterGroup') is not None:
            for k in map.get('ParameterGroup'):
                temp_model = DescribeParameterGroupResponseParamGroupParameterGroup()
                self.parameter_group.append(temp_model.from_map(k))
        else:
            self.parameter_group = None
        return self


class ModifyParameterGroupRequest(TeaModel):
    def __init__(self, parameter_group_id=None, parameter_group_name=None, parameter_group_desc=None,
                 parameters=None, region_id=None):
        self.parameter_group_id = parameter_group_id  # type: str
        self.parameter_group_name = parameter_group_name  # type: str
        self.parameter_group_desc = parameter_group_desc  # type: str
        self.parameters = parameters    # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.parameter_group_id, 'parameter_group_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ParameterGroupId'] = self.parameter_group_id
        result['ParameterGroupName'] = self.parameter_group_name
        result['ParameterGroupDesc'] = self.parameter_group_desc
        result['Parameters'] = self.parameters
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.parameter_group_id = map.get('ParameterGroupId')
        self.parameter_group_name = map.get('ParameterGroupName')
        self.parameter_group_desc = map.get('ParameterGroupDesc')
        self.parameters = map.get('Parameters')
        self.region_id = map.get('RegionId')
        return self


class ModifyParameterGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteParameterGroupRequest(TeaModel):
    def __init__(self, region_id=None, parameter_group_id=None):
        self.region_id = region_id      # type: str
        self.parameter_group_id = parameter_group_id  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.parameter_group_id, 'parameter_group_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ParameterGroupId'] = self.parameter_group_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.parameter_group_id = map.get('ParameterGroupId')
        return self


class DeleteParameterGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifySQLCollectorRetentionRequest(TeaModel):
    def __init__(self, security_token=None, dbinstance_id=None, config_value=None, resource_group_id=None):
        self.security_token = security_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.config_value = config_value  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.config_value, 'config_value')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DBInstanceId'] = self.dbinstance_id
        result['ConfigValue'] = self.config_value
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.config_value = map.get('ConfigValue')
        self.resource_group_id = map.get('ResourceGroupId')
        return self


class ModifySQLCollectorRetentionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeSQLCollectorRetentionRequest(TeaModel):
    def __init__(self, security_token=None, dbinstance_id=None, resource_group_id=None):
        self.security_token = security_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DBInstanceId'] = self.dbinstance_id
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.resource_group_id = map.get('ResourceGroupId')
        return self


class DescribeSQLCollectorRetentionResponse(TeaModel):
    def __init__(self, request_id=None, config_value=None):
        self.request_id = request_id    # type: str
        self.config_value = config_value  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.config_value, 'config_value')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ConfigValue'] = self.config_value
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.config_value = map.get('ConfigValue')
        return self


class CheckInstanceExistRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class CheckInstanceExistResponse(TeaModel):
    def __init__(self, request_id=None, is_exist_instance=None):
        self.request_id = request_id    # type: str
        self.is_exist_instance = is_exist_instance  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_exist_instance, 'is_exist_instance')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['IsExistInstance'] = self.is_exist_instance
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.is_exist_instance = map.get('IsExistInstance')
        return self


class DescribeLogBackupFilesRequest(TeaModel):
    def __init__(self, dbinstance_id=None, start_time=None, end_time=None, page_size=None, page_number=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeLogBackupFilesResponse(TeaModel):
    def __init__(self, request_id=None, total_record_count=None, page_number=None, page_record_count=None,
                 total_file_size=None, items=None):
        self.request_id = request_id    # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.total_file_size = total_file_size  # type: int
        self.items = items              # type: DescribeLogBackupFilesResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.total_file_size, 'total_file_size')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalRecordCount'] = self.total_record_count
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        result['TotalFileSize'] = self.total_file_size
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        self.total_file_size = map.get('TotalFileSize')
        if map.get('Items') is not None:
            temp_model = DescribeLogBackupFilesResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeLogBackupFilesResponseItemsBinLogFile(TeaModel):
    def __init__(self, file_size=None, log_begin_time=None, log_end_time=None, download_link=None,
                 intranet_download_link=None, link_expired_time=None):
        self.file_size = file_size      # type: int
        self.log_begin_time = log_begin_time  # type: str
        self.log_end_time = log_end_time  # type: str
        self.download_link = download_link  # type: str
        self.intranet_download_link = intranet_download_link  # type: str
        self.link_expired_time = link_expired_time  # type: str

    def validate(self):
        self.validate_required(self.file_size, 'file_size')
        self.validate_required(self.log_begin_time, 'log_begin_time')
        self.validate_required(self.log_end_time, 'log_end_time')
        self.validate_required(self.download_link, 'download_link')
        self.validate_required(self.intranet_download_link, 'intranet_download_link')
        self.validate_required(self.link_expired_time, 'link_expired_time')

    def to_map(self):
        result = {}
        result['FileSize'] = self.file_size
        result['LogBeginTime'] = self.log_begin_time
        result['LogEndTime'] = self.log_end_time
        result['DownloadLink'] = self.download_link
        result['IntranetDownloadLink'] = self.intranet_download_link
        result['LinkExpiredTime'] = self.link_expired_time
        return result

    def from_map(self, map={}):
        self.file_size = map.get('FileSize')
        self.log_begin_time = map.get('LogBeginTime')
        self.log_end_time = map.get('LogEndTime')
        self.download_link = map.get('DownloadLink')
        self.intranet_download_link = map.get('IntranetDownloadLink')
        self.link_expired_time = map.get('LinkExpiredTime')
        return self


class DescribeLogBackupFilesResponseItems(TeaModel):
    def __init__(self, bin_log_file=None):
        self.bin_log_file = bin_log_file  # type: List[DescribeLogBackupFilesResponseItemsBinLogFile]

    def validate(self):
        self.validate_required(self.bin_log_file, 'bin_log_file')
        if self.bin_log_file:
            for k in self.bin_log_file:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['BinLogFile'] = []
        if self.bin_log_file is not None:
            for k in self.bin_log_file:
                result['BinLogFile'].append(k.to_map() if k else None)
        else:
            result['BinLogFile'] = None
        return result

    def from_map(self, map={}):
        self.bin_log_file = []
        if map.get('BinLogFile') is not None:
            for k in map.get('BinLogFile'):
                temp_model = DescribeLogBackupFilesResponseItemsBinLogFile()
                self.bin_log_file.append(temp_model.from_map(k))
        else:
            self.bin_log_file = None
        return self


class MigrateSecurityIPModeRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        # description: The ID of the instance. ; 
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class MigrateSecurityIPModeResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, security_ipmode=None):
        # description: The ID of the request. ; 
        self.request_id = request_id    # type: str
        # description: The ID of the instance. ; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: The mode of the whitelist after the switch. Valid values:**safety**.; 
        self.security_ipmode = security_ipmode  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.security_ipmode, 'security_ipmode')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['SecurityIPMode'] = self.security_ipmode
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.security_ipmode = map.get('SecurityIPMode')
        return self


class SwitchDBInstanceVpcRequest(TeaModel):
    def __init__(self, dbinstance_id=None, vpcid=None, v_switch_id=None, private_ip_address=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.vpcid = vpcid              # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.private_ip_address = private_ip_address  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['VPCId'] = self.vpcid
        result['VSwitchId'] = self.v_switch_id
        result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.vpcid = map.get('VPCId')
        self.v_switch_id = map.get('VSwitchId')
        self.private_ip_address = map.get('PrivateIpAddress')
        return self


class SwitchDBInstanceVpcResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeCollationTimeZonesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class DescribeCollationTimeZonesResponse(TeaModel):
    def __init__(self, request_id=None, collation_time_zones=None):
        self.request_id = request_id    # type: str
        self.collation_time_zones = collation_time_zones  # type: DescribeCollationTimeZonesResponseCollationTimeZones

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.collation_time_zones, 'collation_time_zones')
        if self.collation_time_zones:
            self.collation_time_zones.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.collation_time_zones is not None:
            result['CollationTimeZones'] = self.collation_time_zones.to_map()
        else:
            result['CollationTimeZones'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('CollationTimeZones') is not None:
            temp_model = DescribeCollationTimeZonesResponseCollationTimeZones()
            self.collation_time_zones = temp_model.from_map(map['CollationTimeZones'])
        else:
            self.collation_time_zones = None
        return self


class DescribeCollationTimeZonesResponseCollationTimeZonesCollationTimeZone(TeaModel):
    def __init__(self, time_zone=None, standard_time_offset=None, description=None):
        self.time_zone = time_zone      # type: str
        self.standard_time_offset = standard_time_offset  # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.time_zone, 'time_zone')
        self.validate_required(self.standard_time_offset, 'standard_time_offset')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        result['TimeZone'] = self.time_zone
        result['StandardTimeOffset'] = self.standard_time_offset
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.time_zone = map.get('TimeZone')
        self.standard_time_offset = map.get('StandardTimeOffset')
        self.description = map.get('Description')
        return self


class DescribeCollationTimeZonesResponseCollationTimeZones(TeaModel):
    def __init__(self, collation_time_zone=None):
        self.collation_time_zone = collation_time_zone  # type: List[DescribeCollationTimeZonesResponseCollationTimeZonesCollationTimeZone]

    def validate(self):
        self.validate_required(self.collation_time_zone, 'collation_time_zone')
        if self.collation_time_zone:
            for k in self.collation_time_zone:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CollationTimeZone'] = []
        if self.collation_time_zone is not None:
            for k in self.collation_time_zone:
                result['CollationTimeZone'].append(k.to_map() if k else None)
        else:
            result['CollationTimeZone'] = None
        return result

    def from_map(self, map={}):
        self.collation_time_zone = []
        if map.get('CollationTimeZone') is not None:
            for k in map.get('CollationTimeZone'):
                temp_model = DescribeCollationTimeZonesResponseCollationTimeZonesCollationTimeZone()
                self.collation_time_zone.append(temp_model.from_map(k))
        else:
            self.collation_time_zone = None
        return self


class DescribeInstanceKeywordsRequest(TeaModel):
    def __init__(self, key=None):
        self.key = key                  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Key'] = self.key
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        return self


class DescribeInstanceKeywordsResponse(TeaModel):
    def __init__(self, request_id=None, key=None, words=None):
        self.request_id = request_id    # type: str
        self.key = key                  # type: str
        self.words = words              # type: DescribeInstanceKeywordsResponseWords

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.key, 'key')
        self.validate_required(self.words, 'words')
        if self.words:
            self.words.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Key'] = self.key
        if self.words is not None:
            result['Words'] = self.words.to_map()
        else:
            result['Words'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.key = map.get('Key')
        if map.get('Words') is not None:
            temp_model = DescribeInstanceKeywordsResponseWords()
            self.words = temp_model.from_map(map['Words'])
        else:
            self.words = None
        return self


class DescribeInstanceKeywordsResponseWords(TeaModel):
    def __init__(self, word=None):
        self.word = word                # type: List[str]

    def validate(self):
        self.validate_required(self.word, 'word')

    def to_map(self):
        result = {}
        result['word'] = self.word
        return result

    def from_map(self, map={}):
        self.word = map.get('word')
        return self


class ModifyCollationTimeZoneRequest(TeaModel):
    def __init__(self, dbinstance_id=None, collation=None, timezone=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.collation = collation      # type: str
        self.timezone = timezone        # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['Collation'] = self.collation
        result['Timezone'] = self.timezone
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.collation = map.get('Collation')
        self.timezone = map.get('Timezone')
        return self


class ModifyCollationTimeZoneResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, task_id=None, timezone=None, collation=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.task_id = task_id          # type: str
        self.timezone = timezone        # type: str
        self.collation = collation      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.timezone, 'timezone')
        self.validate_required(self.collation, 'collation')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['TaskId'] = self.task_id
        result['Timezone'] = self.timezone
        result['Collation'] = self.collation
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.task_id = map.get('TaskId')
        self.timezone = map.get('Timezone')
        self.collation = map.get('Collation')
        return self


class DescribeBackupDatabaseRequest(TeaModel):
    def __init__(self, dbinstance_id=None, backup_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.backup_id = backup_id      # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['BackupId'] = self.backup_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.backup_id = map.get('BackupId')
        return self


class DescribeBackupDatabaseResponse(TeaModel):
    def __init__(self, request_id=None, database_names=None):
        self.request_id = request_id    # type: str
        self.database_names = database_names  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.database_names, 'database_names')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DatabaseNames'] = self.database_names
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.database_names = map.get('DatabaseNames')
        return self


class CopyDatabaseBetweenInstancesRequest(TeaModel):
    def __init__(self, dbinstance_id=None, target_dbinstance_id=None, db_names=None, backup_id=None,
                 restore_time=None, sync_user_privilege=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.target_dbinstance_id = target_dbinstance_id  # type: str
        self.db_names = db_names        # type: str
        self.backup_id = backup_id      # type: str
        self.restore_time = restore_time  # type: str
        self.sync_user_privilege = sync_user_privilege  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.target_dbinstance_id, 'target_dbinstance_id')
        self.validate_required(self.db_names, 'db_names')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['TargetDBInstanceId'] = self.target_dbinstance_id
        result['DbNames'] = self.db_names
        result['BackupId'] = self.backup_id
        result['RestoreTime'] = self.restore_time
        result['SyncUserPrivilege'] = self.sync_user_privilege
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.target_dbinstance_id = map.get('TargetDBInstanceId')
        self.db_names = map.get('DbNames')
        self.backup_id = map.get('BackupId')
        self.restore_time = map.get('RestoreTime')
        self.sync_user_privilege = map.get('SyncUserPrivilege')
        return self


class CopyDatabaseBetweenInstancesResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class RecoveryDBInstanceRequest(TeaModel):
    def __init__(self, dbinstance_class=None, dbinstance_storage=None, pay_type=None, instance_network_type=None,
                 dbinstance_id=None, target_dbinstance_id=None, db_names=None, backup_id=None, restore_time=None, vpcid=None,
                 v_switch_id=None, private_ip_address=None, used_time=None, period=None, dbinstance_storage_type=None):
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_storage = dbinstance_storage  # type: int
        self.pay_type = pay_type        # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.target_dbinstance_id = target_dbinstance_id  # type: str
        self.db_names = db_names        # type: str
        self.backup_id = backup_id      # type: str
        self.restore_time = restore_time  # type: str
        self.vpcid = vpcid              # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.used_time = used_time      # type: str
        self.period = period            # type: str
        self.dbinstance_storage_type = dbinstance_storage_type  # type: str

    def validate(self):
        self.validate_required(self.db_names, 'db_names')

    def to_map(self):
        result = {}
        result['DBInstanceClass'] = self.dbinstance_class
        result['DBInstanceStorage'] = self.dbinstance_storage
        result['PayType'] = self.pay_type
        result['InstanceNetworkType'] = self.instance_network_type
        result['DBInstanceId'] = self.dbinstance_id
        result['TargetDBInstanceId'] = self.target_dbinstance_id
        result['DbNames'] = self.db_names
        result['BackupId'] = self.backup_id
        result['RestoreTime'] = self.restore_time
        result['VPCId'] = self.vpcid
        result['VSwitchId'] = self.v_switch_id
        result['PrivateIpAddress'] = self.private_ip_address
        result['UsedTime'] = self.used_time
        result['Period'] = self.period
        result['DBInstanceStorageType'] = self.dbinstance_storage_type
        return result

    def from_map(self, map={}):
        self.dbinstance_class = map.get('DBInstanceClass')
        self.dbinstance_storage = map.get('DBInstanceStorage')
        self.pay_type = map.get('PayType')
        self.instance_network_type = map.get('InstanceNetworkType')
        self.dbinstance_id = map.get('DBInstanceId')
        self.target_dbinstance_id = map.get('TargetDBInstanceId')
        self.db_names = map.get('DbNames')
        self.backup_id = map.get('BackupId')
        self.restore_time = map.get('RestoreTime')
        self.vpcid = map.get('VPCId')
        self.v_switch_id = map.get('VSwitchId')
        self.private_ip_address = map.get('PrivateIpAddress')
        self.used_time = map.get('UsedTime')
        self.period = map.get('Period')
        self.dbinstance_storage_type = map.get('DBInstanceStorageType')
        return self


class RecoveryDBInstanceResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, order_id=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.order_id = order_id        # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['OrderId'] = self.order_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.order_id = map.get('OrderId')
        return self


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(self, region_id=None, zone_id=None, instance_charge_type=None, engine=None, engine_version=None,
                 dbinstance_class=None, order_type=None, dbinstance_storage_type=None, category=None, dispense_mode=None):
        self.region_id = region_id      # type: str
        self.zone_id = zone_id          # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.engine = engine            # type: str
        self.engine_version = engine_version  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.order_type = order_type    # type: str
        self.dbinstance_storage_type = dbinstance_storage_type  # type: str
        self.category = category        # type: str
        self.dispense_mode = dispense_mode  # type: int

    def validate(self):
        self.validate_required(self.instance_charge_type, 'instance_charge_type')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ZoneId'] = self.zone_id
        result['InstanceChargeType'] = self.instance_charge_type
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        result['DBInstanceClass'] = self.dbinstance_class
        result['OrderType'] = self.order_type
        result['DBInstanceStorageType'] = self.dbinstance_storage_type
        result['Category'] = self.category
        result['DispenseMode'] = self.dispense_mode
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.zone_id = map.get('ZoneId')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        self.dbinstance_class = map.get('DBInstanceClass')
        self.order_type = map.get('OrderType')
        self.dbinstance_storage_type = map.get('DBInstanceStorageType')
        self.category = map.get('Category')
        self.dispense_mode = map.get('DispenseMode')
        return self


class DescribeAvailableResourceResponse(TeaModel):
    def __init__(self, request_id=None, available_zones=None):
        self.request_id = request_id    # type: str
        self.available_zones = available_zones  # type: DescribeAvailableResourceResponseAvailableZones

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.available_zones, 'available_zones')
        if self.available_zones:
            self.available_zones.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones.to_map()
        else:
            result['AvailableZones'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('AvailableZones') is not None:
            temp_model = DescribeAvailableResourceResponseAvailableZones()
            self.available_zones = temp_model.from_map(map['AvailableZones'])
        else:
            self.available_zones = None
        return self


class DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategorySupportedStorageTypesSupportedStorageTypeAvailableResourcesAvailableResourceDBInstanceStorageRange(TeaModel):
    def __init__(self, max=None, min=None, step=None):
        self.max = max                  # type: int
        self.min = min                  # type: int
        self.step = step                # type: int

    def validate(self):
        self.validate_required(self.max, 'max')
        self.validate_required(self.min, 'min')
        self.validate_required(self.step, 'step')

    def to_map(self):
        result = {}
        result['Max'] = self.max
        result['Min'] = self.min
        result['Step'] = self.step
        return result

    def from_map(self, map={}):
        self.max = map.get('Max')
        self.min = map.get('Min')
        self.step = map.get('Step')
        return self


class DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategorySupportedStorageTypesSupportedStorageTypeAvailableResourcesAvailableResource(TeaModel):
    def __init__(self, dbinstance_class=None, storage_range=None, dbinstance_storage_range=None):
        self.dbinstance_class = dbinstance_class  # type: str
        self.storage_range = storage_range  # type: str
        self.dbinstance_storage_range = dbinstance_storage_range  # type: DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategorySupportedStorageTypesSupportedStorageTypeAvailableResourcesAvailableResourceDBInstanceStorageRange

    def validate(self):
        self.validate_required(self.dbinstance_class, 'dbinstance_class')
        self.validate_required(self.storage_range, 'storage_range')
        self.validate_required(self.dbinstance_storage_range, 'dbinstance_storage_range')
        if self.dbinstance_storage_range:
            self.dbinstance_storage_range.validate()

    def to_map(self):
        result = {}
        result['DBInstanceClass'] = self.dbinstance_class
        result['StorageRange'] = self.storage_range
        if self.dbinstance_storage_range is not None:
            result['DBInstanceStorageRange'] = self.dbinstance_storage_range.to_map()
        else:
            result['DBInstanceStorageRange'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_class = map.get('DBInstanceClass')
        self.storage_range = map.get('StorageRange')
        if map.get('DBInstanceStorageRange') is not None:
            temp_model = DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategorySupportedStorageTypesSupportedStorageTypeAvailableResourcesAvailableResourceDBInstanceStorageRange()
            self.dbinstance_storage_range = temp_model.from_map(map['DBInstanceStorageRange'])
        else:
            self.dbinstance_storage_range = None
        return self


class DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategorySupportedStorageTypesSupportedStorageTypeAvailableResources(TeaModel):
    def __init__(self, available_resource=None):
        self.available_resource = available_resource  # type: List[DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategorySupportedStorageTypesSupportedStorageTypeAvailableResourcesAvailableResource]

    def validate(self):
        self.validate_required(self.available_resource, 'available_resource')
        if self.available_resource:
            for k in self.available_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AvailableResource'] = []
        if self.available_resource is not None:
            for k in self.available_resource:
                result['AvailableResource'].append(k.to_map() if k else None)
        else:
            result['AvailableResource'] = None
        return result

    def from_map(self, map={}):
        self.available_resource = []
        if map.get('AvailableResource') is not None:
            for k in map.get('AvailableResource'):
                temp_model = DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategorySupportedStorageTypesSupportedStorageTypeAvailableResourcesAvailableResource()
                self.available_resource.append(temp_model.from_map(k))
        else:
            self.available_resource = None
        return self


class DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategorySupportedStorageTypesSupportedStorageType(TeaModel):
    def __init__(self, storage_type=None, available_resources=None):
        self.storage_type = storage_type  # type: str
        self.available_resources = available_resources  # type: DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategorySupportedStorageTypesSupportedStorageTypeAvailableResources

    def validate(self):
        self.validate_required(self.storage_type, 'storage_type')
        self.validate_required(self.available_resources, 'available_resources')
        if self.available_resources:
            self.available_resources.validate()

    def to_map(self):
        result = {}
        result['StorageType'] = self.storage_type
        if self.available_resources is not None:
            result['AvailableResources'] = self.available_resources.to_map()
        else:
            result['AvailableResources'] = None
        return result

    def from_map(self, map={}):
        self.storage_type = map.get('StorageType')
        if map.get('AvailableResources') is not None:
            temp_model = DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategorySupportedStorageTypesSupportedStorageTypeAvailableResources()
            self.available_resources = temp_model.from_map(map['AvailableResources'])
        else:
            self.available_resources = None
        return self


class DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategorySupportedStorageTypes(TeaModel):
    def __init__(self, supported_storage_type=None):
        self.supported_storage_type = supported_storage_type  # type: List[DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategorySupportedStorageTypesSupportedStorageType]

    def validate(self):
        self.validate_required(self.supported_storage_type, 'supported_storage_type')
        if self.supported_storage_type:
            for k in self.supported_storage_type:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SupportedStorageType'] = []
        if self.supported_storage_type is not None:
            for k in self.supported_storage_type:
                result['SupportedStorageType'].append(k.to_map() if k else None)
        else:
            result['SupportedStorageType'] = None
        return result

    def from_map(self, map={}):
        self.supported_storage_type = []
        if map.get('SupportedStorageType') is not None:
            for k in map.get('SupportedStorageType'):
                temp_model = DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategorySupportedStorageTypesSupportedStorageType()
                self.supported_storage_type.append(temp_model.from_map(k))
        else:
            self.supported_storage_type = None
        return self


class DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategory(TeaModel):
    def __init__(self, category=None, supported_storage_types=None):
        self.category = category        # type: str
        self.supported_storage_types = supported_storage_types  # type: DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategorySupportedStorageTypes

    def validate(self):
        self.validate_required(self.category, 'category')
        self.validate_required(self.supported_storage_types, 'supported_storage_types')
        if self.supported_storage_types:
            self.supported_storage_types.validate()

    def to_map(self):
        result = {}
        result['Category'] = self.category
        if self.supported_storage_types is not None:
            result['SupportedStorageTypes'] = self.supported_storage_types.to_map()
        else:
            result['SupportedStorageTypes'] = None
        return result

    def from_map(self, map={}):
        self.category = map.get('Category')
        if map.get('SupportedStorageTypes') is not None:
            temp_model = DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategorySupportedStorageTypes()
            self.supported_storage_types = temp_model.from_map(map['SupportedStorageTypes'])
        else:
            self.supported_storage_types = None
        return self


class DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorys(TeaModel):
    def __init__(self, supported_category=None):
        self.supported_category = supported_category  # type: List[DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategory]

    def validate(self):
        self.validate_required(self.supported_category, 'supported_category')
        if self.supported_category:
            for k in self.supported_category:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SupportedCategory'] = []
        if self.supported_category is not None:
            for k in self.supported_category:
                result['SupportedCategory'].append(k.to_map() if k else None)
        else:
            result['SupportedCategory'] = None
        return result

    def from_map(self, map={}):
        self.supported_category = []
        if map.get('SupportedCategory') is not None:
            for k in map.get('SupportedCategory'):
                temp_model = DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorysSupportedCategory()
                self.supported_category.append(temp_model.from_map(k))
        else:
            self.supported_category = None
        return self


class DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion(TeaModel):
    def __init__(self, version=None, supported_categorys=None):
        self.version = version          # type: str
        self.supported_categorys = supported_categorys  # type: DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorys

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.supported_categorys, 'supported_categorys')
        if self.supported_categorys:
            self.supported_categorys.validate()

    def to_map(self):
        result = {}
        result['Version'] = self.version
        if self.supported_categorys is not None:
            result['SupportedCategorys'] = self.supported_categorys.to_map()
        else:
            result['SupportedCategorys'] = None
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        if map.get('SupportedCategorys') is not None:
            temp_model = DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategorys()
            self.supported_categorys = temp_model.from_map(map['SupportedCategorys'])
        else:
            self.supported_categorys = None
        return self


class DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions(TeaModel):
    def __init__(self, supported_engine_version=None):
        self.supported_engine_version = supported_engine_version  # type: List[DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion]

    def validate(self):
        self.validate_required(self.supported_engine_version, 'supported_engine_version')
        if self.supported_engine_version:
            for k in self.supported_engine_version:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SupportedEngineVersion'] = []
        if self.supported_engine_version is not None:
            for k in self.supported_engine_version:
                result['SupportedEngineVersion'].append(k.to_map() if k else None)
        else:
            result['SupportedEngineVersion'] = None
        return result

    def from_map(self, map={}):
        self.supported_engine_version = []
        if map.get('SupportedEngineVersion') is not None:
            for k in map.get('SupportedEngineVersion'):
                temp_model = DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion()
                self.supported_engine_version.append(temp_model.from_map(k))
        else:
            self.supported_engine_version = None
        return self


class DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngine(TeaModel):
    def __init__(self, engine=None, supported_engine_versions=None):
        self.engine = engine            # type: str
        self.supported_engine_versions = supported_engine_versions  # type: DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions

    def validate(self):
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.supported_engine_versions, 'supported_engine_versions')
        if self.supported_engine_versions:
            self.supported_engine_versions.validate()

    def to_map(self):
        result = {}
        result['Engine'] = self.engine
        if self.supported_engine_versions is not None:
            result['SupportedEngineVersions'] = self.supported_engine_versions.to_map()
        else:
            result['SupportedEngineVersions'] = None
        return result

    def from_map(self, map={}):
        self.engine = map.get('Engine')
        if map.get('SupportedEngineVersions') is not None:
            temp_model = DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions()
            self.supported_engine_versions = temp_model.from_map(map['SupportedEngineVersions'])
        else:
            self.supported_engine_versions = None
        return self


class DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEngines(TeaModel):
    def __init__(self, supported_engine=None):
        self.supported_engine = supported_engine  # type: List[DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngine]

    def validate(self):
        self.validate_required(self.supported_engine, 'supported_engine')
        if self.supported_engine:
            for k in self.supported_engine:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SupportedEngine'] = []
        if self.supported_engine is not None:
            for k in self.supported_engine:
                result['SupportedEngine'].append(k.to_map() if k else None)
        else:
            result['SupportedEngine'] = None
        return result

    def from_map(self, map={}):
        self.supported_engine = []
        if map.get('SupportedEngine') is not None:
            for k in map.get('SupportedEngine'):
                temp_model = DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEnginesSupportedEngine()
                self.supported_engine.append(temp_model.from_map(k))
        else:
            self.supported_engine = None
        return self


class DescribeAvailableResourceResponseAvailableZonesAvailableZone(TeaModel):
    def __init__(self, region_id=None, zone_id=None, status=None, supported_engines=None):
        self.region_id = region_id      # type: str
        self.zone_id = zone_id          # type: str
        self.status = status            # type: str
        self.supported_engines = supported_engines  # type: DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEngines

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.supported_engines, 'supported_engines')
        if self.supported_engines:
            self.supported_engines.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ZoneId'] = self.zone_id
        result['Status'] = self.status
        if self.supported_engines is not None:
            result['SupportedEngines'] = self.supported_engines.to_map()
        else:
            result['SupportedEngines'] = None
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.zone_id = map.get('ZoneId')
        self.status = map.get('Status')
        if map.get('SupportedEngines') is not None:
            temp_model = DescribeAvailableResourceResponseAvailableZonesAvailableZoneSupportedEngines()
            self.supported_engines = temp_model.from_map(map['SupportedEngines'])
        else:
            self.supported_engines = None
        return self


class DescribeAvailableResourceResponseAvailableZones(TeaModel):
    def __init__(self, available_zone=None):
        self.available_zone = available_zone  # type: List[DescribeAvailableResourceResponseAvailableZonesAvailableZone]

    def validate(self):
        self.validate_required(self.available_zone, 'available_zone')
        if self.available_zone:
            for k in self.available_zone:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AvailableZone'] = []
        if self.available_zone is not None:
            for k in self.available_zone:
                result['AvailableZone'].append(k.to_map() if k else None)
        else:
            result['AvailableZone'] = None
        return result

    def from_map(self, map={}):
        self.available_zone = []
        if map.get('AvailableZone') is not None:
            for k in map.get('AvailableZone'):
                temp_model = DescribeAvailableResourceResponseAvailableZonesAvailableZone()
                self.available_zone.append(temp_model.from_map(k))
        else:
            self.available_zone = None
        return self


class DestroyDBInstanceRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DestroyDBInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyReadonlyInstanceDelayReplicationTimeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, read_sqlreplication_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.read_sqlreplication_time = read_sqlreplication_time  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.read_sqlreplication_time, 'read_sqlreplication_time')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['ReadSQLReplicationTime'] = self.read_sqlreplication_time
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.read_sqlreplication_time = map.get('ReadSQLReplicationTime')
        return self


class ModifyReadonlyInstanceDelayReplicationTimeResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, read_sqlreplication_time=None, task_id=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.read_sqlreplication_time = read_sqlreplication_time  # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.read_sqlreplication_time, 'read_sqlreplication_time')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['ReadSQLReplicationTime'] = self.read_sqlreplication_time
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.read_sqlreplication_time = map.get('ReadSQLReplicationTime')
        self.task_id = map.get('TaskId')
        return self


class DescribeDBInstanceProxyConfigurationRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeDBInstanceProxyConfigurationResponse(TeaModel):
    def __init__(self, request_id=None, transparent_switch_configuration=None,
                 persistent_connections_configuration=None, attacks_protection_configuration=None):
        self.request_id = request_id    # type: str
        self.transparent_switch_configuration = transparent_switch_configuration  # type: str
        self.persistent_connections_configuration = persistent_connections_configuration  # type: str
        self.attacks_protection_configuration = attacks_protection_configuration  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.transparent_switch_configuration, 'transparent_switch_configuration')
        self.validate_required(self.persistent_connections_configuration, 'persistent_connections_configuration')
        self.validate_required(self.attacks_protection_configuration, 'attacks_protection_configuration')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TransparentSwitchConfiguration'] = self.transparent_switch_configuration
        result['PersistentConnectionsConfiguration'] = self.persistent_connections_configuration
        result['AttacksProtectionConfiguration'] = self.attacks_protection_configuration
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.transparent_switch_configuration = map.get('TransparentSwitchConfiguration')
        self.persistent_connections_configuration = map.get('PersistentConnectionsConfiguration')
        self.attacks_protection_configuration = map.get('AttacksProtectionConfiguration')
        return self


class CreateOnlineDatabaseTaskRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, dbname=None, migrate_task_id=None, check_dbmode=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbname = dbname            # type: str
        self.migrate_task_id = migrate_task_id  # type: str
        self.check_dbmode = check_dbmode  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.migrate_task_id, 'migrate_task_id')
        self.validate_required(self.check_dbmode, 'check_dbmode')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['DBName'] = self.dbname
        result['MigrateTaskId'] = self.migrate_task_id
        result['CheckDBMode'] = self.check_dbmode
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbname = map.get('DBName')
        self.migrate_task_id = map.get('MigrateTaskId')
        self.check_dbmode = map.get('CheckDBMode')
        return self


class CreateOnlineDatabaseTaskResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class UpgradeDBInstanceKernelVersionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, upgrade_time=None, switch_time=None, target_minor_version=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.upgrade_time = upgrade_time  # type: str
        self.switch_time = switch_time  # type: str
        self.target_minor_version = target_minor_version  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['UpgradeTime'] = self.upgrade_time
        result['SwitchTime'] = self.switch_time
        result['TargetMinorVersion'] = self.target_minor_version
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.upgrade_time = map.get('UpgradeTime')
        self.switch_time = map.get('SwitchTime')
        self.target_minor_version = map.get('TargetMinorVersion')
        return self


class UpgradeDBInstanceKernelVersionResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_name=None, task_id=None, target_minor_version=None):
        self.request_id = request_id    # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.task_id = task_id          # type: str
        self.target_minor_version = target_minor_version  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_name, 'dbinstance_name')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.target_minor_version, 'target_minor_version')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceName'] = self.dbinstance_name
        result['TaskId'] = self.task_id
        result['TargetMinorVersion'] = self.target_minor_version
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_name = map.get('DBInstanceName')
        self.task_id = map.get('TaskId')
        self.target_minor_version = map.get('TargetMinorVersion')
        return self


class ModifyDBInstanceProxyConfigurationRequest(TeaModel):
    def __init__(self, dbinstance_id=None, proxy_configuration_key=None, proxy_configuration_value=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.proxy_configuration_key = proxy_configuration_key  # type: str
        self.proxy_configuration_value = proxy_configuration_value  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.proxy_configuration_key, 'proxy_configuration_key')
        self.validate_required(self.proxy_configuration_value, 'proxy_configuration_value')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['ProxyConfigurationKey'] = self.proxy_configuration_key
        result['ProxyConfigurationValue'] = self.proxy_configuration_value
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.proxy_configuration_key = map.get('ProxyConfigurationKey')
        self.proxy_configuration_value = map.get('ProxyConfigurationValue')
        return self


class ModifyDBInstanceProxyConfigurationResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeSecurityGroupConfigurationRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeSecurityGroupConfigurationResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_name=None, items=None):
        self.request_id = request_id    # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.items = items              # type: DescribeSecurityGroupConfigurationResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_name, 'dbinstance_name')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceName'] = self.dbinstance_name
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_name = map.get('DBInstanceName')
        if map.get('Items') is not None:
            temp_model = DescribeSecurityGroupConfigurationResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeSecurityGroupConfigurationResponseItemsEcsSecurityGroupRelation(TeaModel):
    def __init__(self, region_id=None, security_group_id=None, network_type=None):
        self.region_id = region_id      # type: str
        self.security_group_id = security_group_id  # type: str
        self.network_type = network_type  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.network_type, 'network_type')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['SecurityGroupId'] = self.security_group_id
        result['NetworkType'] = self.network_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.security_group_id = map.get('SecurityGroupId')
        self.network_type = map.get('NetworkType')
        return self


class DescribeSecurityGroupConfigurationResponseItems(TeaModel):
    def __init__(self, ecs_security_group_relation=None):
        self.ecs_security_group_relation = ecs_security_group_relation  # type: List[DescribeSecurityGroupConfigurationResponseItemsEcsSecurityGroupRelation]

    def validate(self):
        self.validate_required(self.ecs_security_group_relation, 'ecs_security_group_relation')
        if self.ecs_security_group_relation:
            for k in self.ecs_security_group_relation:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EcsSecurityGroupRelation'] = []
        if self.ecs_security_group_relation is not None:
            for k in self.ecs_security_group_relation:
                result['EcsSecurityGroupRelation'].append(k.to_map() if k else None)
        else:
            result['EcsSecurityGroupRelation'] = None
        return result

    def from_map(self, map={}):
        self.ecs_security_group_relation = []
        if map.get('EcsSecurityGroupRelation') is not None:
            for k in map.get('EcsSecurityGroupRelation'):
                temp_model = DescribeSecurityGroupConfigurationResponseItemsEcsSecurityGroupRelation()
                self.ecs_security_group_relation.append(temp_model.from_map(k))
        else:
            self.ecs_security_group_relation = None
        return self


class ModifySecurityGroupConfigurationRequest(TeaModel):
    def __init__(self, dbinstance_id=None, security_group_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.security_group_id = security_group_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.security_group_id, 'security_group_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.security_group_id = map.get('SecurityGroupId')
        return self


class ModifySecurityGroupConfigurationResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_name=None, items=None):
        self.request_id = request_id    # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.items = items              # type: ModifySecurityGroupConfigurationResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_name, 'dbinstance_name')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceName'] = self.dbinstance_name
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_name = map.get('DBInstanceName')
        if map.get('Items') is not None:
            temp_model = ModifySecurityGroupConfigurationResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class ModifySecurityGroupConfigurationResponseItemsEcsSecurityGroupRelation(TeaModel):
    def __init__(self, region_id=None, security_group_id=None, network_type=None):
        self.region_id = region_id      # type: str
        self.security_group_id = security_group_id  # type: str
        self.network_type = network_type  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.network_type, 'network_type')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['SecurityGroupId'] = self.security_group_id
        result['NetworkType'] = self.network_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.security_group_id = map.get('SecurityGroupId')
        self.network_type = map.get('NetworkType')
        return self


class ModifySecurityGroupConfigurationResponseItems(TeaModel):
    def __init__(self, ecs_security_group_relation=None):
        self.ecs_security_group_relation = ecs_security_group_relation  # type: List[ModifySecurityGroupConfigurationResponseItemsEcsSecurityGroupRelation]

    def validate(self):
        self.validate_required(self.ecs_security_group_relation, 'ecs_security_group_relation')
        if self.ecs_security_group_relation:
            for k in self.ecs_security_group_relation:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EcsSecurityGroupRelation'] = []
        if self.ecs_security_group_relation is not None:
            for k in self.ecs_security_group_relation:
                result['EcsSecurityGroupRelation'].append(k.to_map() if k else None)
        else:
            result['EcsSecurityGroupRelation'] = None
        return result

    def from_map(self, map={}):
        self.ecs_security_group_relation = []
        if map.get('EcsSecurityGroupRelation') is not None:
            for k in map.get('EcsSecurityGroupRelation'):
                temp_model = ModifySecurityGroupConfigurationResponseItemsEcsSecurityGroupRelation()
                self.ecs_security_group_relation.append(temp_model.from_map(k))
        else:
            self.ecs_security_group_relation = None
        return self


class DescribeOssDownloadsForSQLServerRequest(TeaModel):
    def __init__(self, dbinstance_id=None, migrate_task_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.migrate_task_id = migrate_task_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.migrate_task_id, 'migrate_task_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['MigrateTaskId'] = self.migrate_task_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.migrate_task_id = map.get('MigrateTaskId')
        return self


class DescribeOssDownloadsForSQLServerResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_name=None, migrate_iask_id=None, items=None):
        self.request_id = request_id    # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.migrate_iask_id = migrate_iask_id  # type: str
        self.items = items              # type: DescribeOssDownloadsForSQLServerResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_name, 'dbinstance_name')
        self.validate_required(self.migrate_iask_id, 'migrate_iask_id')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceName'] = self.dbinstance_name
        result['MigrateIaskId'] = self.migrate_iask_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_name = map.get('DBInstanceName')
        self.migrate_iask_id = map.get('MigrateIaskId')
        if map.get('Items') is not None:
            temp_model = DescribeOssDownloadsForSQLServerResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeOssDownloadsForSQLServerResponseItemsOssDownload(TeaModel):
    def __init__(self, file_name=None, create_time=None, bak_type=None, file_size=None, status=None, is_avail=None,
                 desc=None):
        self.file_name = file_name      # type: str
        self.create_time = create_time  # type: str
        self.bak_type = bak_type        # type: str
        self.file_size = file_size      # type: str
        self.status = status            # type: str
        self.is_avail = is_avail        # type: str
        self.desc = desc                # type: str

    def validate(self):
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.bak_type, 'bak_type')
        self.validate_required(self.file_size, 'file_size')
        self.validate_required(self.status, 'status')
        self.validate_required(self.is_avail, 'is_avail')
        self.validate_required(self.desc, 'desc')

    def to_map(self):
        result = {}
        result['FileName'] = self.file_name
        result['CreateTime'] = self.create_time
        result['BakType'] = self.bak_type
        result['FileSize'] = self.file_size
        result['Status'] = self.status
        result['IsAvail'] = self.is_avail
        result['Desc'] = self.desc
        return result

    def from_map(self, map={}):
        self.file_name = map.get('FileName')
        self.create_time = map.get('CreateTime')
        self.bak_type = map.get('BakType')
        self.file_size = map.get('FileSize')
        self.status = map.get('Status')
        self.is_avail = map.get('IsAvail')
        self.desc = map.get('Desc')
        return self


class DescribeOssDownloadsForSQLServerResponseItems(TeaModel):
    def __init__(self, oss_download=None):
        self.oss_download = oss_download  # type: List[DescribeOssDownloadsForSQLServerResponseItemsOssDownload]

    def validate(self):
        self.validate_required(self.oss_download, 'oss_download')
        if self.oss_download:
            for k in self.oss_download:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['OssDownload'] = []
        if self.oss_download is not None:
            for k in self.oss_download:
                result['OssDownload'].append(k.to_map() if k else None)
        else:
            result['OssDownload'] = None
        return result

    def from_map(self, map={}):
        self.oss_download = []
        if map.get('OssDownload') is not None:
            for k in map.get('OssDownload'):
                temp_model = DescribeOssDownloadsForSQLServerResponseItemsOssDownload()
                self.oss_download.append(temp_model.from_map(k))
        else:
            self.oss_download = None
        return self


class DescribeMigrateTasksForSQLServerRequest(TeaModel):
    def __init__(self, dbinstance_id=None, start_time=None, end_time=None, page_size=None, page_number=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeMigrateTasksForSQLServerResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, dbinstance_name=None, start_time=None, end_time=None,
                 total_record_count=None, page_number=None, page_record_count=None, items=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items              # type: DescribeMigrateTasksForSQLServerResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbinstance_name, 'dbinstance_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceID'] = self.dbinstance_id
        result['DBInstanceName'] = self.dbinstance_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['TotalRecordCount'] = self.total_record_count
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceID')
        self.dbinstance_name = map.get('DBInstanceName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeMigrateTasksForSQLServerResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeMigrateTasksForSQLServerResponseItemsMigrateTask(TeaModel):
    def __init__(self, dbname=None, migrate_iask_id=None, create_time=None, end_time=None, task_type=None,
                 status=None, is_dbreplaced=None, desc=None):
        self.dbname = dbname            # type: str
        self.migrate_iask_id = migrate_iask_id  # type: str
        self.create_time = create_time  # type: str
        self.end_time = end_time        # type: str
        self.task_type = task_type      # type: str
        self.status = status            # type: str
        self.is_dbreplaced = is_dbreplaced  # type: str
        self.desc = desc                # type: str

    def validate(self):
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.migrate_iask_id, 'migrate_iask_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.task_type, 'task_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.is_dbreplaced, 'is_dbreplaced')
        self.validate_required(self.desc, 'desc')

    def to_map(self):
        result = {}
        result['DBName'] = self.dbname
        result['MigrateIaskId'] = self.migrate_iask_id
        result['CreateTime'] = self.create_time
        result['EndTime'] = self.end_time
        result['TaskType'] = self.task_type
        result['Status'] = self.status
        result['IsDBReplaced'] = self.is_dbreplaced
        result['Desc'] = self.desc
        return result

    def from_map(self, map={}):
        self.dbname = map.get('DBName')
        self.migrate_iask_id = map.get('MigrateIaskId')
        self.create_time = map.get('CreateTime')
        self.end_time = map.get('EndTime')
        self.task_type = map.get('TaskType')
        self.status = map.get('Status')
        self.is_dbreplaced = map.get('IsDBReplaced')
        self.desc = map.get('Desc')
        return self


class DescribeMigrateTasksForSQLServerResponseItems(TeaModel):
    def __init__(self, migrate_task=None):
        self.migrate_task = migrate_task  # type: List[DescribeMigrateTasksForSQLServerResponseItemsMigrateTask]

    def validate(self):
        self.validate_required(self.migrate_task, 'migrate_task')
        if self.migrate_task:
            for k in self.migrate_task:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['MigrateTask'] = []
        if self.migrate_task is not None:
            for k in self.migrate_task:
                result['MigrateTask'].append(k.to_map() if k else None)
        else:
            result['MigrateTask'] = None
        return result

    def from_map(self, map={}):
        self.migrate_task = []
        if map.get('MigrateTask') is not None:
            for k in map.get('MigrateTask'):
                temp_model = DescribeMigrateTasksForSQLServerResponseItemsMigrateTask()
                self.migrate_task.append(temp_model.from_map(k))
        else:
            self.migrate_task = None
        return self


class CreateMigrateTaskForSQLServerRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbname=None, task_type=None, is_online_db=None, ossurls=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbname = dbname            # type: str
        self.task_type = task_type      # type: str
        self.is_online_db = is_online_db  # type: str
        self.ossurls = ossurls          # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.task_type, 'task_type')
        self.validate_required(self.is_online_db, 'is_online_db')
        self.validate_required(self.ossurls, 'ossurls')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBName'] = self.dbname
        result['TaskType'] = self.task_type
        result['IsOnlineDB'] = self.is_online_db
        result['OSSUrls'] = self.ossurls
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbname = map.get('DBName')
        self.task_type = map.get('TaskType')
        self.is_online_db = map.get('IsOnlineDB')
        self.ossurls = map.get('OSSUrls')
        return self


class CreateMigrateTaskForSQLServerResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, dbinstance_name=None, task_id=None, dbname=None,
                 migrate_iask_id=None, task_type=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_name = dbinstance_name  # type: str
        self.task_id = task_id          # type: str
        self.dbname = dbname            # type: str
        self.migrate_iask_id = migrate_iask_id  # type: str
        self.task_type = task_type      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbinstance_name, 'dbinstance_name')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.migrate_iask_id, 'migrate_iask_id')
        self.validate_required(self.task_type, 'task_type')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['DBInstanceName'] = self.dbinstance_name
        result['TaskId'] = self.task_id
        result['DBName'] = self.dbname
        result['MigrateIaskId'] = self.migrate_iask_id
        result['TaskType'] = self.task_type
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbinstance_name = map.get('DBInstanceName')
        self.task_id = map.get('TaskId')
        self.dbname = map.get('DBName')
        self.migrate_iask_id = map.get('MigrateIaskId')
        self.task_type = map.get('TaskType')
        return self


class CreateMigrateTaskRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbname=None, backup_mode=None, is_online_db=None, check_dbmode=None,
                 oss_object_positions=None, ossurls=None, migrate_task_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbname = dbname            # type: str
        self.backup_mode = backup_mode  # type: str
        self.is_online_db = is_online_db  # type: str
        self.check_dbmode = check_dbmode  # type: str
        self.oss_object_positions = oss_object_positions  # type: str
        self.ossurls = ossurls          # type: str
        self.migrate_task_id = migrate_task_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.backup_mode, 'backup_mode')
        self.validate_required(self.is_online_db, 'is_online_db')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBName'] = self.dbname
        result['BackupMode'] = self.backup_mode
        result['IsOnlineDB'] = self.is_online_db
        result['CheckDBMode'] = self.check_dbmode
        result['OssObjectPositions'] = self.oss_object_positions
        result['OSSUrls'] = self.ossurls
        result['MigrateTaskId'] = self.migrate_task_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbname = map.get('DBName')
        self.backup_mode = map.get('BackupMode')
        self.is_online_db = map.get('IsOnlineDB')
        self.check_dbmode = map.get('CheckDBMode')
        self.oss_object_positions = map.get('OssObjectPositions')
        self.ossurls = map.get('OSSUrls')
        self.migrate_task_id = map.get('MigrateTaskId')
        return self


class CreateMigrateTaskResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, task_id=None, dbname=None, migrate_task_id=None,
                 backup_mode=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.task_id = task_id          # type: str
        self.dbname = dbname            # type: str
        self.migrate_task_id = migrate_task_id  # type: str
        self.backup_mode = backup_mode  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.migrate_task_id, 'migrate_task_id')
        self.validate_required(self.backup_mode, 'backup_mode')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['TaskId'] = self.task_id
        result['DBName'] = self.dbname
        result['MigrateTaskId'] = self.migrate_task_id
        result['BackupMode'] = self.backup_mode
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.task_id = map.get('TaskId')
        self.dbname = map.get('DBName')
        self.migrate_task_id = map.get('MigrateTaskId')
        self.backup_mode = map.get('BackupMode')
        return self


class DescribeOssDownloadsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, migrate_task_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.migrate_task_id = migrate_task_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.migrate_task_id, 'migrate_task_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['MigrateTaskId'] = self.migrate_task_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.migrate_task_id = map.get('MigrateTaskId')
        return self


class DescribeOssDownloadsResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, migrate_task_id=None, items=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.migrate_task_id = migrate_task_id  # type: str
        self.items = items              # type: DescribeOssDownloadsResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.migrate_task_id, 'migrate_task_id')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['MigrateTaskId'] = self.migrate_task_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.migrate_task_id = map.get('MigrateTaskId')
        if map.get('Items') is not None:
            temp_model = DescribeOssDownloadsResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeOssDownloadsResponseItemsOssDownload(TeaModel):
    def __init__(self, file_name=None, create_time=None, end_time=None, backup_mode=None, file_size=None,
                 status=None, is_available=None, description=None):
        self.file_name = file_name      # type: str
        self.create_time = create_time  # type: str
        self.end_time = end_time        # type: str
        self.backup_mode = backup_mode  # type: str
        self.file_size = file_size      # type: str
        self.status = status            # type: str
        self.is_available = is_available  # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.backup_mode, 'backup_mode')
        self.validate_required(self.file_size, 'file_size')
        self.validate_required(self.status, 'status')
        self.validate_required(self.is_available, 'is_available')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        result['FileName'] = self.file_name
        result['CreateTime'] = self.create_time
        result['EndTime'] = self.end_time
        result['BackupMode'] = self.backup_mode
        result['FileSize'] = self.file_size
        result['Status'] = self.status
        result['IsAvailable'] = self.is_available
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.file_name = map.get('FileName')
        self.create_time = map.get('CreateTime')
        self.end_time = map.get('EndTime')
        self.backup_mode = map.get('BackupMode')
        self.file_size = map.get('FileSize')
        self.status = map.get('Status')
        self.is_available = map.get('IsAvailable')
        self.description = map.get('Description')
        return self


class DescribeOssDownloadsResponseItems(TeaModel):
    def __init__(self, oss_download=None):
        self.oss_download = oss_download  # type: List[DescribeOssDownloadsResponseItemsOssDownload]

    def validate(self):
        self.validate_required(self.oss_download, 'oss_download')
        if self.oss_download:
            for k in self.oss_download:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['OssDownload'] = []
        if self.oss_download is not None:
            for k in self.oss_download:
                result['OssDownload'].append(k.to_map() if k else None)
        else:
            result['OssDownload'] = None
        return result

    def from_map(self, map={}):
        self.oss_download = []
        if map.get('OssDownload') is not None:
            for k in map.get('OssDownload'):
                temp_model = DescribeOssDownloadsResponseItemsOssDownload()
                self.oss_download.append(temp_model.from_map(k))
        else:
            self.oss_download = None
        return self


class DescribeMigrateTasksRequest(TeaModel):
    def __init__(self, dbinstance_id=None, start_time=None, end_time=None, page_size=None, page_number=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeMigrateTasksResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, total_record_count=None, page_number=None,
                 page_record_count=None, items=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items              # type: DescribeMigrateTasksResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['TotalRecordCount'] = self.total_record_count
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeMigrateTasksResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeMigrateTasksResponseItemsMigrateTask(TeaModel):
    def __init__(self, dbname=None, migrate_task_id=None, create_time=None, end_time=None, backup_mode=None,
                 status=None, is_dbreplaced=None, description=None):
        self.dbname = dbname            # type: str
        self.migrate_task_id = migrate_task_id  # type: str
        self.create_time = create_time  # type: str
        self.end_time = end_time        # type: str
        self.backup_mode = backup_mode  # type: str
        self.status = status            # type: str
        self.is_dbreplaced = is_dbreplaced  # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.migrate_task_id, 'migrate_task_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.backup_mode, 'backup_mode')
        self.validate_required(self.status, 'status')
        self.validate_required(self.is_dbreplaced, 'is_dbreplaced')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        result['DBName'] = self.dbname
        result['MigrateTaskId'] = self.migrate_task_id
        result['CreateTime'] = self.create_time
        result['EndTime'] = self.end_time
        result['BackupMode'] = self.backup_mode
        result['Status'] = self.status
        result['IsDBReplaced'] = self.is_dbreplaced
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.dbname = map.get('DBName')
        self.migrate_task_id = map.get('MigrateTaskId')
        self.create_time = map.get('CreateTime')
        self.end_time = map.get('EndTime')
        self.backup_mode = map.get('BackupMode')
        self.status = map.get('Status')
        self.is_dbreplaced = map.get('IsDBReplaced')
        self.description = map.get('Description')
        return self


class DescribeMigrateTasksResponseItems(TeaModel):
    def __init__(self, migrate_task=None):
        self.migrate_task = migrate_task  # type: List[DescribeMigrateTasksResponseItemsMigrateTask]

    def validate(self):
        self.validate_required(self.migrate_task, 'migrate_task')
        if self.migrate_task:
            for k in self.migrate_task:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['MigrateTask'] = []
        if self.migrate_task is not None:
            for k in self.migrate_task:
                result['MigrateTask'].append(k.to_map() if k else None)
        else:
            result['MigrateTask'] = None
        return result

    def from_map(self, map={}):
        self.migrate_task = []
        if map.get('MigrateTask') is not None:
            for k in map.get('MigrateTask'):
                temp_model = DescribeMigrateTasksResponseItemsMigrateTask()
                self.migrate_task.append(temp_model.from_map(k))
        else:
            self.migrate_task = None
        return self


class CopyDatabaseRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class CopyDatabaseResponse(TeaModel):
    def __init__(self, dbname=None, dbstatus=None, task_id=None):
        self.dbname = dbname            # type: str
        self.dbstatus = dbstatus        # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.dbstatus, 'dbstatus')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['DBName'] = self.dbname
        result['DBStatus'] = self.dbstatus
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.dbname = map.get('DBName')
        self.dbstatus = map.get('DBStatus')
        self.task_id = map.get('TaskId')
        return self


class ResetAccountRequest(TeaModel):
    def __init__(self, dbinstance_id=None, account_name=None, account_password=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.account_password, 'account_password')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['AccountName'] = self.account_name
        result['AccountPassword'] = self.account_password
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.account_name = map.get('AccountName')
        self.account_password = map.get('AccountPassword')
        return self


class ResetAccountResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeDBInstancesAsCsvRequest(TeaModel):
    def __init__(self, region_id=None, dbinstance_id=None):
        self.region_id = region_id      # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeDBInstancesAsCsvResponse(TeaModel):
    def __init__(self, request_id=None, items=None):
        self.request_id = request_id    # type: str
        self.items = items              # type: DescribeDBInstancesAsCsvResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Items') is not None:
            temp_model = DescribeDBInstancesAsCsvResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeDBInstancesAsCsvResponseItemsDBInstanceAttribute(TeaModel):
    def __init__(self, dbinstance_id=None, pay_type=None, dbinstance_class_type=None, dbinstance_type=None,
                 region_id=None, connection_string=None, port=None, engine=None, engine_version=None, dbinstance_class=None,
                 dbinstance_memory=None, dbinstance_storage=None, dbinstance_net_type=None, dbinstance_status=None,
                 dbinstance_description=None, lock_mode=None, lock_reason=None, read_delay_time=None, dbmax_quantity=None,
                 account_max_quantity=None, creation_time=None, expire_time=None, maintain_time=None, availability_value=None,
                 max_iops=None, max_connections=None, master_instance_id=None, dbinstance_cpu=None,
                 increment_source_dbinstance_id=None, guard_dbinstance_id=None, temp_dbinstance_id=None, security_iplist=None, zone_id=None,
                 instance_network_type=None, category=None, account_type=None, support_upgrade_account_type=None, vpc_id=None,
                 v_switch_id=None, connection_mode=None, tags=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.pay_type = pay_type        # type: str
        self.dbinstance_class_type = dbinstance_class_type  # type: str
        self.dbinstance_type = dbinstance_type  # type: str
        self.region_id = region_id      # type: str
        self.connection_string = connection_string  # type: str
        self.port = port                # type: str
        self.engine = engine            # type: str
        self.engine_version = engine_version  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_memory = dbinstance_memory  # type: int
        self.dbinstance_storage = dbinstance_storage  # type: int
        self.dbinstance_net_type = dbinstance_net_type  # type: str
        self.dbinstance_status = dbinstance_status  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.lock_mode = lock_mode      # type: str
        self.lock_reason = lock_reason  # type: str
        self.read_delay_time = read_delay_time  # type: str
        self.dbmax_quantity = dbmax_quantity  # type: int
        self.account_max_quantity = account_max_quantity  # type: int
        self.creation_time = creation_time  # type: str
        self.expire_time = expire_time  # type: str
        self.maintain_time = maintain_time  # type: str
        self.availability_value = availability_value  # type: str
        self.max_iops = max_iops        # type: int
        self.max_connections = max_connections  # type: int
        self.master_instance_id = master_instance_id  # type: str
        self.dbinstance_cpu = dbinstance_cpu  # type: str
        self.increment_source_dbinstance_id = increment_source_dbinstance_id  # type: str
        self.guard_dbinstance_id = guard_dbinstance_id  # type: str
        self.temp_dbinstance_id = temp_dbinstance_id  # type: str
        self.security_iplist = security_iplist  # type: str
        self.zone_id = zone_id          # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.category = category        # type: str
        self.account_type = account_type  # type: str
        self.support_upgrade_account_type = support_upgrade_account_type  # type: str
        self.vpc_id = vpc_id            # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.connection_mode = connection_mode  # type: str
        self.tags = tags                # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.pay_type, 'pay_type')
        self.validate_required(self.dbinstance_class_type, 'dbinstance_class_type')
        self.validate_required(self.dbinstance_type, 'dbinstance_type')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.connection_string, 'connection_string')
        self.validate_required(self.port, 'port')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.dbinstance_class, 'dbinstance_class')
        self.validate_required(self.dbinstance_memory, 'dbinstance_memory')
        self.validate_required(self.dbinstance_storage, 'dbinstance_storage')
        self.validate_required(self.dbinstance_net_type, 'dbinstance_net_type')
        self.validate_required(self.dbinstance_status, 'dbinstance_status')
        self.validate_required(self.dbinstance_description, 'dbinstance_description')
        self.validate_required(self.lock_mode, 'lock_mode')
        self.validate_required(self.lock_reason, 'lock_reason')
        self.validate_required(self.read_delay_time, 'read_delay_time')
        self.validate_required(self.dbmax_quantity, 'dbmax_quantity')
        self.validate_required(self.account_max_quantity, 'account_max_quantity')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.maintain_time, 'maintain_time')
        self.validate_required(self.availability_value, 'availability_value')
        self.validate_required(self.max_iops, 'max_iops')
        self.validate_required(self.max_connections, 'max_connections')
        self.validate_required(self.master_instance_id, 'master_instance_id')
        self.validate_required(self.dbinstance_cpu, 'dbinstance_cpu')
        self.validate_required(self.increment_source_dbinstance_id, 'increment_source_dbinstance_id')
        self.validate_required(self.guard_dbinstance_id, 'guard_dbinstance_id')
        self.validate_required(self.temp_dbinstance_id, 'temp_dbinstance_id')
        self.validate_required(self.security_iplist, 'security_iplist')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.instance_network_type, 'instance_network_type')
        self.validate_required(self.category, 'category')
        self.validate_required(self.account_type, 'account_type')
        self.validate_required(self.support_upgrade_account_type, 'support_upgrade_account_type')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.connection_mode, 'connection_mode')
        self.validate_required(self.tags, 'tags')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['PayType'] = self.pay_type
        result['DBInstanceClassType'] = self.dbinstance_class_type
        result['DBInstanceType'] = self.dbinstance_type
        result['RegionId'] = self.region_id
        result['ConnectionString'] = self.connection_string
        result['Port'] = self.port
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        result['DBInstanceClass'] = self.dbinstance_class
        result['DBInstanceMemory'] = self.dbinstance_memory
        result['DBInstanceStorage'] = self.dbinstance_storage
        result['DBInstanceNetType'] = self.dbinstance_net_type
        result['DBInstanceStatus'] = self.dbinstance_status
        result['DBInstanceDescription'] = self.dbinstance_description
        result['LockMode'] = self.lock_mode
        result['LockReason'] = self.lock_reason
        result['ReadDelayTime'] = self.read_delay_time
        result['DBMaxQuantity'] = self.dbmax_quantity
        result['AccountMaxQuantity'] = self.account_max_quantity
        result['CreationTime'] = self.creation_time
        result['ExpireTime'] = self.expire_time
        result['MaintainTime'] = self.maintain_time
        result['AvailabilityValue'] = self.availability_value
        result['MaxIOPS'] = self.max_iops
        result['MaxConnections'] = self.max_connections
        result['MasterInstanceId'] = self.master_instance_id
        result['DBInstanceCPU'] = self.dbinstance_cpu
        result['IncrementSourceDBInstanceId'] = self.increment_source_dbinstance_id
        result['GuardDBInstanceId'] = self.guard_dbinstance_id
        result['TempDBInstanceId'] = self.temp_dbinstance_id
        result['SecurityIPList'] = self.security_iplist
        result['ZoneId'] = self.zone_id
        result['InstanceNetworkType'] = self.instance_network_type
        result['Category'] = self.category
        result['AccountType'] = self.account_type
        result['SupportUpgradeAccountType'] = self.support_upgrade_account_type
        result['VpcId'] = self.vpc_id
        result['VSwitchId'] = self.v_switch_id
        result['ConnectionMode'] = self.connection_mode
        result['Tags'] = self.tags
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.pay_type = map.get('PayType')
        self.dbinstance_class_type = map.get('DBInstanceClassType')
        self.dbinstance_type = map.get('DBInstanceType')
        self.region_id = map.get('RegionId')
        self.connection_string = map.get('ConnectionString')
        self.port = map.get('Port')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        self.dbinstance_class = map.get('DBInstanceClass')
        self.dbinstance_memory = map.get('DBInstanceMemory')
        self.dbinstance_storage = map.get('DBInstanceStorage')
        self.dbinstance_net_type = map.get('DBInstanceNetType')
        self.dbinstance_status = map.get('DBInstanceStatus')
        self.dbinstance_description = map.get('DBInstanceDescription')
        self.lock_mode = map.get('LockMode')
        self.lock_reason = map.get('LockReason')
        self.read_delay_time = map.get('ReadDelayTime')
        self.dbmax_quantity = map.get('DBMaxQuantity')
        self.account_max_quantity = map.get('AccountMaxQuantity')
        self.creation_time = map.get('CreationTime')
        self.expire_time = map.get('ExpireTime')
        self.maintain_time = map.get('MaintainTime')
        self.availability_value = map.get('AvailabilityValue')
        self.max_iops = map.get('MaxIOPS')
        self.max_connections = map.get('MaxConnections')
        self.master_instance_id = map.get('MasterInstanceId')
        self.dbinstance_cpu = map.get('DBInstanceCPU')
        self.increment_source_dbinstance_id = map.get('IncrementSourceDBInstanceId')
        self.guard_dbinstance_id = map.get('GuardDBInstanceId')
        self.temp_dbinstance_id = map.get('TempDBInstanceId')
        self.security_iplist = map.get('SecurityIPList')
        self.zone_id = map.get('ZoneId')
        self.instance_network_type = map.get('InstanceNetworkType')
        self.category = map.get('Category')
        self.account_type = map.get('AccountType')
        self.support_upgrade_account_type = map.get('SupportUpgradeAccountType')
        self.vpc_id = map.get('VpcId')
        self.v_switch_id = map.get('VSwitchId')
        self.connection_mode = map.get('ConnectionMode')
        self.tags = map.get('Tags')
        return self


class DescribeDBInstancesAsCsvResponseItems(TeaModel):
    def __init__(self, dbinstance_attribute=None):
        self.dbinstance_attribute = dbinstance_attribute  # type: List[DescribeDBInstancesAsCsvResponseItemsDBInstanceAttribute]

    def validate(self):
        self.validate_required(self.dbinstance_attribute, 'dbinstance_attribute')
        if self.dbinstance_attribute:
            for k in self.dbinstance_attribute:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DBInstanceAttribute'] = []
        if self.dbinstance_attribute is not None:
            for k in self.dbinstance_attribute:
                result['DBInstanceAttribute'].append(k.to_map() if k else None)
        else:
            result['DBInstanceAttribute'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_attribute = []
        if map.get('DBInstanceAttribute') is not None:
            for k in map.get('DBInstanceAttribute'):
                temp_model = DescribeDBInstancesAsCsvResponseItemsDBInstanceAttribute()
                self.dbinstance_attribute.append(temp_model.from_map(k))
        else:
            self.dbinstance_attribute = None
        return self


class ModifyDBInstanceNetworkExpireTimeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, connection_string=None, classic_expired_days=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.connection_string = connection_string  # type: str
        self.classic_expired_days = classic_expired_days  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.connection_string, 'connection_string')
        self.validate_required(self.classic_expired_days, 'classic_expired_days')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['ConnectionString'] = self.connection_string
        result['ClassicExpiredDays'] = self.classic_expired_days
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.connection_string = map.get('ConnectionString')
        self.classic_expired_days = map.get('ClassicExpiredDays')
        return self


class ModifyDBInstanceNetworkExpireTimeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyResourceGroupRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, resource_group_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.resource_group_id, 'resource_group_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.resource_group_id = map.get('ResourceGroupId')
        return self


class ModifyResourceGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeRenewalPriceRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, region_id=None, pay_type=None, dbinstance_class=None,
                 used_time=None, time_type=None, quantity=None, order_type=None, business_info=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id      # type: str
        self.pay_type = pay_type        # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.used_time = used_time      # type: int
        self.time_type = time_type      # type: str
        self.quantity = quantity        # type: int
        self.order_type = order_type    # type: str
        self.business_info = business_info  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.used_time, 'used_time')
        self.validate_required(self.time_type, 'time_type')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['RegionId'] = self.region_id
        result['PayType'] = self.pay_type
        result['DBInstanceClass'] = self.dbinstance_class
        result['UsedTime'] = self.used_time
        result['TimeType'] = self.time_type
        result['Quantity'] = self.quantity
        result['OrderType'] = self.order_type
        result['BusinessInfo'] = self.business_info
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.region_id = map.get('RegionId')
        self.pay_type = map.get('PayType')
        self.dbinstance_class = map.get('DBInstanceClass')
        self.used_time = map.get('UsedTime')
        self.time_type = map.get('TimeType')
        self.quantity = map.get('Quantity')
        self.order_type = map.get('OrderType')
        self.business_info = map.get('BusinessInfo')
        return self


class DescribeRenewalPriceResponse(TeaModel):
    def __init__(self, request_id=None, rules=None, price_info=None):
        self.request_id = request_id    # type: str
        self.rules = rules              # type: DescribeRenewalPriceResponseRules
        self.price_info = price_info    # type: DescribeRenewalPriceResponsePriceInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.rules, 'rules')
        if self.rules:
            self.rules.validate()
        self.validate_required(self.price_info, 'price_info')
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        else:
            result['Rules'] = None
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        else:
            result['PriceInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Rules') is not None:
            temp_model = DescribeRenewalPriceResponseRules()
            self.rules = temp_model.from_map(map['Rules'])
        else:
            self.rules = None
        if map.get('PriceInfo') is not None:
            temp_model = DescribeRenewalPriceResponsePriceInfo()
            self.price_info = temp_model.from_map(map['PriceInfo'])
        else:
            self.price_info = None
        return self


class DescribeRenewalPriceResponseRulesRule(TeaModel):
    def __init__(self, rule_id=None, name=None, description=None):
        self.rule_id = rule_id          # type: int
        self.name = name                # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        result['RuleId'] = self.rule_id
        result['Name'] = self.name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.rule_id = map.get('RuleId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        return self


class DescribeRenewalPriceResponseRules(TeaModel):
    def __init__(self, rule=None):
        self.rule = rule                # type: List[DescribeRenewalPriceResponseRulesRule]

    def validate(self):
        self.validate_required(self.rule, 'rule')
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        else:
            result['Rule'] = None
        return result

    def from_map(self, map={}):
        self.rule = []
        if map.get('Rule') is not None:
            for k in map.get('Rule'):
                temp_model = DescribeRenewalPriceResponseRulesRule()
                self.rule.append(temp_model.from_map(k))
        else:
            self.rule = None
        return self


class DescribeRenewalPriceResponsePriceInfoCouponsCoupon(TeaModel):
    def __init__(self, coupon_no=None, name=None, description=None, is_selected=None):
        self.coupon_no = coupon_no      # type: str
        self.name = name                # type: str
        self.description = description  # type: str
        self.is_selected = is_selected  # type: str

    def validate(self):
        self.validate_required(self.coupon_no, 'coupon_no')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.is_selected, 'is_selected')

    def to_map(self):
        result = {}
        result['CouponNo'] = self.coupon_no
        result['Name'] = self.name
        result['Description'] = self.description
        result['IsSelected'] = self.is_selected
        return result

    def from_map(self, map={}):
        self.coupon_no = map.get('CouponNo')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.is_selected = map.get('IsSelected')
        return self


class DescribeRenewalPriceResponsePriceInfoCoupons(TeaModel):
    def __init__(self, coupon=None):
        self.coupon = coupon            # type: List[DescribeRenewalPriceResponsePriceInfoCouponsCoupon]

    def validate(self):
        self.validate_required(self.coupon, 'coupon')
        if self.coupon:
            for k in self.coupon:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Coupon'] = []
        if self.coupon is not None:
            for k in self.coupon:
                result['Coupon'].append(k.to_map() if k else None)
        else:
            result['Coupon'] = None
        return result

    def from_map(self, map={}):
        self.coupon = []
        if map.get('Coupon') is not None:
            for k in map.get('Coupon'):
                temp_model = DescribeRenewalPriceResponsePriceInfoCouponsCoupon()
                self.coupon.append(temp_model.from_map(k))
        else:
            self.coupon = None
        return self


class DescribeRenewalPriceResponsePriceInfoActivityInfo(TeaModel):
    def __init__(self, check_err_msg=None, error_code=None, success=None):
        self.check_err_msg = check_err_msg  # type: str
        self.error_code = error_code    # type: str
        self.success = success          # type: str

    def validate(self):
        self.validate_required(self.check_err_msg, 'check_err_msg')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['CheckErrMsg'] = self.check_err_msg
        result['ErrorCode'] = self.error_code
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.check_err_msg = map.get('CheckErrMsg')
        self.error_code = map.get('ErrorCode')
        self.success = map.get('Success')
        return self


class DescribeRenewalPriceResponsePriceInfoRuleIds(TeaModel):
    def __init__(self, rule_id=None):
        # RuleId
        self.rule_id = rule_id          # type: List[str]

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')

    def to_map(self):
        result = {}
        result['RuleId'] = self.rule_id
        return result

    def from_map(self, map={}):
        self.rule_id = map.get('RuleId')
        return self


class DescribeRenewalPriceResponsePriceInfo(TeaModel):
    def __init__(self, currency=None, original_price=None, trade_price=None, discount_price=None, coupons=None,
                 activity_info=None, rule_ids=None):
        self.currency = currency        # type: str
        self.original_price = original_price  # type: float
        self.trade_price = trade_price  # type: float
        self.discount_price = discount_price  # type: float
        self.coupons = coupons          # type: DescribeRenewalPriceResponsePriceInfoCoupons
        self.activity_info = activity_info  # type: DescribeRenewalPriceResponsePriceInfoActivityInfo
        self.rule_ids = rule_ids        # type: DescribeRenewalPriceResponsePriceInfoRuleIds

    def validate(self):
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.original_price, 'original_price')
        self.validate_required(self.trade_price, 'trade_price')
        self.validate_required(self.discount_price, 'discount_price')
        self.validate_required(self.coupons, 'coupons')
        if self.coupons:
            self.coupons.validate()
        self.validate_required(self.activity_info, 'activity_info')
        if self.activity_info:
            self.activity_info.validate()
        self.validate_required(self.rule_ids, 'rule_ids')
        if self.rule_ids:
            self.rule_ids.validate()

    def to_map(self):
        result = {}
        result['Currency'] = self.currency
        result['OriginalPrice'] = self.original_price
        result['TradePrice'] = self.trade_price
        result['DiscountPrice'] = self.discount_price
        if self.coupons is not None:
            result['Coupons'] = self.coupons.to_map()
        else:
            result['Coupons'] = None
        if self.activity_info is not None:
            result['ActivityInfo'] = self.activity_info.to_map()
        else:
            result['ActivityInfo'] = None
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()
        else:
            result['RuleIds'] = None
        return result

    def from_map(self, map={}):
        self.currency = map.get('Currency')
        self.original_price = map.get('OriginalPrice')
        self.trade_price = map.get('TradePrice')
        self.discount_price = map.get('DiscountPrice')
        if map.get('Coupons') is not None:
            temp_model = DescribeRenewalPriceResponsePriceInfoCoupons()
            self.coupons = temp_model.from_map(map['Coupons'])
        else:
            self.coupons = None
        if map.get('ActivityInfo') is not None:
            temp_model = DescribeRenewalPriceResponsePriceInfoActivityInfo()
            self.activity_info = temp_model.from_map(map['ActivityInfo'])
        else:
            self.activity_info = None
        if map.get('RuleIds') is not None:
            temp_model = DescribeRenewalPriceResponsePriceInfoRuleIds()
            self.rule_ids = temp_model.from_map(map['RuleIds'])
        else:
            self.rule_ids = None
        return self


class DescribePriceRequest(TeaModel):
    def __init__(self, client_token=None, commodity_code=None, region_id=None, engine=None, engine_version=None,
                 dbinstance_class=None, dbinstance_storage=None, pay_type=None, zone_id=None, used_time=None, time_type=None,
                 quantity=None, instance_used_type=None, order_type=None, dbinstance_storage_type=None, dbinstance_id=None):
        self.client_token = client_token  # type: str
        self.commodity_code = commodity_code  # type: str
        self.region_id = region_id      # type: str
        self.engine = engine            # type: str
        self.engine_version = engine_version  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_storage = dbinstance_storage  # type: int
        self.pay_type = pay_type        # type: str
        self.zone_id = zone_id          # type: str
        self.used_time = used_time      # type: int
        self.time_type = time_type      # type: str
        self.quantity = quantity        # type: int
        self.instance_used_type = instance_used_type  # type: int
        self.order_type = order_type    # type: str
        self.dbinstance_storage_type = dbinstance_storage_type  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.dbinstance_class, 'dbinstance_class')
        self.validate_required(self.dbinstance_storage, 'dbinstance_storage')
        self.validate_required(self.quantity, 'quantity')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['CommodityCode'] = self.commodity_code
        result['RegionId'] = self.region_id
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        result['DBInstanceClass'] = self.dbinstance_class
        result['DBInstanceStorage'] = self.dbinstance_storage
        result['PayType'] = self.pay_type
        result['ZoneId'] = self.zone_id
        result['UsedTime'] = self.used_time
        result['TimeType'] = self.time_type
        result['Quantity'] = self.quantity
        result['InstanceUsedType'] = self.instance_used_type
        result['OrderType'] = self.order_type
        result['DBInstanceStorageType'] = self.dbinstance_storage_type
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.commodity_code = map.get('CommodityCode')
        self.region_id = map.get('RegionId')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        self.dbinstance_class = map.get('DBInstanceClass')
        self.dbinstance_storage = map.get('DBInstanceStorage')
        self.pay_type = map.get('PayType')
        self.zone_id = map.get('ZoneId')
        self.used_time = map.get('UsedTime')
        self.time_type = map.get('TimeType')
        self.quantity = map.get('Quantity')
        self.instance_used_type = map.get('InstanceUsedType')
        self.order_type = map.get('OrderType')
        self.dbinstance_storage_type = map.get('DBInstanceStorageType')
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribePriceResponse(TeaModel):
    def __init__(self, request_id=None, rules=None, price_info=None):
        self.request_id = request_id    # type: str
        self.rules = rules              # type: DescribePriceResponseRules
        self.price_info = price_info    # type: DescribePriceResponsePriceInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.rules, 'rules')
        if self.rules:
            self.rules.validate()
        self.validate_required(self.price_info, 'price_info')
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.rules is not None:
            result['Rules'] = self.rules.to_map()
        else:
            result['Rules'] = None
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        else:
            result['PriceInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Rules') is not None:
            temp_model = DescribePriceResponseRules()
            self.rules = temp_model.from_map(map['Rules'])
        else:
            self.rules = None
        if map.get('PriceInfo') is not None:
            temp_model = DescribePriceResponsePriceInfo()
            self.price_info = temp_model.from_map(map['PriceInfo'])
        else:
            self.price_info = None
        return self


class DescribePriceResponseRulesRule(TeaModel):
    def __init__(self, rule_id=None, name=None, description=None):
        self.rule_id = rule_id          # type: int
        self.name = name                # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')

    def to_map(self):
        result = {}
        result['RuleId'] = self.rule_id
        result['Name'] = self.name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.rule_id = map.get('RuleId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        return self


class DescribePriceResponseRules(TeaModel):
    def __init__(self, rule=None):
        self.rule = rule                # type: List[DescribePriceResponseRulesRule]

    def validate(self):
        self.validate_required(self.rule, 'rule')
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        else:
            result['Rule'] = None
        return result

    def from_map(self, map={}):
        self.rule = []
        if map.get('Rule') is not None:
            for k in map.get('Rule'):
                temp_model = DescribePriceResponseRulesRule()
                self.rule.append(temp_model.from_map(k))
        else:
            self.rule = None
        return self


class DescribePriceResponsePriceInfoCouponsCoupon(TeaModel):
    def __init__(self, coupon_no=None, name=None, description=None, is_selected=None):
        self.coupon_no = coupon_no      # type: str
        self.name = name                # type: str
        self.description = description  # type: str
        self.is_selected = is_selected  # type: str

    def validate(self):
        self.validate_required(self.coupon_no, 'coupon_no')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.is_selected, 'is_selected')

    def to_map(self):
        result = {}
        result['CouponNo'] = self.coupon_no
        result['Name'] = self.name
        result['Description'] = self.description
        result['IsSelected'] = self.is_selected
        return result

    def from_map(self, map={}):
        self.coupon_no = map.get('CouponNo')
        self.name = map.get('Name')
        self.description = map.get('Description')
        self.is_selected = map.get('IsSelected')
        return self


class DescribePriceResponsePriceInfoCoupons(TeaModel):
    def __init__(self, coupon=None):
        self.coupon = coupon            # type: List[DescribePriceResponsePriceInfoCouponsCoupon]

    def validate(self):
        self.validate_required(self.coupon, 'coupon')
        if self.coupon:
            for k in self.coupon:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Coupon'] = []
        if self.coupon is not None:
            for k in self.coupon:
                result['Coupon'].append(k.to_map() if k else None)
        else:
            result['Coupon'] = None
        return result

    def from_map(self, map={}):
        self.coupon = []
        if map.get('Coupon') is not None:
            for k in map.get('Coupon'):
                temp_model = DescribePriceResponsePriceInfoCouponsCoupon()
                self.coupon.append(temp_model.from_map(k))
        else:
            self.coupon = None
        return self


class DescribePriceResponsePriceInfoActivityInfo(TeaModel):
    def __init__(self, check_err_msg=None, error_code=None, success=None):
        self.check_err_msg = check_err_msg  # type: str
        self.error_code = error_code    # type: str
        self.success = success          # type: str

    def validate(self):
        self.validate_required(self.check_err_msg, 'check_err_msg')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['CheckErrMsg'] = self.check_err_msg
        result['ErrorCode'] = self.error_code
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.check_err_msg = map.get('CheckErrMsg')
        self.error_code = map.get('ErrorCode')
        self.success = map.get('Success')
        return self


class DescribePriceResponsePriceInfoRuleIds(TeaModel):
    def __init__(self, rule_id=None):
        # RuleId
        self.rule_id = rule_id          # type: List[str]

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')

    def to_map(self):
        result = {}
        result['RuleId'] = self.rule_id
        return result

    def from_map(self, map={}):
        self.rule_id = map.get('RuleId')
        return self


class DescribePriceResponsePriceInfo(TeaModel):
    def __init__(self, currency=None, original_price=None, trade_price=None, discount_price=None, coupons=None,
                 activity_info=None, rule_ids=None):
        self.currency = currency        # type: str
        self.original_price = original_price  # type: float
        self.trade_price = trade_price  # type: float
        self.discount_price = discount_price  # type: float
        self.coupons = coupons          # type: DescribePriceResponsePriceInfoCoupons
        self.activity_info = activity_info  # type: DescribePriceResponsePriceInfoActivityInfo
        self.rule_ids = rule_ids        # type: DescribePriceResponsePriceInfoRuleIds

    def validate(self):
        self.validate_required(self.currency, 'currency')
        self.validate_required(self.original_price, 'original_price')
        self.validate_required(self.trade_price, 'trade_price')
        self.validate_required(self.discount_price, 'discount_price')
        self.validate_required(self.coupons, 'coupons')
        if self.coupons:
            self.coupons.validate()
        self.validate_required(self.activity_info, 'activity_info')
        if self.activity_info:
            self.activity_info.validate()
        self.validate_required(self.rule_ids, 'rule_ids')
        if self.rule_ids:
            self.rule_ids.validate()

    def to_map(self):
        result = {}
        result['Currency'] = self.currency
        result['OriginalPrice'] = self.original_price
        result['TradePrice'] = self.trade_price
        result['DiscountPrice'] = self.discount_price
        if self.coupons is not None:
            result['Coupons'] = self.coupons.to_map()
        else:
            result['Coupons'] = None
        if self.activity_info is not None:
            result['ActivityInfo'] = self.activity_info.to_map()
        else:
            result['ActivityInfo'] = None
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()
        else:
            result['RuleIds'] = None
        return result

    def from_map(self, map={}):
        self.currency = map.get('Currency')
        self.original_price = map.get('OriginalPrice')
        self.trade_price = map.get('TradePrice')
        self.discount_price = map.get('DiscountPrice')
        if map.get('Coupons') is not None:
            temp_model = DescribePriceResponsePriceInfoCoupons()
            self.coupons = temp_model.from_map(map['Coupons'])
        else:
            self.coupons = None
        if map.get('ActivityInfo') is not None:
            temp_model = DescribePriceResponsePriceInfoActivityInfo()
            self.activity_info = temp_model.from_map(map['ActivityInfo'])
        else:
            self.activity_info = None
        if map.get('RuleIds') is not None:
            temp_model = DescribePriceResponsePriceInfoRuleIds()
            self.rule_ids = temp_model.from_map(map['RuleIds'])
        else:
            self.rule_ids = None
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, period=None, auto_pay=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.period = period            # type: int
        self.auto_pay = auto_pay        # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.period, 'period')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['Period'] = self.period
        result['AutoPay'] = self.auto_pay
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.period = map.get('Period')
        self.auto_pay = map.get('AutoPay')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(self, request_id=None, order_id=None):
        self.request_id = request_id    # type: str
        self.order_id = order_id        # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['OrderId'] = self.order_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.order_id = map.get('OrderId')
        return self


class CheckRecoveryConditionsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, backup_id=None, backup_file=None, restore_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.backup_id = backup_id      # type: str
        self.backup_file = backup_file  # type: str
        self.restore_time = restore_time  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['BackupId'] = self.backup_id
        result['BackupFile'] = self.backup_file
        result['RestoreTime'] = self.restore_time
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.backup_id = map.get('BackupId')
        self.backup_file = map.get('BackupFile')
        self.restore_time = map.get('RestoreTime')
        return self


class CheckRecoveryConditionsResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, recovery_status=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.recovery_status = recovery_status  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.recovery_status, 'recovery_status')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['RecoveryStatus'] = self.recovery_status
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.recovery_status = map.get('RecoveryStatus')
        return self


class ModifyInstanceAutoRenewalAttributeRequest(TeaModel):
    def __init__(self, region_id=None, client_token=None, dbinstance_id=None, duration=None, auto_renew=None):
        self.region_id = region_id      # type: str
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.duration = duration        # type: str
        self.auto_renew = auto_renew    # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['Duration'] = self.duration
        result['AutoRenew'] = self.auto_renew
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.duration = map.get('Duration')
        self.auto_renew = map.get('AutoRenew')
        return self


class ModifyInstanceAutoRenewalAttributeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeInstanceAutoRenewalAttributeRequest(TeaModel):
    def __init__(self, client_token=None, proxy_id=None, region_id=None, dbinstance_id=None, page_size=None,
                 page_number=None):
        self.client_token = client_token  # type: str
        self.proxy_id = proxy_id        # type: str
        self.region_id = region_id      # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['proxyId'] = self.proxy_id
        result['RegionId'] = self.region_id
        result['DBInstanceId'] = self.dbinstance_id
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.proxy_id = map.get('proxyId')
        self.region_id = map.get('RegionId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeInstanceAutoRenewalAttributeResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, total_record_count=None, page_record_count=None,
                 items=None):
        self.request_id = request_id    # type: str
        self.page_number = page_number  # type: int
        self.total_record_count = total_record_count  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items              # type: DescribeInstanceAutoRenewalAttributeResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNumber'] = self.page_number
        result['TotalRecordCount'] = self.total_record_count
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_number = map.get('PageNumber')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeInstanceAutoRenewalAttributeResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeInstanceAutoRenewalAttributeResponseItemsItem(TeaModel):
    def __init__(self, dbinstance_id=None, region_id=None, duration=None, status=None, auto_renew=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.region_id = region_id      # type: str
        self.duration = duration        # type: int
        self.status = status            # type: str
        self.auto_renew = auto_renew    # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.status, 'status')
        self.validate_required(self.auto_renew, 'auto_renew')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['RegionId'] = self.region_id
        result['Duration'] = self.duration
        result['Status'] = self.status
        result['AutoRenew'] = self.auto_renew
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.region_id = map.get('RegionId')
        self.duration = map.get('Duration')
        self.status = map.get('Status')
        self.auto_renew = map.get('AutoRenew')
        return self


class DescribeInstanceAutoRenewalAttributeResponseItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[DescribeInstanceAutoRenewalAttributeResponseItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = DescribeInstanceAutoRenewalAttributeResponseItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class ReleaseReadWriteSplittingConnectionRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class ReleaseReadWriteSplittingConnectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyReadWriteSplittingConnectionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, connection_string_prefix=None, port=None, max_delay_time=None,
                 distribution_type=None, weight=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.connection_string_prefix = connection_string_prefix  # type: str
        self.port = port                # type: str
        self.max_delay_time = max_delay_time  # type: str
        self.distribution_type = distribution_type  # type: str
        self.weight = weight            # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['ConnectionStringPrefix'] = self.connection_string_prefix
        result['Port'] = self.port
        result['MaxDelayTime'] = self.max_delay_time
        result['DistributionType'] = self.distribution_type
        result['Weight'] = self.weight
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.connection_string_prefix = map.get('ConnectionStringPrefix')
        self.port = map.get('Port')
        self.max_delay_time = map.get('MaxDelayTime')
        self.distribution_type = map.get('DistributionType')
        self.weight = map.get('Weight')
        return self


class ModifyReadWriteSplittingConnectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CalculateDBInstanceWeightRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class CalculateDBInstanceWeightResponse(TeaModel):
    def __init__(self, request_id=None, items=None):
        self.request_id = request_id    # type: str
        self.items = items              # type: CalculateDBInstanceWeightResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Items') is not None:
            temp_model = CalculateDBInstanceWeightResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class CalculateDBInstanceWeightResponseItemsDBInstanceWeight(TeaModel):
    def __init__(self, dbinstance_id=None, dbinstance_type=None, readonly_instance_sqldelayed_time=None,
                 weight=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_type = dbinstance_type  # type: str
        self.readonly_instance_sqldelayed_time = readonly_instance_sqldelayed_time  # type: str
        self.weight = weight            # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbinstance_type, 'dbinstance_type')
        self.validate_required(self.readonly_instance_sqldelayed_time, 'readonly_instance_sqldelayed_time')
        self.validate_required(self.weight, 'weight')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBInstanceType'] = self.dbinstance_type
        result['ReadonlyInstanceSQLDelayedTime'] = self.readonly_instance_sqldelayed_time
        result['Weight'] = self.weight
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbinstance_type = map.get('DBInstanceType')
        self.readonly_instance_sqldelayed_time = map.get('ReadonlyInstanceSQLDelayedTime')
        self.weight = map.get('Weight')
        return self


class CalculateDBInstanceWeightResponseItems(TeaModel):
    def __init__(self, dbinstance_weight=None):
        self.dbinstance_weight = dbinstance_weight  # type: List[CalculateDBInstanceWeightResponseItemsDBInstanceWeight]

    def validate(self):
        self.validate_required(self.dbinstance_weight, 'dbinstance_weight')
        if self.dbinstance_weight:
            for k in self.dbinstance_weight:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DBInstanceWeight'] = []
        if self.dbinstance_weight is not None:
            for k in self.dbinstance_weight:
                result['DBInstanceWeight'].append(k.to_map() if k else None)
        else:
            result['DBInstanceWeight'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_weight = []
        if map.get('DBInstanceWeight') is not None:
            for k in map.get('DBInstanceWeight'):
                temp_model = CalculateDBInstanceWeightResponseItemsDBInstanceWeight()
                self.dbinstance_weight.append(temp_model.from_map(k))
        else:
            self.dbinstance_weight = None
        return self


class AllocateReadWriteSplittingConnectionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, connection_string_prefix=None, port=None, max_delay_time=None,
                 net_type=None, distribution_type=None, weight=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.connection_string_prefix = connection_string_prefix  # type: str
        self.port = port                # type: str
        self.max_delay_time = max_delay_time  # type: str
        self.net_type = net_type        # type: str
        self.distribution_type = distribution_type  # type: str
        self.weight = weight            # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['ConnectionStringPrefix'] = self.connection_string_prefix
        result['Port'] = self.port
        result['MaxDelayTime'] = self.max_delay_time
        result['NetType'] = self.net_type
        result['DistributionType'] = self.distribution_type
        result['Weight'] = self.weight
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.connection_string_prefix = map.get('ConnectionStringPrefix')
        self.port = map.get('Port')
        self.max_delay_time = map.get('MaxDelayTime')
        self.net_type = map.get('NetType')
        self.distribution_type = map.get('DistributionType')
        self.weight = map.get('Weight')
        return self


class AllocateReadWriteSplittingConnectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyDBInstancePayTypeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, used_time=None, pay_type=None, period=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.used_time = used_time      # type: int
        self.pay_type = pay_type        # type: str
        self.period = period            # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.pay_type, 'pay_type')
        self.validate_required(self.period, 'period')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['UsedTime'] = self.used_time
        result['PayType'] = self.pay_type
        result['Period'] = self.period
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.used_time = map.get('UsedTime')
        self.pay_type = map.get('PayType')
        self.period = map.get('Period')
        return self


class ModifyDBInstancePayTypeResponse(TeaModel):
    def __init__(self, order_id=None):
        self.order_id = order_id        # type: int

    def validate(self):
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = {}
        result['OrderId'] = self.order_id
        return result

    def from_map(self, map={}):
        self.order_id = map.get('OrderId')
        return self


class DescribeCharacterSetNameRequest(TeaModel):
    def __init__(self, engine=None, region_id=None):
        self.engine = engine            # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['Engine'] = self.engine
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.engine = map.get('Engine')
        self.region_id = map.get('RegionId')
        return self


class DescribeCharacterSetNameResponse(TeaModel):
    def __init__(self, request_id=None, engine=None, character_set_name_items=None):
        self.request_id = request_id    # type: str
        self.engine = engine            # type: str
        self.character_set_name_items = character_set_name_items  # type: DescribeCharacterSetNameResponseCharacterSetNameItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.character_set_name_items, 'character_set_name_items')
        if self.character_set_name_items:
            self.character_set_name_items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Engine'] = self.engine
        if self.character_set_name_items is not None:
            result['CharacterSetNameItems'] = self.character_set_name_items.to_map()
        else:
            result['CharacterSetNameItems'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.engine = map.get('Engine')
        if map.get('CharacterSetNameItems') is not None:
            temp_model = DescribeCharacterSetNameResponseCharacterSetNameItems()
            self.character_set_name_items = temp_model.from_map(map['CharacterSetNameItems'])
        else:
            self.character_set_name_items = None
        return self


class DescribeCharacterSetNameResponseCharacterSetNameItems(TeaModel):
    def __init__(self, character_set_name=None):
        self.character_set_name = character_set_name  # type: List[str]

    def validate(self):
        self.validate_required(self.character_set_name, 'character_set_name')

    def to_map(self):
        result = {}
        result['CharacterSetName'] = self.character_set_name
        return result

    def from_map(self, map={}):
        self.character_set_name = map.get('CharacterSetName')
        return self


class DeleteBackupRequest(TeaModel):
    def __init__(self, dbinstance_id=None, backup_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.backup_id = backup_id      # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.backup_id, 'backup_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['BackupId'] = self.backup_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.backup_id = map.get('BackupId')
        return self


class DeleteBackupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeDiagnosticReportListRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeDiagnosticReportListResponse(TeaModel):
    def __init__(self, request_id=None, report_list=None):
        self.request_id = request_id    # type: str
        self.report_list = report_list  # type: List[DescribeDiagnosticReportListResponseReportList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.report_list, 'report_list')
        if self.report_list:
            for k in self.report_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ReportList'] = []
        if self.report_list is not None:
            for k in self.report_list:
                result['ReportList'].append(k.to_map() if k else None)
        else:
            result['ReportList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.report_list = []
        if map.get('ReportList') is not None:
            for k in map.get('ReportList'):
                temp_model = DescribeDiagnosticReportListResponseReportList()
                self.report_list.append(temp_model.from_map(k))
        else:
            self.report_list = None
        return self


class DescribeDiagnosticReportListResponseReportList(TeaModel):
    def __init__(self, diagnostic_time=None, score=None, start_time=None, end_time=None, download_url=None):
        self.diagnostic_time = diagnostic_time  # type: str
        self.score = score              # type: int
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.download_url = download_url  # type: str

    def validate(self):
        self.validate_required(self.diagnostic_time, 'diagnostic_time')
        self.validate_required(self.score, 'score')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.download_url, 'download_url')

    def to_map(self):
        result = {}
        result['DiagnosticTime'] = self.diagnostic_time
        result['Score'] = self.score
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['DownloadURL'] = self.download_url
        return result

    def from_map(self, map={}):
        self.diagnostic_time = map.get('DiagnosticTime')
        self.score = map.get('Score')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.download_url = map.get('DownloadURL')
        return self


class CreateDiagnosticReportRequest(TeaModel):
    def __init__(self, dbinstance_id=None, start_time=None, end_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class CreateDiagnosticReportResponse(TeaModel):
    def __init__(self, request_id=None, report_id=None):
        self.request_id = request_id    # type: str
        self.report_id = report_id      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.report_id, 'report_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ReportId'] = self.report_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.report_id = map.get('ReportId')
        return self


class CloneDBInstanceRequest(TeaModel):
    def __init__(self, region_id=None, zone_id=None, dbinstance_class=None, dbinstance_storage=None, db_names=None,
                 pay_type=None, instance_network_type=None, dbinstance_id=None, backup_id=None, restore_time=None,
                 vpcid=None, v_switch_id=None, private_ip_address=None, used_time=None, period=None, category=None,
                 dbinstance_storage_type=None, restore_table=None, table_meta=None, dedicated_host_group_id=None, backup_type=None):
        self.region_id = region_id      # type: str
        self.zone_id = zone_id          # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_storage = dbinstance_storage  # type: int
        self.db_names = db_names        # type: str
        self.pay_type = pay_type        # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.backup_id = backup_id      # type: str
        self.restore_time = restore_time  # type: str
        self.vpcid = vpcid              # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.used_time = used_time      # type: int
        self.period = period            # type: str
        self.category = category        # type: str
        self.dbinstance_storage_type = dbinstance_storage_type  # type: str
        self.restore_table = restore_table  # type: str
        self.table_meta = table_meta    # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.backup_type = backup_type  # type: str

    def validate(self):
        self.validate_required(self.pay_type, 'pay_type')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ZoneId'] = self.zone_id
        result['DBInstanceClass'] = self.dbinstance_class
        result['DBInstanceStorage'] = self.dbinstance_storage
        result['DbNames'] = self.db_names
        result['PayType'] = self.pay_type
        result['InstanceNetworkType'] = self.instance_network_type
        result['DBInstanceId'] = self.dbinstance_id
        result['BackupId'] = self.backup_id
        result['RestoreTime'] = self.restore_time
        result['VPCId'] = self.vpcid
        result['VSwitchId'] = self.v_switch_id
        result['PrivateIpAddress'] = self.private_ip_address
        result['UsedTime'] = self.used_time
        result['Period'] = self.period
        result['Category'] = self.category
        result['DBInstanceStorageType'] = self.dbinstance_storage_type
        result['RestoreTable'] = self.restore_table
        result['TableMeta'] = self.table_meta
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['BackupType'] = self.backup_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.zone_id = map.get('ZoneId')
        self.dbinstance_class = map.get('DBInstanceClass')
        self.dbinstance_storage = map.get('DBInstanceStorage')
        self.db_names = map.get('DbNames')
        self.pay_type = map.get('PayType')
        self.instance_network_type = map.get('InstanceNetworkType')
        self.dbinstance_id = map.get('DBInstanceId')
        self.backup_id = map.get('BackupId')
        self.restore_time = map.get('RestoreTime')
        self.vpcid = map.get('VPCId')
        self.v_switch_id = map.get('VSwitchId')
        self.private_ip_address = map.get('PrivateIpAddress')
        self.used_time = map.get('UsedTime')
        self.period = map.get('Period')
        self.category = map.get('Category')
        self.dbinstance_storage_type = map.get('DBInstanceStorageType')
        self.restore_table = map.get('RestoreTable')
        self.table_meta = map.get('TableMeta')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.backup_type = map.get('BackupType')
        return self


class CloneDBInstanceResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, order_id=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.order_id = order_id        # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.order_id, 'order_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['OrderId'] = self.order_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.order_id = map.get('OrderId')
        return self


class DescribeTagsRequest(TeaModel):
    def __init__(self, client_token=None, proxy_id=None, region_id=None, dbinstance_id=None, tags=None):
        # description: 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII字符，且该参数值中不能包含非ASCII字符。; 
        self.client_token = client_token  # type: str
        # description: 代理模式ID。; 
        self.proxy_id = proxy_id        # type: str
        # description: 地域ID，可以通过接口[DescribeRegions](~~26243~~)查看可用的地域ID。; 
        self.region_id = region_id      # type: str
        # description: 实例ID。>传入该参数，其他过滤条件失效。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: 需要查询的标签，包括TagKey和TagValue。格式：{“key1”:”value1”}。; 
        self.tags = tags                # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['proxyId'] = self.proxy_id
        result['RegionId'] = self.region_id
        result['DBInstanceId'] = self.dbinstance_id
        result['Tags'] = self.tags
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.proxy_id = map.get('proxyId')
        self.region_id = map.get('RegionId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.tags = map.get('Tags')
        return self


class DescribeTagsResponse(TeaModel):
    def __init__(self, request_id=None, items=None):
        # description: 请求ID。; 
        self.request_id = request_id    # type: str
        # description: 由Tag信息组成的数组。
        self.items = items              # type: DescribeTagsResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Items') is not None:
            temp_model = DescribeTagsResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeTagsResponseItemsTagInfosDBInstanceIds(TeaModel):
    def __init__(self, dbinstance_ids=None):
        # DBInstanceIds
        self.dbinstance_ids = dbinstance_ids  # type: List[str]

    def validate(self):
        self.validate_required(self.dbinstance_ids, 'dbinstance_ids')

    def to_map(self):
        result = {}
        result['DBInstanceIds'] = self.dbinstance_ids
        return result

    def from_map(self, map={}):
        self.dbinstance_ids = map.get('DBInstanceIds')
        return self


class DescribeTagsResponseItemsTagInfos(TeaModel):
    def __init__(self, tag_key=None, tag_value=None, dbinstance_ids=None):
        # description: 标签键。; 
        self.tag_key = tag_key          # type: str
        # description: 标签值。; 
        self.tag_value = tag_value      # type: str
        self.dbinstance_ids = dbinstance_ids  # type: DescribeTagsResponseItemsTagInfosDBInstanceIds

    def validate(self):
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')
        self.validate_required(self.dbinstance_ids, 'dbinstance_ids')
        if self.dbinstance_ids:
            self.dbinstance_ids.validate()

    def to_map(self):
        result = {}
        result['TagKey'] = self.tag_key
        result['TagValue'] = self.tag_value
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids.to_map()
        else:
            result['DBInstanceIds'] = None
        return result

    def from_map(self, map={}):
        self.tag_key = map.get('TagKey')
        self.tag_value = map.get('TagValue')
        if map.get('DBInstanceIds') is not None:
            temp_model = DescribeTagsResponseItemsTagInfosDBInstanceIds()
            self.dbinstance_ids = temp_model.from_map(map['DBInstanceIds'])
        else:
            self.dbinstance_ids = None
        return self


class DescribeTagsResponseItems(TeaModel):
    def __init__(self, tag_infos=None):
        self.tag_infos = tag_infos      # type: List[DescribeTagsResponseItemsTagInfos]

    def validate(self):
        self.validate_required(self.tag_infos, 'tag_infos')
        if self.tag_infos:
            for k in self.tag_infos:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TagInfos'] = []
        if self.tag_infos is not None:
            for k in self.tag_infos:
                result['TagInfos'].append(k.to_map() if k else None)
        else:
            result['TagInfos'] = None
        return result

    def from_map(self, map={}):
        self.tag_infos = []
        if map.get('TagInfos') is not None:
            for k in map.get('TagInfos'):
                temp_model = DescribeTagsResponseItemsTagInfos()
                self.tag_infos.append(temp_model.from_map(k))
        else:
            self.tag_infos = None
        return self


class DescribeDBInstanceByTagsRequest(TeaModel):
    def __init__(self, client_token=None, proxy_id=None, region_id=None, dbinstance_id=None, page_size=None,
                 page_number=None):
        self.client_token = client_token  # type: str
        self.proxy_id = proxy_id        # type: str
        self.region_id = region_id      # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['proxyId'] = self.proxy_id
        result['RegionId'] = self.region_id
        result['DBInstanceId'] = self.dbinstance_id
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.proxy_id = map.get('proxyId')
        self.region_id = map.get('RegionId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeDBInstanceByTagsResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_record_count=None, total_record_count=None,
                 items=None):
        self.request_id = request_id    # type: str
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.total_record_count = total_record_count  # type: int
        self.items = items              # type: DescribeDBInstanceByTagsResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        result['TotalRecordCount'] = self.total_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        self.total_record_count = map.get('TotalRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeDBInstanceByTagsResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeDBInstanceByTagsResponseItemsDBInstanceTagTagsTag(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key          # type: str
        self.tag_value = tag_value      # type: str

    def validate(self):
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')

    def to_map(self):
        result = {}
        result['TagKey'] = self.tag_key
        result['TagValue'] = self.tag_value
        return result

    def from_map(self, map={}):
        self.tag_key = map.get('TagKey')
        self.tag_value = map.get('TagValue')
        return self


class DescribeDBInstanceByTagsResponseItemsDBInstanceTagTags(TeaModel):
    def __init__(self, tag=None):
        self.tag = tag                  # type: List[DescribeDBInstanceByTagsResponseItemsDBInstanceTagTagsTag]

    def validate(self):
        self.validate_required(self.tag, 'tag')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = DescribeDBInstanceByTagsResponseItemsDBInstanceTagTagsTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class DescribeDBInstanceByTagsResponseItemsDBInstanceTag(TeaModel):
    def __init__(self, dbinstance_id=None, tags=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.tags = tags                # type: DescribeDBInstanceByTagsResponseItemsDBInstanceTagTags

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.tags, 'tags')
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        else:
            result['Tags'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        if map.get('Tags') is not None:
            temp_model = DescribeDBInstanceByTagsResponseItemsDBInstanceTagTags()
            self.tags = temp_model.from_map(map['Tags'])
        else:
            self.tags = None
        return self


class DescribeDBInstanceByTagsResponseItems(TeaModel):
    def __init__(self, dbinstance_tag=None):
        self.dbinstance_tag = dbinstance_tag  # type: List[DescribeDBInstanceByTagsResponseItemsDBInstanceTag]

    def validate(self):
        self.validate_required(self.dbinstance_tag, 'dbinstance_tag')
        if self.dbinstance_tag:
            for k in self.dbinstance_tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DBInstanceTag'] = []
        if self.dbinstance_tag is not None:
            for k in self.dbinstance_tag:
                result['DBInstanceTag'].append(k.to_map() if k else None)
        else:
            result['DBInstanceTag'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_tag = []
        if map.get('DBInstanceTag') is not None:
            for k in map.get('DBInstanceTag'):
                temp_model = DescribeDBInstanceByTagsResponseItemsDBInstanceTag()
                self.dbinstance_tag.append(temp_model.from_map(k))
        else:
            self.dbinstance_tag = None
        return self


class RevokeOperatorPermissionRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class RevokeOperatorPermissionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyDBInstanceTDERequest(TeaModel):
    def __init__(self, dbinstance_id=None, tdestatus=None, dbname=None, encryption_key=None, role_arn=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.tdestatus = tdestatus      # type: str
        self.dbname = dbname            # type: str
        self.encryption_key = encryption_key  # type: str
        self.role_arn = role_arn        # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.tdestatus, 'tdestatus')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['TDEStatus'] = self.tdestatus
        result['DBName'] = self.dbname
        result['EncryptionKey'] = self.encryption_key
        result['RoleArn'] = self.role_arn
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.tdestatus = map.get('TDEStatus')
        self.dbname = map.get('DBName')
        self.encryption_key = map.get('EncryptionKey')
        self.role_arn = map.get('RoleArn')
        return self


class ModifyDBInstanceTDEResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyDBInstanceSSLRequest(TeaModel):
    def __init__(self, dbinstance_id=None, connection_string=None, sslenabled=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.connection_string = connection_string  # type: str
        self.sslenabled = sslenabled    # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.connection_string, 'connection_string')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['ConnectionString'] = self.connection_string
        result['SSLEnabled'] = self.sslenabled
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.connection_string = map.get('ConnectionString')
        self.sslenabled = map.get('SSLEnabled')
        return self


class ModifyDBInstanceSSLResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class GrantOperatorPermissionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, expired_time=None, privileges=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.expired_time = expired_time  # type: str
        self.privileges = privileges    # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.expired_time, 'expired_time')
        self.validate_required(self.privileges, 'privileges')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['ExpiredTime'] = self.expired_time
        result['Privileges'] = self.privileges
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.expired_time = map.get('ExpiredTime')
        self.privileges = map.get('Privileges')
        return self


class GrantOperatorPermissionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeDBInstanceTDERequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeDBInstanceTDEResponse(TeaModel):
    def __init__(self, request_id=None, tdestatus=None, databases=None):
        self.request_id = request_id    # type: str
        self.tdestatus = tdestatus      # type: str
        self.databases = databases      # type: DescribeDBInstanceTDEResponseDatabases

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.tdestatus, 'tdestatus')
        self.validate_required(self.databases, 'databases')
        if self.databases:
            self.databases.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TDEStatus'] = self.tdestatus
        if self.databases is not None:
            result['Databases'] = self.databases.to_map()
        else:
            result['Databases'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.tdestatus = map.get('TDEStatus')
        if map.get('Databases') is not None:
            temp_model = DescribeDBInstanceTDEResponseDatabases()
            self.databases = temp_model.from_map(map['Databases'])
        else:
            self.databases = None
        return self


class DescribeDBInstanceTDEResponseDatabasesDatabase(TeaModel):
    def __init__(self, dbname=None, tdestatus=None):
        self.dbname = dbname            # type: str
        self.tdestatus = tdestatus      # type: str

    def validate(self):
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.tdestatus, 'tdestatus')

    def to_map(self):
        result = {}
        result['DBName'] = self.dbname
        result['TDEStatus'] = self.tdestatus
        return result

    def from_map(self, map={}):
        self.dbname = map.get('DBName')
        self.tdestatus = map.get('TDEStatus')
        return self


class DescribeDBInstanceTDEResponseDatabases(TeaModel):
    def __init__(self, database=None):
        self.database = database        # type: List[DescribeDBInstanceTDEResponseDatabasesDatabase]

    def validate(self):
        self.validate_required(self.database, 'database')
        if self.database:
            for k in self.database:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Database'] = []
        if self.database is not None:
            for k in self.database:
                result['Database'].append(k.to_map() if k else None)
        else:
            result['Database'] = None
        return result

    def from_map(self, map={}):
        self.database = []
        if map.get('Database') is not None:
            for k in map.get('Database'):
                temp_model = DescribeDBInstanceTDEResponseDatabasesDatabase()
                self.database.append(temp_model.from_map(k))
        else:
            self.database = None
        return self


class DescribeDBInstanceSSLRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeDBInstanceSSLResponse(TeaModel):
    def __init__(self, request_id=None, connection_string=None, sslexpire_time=None, require_update=None,
                 require_update_reason=None):
        self.request_id = request_id    # type: str
        self.connection_string = connection_string  # type: str
        self.sslexpire_time = sslexpire_time  # type: str
        self.require_update = require_update  # type: str
        self.require_update_reason = require_update_reason  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.connection_string, 'connection_string')
        self.validate_required(self.sslexpire_time, 'sslexpire_time')
        self.validate_required(self.require_update, 'require_update')
        self.validate_required(self.require_update_reason, 'require_update_reason')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ConnectionString'] = self.connection_string
        result['SSLExpireTime'] = self.sslexpire_time
        result['RequireUpdate'] = self.require_update
        result['RequireUpdateReason'] = self.require_update_reason
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.connection_string = map.get('ConnectionString')
        self.sslexpire_time = map.get('SSLExpireTime')
        self.require_update = map.get('RequireUpdate')
        self.require_update_reason = map.get('RequireUpdateReason')
        return self


class DescribeSQLLogFilesRequest(TeaModel):
    def __init__(self, dbinstance_id=None, file_name=None, page_size=None, page_number=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.file_name = file_name      # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['FileName'] = self.file_name
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.file_name = map.get('FileName')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeSQLLogFilesResponse(TeaModel):
    def __init__(self, request_id=None, total_record_count=None, page_number=None, page_record_count=None,
                 items=None):
        self.request_id = request_id    # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items              # type: DescribeSQLLogFilesResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalRecordCount'] = self.total_record_count
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeSQLLogFilesResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeSQLLogFilesResponseItemsLogFile(TeaModel):
    def __init__(self, file_id=None, log_status=None, log_download_url=None, log_size=None, log_start_time=None,
                 log_end_time=None):
        self.file_id = file_id          # type: str
        self.log_status = log_status    # type: str
        self.log_download_url = log_download_url  # type: str
        self.log_size = log_size        # type: str
        self.log_start_time = log_start_time  # type: str
        self.log_end_time = log_end_time  # type: str

    def validate(self):
        self.validate_required(self.file_id, 'file_id')
        self.validate_required(self.log_status, 'log_status')
        self.validate_required(self.log_download_url, 'log_download_url')
        self.validate_required(self.log_size, 'log_size')
        self.validate_required(self.log_start_time, 'log_start_time')
        self.validate_required(self.log_end_time, 'log_end_time')

    def to_map(self):
        result = {}
        result['FileID'] = self.file_id
        result['LogStatus'] = self.log_status
        result['LogDownloadURL'] = self.log_download_url
        result['LogSize'] = self.log_size
        result['LogStartTime'] = self.log_start_time
        result['LogEndTime'] = self.log_end_time
        return result

    def from_map(self, map={}):
        self.file_id = map.get('FileID')
        self.log_status = map.get('LogStatus')
        self.log_download_url = map.get('LogDownloadURL')
        self.log_size = map.get('LogSize')
        self.log_start_time = map.get('LogStartTime')
        self.log_end_time = map.get('LogEndTime')
        return self


class DescribeSQLLogFilesResponseItems(TeaModel):
    def __init__(self, log_file=None):
        self.log_file = log_file        # type: List[DescribeSQLLogFilesResponseItemsLogFile]

    def validate(self):
        self.validate_required(self.log_file, 'log_file')
        if self.log_file:
            for k in self.log_file:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LogFile'] = []
        if self.log_file is not None:
            for k in self.log_file:
                result['LogFile'].append(k.to_map() if k else None)
        else:
            result['LogFile'] = None
        return result

    def from_map(self, map={}):
        self.log_file = []
        if map.get('LogFile') is not None:
            for k in map.get('LogFile'):
                temp_model = DescribeSQLLogFilesResponseItemsLogFile()
                self.log_file.append(temp_model.from_map(k))
        else:
            self.log_file = None
        return self


class ModifyDBInstanceMonitorRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, period=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.period = period            # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.period, 'period')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['Period'] = self.period
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.period = map.get('Period')
        return self


class ModifyDBInstanceMonitorResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class SwitchDBInstanceHARequest(TeaModel):
    def __init__(self, dbinstance_id=None, node_id=None, force=None, effective_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.node_id = node_id          # type: str
        self.force = force              # type: str
        self.effective_time = effective_time  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.node_id, 'node_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['NodeId'] = self.node_id
        result['Force'] = self.force
        result['EffectiveTime'] = self.effective_time
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.node_id = map.get('NodeId')
        self.force = map.get('Force')
        self.effective_time = map.get('EffectiveTime')
        return self


class SwitchDBInstanceHAResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeDBInstanceMonitorRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeDBInstanceMonitorResponse(TeaModel):
    def __init__(self, request_id=None, period=None):
        self.request_id = request_id    # type: str
        self.period = period            # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.period, 'period')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Period'] = self.period
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.period = map.get('Period')
        return self


class DescribeSQLCollectorPolicyRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, resource_group_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.resource_group_id = map.get('ResourceGroupId')
        return self


class DescribeSQLCollectorPolicyResponse(TeaModel):
    def __init__(self, request_id=None, sqlcollector_status=None, storage_period=None):
        self.request_id = request_id    # type: str
        self.sqlcollector_status = sqlcollector_status  # type: str
        self.storage_period = storage_period  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.sqlcollector_status, 'sqlcollector_status')
        self.validate_required(self.storage_period, 'storage_period')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['SQLCollectorStatus'] = self.sqlcollector_status
        result['StoragePeriod'] = self.storage_period
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.sqlcollector_status = map.get('SQLCollectorStatus')
        self.storage_period = map.get('StoragePeriod')
        return self


class ModifySQLCollectorPolicyRequest(TeaModel):
    def __init__(self, dbinstance_id=None, sqlcollector_status=None, resource_group_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.sqlcollector_status = sqlcollector_status  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.sqlcollector_status, 'sqlcollector_status')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['SQLCollectorStatus'] = self.sqlcollector_status
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.sqlcollector_status = map.get('SQLCollectorStatus')
        self.resource_group_id = map.get('ResourceGroupId')
        return self


class ModifySQLCollectorPolicyResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyDBInstanceHAConfigRequest(TeaModel):
    def __init__(self, sync_mode=None, hamode=None, db_instance_id=None):
        self.sync_mode = sync_mode      # type: str
        self.hamode = hamode            # type: str
        self.db_instance_id = db_instance_id  # type: str

    def validate(self):
        self.validate_required(self.sync_mode, 'sync_mode')
        self.validate_required(self.hamode, 'hamode')
        self.validate_required(self.db_instance_id, 'db_instance_id')

    def to_map(self):
        result = {}
        result['SyncMode'] = self.sync_mode
        result['HAMode'] = self.hamode
        result['DbInstanceId'] = self.db_instance_id
        return result

    def from_map(self, map={}):
        self.sync_mode = map.get('SyncMode')
        self.hamode = map.get('HAMode')
        self.db_instance_id = map.get('DbInstanceId')
        return self


class ModifyDBInstanceHAConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeDBInstanceHAConfigRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeDBInstanceHAConfigResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, sync_mode=None, hamode=None, host_instance_infos=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.sync_mode = sync_mode      # type: str
        self.hamode = hamode            # type: str
        self.host_instance_infos = host_instance_infos  # type: DescribeDBInstanceHAConfigResponseHostInstanceInfos

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.sync_mode, 'sync_mode')
        self.validate_required(self.hamode, 'hamode')
        self.validate_required(self.host_instance_infos, 'host_instance_infos')
        if self.host_instance_infos:
            self.host_instance_infos.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['SyncMode'] = self.sync_mode
        result['HAMode'] = self.hamode
        if self.host_instance_infos is not None:
            result['HostInstanceInfos'] = self.host_instance_infos.to_map()
        else:
            result['HostInstanceInfos'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.sync_mode = map.get('SyncMode')
        self.hamode = map.get('HAMode')
        if map.get('HostInstanceInfos') is not None:
            temp_model = DescribeDBInstanceHAConfigResponseHostInstanceInfos()
            self.host_instance_infos = temp_model.from_map(map['HostInstanceInfos'])
        else:
            self.host_instance_infos = None
        return self


class DescribeDBInstanceHAConfigResponseHostInstanceInfosNodeInfo(TeaModel):
    def __init__(self, node_id=None, region_id=None, log_sync_time=None, data_sync_time=None, node_type=None,
                 zone_id=None, sync_status=None):
        self.node_id = node_id          # type: str
        self.region_id = region_id      # type: str
        self.log_sync_time = log_sync_time  # type: str
        self.data_sync_time = data_sync_time  # type: str
        self.node_type = node_type      # type: str
        self.zone_id = zone_id          # type: str
        self.sync_status = sync_status  # type: str

    def validate(self):
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.log_sync_time, 'log_sync_time')
        self.validate_required(self.data_sync_time, 'data_sync_time')
        self.validate_required(self.node_type, 'node_type')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.sync_status, 'sync_status')

    def to_map(self):
        result = {}
        result['NodeId'] = self.node_id
        result['RegionId'] = self.region_id
        result['LogSyncTime'] = self.log_sync_time
        result['DataSyncTime'] = self.data_sync_time
        result['NodeType'] = self.node_type
        result['ZoneId'] = self.zone_id
        result['SyncStatus'] = self.sync_status
        return result

    def from_map(self, map={}):
        self.node_id = map.get('NodeId')
        self.region_id = map.get('RegionId')
        self.log_sync_time = map.get('LogSyncTime')
        self.data_sync_time = map.get('DataSyncTime')
        self.node_type = map.get('NodeType')
        self.zone_id = map.get('ZoneId')
        self.sync_status = map.get('SyncStatus')
        return self


class DescribeDBInstanceHAConfigResponseHostInstanceInfos(TeaModel):
    def __init__(self, node_info=None):
        self.node_info = node_info      # type: List[DescribeDBInstanceHAConfigResponseHostInstanceInfosNodeInfo]

    def validate(self):
        self.validate_required(self.node_info, 'node_info')
        if self.node_info:
            for k in self.node_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['NodeInfo'] = []
        if self.node_info is not None:
            for k in self.node_info:
                result['NodeInfo'].append(k.to_map() if k else None)
        else:
            result['NodeInfo'] = None
        return result

    def from_map(self, map={}):
        self.node_info = []
        if map.get('NodeInfo') is not None:
            for k in map.get('NodeInfo'):
                temp_model = DescribeDBInstanceHAConfigResponseHostInstanceInfosNodeInfo()
                self.node_info.append(temp_model.from_map(k))
        else:
            self.node_info = None
        return self


class DescribeSQLReportsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, start_time=None, end_time=None, page_size=None, page_number=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeSQLReportsResponse(TeaModel):
    def __init__(self, request_id=None, total_record_count=None, page_number=None, page_record_count=None,
                 items=None):
        self.request_id = request_id    # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items              # type: DescribeSQLReportsResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalRecordCount'] = self.total_record_count
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeSQLReportsResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeSQLReportsResponseItemsItemLatencyTopNItemsLatencyTopNItem(TeaModel):
    def __init__(self, sqltext=None, avg_latency=None, sqlexecute_times=None):
        self.sqltext = sqltext          # type: str
        self.avg_latency = avg_latency  # type: int
        self.sqlexecute_times = sqlexecute_times  # type: int

    def validate(self):
        self.validate_required(self.sqltext, 'sqltext')
        self.validate_required(self.avg_latency, 'avg_latency')
        self.validate_required(self.sqlexecute_times, 'sqlexecute_times')

    def to_map(self):
        result = {}
        result['SQLText'] = self.sqltext
        result['AvgLatency'] = self.avg_latency
        result['SQLExecuteTimes'] = self.sqlexecute_times
        return result

    def from_map(self, map={}):
        self.sqltext = map.get('SQLText')
        self.avg_latency = map.get('AvgLatency')
        self.sqlexecute_times = map.get('SQLExecuteTimes')
        return self


class DescribeSQLReportsResponseItemsItemLatencyTopNItems(TeaModel):
    def __init__(self, latency_top_nitem=None):
        self.latency_top_nitem = latency_top_nitem  # type: List[DescribeSQLReportsResponseItemsItemLatencyTopNItemsLatencyTopNItem]

    def validate(self):
        self.validate_required(self.latency_top_nitem, 'latency_top_nitem')
        if self.latency_top_nitem:
            for k in self.latency_top_nitem:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LatencyTopNItem'] = []
        if self.latency_top_nitem is not None:
            for k in self.latency_top_nitem:
                result['LatencyTopNItem'].append(k.to_map() if k else None)
        else:
            result['LatencyTopNItem'] = None
        return result

    def from_map(self, map={}):
        self.latency_top_nitem = []
        if map.get('LatencyTopNItem') is not None:
            for k in map.get('LatencyTopNItem'):
                temp_model = DescribeSQLReportsResponseItemsItemLatencyTopNItemsLatencyTopNItem()
                self.latency_top_nitem.append(temp_model.from_map(k))
        else:
            self.latency_top_nitem = None
        return self


class DescribeSQLReportsResponseItemsItemQPSTopNItemsQPSTopNItem(TeaModel):
    def __init__(self, sqltext=None, sqlexecute_times=None):
        self.sqltext = sqltext          # type: str
        self.sqlexecute_times = sqlexecute_times  # type: int

    def validate(self):
        self.validate_required(self.sqltext, 'sqltext')
        self.validate_required(self.sqlexecute_times, 'sqlexecute_times')

    def to_map(self):
        result = {}
        result['SQLText'] = self.sqltext
        result['SQLExecuteTimes'] = self.sqlexecute_times
        return result

    def from_map(self, map={}):
        self.sqltext = map.get('SQLText')
        self.sqlexecute_times = map.get('SQLExecuteTimes')
        return self


class DescribeSQLReportsResponseItemsItemQPSTopNItems(TeaModel):
    def __init__(self, qpstop_nitem=None):
        self.qpstop_nitem = qpstop_nitem  # type: List[DescribeSQLReportsResponseItemsItemQPSTopNItemsQPSTopNItem]

    def validate(self):
        self.validate_required(self.qpstop_nitem, 'qpstop_nitem')
        if self.qpstop_nitem:
            for k in self.qpstop_nitem:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['QPSTopNItem'] = []
        if self.qpstop_nitem is not None:
            for k in self.qpstop_nitem:
                result['QPSTopNItem'].append(k.to_map() if k else None)
        else:
            result['QPSTopNItem'] = None
        return result

    def from_map(self, map={}):
        self.qpstop_nitem = []
        if map.get('QPSTopNItem') is not None:
            for k in map.get('QPSTopNItem'):
                temp_model = DescribeSQLReportsResponseItemsItemQPSTopNItemsQPSTopNItem()
                self.qpstop_nitem.append(temp_model.from_map(k))
        else:
            self.qpstop_nitem = None
        return self


class DescribeSQLReportsResponseItemsItem(TeaModel):
    def __init__(self, report_time=None, latency_top_nitems=None, qpstop_nitems=None):
        self.report_time = report_time  # type: str
        self.latency_top_nitems = latency_top_nitems  # type: DescribeSQLReportsResponseItemsItemLatencyTopNItems
        self.qpstop_nitems = qpstop_nitems  # type: DescribeSQLReportsResponseItemsItemQPSTopNItems

    def validate(self):
        self.validate_required(self.report_time, 'report_time')
        self.validate_required(self.latency_top_nitems, 'latency_top_nitems')
        if self.latency_top_nitems:
            self.latency_top_nitems.validate()
        self.validate_required(self.qpstop_nitems, 'qpstop_nitems')
        if self.qpstop_nitems:
            self.qpstop_nitems.validate()

    def to_map(self):
        result = {}
        result['ReportTime'] = self.report_time
        if self.latency_top_nitems is not None:
            result['LatencyTopNItems'] = self.latency_top_nitems.to_map()
        else:
            result['LatencyTopNItems'] = None
        if self.qpstop_nitems is not None:
            result['QPSTopNItems'] = self.qpstop_nitems.to_map()
        else:
            result['QPSTopNItems'] = None
        return result

    def from_map(self, map={}):
        self.report_time = map.get('ReportTime')
        if map.get('LatencyTopNItems') is not None:
            temp_model = DescribeSQLReportsResponseItemsItemLatencyTopNItems()
            self.latency_top_nitems = temp_model.from_map(map['LatencyTopNItems'])
        else:
            self.latency_top_nitems = None
        if map.get('QPSTopNItems') is not None:
            temp_model = DescribeSQLReportsResponseItemsItemQPSTopNItems()
            self.qpstop_nitems = temp_model.from_map(map['QPSTopNItems'])
        else:
            self.qpstop_nitems = None
        return self


class DescribeSQLReportsResponseItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[DescribeSQLReportsResponseItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = DescribeSQLReportsResponseItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class DescribeDBInstanceIPArrayListRequest(TeaModel):
    def __init__(self, dbinstance_id=None, whitelist_network_type=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.whitelist_network_type = whitelist_network_type  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['WhitelistNetworkType'] = self.whitelist_network_type
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.whitelist_network_type = map.get('WhitelistNetworkType')
        return self


class DescribeDBInstanceIPArrayListResponse(TeaModel):
    def __init__(self, request_id=None, items=None):
        self.request_id = request_id    # type: str
        self.items = items              # type: DescribeDBInstanceIPArrayListResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Items') is not None:
            temp_model = DescribeDBInstanceIPArrayListResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeDBInstanceIPArrayListResponseItemsDBInstanceIPArray(TeaModel):
    def __init__(self, dbinstance_iparray_name=None, dbinstance_iparray_attribute=None, security_iptype=None,
                 security_iplist=None):
        self.dbinstance_iparray_name = dbinstance_iparray_name  # type: str
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute  # type: str
        self.security_iptype = security_iptype  # type: str
        self.security_iplist = security_iplist  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_iparray_name, 'dbinstance_iparray_name')
        self.validate_required(self.dbinstance_iparray_attribute, 'dbinstance_iparray_attribute')
        self.validate_required(self.security_iptype, 'security_iptype')
        self.validate_required(self.security_iplist, 'security_iplist')

    def to_map(self):
        result = {}
        result['DBInstanceIPArrayName'] = self.dbinstance_iparray_name
        result['DBInstanceIPArrayAttribute'] = self.dbinstance_iparray_attribute
        result['SecurityIPType'] = self.security_iptype
        result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, map={}):
        self.dbinstance_iparray_name = map.get('DBInstanceIPArrayName')
        self.dbinstance_iparray_attribute = map.get('DBInstanceIPArrayAttribute')
        self.security_iptype = map.get('SecurityIPType')
        self.security_iplist = map.get('SecurityIPList')
        return self


class DescribeDBInstanceIPArrayListResponseItems(TeaModel):
    def __init__(self, dbinstance_iparray=None):
        self.dbinstance_iparray = dbinstance_iparray  # type: List[DescribeDBInstanceIPArrayListResponseItemsDBInstanceIPArray]

    def validate(self):
        self.validate_required(self.dbinstance_iparray, 'dbinstance_iparray')
        if self.dbinstance_iparray:
            for k in self.dbinstance_iparray:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DBInstanceIPArray'] = []
        if self.dbinstance_iparray is not None:
            for k in self.dbinstance_iparray:
                result['DBInstanceIPArray'].append(k.to_map() if k else None)
        else:
            result['DBInstanceIPArray'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_iparray = []
        if map.get('DBInstanceIPArray') is not None:
            for k in map.get('DBInstanceIPArray'):
                temp_model = DescribeDBInstanceIPArrayListResponseItemsDBInstanceIPArray()
                self.dbinstance_iparray.append(temp_model.from_map(k))
        else:
            self.dbinstance_iparray = None
        return self


class DescribeSQLLogReportListRequest(TeaModel):
    def __init__(self, dbinstance_id=None, start_time=None, end_time=None, page_size=None, page_number=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeSQLLogReportListResponse(TeaModel):
    def __init__(self, request_id=None, total_record_count=None, page_number=None, page_record_count=None,
                 items=None):
        self.request_id = request_id    # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items              # type: DescribeSQLLogReportListResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalRecordCount'] = self.total_record_count
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeSQLLogReportListResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeSQLLogReportListResponseItemsItemLatencyTopNItemsLatencyTopNItem(TeaModel):
    def __init__(self, sqltext=None, avg_latency=None, sqlexecute_times=None):
        self.sqltext = sqltext          # type: str
        self.avg_latency = avg_latency  # type: int
        self.sqlexecute_times = sqlexecute_times  # type: int

    def validate(self):
        self.validate_required(self.sqltext, 'sqltext')
        self.validate_required(self.avg_latency, 'avg_latency')
        self.validate_required(self.sqlexecute_times, 'sqlexecute_times')

    def to_map(self):
        result = {}
        result['SQLText'] = self.sqltext
        result['AvgLatency'] = self.avg_latency
        result['SQLExecuteTimes'] = self.sqlexecute_times
        return result

    def from_map(self, map={}):
        self.sqltext = map.get('SQLText')
        self.avg_latency = map.get('AvgLatency')
        self.sqlexecute_times = map.get('SQLExecuteTimes')
        return self


class DescribeSQLLogReportListResponseItemsItemLatencyTopNItems(TeaModel):
    def __init__(self, latency_top_nitem=None):
        self.latency_top_nitem = latency_top_nitem  # type: List[DescribeSQLLogReportListResponseItemsItemLatencyTopNItemsLatencyTopNItem]

    def validate(self):
        self.validate_required(self.latency_top_nitem, 'latency_top_nitem')
        if self.latency_top_nitem:
            for k in self.latency_top_nitem:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LatencyTopNItem'] = []
        if self.latency_top_nitem is not None:
            for k in self.latency_top_nitem:
                result['LatencyTopNItem'].append(k.to_map() if k else None)
        else:
            result['LatencyTopNItem'] = None
        return result

    def from_map(self, map={}):
        self.latency_top_nitem = []
        if map.get('LatencyTopNItem') is not None:
            for k in map.get('LatencyTopNItem'):
                temp_model = DescribeSQLLogReportListResponseItemsItemLatencyTopNItemsLatencyTopNItem()
                self.latency_top_nitem.append(temp_model.from_map(k))
        else:
            self.latency_top_nitem = None
        return self


class DescribeSQLLogReportListResponseItemsItemQPSTopNItemsQPSTopNItem(TeaModel):
    def __init__(self, sqltext=None, sqlexecute_times=None):
        self.sqltext = sqltext          # type: str
        self.sqlexecute_times = sqlexecute_times  # type: int

    def validate(self):
        self.validate_required(self.sqltext, 'sqltext')
        self.validate_required(self.sqlexecute_times, 'sqlexecute_times')

    def to_map(self):
        result = {}
        result['SQLText'] = self.sqltext
        result['SQLExecuteTimes'] = self.sqlexecute_times
        return result

    def from_map(self, map={}):
        self.sqltext = map.get('SQLText')
        self.sqlexecute_times = map.get('SQLExecuteTimes')
        return self


class DescribeSQLLogReportListResponseItemsItemQPSTopNItems(TeaModel):
    def __init__(self, qpstop_nitem=None):
        self.qpstop_nitem = qpstop_nitem  # type: List[DescribeSQLLogReportListResponseItemsItemQPSTopNItemsQPSTopNItem]

    def validate(self):
        self.validate_required(self.qpstop_nitem, 'qpstop_nitem')
        if self.qpstop_nitem:
            for k in self.qpstop_nitem:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['QPSTopNItem'] = []
        if self.qpstop_nitem is not None:
            for k in self.qpstop_nitem:
                result['QPSTopNItem'].append(k.to_map() if k else None)
        else:
            result['QPSTopNItem'] = None
        return result

    def from_map(self, map={}):
        self.qpstop_nitem = []
        if map.get('QPSTopNItem') is not None:
            for k in map.get('QPSTopNItem'):
                temp_model = DescribeSQLLogReportListResponseItemsItemQPSTopNItemsQPSTopNItem()
                self.qpstop_nitem.append(temp_model.from_map(k))
        else:
            self.qpstop_nitem = None
        return self


class DescribeSQLLogReportListResponseItemsItem(TeaModel):
    def __init__(self, report_time=None, latency_top_nitems=None, qpstop_nitems=None):
        self.report_time = report_time  # type: str
        self.latency_top_nitems = latency_top_nitems  # type: DescribeSQLLogReportListResponseItemsItemLatencyTopNItems
        self.qpstop_nitems = qpstop_nitems  # type: DescribeSQLLogReportListResponseItemsItemQPSTopNItems

    def validate(self):
        self.validate_required(self.report_time, 'report_time')
        self.validate_required(self.latency_top_nitems, 'latency_top_nitems')
        if self.latency_top_nitems:
            self.latency_top_nitems.validate()
        self.validate_required(self.qpstop_nitems, 'qpstop_nitems')
        if self.qpstop_nitems:
            self.qpstop_nitems.validate()

    def to_map(self):
        result = {}
        result['ReportTime'] = self.report_time
        if self.latency_top_nitems is not None:
            result['LatencyTopNItems'] = self.latency_top_nitems.to_map()
        else:
            result['LatencyTopNItems'] = None
        if self.qpstop_nitems is not None:
            result['QPSTopNItems'] = self.qpstop_nitems.to_map()
        else:
            result['QPSTopNItems'] = None
        return result

    def from_map(self, map={}):
        self.report_time = map.get('ReportTime')
        if map.get('LatencyTopNItems') is not None:
            temp_model = DescribeSQLLogReportListResponseItemsItemLatencyTopNItems()
            self.latency_top_nitems = temp_model.from_map(map['LatencyTopNItems'])
        else:
            self.latency_top_nitems = None
        if map.get('QPSTopNItems') is not None:
            temp_model = DescribeSQLLogReportListResponseItemsItemQPSTopNItems()
            self.qpstop_nitems = temp_model.from_map(map['QPSTopNItems'])
        else:
            self.qpstop_nitems = None
        return self


class DescribeSQLLogReportListResponseItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[DescribeSQLLogReportListResponseItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = DescribeSQLLogReportListResponseItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class ResetAccountForPGRequest(TeaModel):
    def __init__(self, dbinstance_id=None, account_name=None, account_password=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.account_password, 'account_password')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['AccountName'] = self.account_name
        result['AccountPassword'] = self.account_password
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.account_name = map.get('AccountName')
        self.account_password = map.get('AccountPassword')
        return self


class ResetAccountForPGResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class UpgradeDBInstanceEngineVersionRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, engine_version=None, effective_time=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.engine_version = engine_version  # type: str
        self.effective_time = effective_time  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.engine_version, 'engine_version')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['EngineVersion'] = self.engine_version
        result['EffectiveTime'] = self.effective_time
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.engine_version = map.get('EngineVersion')
        self.effective_time = map.get('EffectiveTime')
        return self


class UpgradeDBInstanceEngineVersionResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        return self


class RevokeAccountPrivilegeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, account_name=None, dbname=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.account_name = account_name  # type: str
        self.dbname = dbname            # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.dbname, 'dbname')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['AccountName'] = self.account_name
        result['DBName'] = self.dbname
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.account_name = map.get('AccountName')
        self.dbname = map.get('DBName')
        return self


class RevokeAccountPrivilegeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class RestartDBInstanceRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class RestartDBInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(self, dbinstance_id=None, account_name=None, account_password=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.account_password, 'account_password')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['AccountName'] = self.account_name
        result['AccountPassword'] = self.account_password
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.account_name = map.get('AccountName')
        self.account_password = map.get('AccountPassword')
        return self


class ResetAccountPasswordResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class RemoveTagsFromResourceRequest(TeaModel):
    def __init__(self, client_token=None, proxy_id=None, region_id=None, dbinstance_id=None, tags=None, tag=None):
        # description: 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII字符，且该参数值中不能包含非ASCII字符。; 
        self.client_token = client_token  # type: str
        # description: 代理模式ID。; 
        self.proxy_id = proxy_id        # type: str
        # description: 地域ID，可以通过接口[DescribeRegions](~~26243~~)查看可用的地域ID。; 
        self.region_id = region_id      # type: str
        # description: 实例ID。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: 需要解绑的一组标签，包括TagKey和TagValue。格式：{"key1":"value1"}。>TagKey不能为空，TagValue可以为空。; 
        self.tags = tags                # type: str
        self.tag = tag                  # type: List[RemoveTagsFromResourceRequestTag]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['proxyId'] = self.proxy_id
        result['RegionId'] = self.region_id
        result['DBInstanceId'] = self.dbinstance_id
        result['Tags'] = self.tags
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.proxy_id = map.get('proxyId')
        self.region_id = map.get('RegionId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.tags = map.get('Tags')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = RemoveTagsFromResourceRequestTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class RemoveTagsFromResourceRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['key'] = self.key
        result['value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('key')
        self.value = map.get('value')
        return self


class RemoveTagsFromResourceResponse(TeaModel):
    def __init__(self, request_id=None):
        # description: 请求ID。; 
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class PurgeDBInstanceLogRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class PurgeDBInstanceLogResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifySecurityIpsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, security_ips=None, dbinstance_iparray_name=None,
                 dbinstance_iparray_attribute=None, security_iptype=None, whitelist_network_type=None, modify_mode=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.security_ips = security_ips  # type: str
        self.dbinstance_iparray_name = dbinstance_iparray_name  # type: str
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute  # type: str
        self.security_iptype = security_iptype  # type: str
        self.whitelist_network_type = whitelist_network_type  # type: str
        self.modify_mode = modify_mode  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.security_ips, 'security_ips')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['SecurityIps'] = self.security_ips
        result['DBInstanceIPArrayName'] = self.dbinstance_iparray_name
        result['DBInstanceIPArrayAttribute'] = self.dbinstance_iparray_attribute
        result['SecurityIPType'] = self.security_iptype
        result['WhitelistNetworkType'] = self.whitelist_network_type
        result['ModifyMode'] = self.modify_mode
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.security_ips = map.get('SecurityIps')
        self.dbinstance_iparray_name = map.get('DBInstanceIPArrayName')
        self.dbinstance_iparray_attribute = map.get('DBInstanceIPArrayAttribute')
        self.security_iptype = map.get('SecurityIPType')
        self.whitelist_network_type = map.get('WhitelistNetworkType')
        self.modify_mode = map.get('ModifyMode')
        return self


class ModifySecurityIpsResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        return self


class ModifyParameterRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, parameters=None, forcerestart=None,
                 parameter_group_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.parameters = parameters    # type: str
        self.forcerestart = forcerestart  # type: bool
        self.parameter_group_id = parameter_group_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['Parameters'] = self.parameters
        result['Forcerestart'] = self.forcerestart
        result['ParameterGroupId'] = self.parameter_group_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.parameters = map.get('Parameters')
        self.forcerestart = map.get('Forcerestart')
        self.parameter_group_id = map.get('ParameterGroupId')
        return self


class ModifyParameterResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyDBInstanceSpecRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbinstance_class=None, dbinstance_storage=None, pay_type=None,
                 effective_time=None, engine_version=None, dbinstance_storage_type=None, direction=None, source_biz=None,
                 dedicated_host_group_id=None, zone_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_storage = dbinstance_storage  # type: int
        self.pay_type = pay_type        # type: str
        self.effective_time = effective_time  # type: str
        self.engine_version = engine_version  # type: str
        self.dbinstance_storage_type = dbinstance_storage_type  # type: str
        self.direction = direction      # type: str
        self.source_biz = source_biz    # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.zone_id = zone_id          # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.pay_type, 'pay_type')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBInstanceClass'] = self.dbinstance_class
        result['DBInstanceStorage'] = self.dbinstance_storage
        result['PayType'] = self.pay_type
        result['EffectiveTime'] = self.effective_time
        result['EngineVersion'] = self.engine_version
        result['DBInstanceStorageType'] = self.dbinstance_storage_type
        result['Direction'] = self.direction
        result['SourceBiz'] = self.source_biz
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['ZoneId'] = self.zone_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbinstance_class = map.get('DBInstanceClass')
        self.dbinstance_storage = map.get('DBInstanceStorage')
        self.pay_type = map.get('PayType')
        self.effective_time = map.get('EffectiveTime')
        self.engine_version = map.get('EngineVersion')
        self.dbinstance_storage_type = map.get('DBInstanceStorageType')
        self.direction = map.get('Direction')
        self.source_biz = map.get('SourceBiz')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.zone_id = map.get('ZoneId')
        return self


class ModifyDBInstanceSpecResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyDBInstanceMaintainTimeRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, maintain_time=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.maintain_time = maintain_time  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.maintain_time, 'maintain_time')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['MaintainTime'] = self.maintain_time
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.maintain_time = map.get('MaintainTime')
        return self


class ModifyDBInstanceMaintainTimeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyDBInstanceDescriptionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbinstance_description=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_description = dbinstance_description  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbinstance_description, 'dbinstance_description')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBInstanceDescription'] = self.dbinstance_description
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbinstance_description = map.get('DBInstanceDescription')
        return self


class ModifyDBInstanceDescriptionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyDBDescriptionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbname=None, dbdescription=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbname = dbname            # type: str
        self.dbdescription = dbdescription  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.dbdescription, 'dbdescription')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBName'] = self.dbname
        result['DBDescription'] = self.dbdescription
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbname = map.get('DBName')
        self.dbdescription = map.get('DBDescription')
        return self


class ModifyDBDescriptionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(self, dbinstance_id=None, backup_policy_mode=None, preferred_backup_time=None,
                 preferred_backup_period=None, backup_retention_period=None, backup_log=None, log_backup_retention_period=None,
                 enable_backup_log=None, local_log_retention_hours=None, local_log_retention_space=None,
                 high_space_usage_protection=None, log_backup_frequency=None, compress_type=None, archive_backup_retention_period=None,
                 archive_backup_keep_policy=None, archive_backup_keep_count=None, released_keep_policy=None,
                 log_backup_local_retention_number=None, category=None, backup_interval=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.backup_policy_mode = backup_policy_mode  # type: str
        self.preferred_backup_time = preferred_backup_time  # type: str
        self.preferred_backup_period = preferred_backup_period  # type: str
        self.backup_retention_period = backup_retention_period  # type: str
        self.backup_log = backup_log    # type: str
        self.log_backup_retention_period = log_backup_retention_period  # type: str
        self.enable_backup_log = enable_backup_log  # type: str
        self.local_log_retention_hours = local_log_retention_hours  # type: str
        self.local_log_retention_space = local_log_retention_space  # type: str
        self.high_space_usage_protection = high_space_usage_protection  # type: str
        self.log_backup_frequency = log_backup_frequency  # type: str
        self.compress_type = compress_type  # type: str
        self.archive_backup_retention_period = archive_backup_retention_period  # type: str
        self.archive_backup_keep_policy = archive_backup_keep_policy  # type: str
        self.archive_backup_keep_count = archive_backup_keep_count  # type: str
        self.released_keep_policy = released_keep_policy  # type: str
        self.log_backup_local_retention_number = log_backup_local_retention_number  # type: int
        self.category = category        # type: str
        self.backup_interval = backup_interval  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['BackupPolicyMode'] = self.backup_policy_mode
        result['PreferredBackupTime'] = self.preferred_backup_time
        result['PreferredBackupPeriod'] = self.preferred_backup_period
        result['BackupRetentionPeriod'] = self.backup_retention_period
        result['BackupLog'] = self.backup_log
        result['LogBackupRetentionPeriod'] = self.log_backup_retention_period
        result['EnableBackupLog'] = self.enable_backup_log
        result['LocalLogRetentionHours'] = self.local_log_retention_hours
        result['LocalLogRetentionSpace'] = self.local_log_retention_space
        result['HighSpaceUsageProtection'] = self.high_space_usage_protection
        result['LogBackupFrequency'] = self.log_backup_frequency
        result['CompressType'] = self.compress_type
        result['ArchiveBackupRetentionPeriod'] = self.archive_backup_retention_period
        result['ArchiveBackupKeepPolicy'] = self.archive_backup_keep_policy
        result['ArchiveBackupKeepCount'] = self.archive_backup_keep_count
        result['ReleasedKeepPolicy'] = self.released_keep_policy
        result['LogBackupLocalRetentionNumber'] = self.log_backup_local_retention_number
        result['Category'] = self.category
        result['BackupInterval'] = self.backup_interval
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.backup_policy_mode = map.get('BackupPolicyMode')
        self.preferred_backup_time = map.get('PreferredBackupTime')
        self.preferred_backup_period = map.get('PreferredBackupPeriod')
        self.backup_retention_period = map.get('BackupRetentionPeriod')
        self.backup_log = map.get('BackupLog')
        self.log_backup_retention_period = map.get('LogBackupRetentionPeriod')
        self.enable_backup_log = map.get('EnableBackupLog')
        self.local_log_retention_hours = map.get('LocalLogRetentionHours')
        self.local_log_retention_space = map.get('LocalLogRetentionSpace')
        self.high_space_usage_protection = map.get('HighSpaceUsageProtection')
        self.log_backup_frequency = map.get('LogBackupFrequency')
        self.compress_type = map.get('CompressType')
        self.archive_backup_retention_period = map.get('ArchiveBackupRetentionPeriod')
        self.archive_backup_keep_policy = map.get('ArchiveBackupKeepPolicy')
        self.archive_backup_keep_count = map.get('ArchiveBackupKeepCount')
        self.released_keep_policy = map.get('ReleasedKeepPolicy')
        self.log_backup_local_retention_number = map.get('LogBackupLocalRetentionNumber')
        self.category = map.get('Category')
        self.backup_interval = map.get('BackupInterval')
        return self


class ModifyBackupPolicyResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, enable_backup_log=None, local_log_retention_hours=None,
                 local_log_retention_space=None, high_space_usage_protection=None, compress_type=None,
                 log_backup_local_retention_number=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.enable_backup_log = enable_backup_log  # type: str
        self.local_log_retention_hours = local_log_retention_hours  # type: int
        self.local_log_retention_space = local_log_retention_space  # type: str
        self.high_space_usage_protection = high_space_usage_protection  # type: str
        self.compress_type = compress_type  # type: str
        self.log_backup_local_retention_number = log_backup_local_retention_number  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.enable_backup_log, 'enable_backup_log')
        self.validate_required(self.local_log_retention_hours, 'local_log_retention_hours')
        self.validate_required(self.local_log_retention_space, 'local_log_retention_space')
        self.validate_required(self.high_space_usage_protection, 'high_space_usage_protection')
        self.validate_required(self.compress_type, 'compress_type')
        self.validate_required(self.log_backup_local_retention_number, 'log_backup_local_retention_number')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceID'] = self.dbinstance_id
        result['EnableBackupLog'] = self.enable_backup_log
        result['LocalLogRetentionHours'] = self.local_log_retention_hours
        result['LocalLogRetentionSpace'] = self.local_log_retention_space
        result['HighSpaceUsageProtection'] = self.high_space_usage_protection
        result['CompressType'] = self.compress_type
        result['LogBackupLocalRetentionNumber'] = self.log_backup_local_retention_number
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceID')
        self.enable_backup_log = map.get('EnableBackupLog')
        self.local_log_retention_hours = map.get('LocalLogRetentionHours')
        self.local_log_retention_space = map.get('LocalLogRetentionSpace')
        self.high_space_usage_protection = map.get('HighSpaceUsageProtection')
        self.compress_type = map.get('CompressType')
        self.log_backup_local_retention_number = map.get('LogBackupLocalRetentionNumber')
        return self


class ModifyAccountDescriptionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, account_name=None, account_description=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.account_name = account_name  # type: str
        self.account_description = account_description  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.account_description, 'account_description')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['AccountName'] = self.account_name
        result['AccountDescription'] = self.account_description
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.account_name = map.get('AccountName')
        self.account_description = map.get('AccountDescription')
        return self


class ModifyAccountDescriptionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class MigrateToOtherZoneRequest(TeaModel):
    def __init__(self, dbinstance_id=None, vpcid=None, zone_id=None, effective_time=None, v_switch_id=None,
                 category=None, zone_id_slave_1=None, zone_id_slave_2=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.vpcid = vpcid              # type: str
        self.zone_id = zone_id          # type: str
        self.effective_time = effective_time  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.category = category        # type: str
        self.zone_id_slave_1 = zone_id_slave_1  # type: str
        self.zone_id_slave_2 = zone_id_slave_2  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.zone_id, 'zone_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['VPCId'] = self.vpcid
        result['ZoneId'] = self.zone_id
        result['EffectiveTime'] = self.effective_time
        result['VSwitchId'] = self.v_switch_id
        result['Category'] = self.category
        result['ZoneIdSlave1'] = self.zone_id_slave_1
        result['ZoneIdSlave2'] = self.zone_id_slave_2
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.vpcid = map.get('VPCId')
        self.zone_id = map.get('ZoneId')
        self.effective_time = map.get('EffectiveTime')
        self.v_switch_id = map.get('VSwitchId')
        self.category = map.get('Category')
        self.zone_id_slave_1 = map.get('ZoneIdSlave1')
        self.zone_id_slave_2 = map.get('ZoneIdSlave2')
        return self


class MigrateToOtherZoneResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ImportDatabaseBetweenInstancesRequest(TeaModel):
    def __init__(self, dbinstance_id=None, source_dbinstance_id=None, dbinfo=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.source_dbinstance_id = source_dbinstance_id  # type: str
        self.dbinfo = dbinfo            # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.source_dbinstance_id, 'source_dbinstance_id')
        self.validate_required(self.dbinfo, 'dbinfo')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['SourceDBInstanceId'] = self.source_dbinstance_id
        result['DBInfo'] = self.dbinfo
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.source_dbinstance_id = map.get('SourceDBInstanceId')
        self.dbinfo = map.get('DBInfo')
        return self


class ImportDatabaseBetweenInstancesResponse(TeaModel):
    def __init__(self, request_id=None, import_id=None):
        self.request_id = request_id    # type: str
        self.import_id = import_id      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.import_id, 'import_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ImportId'] = self.import_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.import_id = map.get('ImportId')
        return self


class GrantAccountPrivilegeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, account_name=None, dbname=None, account_privilege=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.account_name = account_name  # type: str
        self.dbname = dbname            # type: str
        self.account_privilege = account_privilege  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.account_privilege, 'account_privilege')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['AccountName'] = self.account_name
        result['DBName'] = self.dbname
        result['AccountPrivilege'] = self.account_privilege
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.account_name = map.get('AccountName')
        self.dbname = map.get('DBName')
        self.account_privilege = map.get('AccountPrivilege')
        return self


class GrantAccountPrivilegeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeTasksRequest(TeaModel):
    def __init__(self, dbinstance_id=None, start_time=None, end_time=None, page_size=None, page_number=None,
                 status=None, task_action=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.status = status            # type: str
        self.task_action = task_action  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['Status'] = self.status
        result['TaskAction'] = self.task_action
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.status = map.get('Status')
        self.task_action = map.get('TaskAction')
        return self


class DescribeTasksResponse(TeaModel):
    def __init__(self, request_id=None, total_record_count=None, page_number=None, page_record_count=None,
                 items=None):
        self.request_id = request_id    # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items              # type: DescribeTasksResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalRecordCount'] = self.total_record_count
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeTasksResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeTasksResponseItemsTaskProgressInfo(TeaModel):
    def __init__(self, dbname=None, begin_time=None, progress_info=None, finish_time=None, task_action=None,
                 task_id=None, progress=None, expected_finish_time=None, status=None, task_error_code=None,
                 task_error_message=None, steps_info=None, remain=None, step_progress_info=None, current_step_name=None):
        self.dbname = dbname            # type: str
        self.begin_time = begin_time    # type: str
        self.progress_info = progress_info  # type: str
        self.finish_time = finish_time  # type: str
        self.task_action = task_action  # type: str
        self.task_id = task_id          # type: str
        self.progress = progress        # type: str
        self.expected_finish_time = expected_finish_time  # type: str
        self.status = status            # type: str
        self.task_error_code = task_error_code  # type: str
        self.task_error_message = task_error_message  # type: str
        self.steps_info = steps_info    # type: str
        self.remain = remain            # type: int
        self.step_progress_info = step_progress_info  # type: str
        self.current_step_name = current_step_name  # type: str

    def validate(self):
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.begin_time, 'begin_time')
        self.validate_required(self.progress_info, 'progress_info')
        self.validate_required(self.finish_time, 'finish_time')
        self.validate_required(self.task_action, 'task_action')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.progress, 'progress')
        self.validate_required(self.expected_finish_time, 'expected_finish_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.task_error_code, 'task_error_code')
        self.validate_required(self.task_error_message, 'task_error_message')
        self.validate_required(self.steps_info, 'steps_info')
        self.validate_required(self.remain, 'remain')
        self.validate_required(self.step_progress_info, 'step_progress_info')
        self.validate_required(self.current_step_name, 'current_step_name')

    def to_map(self):
        result = {}
        result['DBName'] = self.dbname
        result['BeginTime'] = self.begin_time
        result['ProgressInfo'] = self.progress_info
        result['FinishTime'] = self.finish_time
        result['TaskAction'] = self.task_action
        result['TaskId'] = self.task_id
        result['Progress'] = self.progress
        result['ExpectedFinishTime'] = self.expected_finish_time
        result['Status'] = self.status
        result['TaskErrorCode'] = self.task_error_code
        result['TaskErrorMessage'] = self.task_error_message
        result['StepsInfo'] = self.steps_info
        result['Remain'] = self.remain
        result['StepProgressInfo'] = self.step_progress_info
        result['CurrentStepName'] = self.current_step_name
        return result

    def from_map(self, map={}):
        self.dbname = map.get('DBName')
        self.begin_time = map.get('BeginTime')
        self.progress_info = map.get('ProgressInfo')
        self.finish_time = map.get('FinishTime')
        self.task_action = map.get('TaskAction')
        self.task_id = map.get('TaskId')
        self.progress = map.get('Progress')
        self.expected_finish_time = map.get('ExpectedFinishTime')
        self.status = map.get('Status')
        self.task_error_code = map.get('TaskErrorCode')
        self.task_error_message = map.get('TaskErrorMessage')
        self.steps_info = map.get('StepsInfo')
        self.remain = map.get('Remain')
        self.step_progress_info = map.get('StepProgressInfo')
        self.current_step_name = map.get('CurrentStepName')
        return self


class DescribeTasksResponseItems(TeaModel):
    def __init__(self, task_progress_info=None):
        self.task_progress_info = task_progress_info  # type: List[DescribeTasksResponseItemsTaskProgressInfo]

    def validate(self):
        self.validate_required(self.task_progress_info, 'task_progress_info')
        if self.task_progress_info:
            for k in self.task_progress_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TaskProgressInfo'] = []
        if self.task_progress_info is not None:
            for k in self.task_progress_info:
                result['TaskProgressInfo'].append(k.to_map() if k else None)
        else:
            result['TaskProgressInfo'] = None
        return result

    def from_map(self, map={}):
        self.task_progress_info = []
        if map.get('TaskProgressInfo') is not None:
            for k in map.get('TaskProgressInfo'):
                temp_model = DescribeTasksResponseItemsTaskProgressInfo()
                self.task_progress_info.append(temp_model.from_map(k))
        else:
            self.task_progress_info = None
        return self


class DescribeSQLLogReportsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, start_time=None, end_time=None, page_size=None, page_number=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeSQLLogReportsResponse(TeaModel):
    def __init__(self, request_id=None, total_record_count=None, page_number=None, page_record_count=None,
                 items=None):
        self.request_id = request_id    # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items              # type: DescribeSQLLogReportsResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalRecordCount'] = self.total_record_count
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeSQLLogReportsResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeSQLLogReportsResponseItemsItemLatencyTopNItemsLatencyTopNItem(TeaModel):
    def __init__(self, sqltext=None, avg_latency=None, sqlexecute_times=None):
        self.sqltext = sqltext          # type: str
        self.avg_latency = avg_latency  # type: int
        self.sqlexecute_times = sqlexecute_times  # type: int

    def validate(self):
        self.validate_required(self.sqltext, 'sqltext')
        self.validate_required(self.avg_latency, 'avg_latency')
        self.validate_required(self.sqlexecute_times, 'sqlexecute_times')

    def to_map(self):
        result = {}
        result['SQLText'] = self.sqltext
        result['AvgLatency'] = self.avg_latency
        result['SQLExecuteTimes'] = self.sqlexecute_times
        return result

    def from_map(self, map={}):
        self.sqltext = map.get('SQLText')
        self.avg_latency = map.get('AvgLatency')
        self.sqlexecute_times = map.get('SQLExecuteTimes')
        return self


class DescribeSQLLogReportsResponseItemsItemLatencyTopNItems(TeaModel):
    def __init__(self, latency_top_nitem=None):
        self.latency_top_nitem = latency_top_nitem  # type: List[DescribeSQLLogReportsResponseItemsItemLatencyTopNItemsLatencyTopNItem]

    def validate(self):
        self.validate_required(self.latency_top_nitem, 'latency_top_nitem')
        if self.latency_top_nitem:
            for k in self.latency_top_nitem:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LatencyTopNItem'] = []
        if self.latency_top_nitem is not None:
            for k in self.latency_top_nitem:
                result['LatencyTopNItem'].append(k.to_map() if k else None)
        else:
            result['LatencyTopNItem'] = None
        return result

    def from_map(self, map={}):
        self.latency_top_nitem = []
        if map.get('LatencyTopNItem') is not None:
            for k in map.get('LatencyTopNItem'):
                temp_model = DescribeSQLLogReportsResponseItemsItemLatencyTopNItemsLatencyTopNItem()
                self.latency_top_nitem.append(temp_model.from_map(k))
        else:
            self.latency_top_nitem = None
        return self


class DescribeSQLLogReportsResponseItemsItemQPSTopNItemsQPSTopNItem(TeaModel):
    def __init__(self, sqltext=None, sqlexecute_times=None):
        self.sqltext = sqltext          # type: str
        self.sqlexecute_times = sqlexecute_times  # type: int

    def validate(self):
        self.validate_required(self.sqltext, 'sqltext')
        self.validate_required(self.sqlexecute_times, 'sqlexecute_times')

    def to_map(self):
        result = {}
        result['SQLText'] = self.sqltext
        result['SQLExecuteTimes'] = self.sqlexecute_times
        return result

    def from_map(self, map={}):
        self.sqltext = map.get('SQLText')
        self.sqlexecute_times = map.get('SQLExecuteTimes')
        return self


class DescribeSQLLogReportsResponseItemsItemQPSTopNItems(TeaModel):
    def __init__(self, qpstop_nitem=None):
        self.qpstop_nitem = qpstop_nitem  # type: List[DescribeSQLLogReportsResponseItemsItemQPSTopNItemsQPSTopNItem]

    def validate(self):
        self.validate_required(self.qpstop_nitem, 'qpstop_nitem')
        if self.qpstop_nitem:
            for k in self.qpstop_nitem:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['QPSTopNItem'] = []
        if self.qpstop_nitem is not None:
            for k in self.qpstop_nitem:
                result['QPSTopNItem'].append(k.to_map() if k else None)
        else:
            result['QPSTopNItem'] = None
        return result

    def from_map(self, map={}):
        self.qpstop_nitem = []
        if map.get('QPSTopNItem') is not None:
            for k in map.get('QPSTopNItem'):
                temp_model = DescribeSQLLogReportsResponseItemsItemQPSTopNItemsQPSTopNItem()
                self.qpstop_nitem.append(temp_model.from_map(k))
        else:
            self.qpstop_nitem = None
        return self


class DescribeSQLLogReportsResponseItemsItem(TeaModel):
    def __init__(self, report_time=None, latency_top_nitems=None, qpstop_nitems=None):
        self.report_time = report_time  # type: str
        self.latency_top_nitems = latency_top_nitems  # type: DescribeSQLLogReportsResponseItemsItemLatencyTopNItems
        self.qpstop_nitems = qpstop_nitems  # type: DescribeSQLLogReportsResponseItemsItemQPSTopNItems

    def validate(self):
        self.validate_required(self.report_time, 'report_time')
        self.validate_required(self.latency_top_nitems, 'latency_top_nitems')
        if self.latency_top_nitems:
            self.latency_top_nitems.validate()
        self.validate_required(self.qpstop_nitems, 'qpstop_nitems')
        if self.qpstop_nitems:
            self.qpstop_nitems.validate()

    def to_map(self):
        result = {}
        result['ReportTime'] = self.report_time
        if self.latency_top_nitems is not None:
            result['LatencyTopNItems'] = self.latency_top_nitems.to_map()
        else:
            result['LatencyTopNItems'] = None
        if self.qpstop_nitems is not None:
            result['QPSTopNItems'] = self.qpstop_nitems.to_map()
        else:
            result['QPSTopNItems'] = None
        return result

    def from_map(self, map={}):
        self.report_time = map.get('ReportTime')
        if map.get('LatencyTopNItems') is not None:
            temp_model = DescribeSQLLogReportsResponseItemsItemLatencyTopNItems()
            self.latency_top_nitems = temp_model.from_map(map['LatencyTopNItems'])
        else:
            self.latency_top_nitems = None
        if map.get('QPSTopNItems') is not None:
            temp_model = DescribeSQLLogReportsResponseItemsItemQPSTopNItems()
            self.qpstop_nitems = temp_model.from_map(map['QPSTopNItems'])
        else:
            self.qpstop_nitems = None
        return self


class DescribeSQLLogReportsResponseItems(TeaModel):
    def __init__(self, item=None):
        self.item = item                # type: List[DescribeSQLLogReportsResponseItemsItem]

    def validate(self):
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        return result

    def from_map(self, map={}):
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = DescribeSQLLogReportsResponseItemsItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        return self


class DescribeSQLLogRecordsRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, sqlid=None, query_keywords=None, start_time=None,
                 database=None, user=None, form=None, end_time=None, page_size=None, page_number=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.sqlid = sqlid              # type: int
        self.query_keywords = query_keywords  # type: str
        self.start_time = start_time    # type: str
        self.database = database        # type: str
        self.user = user                # type: str
        self.form = form                # type: str
        self.end_time = end_time        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['SQLId'] = self.sqlid
        result['QueryKeywords'] = self.query_keywords
        result['StartTime'] = self.start_time
        result['Database'] = self.database
        result['User'] = self.user
        result['Form'] = self.form
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.sqlid = map.get('SQLId')
        self.query_keywords = map.get('QueryKeywords')
        self.start_time = map.get('StartTime')
        self.database = map.get('Database')
        self.user = map.get('User')
        self.form = map.get('Form')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeSQLLogRecordsResponse(TeaModel):
    def __init__(self, request_id=None, total_record_count=None, page_number=None, page_record_count=None,
                 items=None):
        self.request_id = request_id    # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items              # type: DescribeSQLLogRecordsResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalRecordCount'] = self.total_record_count
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeSQLLogRecordsResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeSQLLogRecordsResponseItemsSQLRecord(TeaModel):
    def __init__(self, dbname=None, account_name=None, host_address=None, sqltext=None, total_execution_times=None,
                 return_row_counts=None, execute_time=None, thread_id=None):
        self.dbname = dbname            # type: str
        self.account_name = account_name  # type: str
        self.host_address = host_address  # type: str
        self.sqltext = sqltext          # type: str
        self.total_execution_times = total_execution_times  # type: int
        self.return_row_counts = return_row_counts  # type: int
        self.execute_time = execute_time  # type: str
        self.thread_id = thread_id      # type: str

    def validate(self):
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.host_address, 'host_address')
        self.validate_required(self.sqltext, 'sqltext')
        self.validate_required(self.total_execution_times, 'total_execution_times')
        self.validate_required(self.return_row_counts, 'return_row_counts')
        self.validate_required(self.execute_time, 'execute_time')
        self.validate_required(self.thread_id, 'thread_id')

    def to_map(self):
        result = {}
        result['DBName'] = self.dbname
        result['AccountName'] = self.account_name
        result['HostAddress'] = self.host_address
        result['SQLText'] = self.sqltext
        result['TotalExecutionTimes'] = self.total_execution_times
        result['ReturnRowCounts'] = self.return_row_counts
        result['ExecuteTime'] = self.execute_time
        result['ThreadID'] = self.thread_id
        return result

    def from_map(self, map={}):
        self.dbname = map.get('DBName')
        self.account_name = map.get('AccountName')
        self.host_address = map.get('HostAddress')
        self.sqltext = map.get('SQLText')
        self.total_execution_times = map.get('TotalExecutionTimes')
        self.return_row_counts = map.get('ReturnRowCounts')
        self.execute_time = map.get('ExecuteTime')
        self.thread_id = map.get('ThreadID')
        return self


class DescribeSQLLogRecordsResponseItems(TeaModel):
    def __init__(self, sqlrecord=None):
        self.sqlrecord = sqlrecord      # type: List[DescribeSQLLogRecordsResponseItemsSQLRecord]

    def validate(self):
        self.validate_required(self.sqlrecord, 'sqlrecord')
        if self.sqlrecord:
            for k in self.sqlrecord:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SQLRecord'] = []
        if self.sqlrecord is not None:
            for k in self.sqlrecord:
                result['SQLRecord'].append(k.to_map() if k else None)
        else:
            result['SQLRecord'] = None
        return result

    def from_map(self, map={}):
        self.sqlrecord = []
        if map.get('SQLRecord') is not None:
            for k in map.get('SQLRecord'):
                temp_model = DescribeSQLLogRecordsResponseItemsSQLRecord()
                self.sqlrecord.append(temp_model.from_map(k))
        else:
            self.sqlrecord = None
        return self


class DescribeSlowLogsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, start_time=None, end_time=None, dbname=None, sort_key=None,
                 page_size=None, page_number=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.dbname = dbname            # type: str
        self.sort_key = sort_key        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['DBName'] = self.dbname
        result['SortKey'] = self.sort_key
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.dbname = map.get('DBName')
        self.sort_key = map.get('SortKey')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeSlowLogsResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, engine=None, start_time=None, end_time=None,
                 total_record_count=None, page_number=None, page_record_count=None, items=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.engine = engine            # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items              # type: DescribeSlowLogsResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['Engine'] = self.engine
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['TotalRecordCount'] = self.total_record_count
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.engine = map.get('Engine')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeSlowLogsResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeSlowLogsResponseItemsSQLSlowLog(TeaModel):
    def __init__(self, slow_log_id=None, sqlhash=None, sqlid_str=None, dbname=None, sqltext=None,
                 my_sqltotal_execution_counts=None, my_sqltotal_execution_times=None, total_lock_times=None, max_lock_time=None,
                 parse_total_row_counts=None, parse_max_row_count=None, return_total_row_counts=None, return_max_row_count=None,
                 create_time=None, sqlserver_total_execution_counts=None, sqlserver_total_execution_times=None,
                 total_logical_read_counts=None, total_physical_read_counts=None, report_time=None, max_execution_time=None,
                 avg_execution_time=None, avg_physical_read_counts=None, max_physical_read_counts=None,
                 min_physical_read_counts=None, avg_logical_read_counts=None, max_logical_read_counts=None, min_logical_read_counts=None,
                 total_iowrite_counts=None, avg_iowrite_counts=None, max_iowrite_counts=None, min_iowrite_counts=None,
                 total_rows_affected_counts=None, avg_rows_affected_counts=None, max_rows_affected_counts=None,
                 min_rows_affected_counts=None, total_last_rows_affected_counts=None, avg_last_rows_affected_counts=None,
                 max_last_rows_affected_counts=None, min_last_rows_affected_counts=None, sqlserver_min_execution_time=None,
                 sqlserver_avg_execution_time=None, sqlserver_total_cpu_time=None, sqlserver_avg_cpu_time=None, sqlserver_max_cpu_time=None,
                 sqlserver_min_cpu_time=None):
        self.slow_log_id = slow_log_id  # type: int
        self.sqlhash = sqlhash          # type: str
        self.sqlid_str = sqlid_str      # type: str
        self.dbname = dbname            # type: str
        self.sqltext = sqltext          # type: str
        self.my_sqltotal_execution_counts = my_sqltotal_execution_counts  # type: int
        self.my_sqltotal_execution_times = my_sqltotal_execution_times  # type: int
        self.total_lock_times = total_lock_times  # type: int
        self.max_lock_time = max_lock_time  # type: int
        self.parse_total_row_counts = parse_total_row_counts  # type: int
        self.parse_max_row_count = parse_max_row_count  # type: int
        self.return_total_row_counts = return_total_row_counts  # type: int
        self.return_max_row_count = return_max_row_count  # type: int
        self.create_time = create_time  # type: str
        self.sqlserver_total_execution_counts = sqlserver_total_execution_counts  # type: int
        self.sqlserver_total_execution_times = sqlserver_total_execution_times  # type: int
        self.total_logical_read_counts = total_logical_read_counts  # type: int
        self.total_physical_read_counts = total_physical_read_counts  # type: int
        self.report_time = report_time  # type: str
        self.max_execution_time = max_execution_time  # type: int
        self.avg_execution_time = avg_execution_time  # type: int
        self.avg_physical_read_counts = avg_physical_read_counts  # type: int
        self.max_physical_read_counts = max_physical_read_counts  # type: int
        self.min_physical_read_counts = min_physical_read_counts  # type: int
        self.avg_logical_read_counts = avg_logical_read_counts  # type: int
        self.max_logical_read_counts = max_logical_read_counts  # type: int
        self.min_logical_read_counts = min_logical_read_counts  # type: int
        self.total_iowrite_counts = total_iowrite_counts  # type: int
        self.avg_iowrite_counts = avg_iowrite_counts  # type: int
        self.max_iowrite_counts = max_iowrite_counts  # type: int
        self.min_iowrite_counts = min_iowrite_counts  # type: int
        self.total_rows_affected_counts = total_rows_affected_counts  # type: int
        self.avg_rows_affected_counts = avg_rows_affected_counts  # type: int
        self.max_rows_affected_counts = max_rows_affected_counts  # type: int
        self.min_rows_affected_counts = min_rows_affected_counts  # type: int
        self.total_last_rows_affected_counts = total_last_rows_affected_counts  # type: int
        self.avg_last_rows_affected_counts = avg_last_rows_affected_counts  # type: int
        self.max_last_rows_affected_counts = max_last_rows_affected_counts  # type: int
        self.min_last_rows_affected_counts = min_last_rows_affected_counts  # type: int
        self.sqlserver_min_execution_time = sqlserver_min_execution_time  # type: int
        self.sqlserver_avg_execution_time = sqlserver_avg_execution_time  # type: int
        self.sqlserver_total_cpu_time = sqlserver_total_cpu_time  # type: int
        self.sqlserver_avg_cpu_time = sqlserver_avg_cpu_time  # type: int
        self.sqlserver_max_cpu_time = sqlserver_max_cpu_time  # type: int
        self.sqlserver_min_cpu_time = sqlserver_min_cpu_time  # type: int

    def validate(self):
        self.validate_required(self.slow_log_id, 'slow_log_id')
        self.validate_required(self.sqlhash, 'sqlhash')
        self.validate_required(self.sqlid_str, 'sqlid_str')
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.sqltext, 'sqltext')
        self.validate_required(self.my_sqltotal_execution_counts, 'my_sqltotal_execution_counts')
        self.validate_required(self.my_sqltotal_execution_times, 'my_sqltotal_execution_times')
        self.validate_required(self.total_lock_times, 'total_lock_times')
        self.validate_required(self.max_lock_time, 'max_lock_time')
        self.validate_required(self.parse_total_row_counts, 'parse_total_row_counts')
        self.validate_required(self.parse_max_row_count, 'parse_max_row_count')
        self.validate_required(self.return_total_row_counts, 'return_total_row_counts')
        self.validate_required(self.return_max_row_count, 'return_max_row_count')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.sqlserver_total_execution_counts, 'sqlserver_total_execution_counts')
        self.validate_required(self.sqlserver_total_execution_times, 'sqlserver_total_execution_times')
        self.validate_required(self.total_logical_read_counts, 'total_logical_read_counts')
        self.validate_required(self.total_physical_read_counts, 'total_physical_read_counts')
        self.validate_required(self.report_time, 'report_time')
        self.validate_required(self.max_execution_time, 'max_execution_time')
        self.validate_required(self.avg_execution_time, 'avg_execution_time')
        self.validate_required(self.avg_physical_read_counts, 'avg_physical_read_counts')
        self.validate_required(self.max_physical_read_counts, 'max_physical_read_counts')
        self.validate_required(self.min_physical_read_counts, 'min_physical_read_counts')
        self.validate_required(self.avg_logical_read_counts, 'avg_logical_read_counts')
        self.validate_required(self.max_logical_read_counts, 'max_logical_read_counts')
        self.validate_required(self.min_logical_read_counts, 'min_logical_read_counts')
        self.validate_required(self.total_iowrite_counts, 'total_iowrite_counts')
        self.validate_required(self.avg_iowrite_counts, 'avg_iowrite_counts')
        self.validate_required(self.max_iowrite_counts, 'max_iowrite_counts')
        self.validate_required(self.min_iowrite_counts, 'min_iowrite_counts')
        self.validate_required(self.total_rows_affected_counts, 'total_rows_affected_counts')
        self.validate_required(self.avg_rows_affected_counts, 'avg_rows_affected_counts')
        self.validate_required(self.max_rows_affected_counts, 'max_rows_affected_counts')
        self.validate_required(self.min_rows_affected_counts, 'min_rows_affected_counts')
        self.validate_required(self.total_last_rows_affected_counts, 'total_last_rows_affected_counts')
        self.validate_required(self.avg_last_rows_affected_counts, 'avg_last_rows_affected_counts')
        self.validate_required(self.max_last_rows_affected_counts, 'max_last_rows_affected_counts')
        self.validate_required(self.min_last_rows_affected_counts, 'min_last_rows_affected_counts')
        self.validate_required(self.sqlserver_min_execution_time, 'sqlserver_min_execution_time')
        self.validate_required(self.sqlserver_avg_execution_time, 'sqlserver_avg_execution_time')
        self.validate_required(self.sqlserver_total_cpu_time, 'sqlserver_total_cpu_time')
        self.validate_required(self.sqlserver_avg_cpu_time, 'sqlserver_avg_cpu_time')
        self.validate_required(self.sqlserver_max_cpu_time, 'sqlserver_max_cpu_time')
        self.validate_required(self.sqlserver_min_cpu_time, 'sqlserver_min_cpu_time')

    def to_map(self):
        result = {}
        result['SlowLogId'] = self.slow_log_id
        result['SQLHASH'] = self.sqlhash
        result['SQLIdStr'] = self.sqlid_str
        result['DBName'] = self.dbname
        result['SQLText'] = self.sqltext
        result['MySQLTotalExecutionCounts'] = self.my_sqltotal_execution_counts
        result['MySQLTotalExecutionTimes'] = self.my_sqltotal_execution_times
        result['TotalLockTimes'] = self.total_lock_times
        result['MaxLockTime'] = self.max_lock_time
        result['ParseTotalRowCounts'] = self.parse_total_row_counts
        result['ParseMaxRowCount'] = self.parse_max_row_count
        result['ReturnTotalRowCounts'] = self.return_total_row_counts
        result['ReturnMaxRowCount'] = self.return_max_row_count
        result['CreateTime'] = self.create_time
        result['SQLServerTotalExecutionCounts'] = self.sqlserver_total_execution_counts
        result['SQLServerTotalExecutionTimes'] = self.sqlserver_total_execution_times
        result['TotalLogicalReadCounts'] = self.total_logical_read_counts
        result['TotalPhysicalReadCounts'] = self.total_physical_read_counts
        result['ReportTime'] = self.report_time
        result['MaxExecutionTime'] = self.max_execution_time
        result['AvgExecutionTime'] = self.avg_execution_time
        result['AvgPhysicalReadCounts'] = self.avg_physical_read_counts
        result['MaxPhysicalReadCounts'] = self.max_physical_read_counts
        result['MinPhysicalReadCounts'] = self.min_physical_read_counts
        result['AvgLogicalReadCounts'] = self.avg_logical_read_counts
        result['MaxLogicalReadCounts'] = self.max_logical_read_counts
        result['MinLogicalReadCounts'] = self.min_logical_read_counts
        result['TotalIOWriteCounts'] = self.total_iowrite_counts
        result['AvgIOWriteCounts'] = self.avg_iowrite_counts
        result['MaxIOWriteCounts'] = self.max_iowrite_counts
        result['MinIOWriteCounts'] = self.min_iowrite_counts
        result['TotalRowsAffectedCounts'] = self.total_rows_affected_counts
        result['AvgRowsAffectedCounts'] = self.avg_rows_affected_counts
        result['MaxRowsAffectedCounts'] = self.max_rows_affected_counts
        result['MinRowsAffectedCounts'] = self.min_rows_affected_counts
        result['TotalLastRowsAffectedCounts'] = self.total_last_rows_affected_counts
        result['AvgLastRowsAffectedCounts'] = self.avg_last_rows_affected_counts
        result['MaxLastRowsAffectedCounts'] = self.max_last_rows_affected_counts
        result['MinLastRowsAffectedCounts'] = self.min_last_rows_affected_counts
        result['SQLServerMinExecutionTime'] = self.sqlserver_min_execution_time
        result['SQLServerAvgExecutionTime'] = self.sqlserver_avg_execution_time
        result['SQLServerTotalCpuTime'] = self.sqlserver_total_cpu_time
        result['SQLServerAvgCpuTime'] = self.sqlserver_avg_cpu_time
        result['SQLServerMaxCpuTime'] = self.sqlserver_max_cpu_time
        result['SQLServerMinCpuTime'] = self.sqlserver_min_cpu_time
        return result

    def from_map(self, map={}):
        self.slow_log_id = map.get('SlowLogId')
        self.sqlhash = map.get('SQLHASH')
        self.sqlid_str = map.get('SQLIdStr')
        self.dbname = map.get('DBName')
        self.sqltext = map.get('SQLText')
        self.my_sqltotal_execution_counts = map.get('MySQLTotalExecutionCounts')
        self.my_sqltotal_execution_times = map.get('MySQLTotalExecutionTimes')
        self.total_lock_times = map.get('TotalLockTimes')
        self.max_lock_time = map.get('MaxLockTime')
        self.parse_total_row_counts = map.get('ParseTotalRowCounts')
        self.parse_max_row_count = map.get('ParseMaxRowCount')
        self.return_total_row_counts = map.get('ReturnTotalRowCounts')
        self.return_max_row_count = map.get('ReturnMaxRowCount')
        self.create_time = map.get('CreateTime')
        self.sqlserver_total_execution_counts = map.get('SQLServerTotalExecutionCounts')
        self.sqlserver_total_execution_times = map.get('SQLServerTotalExecutionTimes')
        self.total_logical_read_counts = map.get('TotalLogicalReadCounts')
        self.total_physical_read_counts = map.get('TotalPhysicalReadCounts')
        self.report_time = map.get('ReportTime')
        self.max_execution_time = map.get('MaxExecutionTime')
        self.avg_execution_time = map.get('AvgExecutionTime')
        self.avg_physical_read_counts = map.get('AvgPhysicalReadCounts')
        self.max_physical_read_counts = map.get('MaxPhysicalReadCounts')
        self.min_physical_read_counts = map.get('MinPhysicalReadCounts')
        self.avg_logical_read_counts = map.get('AvgLogicalReadCounts')
        self.max_logical_read_counts = map.get('MaxLogicalReadCounts')
        self.min_logical_read_counts = map.get('MinLogicalReadCounts')
        self.total_iowrite_counts = map.get('TotalIOWriteCounts')
        self.avg_iowrite_counts = map.get('AvgIOWriteCounts')
        self.max_iowrite_counts = map.get('MaxIOWriteCounts')
        self.min_iowrite_counts = map.get('MinIOWriteCounts')
        self.total_rows_affected_counts = map.get('TotalRowsAffectedCounts')
        self.avg_rows_affected_counts = map.get('AvgRowsAffectedCounts')
        self.max_rows_affected_counts = map.get('MaxRowsAffectedCounts')
        self.min_rows_affected_counts = map.get('MinRowsAffectedCounts')
        self.total_last_rows_affected_counts = map.get('TotalLastRowsAffectedCounts')
        self.avg_last_rows_affected_counts = map.get('AvgLastRowsAffectedCounts')
        self.max_last_rows_affected_counts = map.get('MaxLastRowsAffectedCounts')
        self.min_last_rows_affected_counts = map.get('MinLastRowsAffectedCounts')
        self.sqlserver_min_execution_time = map.get('SQLServerMinExecutionTime')
        self.sqlserver_avg_execution_time = map.get('SQLServerAvgExecutionTime')
        self.sqlserver_total_cpu_time = map.get('SQLServerTotalCpuTime')
        self.sqlserver_avg_cpu_time = map.get('SQLServerAvgCpuTime')
        self.sqlserver_max_cpu_time = map.get('SQLServerMaxCpuTime')
        self.sqlserver_min_cpu_time = map.get('SQLServerMinCpuTime')
        return self


class DescribeSlowLogsResponseItems(TeaModel):
    def __init__(self, sqlslow_log=None):
        self.sqlslow_log = sqlslow_log  # type: List[DescribeSlowLogsResponseItemsSQLSlowLog]

    def validate(self):
        self.validate_required(self.sqlslow_log, 'sqlslow_log')
        if self.sqlslow_log:
            for k in self.sqlslow_log:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SQLSlowLog'] = []
        if self.sqlslow_log is not None:
            for k in self.sqlslow_log:
                result['SQLSlowLog'].append(k.to_map() if k else None)
        else:
            result['SQLSlowLog'] = None
        return result

    def from_map(self, map={}):
        self.sqlslow_log = []
        if map.get('SQLSlowLog') is not None:
            for k in map.get('SQLSlowLog'):
                temp_model = DescribeSlowLogsResponseItemsSQLSlowLog()
                self.sqlslow_log.append(temp_model.from_map(k))
        else:
            self.sqlslow_log = None
        return self


class DescribeSlowLogRecordsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, sqlhash=None, start_time=None, end_time=None, dbname=None, page_size=None,
                 page_number=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.sqlhash = sqlhash          # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.dbname = dbname            # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['SQLHASH'] = self.sqlhash
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['DBName'] = self.dbname
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.sqlhash = map.get('SQLHASH')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.dbname = map.get('DBName')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeSlowLogRecordsResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, engine=None, total_record_count=None, page_number=None,
                 page_record_count=None, sqlhash=None, cputime=None, logical_ioread=None, physical_ioread=None, writes_iocount=None,
                 rows_affected_count=None, last_rows_affected_count=None, user_name=None, items=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.engine = engine            # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.sqlhash = sqlhash          # type: str
        self.cputime = cputime          # type: int
        self.logical_ioread = logical_ioread  # type: int
        self.physical_ioread = physical_ioread  # type: int
        self.writes_iocount = writes_iocount  # type: int
        self.rows_affected_count = rows_affected_count  # type: int
        self.last_rows_affected_count = last_rows_affected_count  # type: int
        self.user_name = user_name      # type: str
        self.items = items              # type: DescribeSlowLogRecordsResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.sqlhash, 'sqlhash')
        self.validate_required(self.cputime, 'cputime')
        self.validate_required(self.logical_ioread, 'logical_ioread')
        self.validate_required(self.physical_ioread, 'physical_ioread')
        self.validate_required(self.writes_iocount, 'writes_iocount')
        self.validate_required(self.rows_affected_count, 'rows_affected_count')
        self.validate_required(self.last_rows_affected_count, 'last_rows_affected_count')
        self.validate_required(self.user_name, 'user_name')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['Engine'] = self.engine
        result['TotalRecordCount'] = self.total_record_count
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        result['SQLHash'] = self.sqlhash
        result['CPUTime'] = self.cputime
        result['LogicalIORead'] = self.logical_ioread
        result['PhysicalIORead'] = self.physical_ioread
        result['WritesIOCount'] = self.writes_iocount
        result['RowsAffectedCount'] = self.rows_affected_count
        result['LastRowsAffectedCount'] = self.last_rows_affected_count
        result['UserName'] = self.user_name
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.engine = map.get('Engine')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        self.sqlhash = map.get('SQLHash')
        self.cputime = map.get('CPUTime')
        self.logical_ioread = map.get('LogicalIORead')
        self.physical_ioread = map.get('PhysicalIORead')
        self.writes_iocount = map.get('WritesIOCount')
        self.rows_affected_count = map.get('RowsAffectedCount')
        self.last_rows_affected_count = map.get('LastRowsAffectedCount')
        self.user_name = map.get('UserName')
        if map.get('Items') is not None:
            temp_model = DescribeSlowLogRecordsResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeSlowLogRecordsResponseItemsSQLSlowRecord(TeaModel):
    def __init__(self, host_address=None, dbname=None, sqltext=None, query_times=None, lock_times=None,
                 parse_row_counts=None, return_row_counts=None, execution_start_time=None, query_time_ms=None, cpu_time=None,
                 logical_ioread=None, physical_ioread=None, write_iocount=None, rows_affected_count=None,
                 last_rows_affected_count=None, user_name=None, application_name=None, client_host_name=None):
        self.host_address = host_address  # type: str
        self.dbname = dbname            # type: str
        self.sqltext = sqltext          # type: str
        self.query_times = query_times  # type: int
        self.lock_times = lock_times    # type: int
        self.parse_row_counts = parse_row_counts  # type: int
        self.return_row_counts = return_row_counts  # type: int
        self.execution_start_time = execution_start_time  # type: str
        self.query_time_ms = query_time_ms  # type: int
        self.cpu_time = cpu_time        # type: int
        self.logical_ioread = logical_ioread  # type: int
        self.physical_ioread = physical_ioread  # type: int
        self.write_iocount = write_iocount  # type: int
        self.rows_affected_count = rows_affected_count  # type: int
        self.last_rows_affected_count = last_rows_affected_count  # type: int
        self.user_name = user_name      # type: str
        self.application_name = application_name  # type: str
        self.client_host_name = client_host_name  # type: str

    def validate(self):
        self.validate_required(self.host_address, 'host_address')
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.sqltext, 'sqltext')
        self.validate_required(self.query_times, 'query_times')
        self.validate_required(self.lock_times, 'lock_times')
        self.validate_required(self.parse_row_counts, 'parse_row_counts')
        self.validate_required(self.return_row_counts, 'return_row_counts')
        self.validate_required(self.execution_start_time, 'execution_start_time')
        self.validate_required(self.query_time_ms, 'query_time_ms')
        self.validate_required(self.cpu_time, 'cpu_time')
        self.validate_required(self.logical_ioread, 'logical_ioread')
        self.validate_required(self.physical_ioread, 'physical_ioread')
        self.validate_required(self.write_iocount, 'write_iocount')
        self.validate_required(self.rows_affected_count, 'rows_affected_count')
        self.validate_required(self.last_rows_affected_count, 'last_rows_affected_count')
        self.validate_required(self.user_name, 'user_name')
        self.validate_required(self.application_name, 'application_name')
        self.validate_required(self.client_host_name, 'client_host_name')

    def to_map(self):
        result = {}
        result['HostAddress'] = self.host_address
        result['DBName'] = self.dbname
        result['SQLText'] = self.sqltext
        result['QueryTimes'] = self.query_times
        result['LockTimes'] = self.lock_times
        result['ParseRowCounts'] = self.parse_row_counts
        result['ReturnRowCounts'] = self.return_row_counts
        result['ExecutionStartTime'] = self.execution_start_time
        result['QueryTimeMS'] = self.query_time_ms
        result['CpuTime'] = self.cpu_time
        result['LogicalIORead'] = self.logical_ioread
        result['PhysicalIORead'] = self.physical_ioread
        result['WriteIOCount'] = self.write_iocount
        result['RowsAffectedCount'] = self.rows_affected_count
        result['LastRowsAffectedCount'] = self.last_rows_affected_count
        result['UserName'] = self.user_name
        result['ApplicationName'] = self.application_name
        result['ClientHostName'] = self.client_host_name
        return result

    def from_map(self, map={}):
        self.host_address = map.get('HostAddress')
        self.dbname = map.get('DBName')
        self.sqltext = map.get('SQLText')
        self.query_times = map.get('QueryTimes')
        self.lock_times = map.get('LockTimes')
        self.parse_row_counts = map.get('ParseRowCounts')
        self.return_row_counts = map.get('ReturnRowCounts')
        self.execution_start_time = map.get('ExecutionStartTime')
        self.query_time_ms = map.get('QueryTimeMS')
        self.cpu_time = map.get('CpuTime')
        self.logical_ioread = map.get('LogicalIORead')
        self.physical_ioread = map.get('PhysicalIORead')
        self.write_iocount = map.get('WriteIOCount')
        self.rows_affected_count = map.get('RowsAffectedCount')
        self.last_rows_affected_count = map.get('LastRowsAffectedCount')
        self.user_name = map.get('UserName')
        self.application_name = map.get('ApplicationName')
        self.client_host_name = map.get('ClientHostName')
        return self


class DescribeSlowLogRecordsResponseItems(TeaModel):
    def __init__(self, sqlslow_record=None):
        self.sqlslow_record = sqlslow_record  # type: List[DescribeSlowLogRecordsResponseItemsSQLSlowRecord]

    def validate(self):
        self.validate_required(self.sqlslow_record, 'sqlslow_record')
        if self.sqlslow_record:
            for k in self.sqlslow_record:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SQLSlowRecord'] = []
        if self.sqlslow_record is not None:
            for k in self.sqlslow_record:
                result['SQLSlowRecord'].append(k.to_map() if k else None)
        else:
            result['SQLSlowRecord'] = None
        return result

    def from_map(self, map={}):
        self.sqlslow_record = []
        if map.get('SQLSlowRecord') is not None:
            for k in map.get('SQLSlowRecord'):
                temp_model = DescribeSlowLogRecordsResponseItemsSQLSlowRecord()
                self.sqlslow_record.append(temp_model.from_map(k))
        else:
            self.sqlslow_record = None
        return self


class DescribeResourceUsageRequest(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeResourceUsageResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, engine=None, disk_used=None, data_size=None,
                 log_size=None, backup_size=None, backup_oss_data_size=None, backup_oss_log_size=None, sqlsize=None,
                 cold_backup_size=None, backup_data_size=None, backup_log_size=None, paid_backup_size=None,
                 archive_backup_size=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.engine = engine            # type: str
        self.disk_used = disk_used      # type: int
        self.data_size = data_size      # type: int
        self.log_size = log_size        # type: int
        self.backup_size = backup_size  # type: int
        self.backup_oss_data_size = backup_oss_data_size  # type: int
        self.backup_oss_log_size = backup_oss_log_size  # type: int
        self.sqlsize = sqlsize          # type: int
        self.cold_backup_size = cold_backup_size  # type: int
        self.backup_data_size = backup_data_size  # type: int
        self.backup_log_size = backup_log_size  # type: int
        self.paid_backup_size = paid_backup_size  # type: int
        self.archive_backup_size = archive_backup_size  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.disk_used, 'disk_used')
        self.validate_required(self.data_size, 'data_size')
        self.validate_required(self.log_size, 'log_size')
        self.validate_required(self.backup_size, 'backup_size')
        self.validate_required(self.backup_oss_data_size, 'backup_oss_data_size')
        self.validate_required(self.backup_oss_log_size, 'backup_oss_log_size')
        self.validate_required(self.sqlsize, 'sqlsize')
        self.validate_required(self.cold_backup_size, 'cold_backup_size')
        self.validate_required(self.backup_data_size, 'backup_data_size')
        self.validate_required(self.backup_log_size, 'backup_log_size')
        self.validate_required(self.paid_backup_size, 'paid_backup_size')
        self.validate_required(self.archive_backup_size, 'archive_backup_size')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['Engine'] = self.engine
        result['DiskUsed'] = self.disk_used
        result['DataSize'] = self.data_size
        result['LogSize'] = self.log_size
        result['BackupSize'] = self.backup_size
        result['BackupOssDataSize'] = self.backup_oss_data_size
        result['BackupOssLogSize'] = self.backup_oss_log_size
        result['SQLSize'] = self.sqlsize
        result['ColdBackupSize'] = self.cold_backup_size
        result['BackupDataSize'] = self.backup_data_size
        result['BackupLogSize'] = self.backup_log_size
        result['PaidBackupSize'] = self.paid_backup_size
        result['ArchiveBackupSize'] = self.archive_backup_size
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.engine = map.get('Engine')
        self.disk_used = map.get('DiskUsed')
        self.data_size = map.get('DataSize')
        self.log_size = map.get('LogSize')
        self.backup_size = map.get('BackupSize')
        self.backup_oss_data_size = map.get('BackupOssDataSize')
        self.backup_oss_log_size = map.get('BackupOssLogSize')
        self.sqlsize = map.get('SQLSize')
        self.cold_backup_size = map.get('ColdBackupSize')
        self.backup_data_size = map.get('BackupDataSize')
        self.backup_log_size = map.get('BackupLogSize')
        self.paid_backup_size = map.get('PaidBackupSize')
        self.archive_backup_size = map.get('ArchiveBackupSize')
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, request_id=None, regions=None):
        self.request_id = request_id    # type: str
        self.regions = regions          # type: DescribeRegionsResponseRegions

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.regions, 'regions')
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        else:
            result['Regions'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Regions') is not None:
            temp_model = DescribeRegionsResponseRegions()
            self.regions = temp_model.from_map(map['Regions'])
        else:
            self.regions = None
        return self


class DescribeRegionsResponseRegionsRDSRegion(TeaModel):
    def __init__(self, region_id=None, zone_id=None):
        self.region_id = region_id      # type: str
        self.zone_id = zone_id          # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.zone_id, 'zone_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ZoneId'] = self.zone_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.zone_id = map.get('ZoneId')
        return self


class DescribeRegionsResponseRegions(TeaModel):
    def __init__(self, rdsregion=None):
        self.rdsregion = rdsregion      # type: List[DescribeRegionsResponseRegionsRDSRegion]

    def validate(self):
        self.validate_required(self.rdsregion, 'rdsregion')
        if self.rdsregion:
            for k in self.rdsregion:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RDSRegion'] = []
        if self.rdsregion is not None:
            for k in self.rdsregion:
                result['RDSRegion'].append(k.to_map() if k else None)
        else:
            result['RDSRegion'] = None
        return result

    def from_map(self, map={}):
        self.rdsregion = []
        if map.get('RDSRegion') is not None:
            for k in map.get('RDSRegion'):
                temp_model = DescribeRegionsResponseRegionsRDSRegion()
                self.rdsregion.append(temp_model.from_map(k))
        else:
            self.rdsregion = None
        return self


class DescribeParameterTemplatesRequest(TeaModel):
    def __init__(self, client_token=None, engine=None, engine_version=None, category=None, region_id=None,
                 dbinstance_id=None):
        self.client_token = client_token  # type: str
        self.engine = engine            # type: str
        self.engine_version = engine_version  # type: str
        self.category = category        # type: str
        self.region_id = region_id      # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        result['Category'] = self.category
        result['RegionId'] = self.region_id
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        self.category = map.get('Category')
        self.region_id = map.get('RegionId')
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeParameterTemplatesResponse(TeaModel):
    def __init__(self, request_id=None, engine=None, engine_version=None, parameter_count=None, parameters=None):
        self.request_id = request_id    # type: str
        self.engine = engine            # type: str
        self.engine_version = engine_version  # type: str
        self.parameter_count = parameter_count  # type: str
        self.parameters = parameters    # type: DescribeParameterTemplatesResponseParameters

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.parameter_count, 'parameter_count')
        self.validate_required(self.parameters, 'parameters')
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        result['ParameterCount'] = self.parameter_count
        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()
        else:
            result['Parameters'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        self.parameter_count = map.get('ParameterCount')
        if map.get('Parameters') is not None:
            temp_model = DescribeParameterTemplatesResponseParameters()
            self.parameters = temp_model.from_map(map['Parameters'])
        else:
            self.parameters = None
        return self


class DescribeParameterTemplatesResponseParametersTemplateRecord(TeaModel):
    def __init__(self, parameter_name=None, parameter_value=None, force_modify=None, force_restart=None,
                 checking_code=None, parameter_description=None):
        self.parameter_name = parameter_name  # type: str
        self.parameter_value = parameter_value  # type: str
        self.force_modify = force_modify  # type: str
        self.force_restart = force_restart  # type: str
        self.checking_code = checking_code  # type: str
        self.parameter_description = parameter_description  # type: str

    def validate(self):
        self.validate_required(self.parameter_name, 'parameter_name')
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.force_modify, 'force_modify')
        self.validate_required(self.force_restart, 'force_restart')
        self.validate_required(self.checking_code, 'checking_code')
        self.validate_required(self.parameter_description, 'parameter_description')

    def to_map(self):
        result = {}
        result['ParameterName'] = self.parameter_name
        result['ParameterValue'] = self.parameter_value
        result['ForceModify'] = self.force_modify
        result['ForceRestart'] = self.force_restart
        result['CheckingCode'] = self.checking_code
        result['ParameterDescription'] = self.parameter_description
        return result

    def from_map(self, map={}):
        self.parameter_name = map.get('ParameterName')
        self.parameter_value = map.get('ParameterValue')
        self.force_modify = map.get('ForceModify')
        self.force_restart = map.get('ForceRestart')
        self.checking_code = map.get('CheckingCode')
        self.parameter_description = map.get('ParameterDescription')
        return self


class DescribeParameterTemplatesResponseParameters(TeaModel):
    def __init__(self, template_record=None):
        self.template_record = template_record  # type: List[DescribeParameterTemplatesResponseParametersTemplateRecord]

    def validate(self):
        self.validate_required(self.template_record, 'template_record')
        if self.template_record:
            for k in self.template_record:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TemplateRecord'] = []
        if self.template_record is not None:
            for k in self.template_record:
                result['TemplateRecord'].append(k.to_map() if k else None)
        else:
            result['TemplateRecord'] = None
        return result

    def from_map(self, map={}):
        self.template_record = []
        if map.get('TemplateRecord') is not None:
            for k in map.get('TemplateRecord'):
                temp_model = DescribeParameterTemplatesResponseParametersTemplateRecord()
                self.template_record.append(temp_model.from_map(k))
        else:
            self.template_record = None
        return self


class DescribeParametersRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeParametersResponse(TeaModel):
    def __init__(self, request_id=None, engine=None, engine_version=None, config_parameters=None,
                 running_parameters=None):
        self.request_id = request_id    # type: str
        self.engine = engine            # type: str
        self.engine_version = engine_version  # type: str
        self.config_parameters = config_parameters  # type: DescribeParametersResponseConfigParameters
        self.running_parameters = running_parameters  # type: DescribeParametersResponseRunningParameters

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.config_parameters, 'config_parameters')
        if self.config_parameters:
            self.config_parameters.validate()
        self.validate_required(self.running_parameters, 'running_parameters')
        if self.running_parameters:
            self.running_parameters.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        if self.config_parameters is not None:
            result['ConfigParameters'] = self.config_parameters.to_map()
        else:
            result['ConfigParameters'] = None
        if self.running_parameters is not None:
            result['RunningParameters'] = self.running_parameters.to_map()
        else:
            result['RunningParameters'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        if map.get('ConfigParameters') is not None:
            temp_model = DescribeParametersResponseConfigParameters()
            self.config_parameters = temp_model.from_map(map['ConfigParameters'])
        else:
            self.config_parameters = None
        if map.get('RunningParameters') is not None:
            temp_model = DescribeParametersResponseRunningParameters()
            self.running_parameters = temp_model.from_map(map['RunningParameters'])
        else:
            self.running_parameters = None
        return self


class DescribeParametersResponseConfigParametersDBInstanceParameter(TeaModel):
    def __init__(self, parameter_name=None, parameter_value=None, parameter_description=None):
        self.parameter_name = parameter_name  # type: str
        self.parameter_value = parameter_value  # type: str
        self.parameter_description = parameter_description  # type: str

    def validate(self):
        self.validate_required(self.parameter_name, 'parameter_name')
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_description, 'parameter_description')

    def to_map(self):
        result = {}
        result['ParameterName'] = self.parameter_name
        result['ParameterValue'] = self.parameter_value
        result['ParameterDescription'] = self.parameter_description
        return result

    def from_map(self, map={}):
        self.parameter_name = map.get('ParameterName')
        self.parameter_value = map.get('ParameterValue')
        self.parameter_description = map.get('ParameterDescription')
        return self


class DescribeParametersResponseConfigParameters(TeaModel):
    def __init__(self, dbinstance_parameter=None):
        self.dbinstance_parameter = dbinstance_parameter  # type: List[DescribeParametersResponseConfigParametersDBInstanceParameter]

    def validate(self):
        self.validate_required(self.dbinstance_parameter, 'dbinstance_parameter')
        if self.dbinstance_parameter:
            for k in self.dbinstance_parameter:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DBInstanceParameter'] = []
        if self.dbinstance_parameter is not None:
            for k in self.dbinstance_parameter:
                result['DBInstanceParameter'].append(k.to_map() if k else None)
        else:
            result['DBInstanceParameter'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_parameter = []
        if map.get('DBInstanceParameter') is not None:
            for k in map.get('DBInstanceParameter'):
                temp_model = DescribeParametersResponseConfigParametersDBInstanceParameter()
                self.dbinstance_parameter.append(temp_model.from_map(k))
        else:
            self.dbinstance_parameter = None
        return self


class DescribeParametersResponseRunningParametersDBInstanceParameter(TeaModel):
    def __init__(self, parameter_name=None, parameter_value=None, parameter_description=None):
        self.parameter_name = parameter_name  # type: str
        self.parameter_value = parameter_value  # type: str
        self.parameter_description = parameter_description  # type: str

    def validate(self):
        self.validate_required(self.parameter_name, 'parameter_name')
        self.validate_required(self.parameter_value, 'parameter_value')
        self.validate_required(self.parameter_description, 'parameter_description')

    def to_map(self):
        result = {}
        result['ParameterName'] = self.parameter_name
        result['ParameterValue'] = self.parameter_value
        result['ParameterDescription'] = self.parameter_description
        return result

    def from_map(self, map={}):
        self.parameter_name = map.get('ParameterName')
        self.parameter_value = map.get('ParameterValue')
        self.parameter_description = map.get('ParameterDescription')
        return self


class DescribeParametersResponseRunningParameters(TeaModel):
    def __init__(self, dbinstance_parameter=None):
        self.dbinstance_parameter = dbinstance_parameter  # type: List[DescribeParametersResponseRunningParametersDBInstanceParameter]

    def validate(self):
        self.validate_required(self.dbinstance_parameter, 'dbinstance_parameter')
        if self.dbinstance_parameter:
            for k in self.dbinstance_parameter:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DBInstanceParameter'] = []
        if self.dbinstance_parameter is not None:
            for k in self.dbinstance_parameter:
                result['DBInstanceParameter'].append(k.to_map() if k else None)
        else:
            result['DBInstanceParameter'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_parameter = []
        if map.get('DBInstanceParameter') is not None:
            for k in map.get('DBInstanceParameter'):
                temp_model = DescribeParametersResponseRunningParametersDBInstanceParameter()
                self.dbinstance_parameter.append(temp_model.from_map(k))
        else:
            self.dbinstance_parameter = None
        return self


class DescribeModifyParameterLogRequest(TeaModel):
    def __init__(self, dbinstance_id=None, start_time=None, end_time=None, page_size=None, page_number=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeModifyParameterLogResponse(TeaModel):
    def __init__(self, request_id=None, engine=None, dbinstance_id=None, engine_version=None,
                 total_record_count=None, page_number=None, page_record_count=None, items=None):
        self.request_id = request_id    # type: str
        self.engine = engine            # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.engine_version = engine_version  # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items              # type: DescribeModifyParameterLogResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Engine'] = self.engine
        result['DBInstanceId'] = self.dbinstance_id
        result['EngineVersion'] = self.engine_version
        result['TotalRecordCount'] = self.total_record_count
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.engine = map.get('Engine')
        self.dbinstance_id = map.get('DBInstanceId')
        self.engine_version = map.get('EngineVersion')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeModifyParameterLogResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeModifyParameterLogResponseItemsParameterChangeLog(TeaModel):
    def __init__(self, modify_time=None, old_parameter_value=None, new_parameter_value=None, parameter_name=None,
                 status=None):
        self.modify_time = modify_time  # type: str
        self.old_parameter_value = old_parameter_value  # type: str
        self.new_parameter_value = new_parameter_value  # type: str
        self.parameter_name = parameter_name  # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.old_parameter_value, 'old_parameter_value')
        self.validate_required(self.new_parameter_value, 'new_parameter_value')
        self.validate_required(self.parameter_name, 'parameter_name')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['ModifyTime'] = self.modify_time
        result['OldParameterValue'] = self.old_parameter_value
        result['NewParameterValue'] = self.new_parameter_value
        result['ParameterName'] = self.parameter_name
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.modify_time = map.get('ModifyTime')
        self.old_parameter_value = map.get('OldParameterValue')
        self.new_parameter_value = map.get('NewParameterValue')
        self.parameter_name = map.get('ParameterName')
        self.status = map.get('Status')
        return self


class DescribeModifyParameterLogResponseItems(TeaModel):
    def __init__(self, parameter_change_log=None):
        self.parameter_change_log = parameter_change_log  # type: List[DescribeModifyParameterLogResponseItemsParameterChangeLog]

    def validate(self):
        self.validate_required(self.parameter_change_log, 'parameter_change_log')
        if self.parameter_change_log:
            for k in self.parameter_change_log:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ParameterChangeLog'] = []
        if self.parameter_change_log is not None:
            for k in self.parameter_change_log:
                result['ParameterChangeLog'].append(k.to_map() if k else None)
        else:
            result['ParameterChangeLog'] = None
        return result

    def from_map(self, map={}):
        self.parameter_change_log = []
        if map.get('ParameterChangeLog') is not None:
            for k in map.get('ParameterChangeLog'):
                temp_model = DescribeModifyParameterLogResponseItemsParameterChangeLog()
                self.parameter_change_log.append(temp_model.from_map(k))
        else:
            self.parameter_change_log = None
        return self


class DescribeErrorLogsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, start_time=None, end_time=None, page_size=None, page_number=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeErrorLogsResponse(TeaModel):
    def __init__(self, page_number=None, page_record_count=None, request_id=None, total_record_count=None,
                 items=None):
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.request_id = request_id    # type: str
        self.total_record_count = total_record_count  # type: int
        self.items = items              # type: DescribeErrorLogsResponseItems

    def validate(self):
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        result['RequestId'] = self.request_id
        result['TotalRecordCount'] = self.total_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        self.request_id = map.get('RequestId')
        self.total_record_count = map.get('TotalRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeErrorLogsResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeErrorLogsResponseItemsErrorLog(TeaModel):
    def __init__(self, create_time=None, error_info=None):
        self.create_time = create_time  # type: str
        self.error_info = error_info    # type: str

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.error_info, 'error_info')

    def to_map(self):
        result = {}
        result['CreateTime'] = self.create_time
        result['ErrorInfo'] = self.error_info
        return result

    def from_map(self, map={}):
        self.create_time = map.get('CreateTime')
        self.error_info = map.get('ErrorInfo')
        return self


class DescribeErrorLogsResponseItems(TeaModel):
    def __init__(self, error_log=None):
        self.error_log = error_log      # type: List[DescribeErrorLogsResponseItemsErrorLog]

    def validate(self):
        self.validate_required(self.error_log, 'error_log')
        if self.error_log:
            for k in self.error_log:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ErrorLog'] = []
        if self.error_log is not None:
            for k in self.error_log:
                result['ErrorLog'].append(k.to_map() if k else None)
        else:
            result['ErrorLog'] = None
        return result

    def from_map(self, map={}):
        self.error_log = []
        if map.get('ErrorLog') is not None:
            for k in map.get('ErrorLog'):
                temp_model = DescribeErrorLogsResponseItemsErrorLog()
                self.error_log.append(temp_model.from_map(k))
        else:
            self.error_log = None
        return self


class DescribeDBInstancePerformanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, key=None, start_time=None, end_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.key = key                  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.key, 'key')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['Key'] = self.key
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.key = map.get('Key')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class DescribeDBInstancePerformanceResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, engine=None, start_time=None, end_time=None,
                 performance_keys=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.engine = engine            # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.performance_keys = performance_keys  # type: DescribeDBInstancePerformanceResponsePerformanceKeys

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.performance_keys, 'performance_keys')
        if self.performance_keys:
            self.performance_keys.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['Engine'] = self.engine
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        if self.performance_keys is not None:
            result['PerformanceKeys'] = self.performance_keys.to_map()
        else:
            result['PerformanceKeys'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.engine = map.get('Engine')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        if map.get('PerformanceKeys') is not None:
            temp_model = DescribeDBInstancePerformanceResponsePerformanceKeys()
            self.performance_keys = temp_model.from_map(map['PerformanceKeys'])
        else:
            self.performance_keys = None
        return self


class DescribeDBInstancePerformanceResponsePerformanceKeysPerformanceKeyValuesPerformanceValue(TeaModel):
    def __init__(self, value=None, date=None):
        self.value = value              # type: str
        self.date = date                # type: str

    def validate(self):
        self.validate_required(self.value, 'value')
        self.validate_required(self.date, 'date')

    def to_map(self):
        result = {}
        result['Value'] = self.value
        result['Date'] = self.date
        return result

    def from_map(self, map={}):
        self.value = map.get('Value')
        self.date = map.get('Date')
        return self


class DescribeDBInstancePerformanceResponsePerformanceKeysPerformanceKeyValues(TeaModel):
    def __init__(self, performance_value=None):
        self.performance_value = performance_value  # type: List[DescribeDBInstancePerformanceResponsePerformanceKeysPerformanceKeyValuesPerformanceValue]

    def validate(self):
        self.validate_required(self.performance_value, 'performance_value')
        if self.performance_value:
            for k in self.performance_value:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PerformanceValue'] = []
        if self.performance_value is not None:
            for k in self.performance_value:
                result['PerformanceValue'].append(k.to_map() if k else None)
        else:
            result['PerformanceValue'] = None
        return result

    def from_map(self, map={}):
        self.performance_value = []
        if map.get('PerformanceValue') is not None:
            for k in map.get('PerformanceValue'):
                temp_model = DescribeDBInstancePerformanceResponsePerformanceKeysPerformanceKeyValuesPerformanceValue()
                self.performance_value.append(temp_model.from_map(k))
        else:
            self.performance_value = None
        return self


class DescribeDBInstancePerformanceResponsePerformanceKeysPerformanceKey(TeaModel):
    def __init__(self, key=None, unit=None, value_format=None, values=None):
        self.key = key                  # type: str
        self.unit = unit                # type: str
        self.value_format = value_format  # type: str
        self.values = values            # type: DescribeDBInstancePerformanceResponsePerformanceKeysPerformanceKeyValues

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.unit, 'unit')
        self.validate_required(self.value_format, 'value_format')
        self.validate_required(self.values, 'values')
        if self.values:
            self.values.validate()

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Unit'] = self.unit
        result['ValueFormat'] = self.value_format
        if self.values is not None:
            result['Values'] = self.values.to_map()
        else:
            result['Values'] = None
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.unit = map.get('Unit')
        self.value_format = map.get('ValueFormat')
        if map.get('Values') is not None:
            temp_model = DescribeDBInstancePerformanceResponsePerformanceKeysPerformanceKeyValues()
            self.values = temp_model.from_map(map['Values'])
        else:
            self.values = None
        return self


class DescribeDBInstancePerformanceResponsePerformanceKeys(TeaModel):
    def __init__(self, performance_key=None):
        self.performance_key = performance_key  # type: List[DescribeDBInstancePerformanceResponsePerformanceKeysPerformanceKey]

    def validate(self):
        self.validate_required(self.performance_key, 'performance_key')
        if self.performance_key:
            for k in self.performance_key:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PerformanceKey'] = []
        if self.performance_key is not None:
            for k in self.performance_key:
                result['PerformanceKey'].append(k.to_map() if k else None)
        else:
            result['PerformanceKey'] = None
        return result

    def from_map(self, map={}):
        self.performance_key = []
        if map.get('PerformanceKey') is not None:
            for k in map.get('PerformanceKey'):
                temp_model = DescribeDBInstancePerformanceResponsePerformanceKeysPerformanceKey()
                self.performance_key.append(temp_model.from_map(k))
        else:
            self.performance_key = None
        return self


class DescribeDatabasesRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbname=None, dbstatus=None, page_size=None, page_number=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbname = dbname            # type: str
        self.dbstatus = dbstatus        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBName'] = self.dbname
        result['DBStatus'] = self.dbstatus
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbname = map.get('DBName')
        self.dbstatus = map.get('DBStatus')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeDatabasesResponse(TeaModel):
    def __init__(self, request_id=None, databases=None):
        self.request_id = request_id    # type: str
        self.databases = databases      # type: DescribeDatabasesResponseDatabases

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.databases, 'databases')
        if self.databases:
            self.databases.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.databases is not None:
            result['Databases'] = self.databases.to_map()
        else:
            result['Databases'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Databases') is not None:
            temp_model = DescribeDatabasesResponseDatabases()
            self.databases = temp_model.from_map(map['Databases'])
        else:
            self.databases = None
        return self


class DescribeDatabasesResponseDatabasesDatabaseAccountsAccountPrivilegeInfo(TeaModel):
    def __init__(self, account=None, account_privilege=None, account_privilege_detail=None):
        self.account = account          # type: str
        self.account_privilege = account_privilege  # type: str
        self.account_privilege_detail = account_privilege_detail  # type: str

    def validate(self):
        self.validate_required(self.account, 'account')
        self.validate_required(self.account_privilege, 'account_privilege')
        self.validate_required(self.account_privilege_detail, 'account_privilege_detail')

    def to_map(self):
        result = {}
        result['Account'] = self.account
        result['AccountPrivilege'] = self.account_privilege
        result['AccountPrivilegeDetail'] = self.account_privilege_detail
        return result

    def from_map(self, map={}):
        self.account = map.get('Account')
        self.account_privilege = map.get('AccountPrivilege')
        self.account_privilege_detail = map.get('AccountPrivilegeDetail')
        return self


class DescribeDatabasesResponseDatabasesDatabaseAccounts(TeaModel):
    def __init__(self, account_privilege_info=None):
        self.account_privilege_info = account_privilege_info  # type: List[DescribeDatabasesResponseDatabasesDatabaseAccountsAccountPrivilegeInfo]

    def validate(self):
        self.validate_required(self.account_privilege_info, 'account_privilege_info')
        if self.account_privilege_info:
            for k in self.account_privilege_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AccountPrivilegeInfo'] = []
        if self.account_privilege_info is not None:
            for k in self.account_privilege_info:
                result['AccountPrivilegeInfo'].append(k.to_map() if k else None)
        else:
            result['AccountPrivilegeInfo'] = None
        return result

    def from_map(self, map={}):
        self.account_privilege_info = []
        if map.get('AccountPrivilegeInfo') is not None:
            for k in map.get('AccountPrivilegeInfo'):
                temp_model = DescribeDatabasesResponseDatabasesDatabaseAccountsAccountPrivilegeInfo()
                self.account_privilege_info.append(temp_model.from_map(k))
        else:
            self.account_privilege_info = None
        return self


class DescribeDatabasesResponseDatabasesDatabase(TeaModel):
    def __init__(self, dbname=None, dbinstance_id=None, engine=None, dbstatus=None, character_set_name=None,
                 dbdescription=None, accounts=None):
        self.dbname = dbname            # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.engine = engine            # type: str
        self.dbstatus = dbstatus        # type: str
        self.character_set_name = character_set_name  # type: str
        self.dbdescription = dbdescription  # type: str
        self.accounts = accounts        # type: DescribeDatabasesResponseDatabasesDatabaseAccounts

    def validate(self):
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.dbstatus, 'dbstatus')
        self.validate_required(self.character_set_name, 'character_set_name')
        self.validate_required(self.dbdescription, 'dbdescription')
        self.validate_required(self.accounts, 'accounts')
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        result = {}
        result['DBName'] = self.dbname
        result['DBInstanceId'] = self.dbinstance_id
        result['Engine'] = self.engine
        result['DBStatus'] = self.dbstatus
        result['CharacterSetName'] = self.character_set_name
        result['DBDescription'] = self.dbdescription
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        else:
            result['Accounts'] = None
        return result

    def from_map(self, map={}):
        self.dbname = map.get('DBName')
        self.dbinstance_id = map.get('DBInstanceId')
        self.engine = map.get('Engine')
        self.dbstatus = map.get('DBStatus')
        self.character_set_name = map.get('CharacterSetName')
        self.dbdescription = map.get('DBDescription')
        if map.get('Accounts') is not None:
            temp_model = DescribeDatabasesResponseDatabasesDatabaseAccounts()
            self.accounts = temp_model.from_map(map['Accounts'])
        else:
            self.accounts = None
        return self


class DescribeDatabasesResponseDatabases(TeaModel):
    def __init__(self, database=None):
        self.database = database        # type: List[DescribeDatabasesResponseDatabasesDatabase]

    def validate(self):
        self.validate_required(self.database, 'database')
        if self.database:
            for k in self.database:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Database'] = []
        if self.database is not None:
            for k in self.database:
                result['Database'].append(k.to_map() if k else None)
        else:
            result['Database'] = None
        return result

    def from_map(self, map={}):
        self.database = []
        if map.get('Database') is not None:
            for k in map.get('Database'):
                temp_model = DescribeDatabasesResponseDatabasesDatabase()
                self.database.append(temp_model.from_map(k))
        else:
            self.database = None
        return self


class DescribeBinlogFilesRequest(TeaModel):
    def __init__(self, dbinstance_id=None, start_time=None, end_time=None, page_size=None, page_number=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeBinlogFilesResponse(TeaModel):
    def __init__(self, request_id=None, total_record_count=None, page_number=None, page_record_count=None,
                 total_file_size=None, items=None):
        self.request_id = request_id    # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.total_file_size = total_file_size  # type: int
        self.items = items              # type: DescribeBinlogFilesResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.total_file_size, 'total_file_size')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalRecordCount'] = self.total_record_count
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        result['TotalFileSize'] = self.total_file_size
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        self.total_file_size = map.get('TotalFileSize')
        if map.get('Items') is not None:
            temp_model = DescribeBinlogFilesResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeBinlogFilesResponseItemsBinLogFile(TeaModel):
    def __init__(self, file_size=None, log_begin_time=None, log_end_time=None, download_link=None,
                 intranet_download_link=None, link_expired_time=None, checksum=None, host_instance_id=None, log_file_name=None):
        self.file_size = file_size      # type: int
        self.log_begin_time = log_begin_time  # type: str
        self.log_end_time = log_end_time  # type: str
        self.download_link = download_link  # type: str
        self.intranet_download_link = intranet_download_link  # type: str
        self.link_expired_time = link_expired_time  # type: str
        self.checksum = checksum        # type: str
        self.host_instance_id = host_instance_id  # type: str
        self.log_file_name = log_file_name  # type: str

    def validate(self):
        self.validate_required(self.file_size, 'file_size')
        self.validate_required(self.log_begin_time, 'log_begin_time')
        self.validate_required(self.log_end_time, 'log_end_time')
        self.validate_required(self.download_link, 'download_link')
        self.validate_required(self.intranet_download_link, 'intranet_download_link')
        self.validate_required(self.link_expired_time, 'link_expired_time')
        self.validate_required(self.checksum, 'checksum')
        self.validate_required(self.host_instance_id, 'host_instance_id')
        self.validate_required(self.log_file_name, 'log_file_name')

    def to_map(self):
        result = {}
        result['FileSize'] = self.file_size
        result['LogBeginTime'] = self.log_begin_time
        result['LogEndTime'] = self.log_end_time
        result['DownloadLink'] = self.download_link
        result['IntranetDownloadLink'] = self.intranet_download_link
        result['LinkExpiredTime'] = self.link_expired_time
        result['Checksum'] = self.checksum
        result['HostInstanceID'] = self.host_instance_id
        result['LogFileName'] = self.log_file_name
        return result

    def from_map(self, map={}):
        self.file_size = map.get('FileSize')
        self.log_begin_time = map.get('LogBeginTime')
        self.log_end_time = map.get('LogEndTime')
        self.download_link = map.get('DownloadLink')
        self.intranet_download_link = map.get('IntranetDownloadLink')
        self.link_expired_time = map.get('LinkExpiredTime')
        self.checksum = map.get('Checksum')
        self.host_instance_id = map.get('HostInstanceID')
        self.log_file_name = map.get('LogFileName')
        return self


class DescribeBinlogFilesResponseItems(TeaModel):
    def __init__(self, bin_log_file=None):
        self.bin_log_file = bin_log_file  # type: List[DescribeBinlogFilesResponseItemsBinLogFile]

    def validate(self):
        self.validate_required(self.bin_log_file, 'bin_log_file')
        if self.bin_log_file:
            for k in self.bin_log_file:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['BinLogFile'] = []
        if self.bin_log_file is not None:
            for k in self.bin_log_file:
                result['BinLogFile'].append(k.to_map() if k else None)
        else:
            result['BinLogFile'] = None
        return result

    def from_map(self, map={}):
        self.bin_log_file = []
        if map.get('BinLogFile') is not None:
            for k in map.get('BinLogFile'):
                temp_model = DescribeBinlogFilesResponseItemsBinLogFile()
                self.bin_log_file.append(temp_model.from_map(k))
        else:
            self.bin_log_file = None
        return self


class DescribeBackupTasksRequest(TeaModel):
    def __init__(self, client_token=None, flag=None, dbinstance_id=None, backup_job_id=None, backup_mode=None,
                 backup_job_status=None):
        self.client_token = client_token  # type: str
        self.flag = flag                # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.backup_job_id = backup_job_id  # type: int
        self.backup_mode = backup_mode  # type: str
        self.backup_job_status = backup_job_status  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['Flag'] = self.flag
        result['DBInstanceId'] = self.dbinstance_id
        result['BackupJobId'] = self.backup_job_id
        result['BackupMode'] = self.backup_mode
        result['BackupJobStatus'] = self.backup_job_status
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.flag = map.get('Flag')
        self.dbinstance_id = map.get('DBInstanceId')
        self.backup_job_id = map.get('BackupJobId')
        self.backup_mode = map.get('BackupMode')
        self.backup_job_status = map.get('BackupJobStatus')
        return self


class DescribeBackupTasksResponse(TeaModel):
    def __init__(self, request_id=None, items=None):
        self.request_id = request_id    # type: str
        self.items = items              # type: DescribeBackupTasksResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Items') is not None:
            temp_model = DescribeBackupTasksResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeBackupTasksResponseItemsBackupJob(TeaModel):
    def __init__(self, backup_progress_status=None, backup_status=None, job_mode=None, process=None,
                 task_action=None, backup_job_id=None, backup_id=None):
        self.backup_progress_status = backup_progress_status  # type: str
        self.backup_status = backup_status  # type: str
        self.job_mode = job_mode        # type: str
        self.process = process          # type: str
        self.task_action = task_action  # type: str
        self.backup_job_id = backup_job_id  # type: str
        self.backup_id = backup_id      # type: str

    def validate(self):
        self.validate_required(self.backup_progress_status, 'backup_progress_status')
        self.validate_required(self.backup_status, 'backup_status')
        self.validate_required(self.job_mode, 'job_mode')
        self.validate_required(self.process, 'process')
        self.validate_required(self.task_action, 'task_action')
        self.validate_required(self.backup_job_id, 'backup_job_id')
        self.validate_required(self.backup_id, 'backup_id')

    def to_map(self):
        result = {}
        result['BackupProgressStatus'] = self.backup_progress_status
        result['BackupStatus'] = self.backup_status
        result['JobMode'] = self.job_mode
        result['Process'] = self.process
        result['TaskAction'] = self.task_action
        result['BackupJobId'] = self.backup_job_id
        result['BackupId'] = self.backup_id
        return result

    def from_map(self, map={}):
        self.backup_progress_status = map.get('BackupProgressStatus')
        self.backup_status = map.get('BackupStatus')
        self.job_mode = map.get('JobMode')
        self.process = map.get('Process')
        self.task_action = map.get('TaskAction')
        self.backup_job_id = map.get('BackupJobId')
        self.backup_id = map.get('BackupId')
        return self


class DescribeBackupTasksResponseItems(TeaModel):
    def __init__(self, backup_job=None):
        self.backup_job = backup_job    # type: List[DescribeBackupTasksResponseItemsBackupJob]

    def validate(self):
        self.validate_required(self.backup_job, 'backup_job')
        if self.backup_job:
            for k in self.backup_job:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['BackupJob'] = []
        if self.backup_job is not None:
            for k in self.backup_job:
                result['BackupJob'].append(k.to_map() if k else None)
        else:
            result['BackupJob'] = None
        return result

    def from_map(self, map={}):
        self.backup_job = []
        if map.get('BackupJob') is not None:
            for k in map.get('BackupJob'):
                temp_model = DescribeBackupTasksResponseItemsBackupJob()
                self.backup_job.append(temp_model.from_map(k))
        else:
            self.backup_job = None
        return self


class DescribeBackupsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, backup_id=None, backup_status=None, backup_mode=None, start_time=None,
                 end_time=None, page_size=None, page_number=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.backup_id = backup_id      # type: str
        self.backup_status = backup_status  # type: str
        self.backup_mode = backup_mode  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['BackupId'] = self.backup_id
        result['BackupStatus'] = self.backup_status
        result['BackupMode'] = self.backup_mode
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.backup_id = map.get('BackupId')
        self.backup_status = map.get('BackupStatus')
        self.backup_mode = map.get('BackupMode')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeBackupsResponse(TeaModel):
    def __init__(self, request_id=None, total_record_count=None, page_number=None, page_record_count=None,
                 total_ecs_snapshot_size=None, items=None):
        self.request_id = request_id    # type: str
        self.total_record_count = total_record_count  # type: str
        self.page_number = page_number  # type: str
        self.page_record_count = page_record_count  # type: str
        self.total_ecs_snapshot_size = total_ecs_snapshot_size  # type: int
        self.items = items              # type: DescribeBackupsResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.total_ecs_snapshot_size, 'total_ecs_snapshot_size')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalRecordCount'] = self.total_record_count
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        result['TotalEcsSnapshotSize'] = self.total_ecs_snapshot_size
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        self.total_ecs_snapshot_size = map.get('TotalEcsSnapshotSize')
        if map.get('Items') is not None:
            temp_model = DescribeBackupsResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeBackupsResponseItemsBackup(TeaModel):
    def __init__(self, backup_id=None, dbinstance_id=None, backup_status=None, backup_start_time=None,
                 backup_end_time=None, backup_type=None, backup_mode=None, backup_method=None, backup_download_url=None,
                 backup_intranet_download_url=None, backup_size=None, host_instance_id=None, store_status=None, meta_status=None,
                 consistent_time=None, backup_initiator=None, copy_only_backup=None, storage_class=None, is_avail=None,
                 encryption=None):
        self.backup_id = backup_id      # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.backup_status = backup_status  # type: str
        self.backup_start_time = backup_start_time  # type: str
        self.backup_end_time = backup_end_time  # type: str
        self.backup_type = backup_type  # type: str
        self.backup_mode = backup_mode  # type: str
        self.backup_method = backup_method  # type: str
        self.backup_download_url = backup_download_url  # type: str
        self.backup_intranet_download_url = backup_intranet_download_url  # type: str
        self.backup_size = backup_size  # type: int
        self.host_instance_id = host_instance_id  # type: str
        self.store_status = store_status  # type: str
        self.meta_status = meta_status  # type: str
        self.consistent_time = consistent_time  # type: int
        self.backup_initiator = backup_initiator  # type: str
        self.copy_only_backup = copy_only_backup  # type: str
        self.storage_class = storage_class  # type: str
        self.is_avail = is_avail        # type: int
        self.encryption = encryption    # type: str

    def validate(self):
        self.validate_required(self.backup_id, 'backup_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.backup_status, 'backup_status')
        self.validate_required(self.backup_start_time, 'backup_start_time')
        self.validate_required(self.backup_end_time, 'backup_end_time')
        self.validate_required(self.backup_type, 'backup_type')
        self.validate_required(self.backup_mode, 'backup_mode')
        self.validate_required(self.backup_method, 'backup_method')
        self.validate_required(self.backup_download_url, 'backup_download_url')
        self.validate_required(self.backup_intranet_download_url, 'backup_intranet_download_url')
        self.validate_required(self.backup_size, 'backup_size')
        self.validate_required(self.host_instance_id, 'host_instance_id')
        self.validate_required(self.store_status, 'store_status')
        self.validate_required(self.meta_status, 'meta_status')
        self.validate_required(self.consistent_time, 'consistent_time')
        self.validate_required(self.backup_initiator, 'backup_initiator')
        self.validate_required(self.copy_only_backup, 'copy_only_backup')
        self.validate_required(self.storage_class, 'storage_class')
        self.validate_required(self.is_avail, 'is_avail')
        self.validate_required(self.encryption, 'encryption')

    def to_map(self):
        result = {}
        result['BackupId'] = self.backup_id
        result['DBInstanceId'] = self.dbinstance_id
        result['BackupStatus'] = self.backup_status
        result['BackupStartTime'] = self.backup_start_time
        result['BackupEndTime'] = self.backup_end_time
        result['BackupType'] = self.backup_type
        result['BackupMode'] = self.backup_mode
        result['BackupMethod'] = self.backup_method
        result['BackupDownloadURL'] = self.backup_download_url
        result['BackupIntranetDownloadURL'] = self.backup_intranet_download_url
        result['BackupSize'] = self.backup_size
        result['HostInstanceID'] = self.host_instance_id
        result['StoreStatus'] = self.store_status
        result['MetaStatus'] = self.meta_status
        result['ConsistentTime'] = self.consistent_time
        result['BackupInitiator'] = self.backup_initiator
        result['CopyOnlyBackup'] = self.copy_only_backup
        result['StorageClass'] = self.storage_class
        result['IsAvail'] = self.is_avail
        result['Encryption'] = self.encryption
        return result

    def from_map(self, map={}):
        self.backup_id = map.get('BackupId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.backup_status = map.get('BackupStatus')
        self.backup_start_time = map.get('BackupStartTime')
        self.backup_end_time = map.get('BackupEndTime')
        self.backup_type = map.get('BackupType')
        self.backup_mode = map.get('BackupMode')
        self.backup_method = map.get('BackupMethod')
        self.backup_download_url = map.get('BackupDownloadURL')
        self.backup_intranet_download_url = map.get('BackupIntranetDownloadURL')
        self.backup_size = map.get('BackupSize')
        self.host_instance_id = map.get('HostInstanceID')
        self.store_status = map.get('StoreStatus')
        self.meta_status = map.get('MetaStatus')
        self.consistent_time = map.get('ConsistentTime')
        self.backup_initiator = map.get('BackupInitiator')
        self.copy_only_backup = map.get('CopyOnlyBackup')
        self.storage_class = map.get('StorageClass')
        self.is_avail = map.get('IsAvail')
        self.encryption = map.get('Encryption')
        return self


class DescribeBackupsResponseItems(TeaModel):
    def __init__(self, backup=None):
        self.backup = backup            # type: List[DescribeBackupsResponseItemsBackup]

    def validate(self):
        self.validate_required(self.backup, 'backup')
        if self.backup:
            for k in self.backup:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Backup'] = []
        if self.backup is not None:
            for k in self.backup:
                result['Backup'].append(k.to_map() if k else None)
        else:
            result['Backup'] = None
        return result

    def from_map(self, map={}):
        self.backup = []
        if map.get('Backup') is not None:
            for k in map.get('Backup'):
                temp_model = DescribeBackupsResponseItemsBackup()
                self.backup.append(temp_model.from_map(k))
        else:
            self.backup = None
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(self, dbinstance_id=None, backup_policy_mode=None, compress_type=None, released_keep_policy=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.backup_policy_mode = backup_policy_mode  # type: str
        self.compress_type = compress_type  # type: str
        self.released_keep_policy = released_keep_policy  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['BackupPolicyMode'] = self.backup_policy_mode
        result['CompressType'] = self.compress_type
        result['ReleasedKeepPolicy'] = self.released_keep_policy
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.backup_policy_mode = map.get('BackupPolicyMode')
        self.compress_type = map.get('CompressType')
        self.released_keep_policy = map.get('ReleasedKeepPolicy')
        return self


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(self, request_id=None, backup_retention_period=None, preferred_next_backup_time=None,
                 preferred_backup_time=None, preferred_backup_period=None, backup_log=None, log_backup_retention_period=None,
                 enable_backup_log=None, local_log_retention_hours=None, local_log_retention_space=None, duplication=None,
                 duplication_content=None, high_space_usage_protection=None, log_backup_frequency=None, compress_type=None,
                 archive_backup_retention_period=None, archive_backup_keep_policy=None, archive_backup_keep_count=None, released_keep_policy=None,
                 log_backup_local_retention_number=None, category=None, support_released_keep=None, backup_interval=None, duplication_location=None):
        self.request_id = request_id    # type: str
        self.backup_retention_period = backup_retention_period  # type: int
        self.preferred_next_backup_time = preferred_next_backup_time  # type: str
        self.preferred_backup_time = preferred_backup_time  # type: str
        self.preferred_backup_period = preferred_backup_period  # type: str
        self.backup_log = backup_log    # type: str
        self.log_backup_retention_period = log_backup_retention_period  # type: int
        self.enable_backup_log = enable_backup_log  # type: str
        self.local_log_retention_hours = local_log_retention_hours  # type: int
        self.local_log_retention_space = local_log_retention_space  # type: str
        self.duplication = duplication  # type: str
        self.duplication_content = duplication_content  # type: str
        self.high_space_usage_protection = high_space_usage_protection  # type: str
        self.log_backup_frequency = log_backup_frequency  # type: str
        self.compress_type = compress_type  # type: str
        self.archive_backup_retention_period = archive_backup_retention_period  # type: str
        self.archive_backup_keep_policy = archive_backup_keep_policy  # type: str
        self.archive_backup_keep_count = archive_backup_keep_count  # type: str
        self.released_keep_policy = released_keep_policy  # type: str
        self.log_backup_local_retention_number = log_backup_local_retention_number  # type: int
        self.category = category        # type: str
        self.support_released_keep = support_released_keep  # type: int
        self.backup_interval = backup_interval  # type: str
        self.duplication_location = duplication_location  # type: DescribeBackupPolicyResponseDuplicationLocation

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.backup_retention_period, 'backup_retention_period')
        self.validate_required(self.preferred_next_backup_time, 'preferred_next_backup_time')
        self.validate_required(self.preferred_backup_time, 'preferred_backup_time')
        self.validate_required(self.preferred_backup_period, 'preferred_backup_period')
        self.validate_required(self.backup_log, 'backup_log')
        self.validate_required(self.log_backup_retention_period, 'log_backup_retention_period')
        self.validate_required(self.enable_backup_log, 'enable_backup_log')
        self.validate_required(self.local_log_retention_hours, 'local_log_retention_hours')
        self.validate_required(self.local_log_retention_space, 'local_log_retention_space')
        self.validate_required(self.duplication, 'duplication')
        self.validate_required(self.duplication_content, 'duplication_content')
        self.validate_required(self.high_space_usage_protection, 'high_space_usage_protection')
        self.validate_required(self.log_backup_frequency, 'log_backup_frequency')
        self.validate_required(self.compress_type, 'compress_type')
        self.validate_required(self.archive_backup_retention_period, 'archive_backup_retention_period')
        self.validate_required(self.archive_backup_keep_policy, 'archive_backup_keep_policy')
        self.validate_required(self.archive_backup_keep_count, 'archive_backup_keep_count')
        self.validate_required(self.released_keep_policy, 'released_keep_policy')
        self.validate_required(self.log_backup_local_retention_number, 'log_backup_local_retention_number')
        self.validate_required(self.category, 'category')
        self.validate_required(self.support_released_keep, 'support_released_keep')
        self.validate_required(self.backup_interval, 'backup_interval')
        self.validate_required(self.duplication_location, 'duplication_location')
        if self.duplication_location:
            self.duplication_location.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['BackupRetentionPeriod'] = self.backup_retention_period
        result['PreferredNextBackupTime'] = self.preferred_next_backup_time
        result['PreferredBackupTime'] = self.preferred_backup_time
        result['PreferredBackupPeriod'] = self.preferred_backup_period
        result['BackupLog'] = self.backup_log
        result['LogBackupRetentionPeriod'] = self.log_backup_retention_period
        result['EnableBackupLog'] = self.enable_backup_log
        result['LocalLogRetentionHours'] = self.local_log_retention_hours
        result['LocalLogRetentionSpace'] = self.local_log_retention_space
        result['Duplication'] = self.duplication
        result['DuplicationContent'] = self.duplication_content
        result['HighSpaceUsageProtection'] = self.high_space_usage_protection
        result['LogBackupFrequency'] = self.log_backup_frequency
        result['CompressType'] = self.compress_type
        result['ArchiveBackupRetentionPeriod'] = self.archive_backup_retention_period
        result['ArchiveBackupKeepPolicy'] = self.archive_backup_keep_policy
        result['ArchiveBackupKeepCount'] = self.archive_backup_keep_count
        result['ReleasedKeepPolicy'] = self.released_keep_policy
        result['LogBackupLocalRetentionNumber'] = self.log_backup_local_retention_number
        result['Category'] = self.category
        result['SupportReleasedKeep'] = self.support_released_keep
        result['BackupInterval'] = self.backup_interval
        if self.duplication_location is not None:
            result['DuplicationLocation'] = self.duplication_location.to_map()
        else:
            result['DuplicationLocation'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.backup_retention_period = map.get('BackupRetentionPeriod')
        self.preferred_next_backup_time = map.get('PreferredNextBackupTime')
        self.preferred_backup_time = map.get('PreferredBackupTime')
        self.preferred_backup_period = map.get('PreferredBackupPeriod')
        self.backup_log = map.get('BackupLog')
        self.log_backup_retention_period = map.get('LogBackupRetentionPeriod')
        self.enable_backup_log = map.get('EnableBackupLog')
        self.local_log_retention_hours = map.get('LocalLogRetentionHours')
        self.local_log_retention_space = map.get('LocalLogRetentionSpace')
        self.duplication = map.get('Duplication')
        self.duplication_content = map.get('DuplicationContent')
        self.high_space_usage_protection = map.get('HighSpaceUsageProtection')
        self.log_backup_frequency = map.get('LogBackupFrequency')
        self.compress_type = map.get('CompressType')
        self.archive_backup_retention_period = map.get('ArchiveBackupRetentionPeriod')
        self.archive_backup_keep_policy = map.get('ArchiveBackupKeepPolicy')
        self.archive_backup_keep_count = map.get('ArchiveBackupKeepCount')
        self.released_keep_policy = map.get('ReleasedKeepPolicy')
        self.log_backup_local_retention_number = map.get('LogBackupLocalRetentionNumber')
        self.category = map.get('Category')
        self.support_released_keep = map.get('SupportReleasedKeep')
        self.backup_interval = map.get('BackupInterval')
        if map.get('DuplicationLocation') is not None:
            temp_model = DescribeBackupPolicyResponseDuplicationLocation()
            self.duplication_location = temp_model.from_map(map['DuplicationLocation'])
        else:
            self.duplication_location = None
        return self


class DescribeBackupPolicyResponseDuplicationLocationLocation(TeaModel):
    def __init__(self, endpoint=None, bucket=None):
        self.endpoint = endpoint        # type: str
        self.bucket = bucket            # type: str

    def validate(self):
        self.validate_required(self.endpoint, 'endpoint')
        self.validate_required(self.bucket, 'bucket')

    def to_map(self):
        result = {}
        result['Endpoint'] = self.endpoint
        result['Bucket'] = self.bucket
        return result

    def from_map(self, map={}):
        self.endpoint = map.get('Endpoint')
        self.bucket = map.get('Bucket')
        return self


class DescribeBackupPolicyResponseDuplicationLocation(TeaModel):
    def __init__(self, sotrage=None, location=None):
        self.sotrage = sotrage          # type: str
        self.location = location        # type: DescribeBackupPolicyResponseDuplicationLocationLocation

    def validate(self):
        self.validate_required(self.sotrage, 'sotrage')
        self.validate_required(self.location, 'location')
        if self.location:
            self.location.validate()

    def to_map(self):
        result = {}
        result['Sotrage'] = self.sotrage
        if self.location is not None:
            result['Location'] = self.location.to_map()
        else:
            result['Location'] = None
        return result

    def from_map(self, map={}):
        self.sotrage = map.get('Sotrage')
        if map.get('Location') is not None:
            temp_model = DescribeBackupPolicyResponseDuplicationLocationLocation()
            self.location = temp_model.from_map(map['Location'])
        else:
            self.location = None
        return self


class DescribeAccountsRequest(TeaModel):
    def __init__(self, dbinstance_id=None, account_name=None, page_size=None, page_number=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.account_name = account_name  # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['AccountName'] = self.account_name
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.account_name = map.get('AccountName')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescribeAccountsResponse(TeaModel):
    def __init__(self, request_id=None, system_admin_account_status=None,
                 system_admin_account_first_activation_time=None, accounts=None):
        self.request_id = request_id    # type: str
        self.system_admin_account_status = system_admin_account_status  # type: str
        self.system_admin_account_first_activation_time = system_admin_account_first_activation_time  # type: str
        self.accounts = accounts        # type: DescribeAccountsResponseAccounts

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.system_admin_account_status, 'system_admin_account_status')
        self.validate_required(self.system_admin_account_first_activation_time, 'system_admin_account_first_activation_time')
        self.validate_required(self.accounts, 'accounts')
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['SystemAdminAccountStatus'] = self.system_admin_account_status
        result['SystemAdminAccountFirstActivationTime'] = self.system_admin_account_first_activation_time
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        else:
            result['Accounts'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.system_admin_account_status = map.get('SystemAdminAccountStatus')
        self.system_admin_account_first_activation_time = map.get('SystemAdminAccountFirstActivationTime')
        if map.get('Accounts') is not None:
            temp_model = DescribeAccountsResponseAccounts()
            self.accounts = temp_model.from_map(map['Accounts'])
        else:
            self.accounts = None
        return self


class DescribeAccountsResponseAccountsDBInstanceAccountDatabasePrivilegesDatabasePrivilege(TeaModel):
    def __init__(self, dbname=None, account_privilege=None, account_privilege_detail=None):
        self.dbname = dbname            # type: str
        self.account_privilege = account_privilege  # type: str
        self.account_privilege_detail = account_privilege_detail  # type: str

    def validate(self):
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.account_privilege, 'account_privilege')
        self.validate_required(self.account_privilege_detail, 'account_privilege_detail')

    def to_map(self):
        result = {}
        result['DBName'] = self.dbname
        result['AccountPrivilege'] = self.account_privilege
        result['AccountPrivilegeDetail'] = self.account_privilege_detail
        return result

    def from_map(self, map={}):
        self.dbname = map.get('DBName')
        self.account_privilege = map.get('AccountPrivilege')
        self.account_privilege_detail = map.get('AccountPrivilegeDetail')
        return self


class DescribeAccountsResponseAccountsDBInstanceAccountDatabasePrivileges(TeaModel):
    def __init__(self, database_privilege=None):
        self.database_privilege = database_privilege  # type: List[DescribeAccountsResponseAccountsDBInstanceAccountDatabasePrivilegesDatabasePrivilege]

    def validate(self):
        self.validate_required(self.database_privilege, 'database_privilege')
        if self.database_privilege:
            for k in self.database_privilege:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DatabasePrivilege'] = []
        if self.database_privilege is not None:
            for k in self.database_privilege:
                result['DatabasePrivilege'].append(k.to_map() if k else None)
        else:
            result['DatabasePrivilege'] = None
        return result

    def from_map(self, map={}):
        self.database_privilege = []
        if map.get('DatabasePrivilege') is not None:
            for k in map.get('DatabasePrivilege'):
                temp_model = DescribeAccountsResponseAccountsDBInstanceAccountDatabasePrivilegesDatabasePrivilege()
                self.database_privilege.append(temp_model.from_map(k))
        else:
            self.database_privilege = None
        return self


class DescribeAccountsResponseAccountsDBInstanceAccount(TeaModel):
    def __init__(self, dbinstance_id=None, account_name=None, account_status=None, account_type=None,
                 account_description=None, priv_exceeded=None, database_privileges=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.account_name = account_name  # type: str
        self.account_status = account_status  # type: str
        self.account_type = account_type  # type: str
        self.account_description = account_description  # type: str
        self.priv_exceeded = priv_exceeded  # type: str
        self.database_privileges = database_privileges  # type: DescribeAccountsResponseAccountsDBInstanceAccountDatabasePrivileges

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.account_status, 'account_status')
        self.validate_required(self.account_type, 'account_type')
        self.validate_required(self.account_description, 'account_description')
        self.validate_required(self.priv_exceeded, 'priv_exceeded')
        self.validate_required(self.database_privileges, 'database_privileges')
        if self.database_privileges:
            self.database_privileges.validate()

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['AccountName'] = self.account_name
        result['AccountStatus'] = self.account_status
        result['AccountType'] = self.account_type
        result['AccountDescription'] = self.account_description
        result['PrivExceeded'] = self.priv_exceeded
        if self.database_privileges is not None:
            result['DatabasePrivileges'] = self.database_privileges.to_map()
        else:
            result['DatabasePrivileges'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.account_name = map.get('AccountName')
        self.account_status = map.get('AccountStatus')
        self.account_type = map.get('AccountType')
        self.account_description = map.get('AccountDescription')
        self.priv_exceeded = map.get('PrivExceeded')
        if map.get('DatabasePrivileges') is not None:
            temp_model = DescribeAccountsResponseAccountsDBInstanceAccountDatabasePrivileges()
            self.database_privileges = temp_model.from_map(map['DatabasePrivileges'])
        else:
            self.database_privileges = None
        return self


class DescribeAccountsResponseAccounts(TeaModel):
    def __init__(self, dbinstance_account=None):
        self.dbinstance_account = dbinstance_account  # type: List[DescribeAccountsResponseAccountsDBInstanceAccount]

    def validate(self):
        self.validate_required(self.dbinstance_account, 'dbinstance_account')
        if self.dbinstance_account:
            for k in self.dbinstance_account:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DBInstanceAccount'] = []
        if self.dbinstance_account is not None:
            for k in self.dbinstance_account:
                result['DBInstanceAccount'].append(k.to_map() if k else None)
        else:
            result['DBInstanceAccount'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_account = []
        if map.get('DBInstanceAccount') is not None:
            for k in map.get('DBInstanceAccount'):
                temp_model = DescribeAccountsResponseAccountsDBInstanceAccount()
                self.dbinstance_account.append(temp_model.from_map(k))
        else:
            self.dbinstance_account = None
        return self


class DescibeImportsFromDatabaseRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, engine=None, import_id=None, start_time=None,
                 end_time=None, page_size=None, page_number=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.engine = engine            # type: str
        self.import_id = import_id      # type: int
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['Engine'] = self.engine
        result['ImportId'] = self.import_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.engine = map.get('Engine')
        self.import_id = map.get('ImportId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        return self


class DescibeImportsFromDatabaseResponse(TeaModel):
    def __init__(self, request_id=None, total_record_count=None, page_number=None, page_record_count=None,
                 items=None):
        self.request_id = request_id    # type: str
        self.total_record_count = total_record_count  # type: int
        self.page_number = page_number  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items              # type: DescibeImportsFromDatabaseResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalRecordCount'] = self.total_record_count
        result['PageNumber'] = self.page_number
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_number = map.get('PageNumber')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescibeImportsFromDatabaseResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescibeImportsFromDatabaseResponseItemsImportResultFromDB(TeaModel):
    def __init__(self, import_id=None, import_data_type=None, import_data_status=None,
                 import_data_status_description=None, incremental_importing_time=None):
        self.import_id = import_id      # type: int
        self.import_data_type = import_data_type  # type: str
        self.import_data_status = import_data_status  # type: str
        self.import_data_status_description = import_data_status_description  # type: str
        self.incremental_importing_time = incremental_importing_time  # type: str

    def validate(self):
        self.validate_required(self.import_id, 'import_id')
        self.validate_required(self.import_data_type, 'import_data_type')
        self.validate_required(self.import_data_status, 'import_data_status')
        self.validate_required(self.import_data_status_description, 'import_data_status_description')
        self.validate_required(self.incremental_importing_time, 'incremental_importing_time')

    def to_map(self):
        result = {}
        result['ImportId'] = self.import_id
        result['ImportDataType'] = self.import_data_type
        result['ImportDataStatus'] = self.import_data_status
        result['ImportDataStatusDescription'] = self.import_data_status_description
        result['IncrementalImportingTime'] = self.incremental_importing_time
        return result

    def from_map(self, map={}):
        self.import_id = map.get('ImportId')
        self.import_data_type = map.get('ImportDataType')
        self.import_data_status = map.get('ImportDataStatus')
        self.import_data_status_description = map.get('ImportDataStatusDescription')
        self.incremental_importing_time = map.get('IncrementalImportingTime')
        return self


class DescibeImportsFromDatabaseResponseItems(TeaModel):
    def __init__(self, import_result_from_db=None):
        self.import_result_from_db = import_result_from_db  # type: List[DescibeImportsFromDatabaseResponseItemsImportResultFromDB]

    def validate(self):
        self.validate_required(self.import_result_from_db, 'import_result_from_db')
        if self.import_result_from_db:
            for k in self.import_result_from_db:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ImportResultFromDB'] = []
        if self.import_result_from_db is not None:
            for k in self.import_result_from_db:
                result['ImportResultFromDB'].append(k.to_map() if k else None)
        else:
            result['ImportResultFromDB'] = None
        return result

    def from_map(self, map={}):
        self.import_result_from_db = []
        if map.get('ImportResultFromDB') is not None:
            for k in map.get('ImportResultFromDB'):
                temp_model = DescibeImportsFromDatabaseResponseItemsImportResultFromDB()
                self.import_result_from_db.append(temp_model.from_map(k))
        else:
            self.import_result_from_db = None
        return self


class DeleteDBInstanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, released_keep_policy=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.released_keep_policy = released_keep_policy  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['ReleasedKeepPolicy'] = self.released_keep_policy
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.released_keep_policy = map.get('ReleasedKeepPolicy')
        return self


class DeleteDBInstanceResponse(TeaModel):
    def __init__(self, request_id=None, region_id=None):
        self.request_id = request_id    # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.region_id = map.get('RegionId')
        return self


class DeleteDatabaseRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbname=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbname = dbname            # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbname, 'dbname')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBName'] = self.dbname
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbname = map.get('DBName')
        return self


class DeleteDatabaseResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(self, dbinstance_id=None, account_name=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.account_name, 'account_name')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['AccountName'] = self.account_name
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.account_name = map.get('AccountName')
        return self


class DeleteAccountResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateTempDBInstanceRequest(TeaModel):
    def __init__(self, dbinstance_id=None, backup_id=None, restore_time=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.backup_id = backup_id      # type: int
        self.restore_time = restore_time  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['BackupId'] = self.backup_id
        result['RestoreTime'] = self.restore_time
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.backup_id = map.get('BackupId')
        self.restore_time = map.get('RestoreTime')
        return self


class CreateTempDBInstanceResponse(TeaModel):
    def __init__(self, request_id=None, temp_dbinstance_id=None):
        self.request_id = request_id    # type: str
        self.temp_dbinstance_id = temp_dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.temp_dbinstance_id, 'temp_dbinstance_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TempDBInstanceId'] = self.temp_dbinstance_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.temp_dbinstance_id = map.get('TempDBInstanceId')
        return self


class CreateDatabaseRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbname=None, character_set_name=None, dbdescription=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbname = dbname            # type: str
        self.character_set_name = character_set_name  # type: str
        self.dbdescription = dbdescription  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbname, 'dbname')
        self.validate_required(self.character_set_name, 'character_set_name')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBName'] = self.dbname
        result['CharacterSetName'] = self.character_set_name
        result['DBDescription'] = self.dbdescription
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbname = map.get('DBName')
        self.character_set_name = map.get('CharacterSetName')
        self.dbdescription = map.get('DBDescription')
        return self


class CreateDatabaseResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateBackupRequest(TeaModel):
    def __init__(self, dbinstance_id=None, dbname=None, backup_strategy=None, backup_method=None, backup_type=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbname = dbname            # type: str
        self.backup_strategy = backup_strategy  # type: str
        self.backup_method = backup_method  # type: str
        self.backup_type = backup_type  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBName'] = self.dbname
        result['BackupStrategy'] = self.backup_strategy
        result['BackupMethod'] = self.backup_method
        result['BackupType'] = self.backup_type
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbname = map.get('DBName')
        self.backup_strategy = map.get('BackupStrategy')
        self.backup_method = map.get('BackupMethod')
        self.backup_type = map.get('BackupType')
        return self


class CreateBackupResponse(TeaModel):
    def __init__(self, request_id=None, backup_job_id=None):
        self.request_id = request_id    # type: str
        self.backup_job_id = backup_job_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.backup_job_id, 'backup_job_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['BackupJobId'] = self.backup_job_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.backup_job_id = map.get('BackupJobId')
        return self


class CreateAccountRequest(TeaModel):
    def __init__(self, dbinstance_id=None, account_name=None, account_password=None, account_description=None,
                 account_type=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.account_name = account_name  # type: str
        self.account_password = account_password  # type: str
        self.account_description = account_description  # type: str
        self.account_type = account_type  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.account_name, 'account_name')
        self.validate_required(self.account_password, 'account_password')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['AccountName'] = self.account_name
        result['AccountPassword'] = self.account_password
        result['AccountDescription'] = self.account_description
        result['AccountType'] = self.account_type
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.account_name = map.get('AccountName')
        self.account_password = map.get('AccountPassword')
        self.account_description = map.get('AccountDescription')
        self.account_type = map.get('AccountType')
        return self


class CreateAccountResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CheckDBNameAvailableRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, dbname=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbname = dbname            # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbname, 'dbname')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['DBName'] = self.dbname
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbname = map.get('DBName')
        return self


class CheckDBNameAvailableResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CheckAccountNameAvailableRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, account_name=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.account_name = account_name  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.account_name, 'account_name')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['AccountName'] = self.account_name
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.account_name = map.get('AccountName')
        return self


class CheckAccountNameAvailableResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CancelImportRequest(TeaModel):
    def __init__(self, dbinstance_id=None, import_id=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.import_id = import_id      # type: int

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.import_id, 'import_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['ImportId'] = self.import_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.import_id = map.get('ImportId')
        return self


class CancelImportResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AddTagsToResourceRequest(TeaModel):
    def __init__(self, client_token=None, proxy_id=None, region_id=None, dbinstance_id=None, tags=None, tag=None):
        self.client_token = client_token  # type: str
        self.proxy_id = proxy_id        # type: str
        self.region_id = region_id      # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.tags = tags                # type: str
        self.tag = tag                  # type: List[AddTagsToResourceRequestTag]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['proxyId'] = self.proxy_id
        result['RegionId'] = self.region_id
        result['DBInstanceId'] = self.dbinstance_id
        result['Tags'] = self.tags
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.proxy_id = map.get('proxyId')
        self.region_id = map.get('RegionId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.tags = map.get('Tags')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = AddTagsToResourceRequestTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class AddTagsToResourceRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['key'] = self.key
        result['value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('key')
        self.value = map.get('value')
        return self


class AddTagsToResourceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class SwitchDBInstanceNetTypeRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, connection_string_prefix=None, port=None,
                 connection_string_type=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.connection_string_prefix = connection_string_prefix  # type: str
        self.port = port                # type: str
        self.connection_string_type = connection_string_type  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.connection_string_prefix, 'connection_string_prefix')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['ConnectionStringPrefix'] = self.connection_string_prefix
        result['Port'] = self.port
        result['ConnectionStringType'] = self.connection_string_type
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.connection_string_prefix = map.get('ConnectionStringPrefix')
        self.port = map.get('Port')
        self.connection_string_type = map.get('ConnectionStringType')
        return self


class SwitchDBInstanceNetTypeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ReleaseInstancePublicConnectionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, current_connection_string=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.current_connection_string = current_connection_string  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.current_connection_string, 'current_connection_string')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['CurrentConnectionString'] = self.current_connection_string
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.current_connection_string = map.get('CurrentConnectionString')
        return self


class ReleaseInstancePublicConnectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyDBInstanceNetworkTypeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, retain_classic=None, classic_expired_days=None,
                 instance_network_type=None, read_write_splitting_classic_expired_days=None, vpcid=None, v_switch_id=None,
                 private_ip_address=None, read_write_splitting_private_ip_address=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.retain_classic = retain_classic  # type: str
        self.classic_expired_days = classic_expired_days  # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.read_write_splitting_classic_expired_days = read_write_splitting_classic_expired_days  # type: int
        self.vpcid = vpcid              # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.read_write_splitting_private_ip_address = read_write_splitting_private_ip_address  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.instance_network_type, 'instance_network_type')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['RetainClassic'] = self.retain_classic
        result['ClassicExpiredDays'] = self.classic_expired_days
        result['InstanceNetworkType'] = self.instance_network_type
        result['ReadWriteSplittingClassicExpiredDays'] = self.read_write_splitting_classic_expired_days
        result['VPCId'] = self.vpcid
        result['VSwitchId'] = self.v_switch_id
        result['PrivateIpAddress'] = self.private_ip_address
        result['ReadWriteSplittingPrivateIpAddress'] = self.read_write_splitting_private_ip_address
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.retain_classic = map.get('RetainClassic')
        self.classic_expired_days = map.get('ClassicExpiredDays')
        self.instance_network_type = map.get('InstanceNetworkType')
        self.read_write_splitting_classic_expired_days = map.get('ReadWriteSplittingClassicExpiredDays')
        self.vpcid = map.get('VPCId')
        self.v_switch_id = map.get('VSwitchId')
        self.private_ip_address = map.get('PrivateIpAddress')
        self.read_write_splitting_private_ip_address = map.get('ReadWriteSplittingPrivateIpAddress')
        return self


class ModifyDBInstanceNetworkTypeResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        return self


class ModifyDBInstanceConnectionStringRequest(TeaModel):
    def __init__(self, dbinstance_id=None, current_connection_string=None, connection_string_prefix=None,
                 port=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.current_connection_string = current_connection_string  # type: str
        self.connection_string_prefix = connection_string_prefix  # type: str
        self.port = port                # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.current_connection_string, 'current_connection_string')
        self.validate_required(self.connection_string_prefix, 'connection_string_prefix')
        self.validate_required(self.port, 'port')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['CurrentConnectionString'] = self.current_connection_string
        result['ConnectionStringPrefix'] = self.connection_string_prefix
        result['Port'] = self.port
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.current_connection_string = map.get('CurrentConnectionString')
        self.connection_string_prefix = map.get('ConnectionStringPrefix')
        self.port = map.get('Port')
        return self


class ModifyDBInstanceConnectionStringResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyDBInstanceConnectionModeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, connection_mode=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.connection_mode = connection_mode  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.connection_mode, 'connection_mode')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['ConnectionMode'] = self.connection_mode
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.connection_mode = map.get('ConnectionMode')
        return self


class ModifyDBInstanceConnectionModeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeDBInstanceNetInfoRequest(TeaModel):
    def __init__(self, client_token=None, dbinstance_id=None, flag=None, dbinstance_net_rwsplit_type=None):
        self.client_token = client_token  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.flag = flag                # type: int
        self.dbinstance_net_rwsplit_type = dbinstance_net_rwsplit_type  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DBInstanceId'] = self.dbinstance_id
        result['Flag'] = self.flag
        result['DBInstanceNetRWSplitType'] = self.dbinstance_net_rwsplit_type
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.dbinstance_id = map.get('DBInstanceId')
        self.flag = map.get('Flag')
        self.dbinstance_net_rwsplit_type = map.get('DBInstanceNetRWSplitType')
        return self


class DescribeDBInstanceNetInfoResponse(TeaModel):
    def __init__(self, request_id=None, instance_network_type=None, security_ipmode=None,
                 dbinstance_net_infos=None):
        self.request_id = request_id    # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.security_ipmode = security_ipmode  # type: str
        self.dbinstance_net_infos = dbinstance_net_infos  # type: DescribeDBInstanceNetInfoResponseDBInstanceNetInfos

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_network_type, 'instance_network_type')
        self.validate_required(self.security_ipmode, 'security_ipmode')
        self.validate_required(self.dbinstance_net_infos, 'dbinstance_net_infos')
        if self.dbinstance_net_infos:
            self.dbinstance_net_infos.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['InstanceNetworkType'] = self.instance_network_type
        result['SecurityIPMode'] = self.security_ipmode
        if self.dbinstance_net_infos is not None:
            result['DBInstanceNetInfos'] = self.dbinstance_net_infos.to_map()
        else:
            result['DBInstanceNetInfos'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.instance_network_type = map.get('InstanceNetworkType')
        self.security_ipmode = map.get('SecurityIPMode')
        if map.get('DBInstanceNetInfos') is not None:
            temp_model = DescribeDBInstanceNetInfoResponseDBInstanceNetInfos()
            self.dbinstance_net_infos = temp_model.from_map(map['DBInstanceNetInfos'])
        else:
            self.dbinstance_net_infos = None
        return self


class DescribeDBInstanceNetInfoResponseDBInstanceNetInfosDBInstanceNetInfoSecurityIPGroupsSecurityIPGroup(TeaModel):
    def __init__(self, security_ipgroup_name=None, security_ips=None):
        self.security_ipgroup_name = security_ipgroup_name  # type: str
        self.security_ips = security_ips  # type: str

    def validate(self):
        self.validate_required(self.security_ipgroup_name, 'security_ipgroup_name')
        self.validate_required(self.security_ips, 'security_ips')

    def to_map(self):
        result = {}
        result['SecurityIPGroupName'] = self.security_ipgroup_name
        result['SecurityIPs'] = self.security_ips
        return result

    def from_map(self, map={}):
        self.security_ipgroup_name = map.get('SecurityIPGroupName')
        self.security_ips = map.get('SecurityIPs')
        return self


class DescribeDBInstanceNetInfoResponseDBInstanceNetInfosDBInstanceNetInfoSecurityIPGroups(TeaModel):
    def __init__(self, security_ipgroup=None):
        self.security_ipgroup = security_ipgroup  # type: List[DescribeDBInstanceNetInfoResponseDBInstanceNetInfosDBInstanceNetInfoSecurityIPGroupsSecurityIPGroup]

    def validate(self):
        self.validate_required(self.security_ipgroup, 'security_ipgroup')
        if self.security_ipgroup:
            for k in self.security_ipgroup:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['securityIPGroup'] = []
        if self.security_ipgroup is not None:
            for k in self.security_ipgroup:
                result['securityIPGroup'].append(k.to_map() if k else None)
        else:
            result['securityIPGroup'] = None
        return result

    def from_map(self, map={}):
        self.security_ipgroup = []
        if map.get('securityIPGroup') is not None:
            for k in map.get('securityIPGroup'):
                temp_model = DescribeDBInstanceNetInfoResponseDBInstanceNetInfosDBInstanceNetInfoSecurityIPGroupsSecurityIPGroup()
                self.security_ipgroup.append(temp_model.from_map(k))
        else:
            self.security_ipgroup = None
        return self


class DescribeDBInstanceNetInfoResponseDBInstanceNetInfosDBInstanceNetInfoDBInstanceWeightsDBInstanceWeight(TeaModel):
    def __init__(self, dbinstance_id=None, dbinstance_type=None, availability=None, weight=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_type = dbinstance_type  # type: str
        self.availability = availability  # type: str
        self.weight = weight            # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbinstance_type, 'dbinstance_type')
        self.validate_required(self.availability, 'availability')
        self.validate_required(self.weight, 'weight')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBInstanceType'] = self.dbinstance_type
        result['Availability'] = self.availability
        result['Weight'] = self.weight
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbinstance_type = map.get('DBInstanceType')
        self.availability = map.get('Availability')
        self.weight = map.get('Weight')
        return self


class DescribeDBInstanceNetInfoResponseDBInstanceNetInfosDBInstanceNetInfoDBInstanceWeights(TeaModel):
    def __init__(self, dbinstance_weight=None):
        self.dbinstance_weight = dbinstance_weight  # type: List[DescribeDBInstanceNetInfoResponseDBInstanceNetInfosDBInstanceNetInfoDBInstanceWeightsDBInstanceWeight]

    def validate(self):
        self.validate_required(self.dbinstance_weight, 'dbinstance_weight')
        if self.dbinstance_weight:
            for k in self.dbinstance_weight:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DBInstanceWeight'] = []
        if self.dbinstance_weight is not None:
            for k in self.dbinstance_weight:
                result['DBInstanceWeight'].append(k.to_map() if k else None)
        else:
            result['DBInstanceWeight'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_weight = []
        if map.get('DBInstanceWeight') is not None:
            for k in map.get('DBInstanceWeight'):
                temp_model = DescribeDBInstanceNetInfoResponseDBInstanceNetInfosDBInstanceNetInfoDBInstanceWeightsDBInstanceWeight()
                self.dbinstance_weight.append(temp_model.from_map(k))
        else:
            self.dbinstance_weight = None
        return self


class DescribeDBInstanceNetInfoResponseDBInstanceNetInfosDBInstanceNetInfo(TeaModel):
    def __init__(self, upgradeable=None, expired_time=None, connection_string=None, ipaddress=None, iptype=None,
                 port=None, vpcid=None, v_switch_id=None, connection_string_type=None, max_delay_time=None,
                 distribution_type=None, security_ipgroups=None, dbinstance_weights=None):
        self.upgradeable = upgradeable  # type: str
        self.expired_time = expired_time  # type: str
        self.connection_string = connection_string  # type: str
        self.ipaddress = ipaddress      # type: str
        self.iptype = iptype            # type: str
        self.port = port                # type: str
        self.vpcid = vpcid              # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.connection_string_type = connection_string_type  # type: str
        self.max_delay_time = max_delay_time  # type: str
        self.distribution_type = distribution_type  # type: str
        self.security_ipgroups = security_ipgroups  # type: DescribeDBInstanceNetInfoResponseDBInstanceNetInfosDBInstanceNetInfoSecurityIPGroups
        self.dbinstance_weights = dbinstance_weights  # type: DescribeDBInstanceNetInfoResponseDBInstanceNetInfosDBInstanceNetInfoDBInstanceWeights

    def validate(self):
        self.validate_required(self.upgradeable, 'upgradeable')
        self.validate_required(self.expired_time, 'expired_time')
        self.validate_required(self.connection_string, 'connection_string')
        self.validate_required(self.ipaddress, 'ipaddress')
        self.validate_required(self.iptype, 'iptype')
        self.validate_required(self.port, 'port')
        self.validate_required(self.vpcid, 'vpcid')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.connection_string_type, 'connection_string_type')
        self.validate_required(self.max_delay_time, 'max_delay_time')
        self.validate_required(self.distribution_type, 'distribution_type')
        self.validate_required(self.security_ipgroups, 'security_ipgroups')
        if self.security_ipgroups:
            self.security_ipgroups.validate()
        self.validate_required(self.dbinstance_weights, 'dbinstance_weights')
        if self.dbinstance_weights:
            self.dbinstance_weights.validate()

    def to_map(self):
        result = {}
        result['Upgradeable'] = self.upgradeable
        result['ExpiredTime'] = self.expired_time
        result['ConnectionString'] = self.connection_string
        result['IPAddress'] = self.ipaddress
        result['IPType'] = self.iptype
        result['Port'] = self.port
        result['VPCId'] = self.vpcid
        result['VSwitchId'] = self.v_switch_id
        result['ConnectionStringType'] = self.connection_string_type
        result['MaxDelayTime'] = self.max_delay_time
        result['DistributionType'] = self.distribution_type
        if self.security_ipgroups is not None:
            result['SecurityIPGroups'] = self.security_ipgroups.to_map()
        else:
            result['SecurityIPGroups'] = None
        if self.dbinstance_weights is not None:
            result['DBInstanceWeights'] = self.dbinstance_weights.to_map()
        else:
            result['DBInstanceWeights'] = None
        return result

    def from_map(self, map={}):
        self.upgradeable = map.get('Upgradeable')
        self.expired_time = map.get('ExpiredTime')
        self.connection_string = map.get('ConnectionString')
        self.ipaddress = map.get('IPAddress')
        self.iptype = map.get('IPType')
        self.port = map.get('Port')
        self.vpcid = map.get('VPCId')
        self.v_switch_id = map.get('VSwitchId')
        self.connection_string_type = map.get('ConnectionStringType')
        self.max_delay_time = map.get('MaxDelayTime')
        self.distribution_type = map.get('DistributionType')
        if map.get('SecurityIPGroups') is not None:
            temp_model = DescribeDBInstanceNetInfoResponseDBInstanceNetInfosDBInstanceNetInfoSecurityIPGroups()
            self.security_ipgroups = temp_model.from_map(map['SecurityIPGroups'])
        else:
            self.security_ipgroups = None
        if map.get('DBInstanceWeights') is not None:
            temp_model = DescribeDBInstanceNetInfoResponseDBInstanceNetInfosDBInstanceNetInfoDBInstanceWeights()
            self.dbinstance_weights = temp_model.from_map(map['DBInstanceWeights'])
        else:
            self.dbinstance_weights = None
        return self


class DescribeDBInstanceNetInfoResponseDBInstanceNetInfos(TeaModel):
    def __init__(self, dbinstance_net_info=None):
        self.dbinstance_net_info = dbinstance_net_info  # type: List[DescribeDBInstanceNetInfoResponseDBInstanceNetInfosDBInstanceNetInfo]

    def validate(self):
        self.validate_required(self.dbinstance_net_info, 'dbinstance_net_info')
        if self.dbinstance_net_info:
            for k in self.dbinstance_net_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DBInstanceNetInfo'] = []
        if self.dbinstance_net_info is not None:
            for k in self.dbinstance_net_info:
                result['DBInstanceNetInfo'].append(k.to_map() if k else None)
        else:
            result['DBInstanceNetInfo'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_net_info = []
        if map.get('DBInstanceNetInfo') is not None:
            for k in map.get('DBInstanceNetInfo'):
                temp_model = DescribeDBInstanceNetInfoResponseDBInstanceNetInfosDBInstanceNetInfo()
                self.dbinstance_net_info.append(temp_model.from_map(k))
        else:
            self.dbinstance_net_info = None
        return self


class CreateReadOnlyDBInstanceRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, zone_id=None, dbinstance_id=None, dbinstance_class=None,
                 dbinstance_storage=None, engine_version=None, pay_type=None, dbinstance_description=None, instance_network_type=None,
                 vpcid=None, v_switch_id=None, private_ip_address=None, resource_group_id=None, category=None,
                 dbinstance_storage_type=None, dedicated_host_group_id=None, target_dedicated_host_id_for_master=None,
                 gdn_instance_name=None, tddl_biz_type=None, tddl_region_config=None, instruction_set_arch=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id      # type: str
        self.zone_id = zone_id          # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_storage = dbinstance_storage  # type: int
        self.engine_version = engine_version  # type: str
        self.pay_type = pay_type        # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.vpcid = vpcid              # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.category = category        # type: str
        self.dbinstance_storage_type = dbinstance_storage_type  # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.target_dedicated_host_id_for_master = target_dedicated_host_id_for_master  # type: str
        self.gdn_instance_name = gdn_instance_name  # type: str
        self.tddl_biz_type = tddl_biz_type  # type: str
        self.tddl_region_config = tddl_region_config  # type: str
        self.instruction_set_arch = instruction_set_arch  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbinstance_class, 'dbinstance_class')
        self.validate_required(self.dbinstance_storage, 'dbinstance_storage')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.pay_type, 'pay_type')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['RegionId'] = self.region_id
        result['ZoneId'] = self.zone_id
        result['DBInstanceId'] = self.dbinstance_id
        result['DBInstanceClass'] = self.dbinstance_class
        result['DBInstanceStorage'] = self.dbinstance_storage
        result['EngineVersion'] = self.engine_version
        result['PayType'] = self.pay_type
        result['DBInstanceDescription'] = self.dbinstance_description
        result['InstanceNetworkType'] = self.instance_network_type
        result['VPCId'] = self.vpcid
        result['VSwitchId'] = self.v_switch_id
        result['PrivateIpAddress'] = self.private_ip_address
        result['ResourceGroupId'] = self.resource_group_id
        result['Category'] = self.category
        result['DBInstanceStorageType'] = self.dbinstance_storage_type
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['TargetDedicatedHostIdForMaster'] = self.target_dedicated_host_id_for_master
        result['GdnInstanceName'] = self.gdn_instance_name
        result['TddlBizType'] = self.tddl_biz_type
        result['TddlRegionConfig'] = self.tddl_region_config
        result['InstructionSetArch'] = self.instruction_set_arch
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.region_id = map.get('RegionId')
        self.zone_id = map.get('ZoneId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbinstance_class = map.get('DBInstanceClass')
        self.dbinstance_storage = map.get('DBInstanceStorage')
        self.engine_version = map.get('EngineVersion')
        self.pay_type = map.get('PayType')
        self.dbinstance_description = map.get('DBInstanceDescription')
        self.instance_network_type = map.get('InstanceNetworkType')
        self.vpcid = map.get('VPCId')
        self.v_switch_id = map.get('VSwitchId')
        self.private_ip_address = map.get('PrivateIpAddress')
        self.resource_group_id = map.get('ResourceGroupId')
        self.category = map.get('Category')
        self.dbinstance_storage_type = map.get('DBInstanceStorageType')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.target_dedicated_host_id_for_master = map.get('TargetDedicatedHostIdForMaster')
        self.gdn_instance_name = map.get('GdnInstanceName')
        self.tddl_biz_type = map.get('TddlBizType')
        self.tddl_region_config = map.get('TddlRegionConfig')
        self.instruction_set_arch = map.get('InstructionSetArch')
        return self


class CreateReadOnlyDBInstanceResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, order_id=None, connection_string=None, port=None):
        self.request_id = request_id    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.order_id = order_id        # type: str
        self.connection_string = connection_string  # type: str
        self.port = port                # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.connection_string, 'connection_string')
        self.validate_required(self.port, 'port')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['OrderId'] = self.order_id
        result['ConnectionString'] = self.connection_string
        result['Port'] = self.port
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.order_id = map.get('OrderId')
        self.connection_string = map.get('ConnectionString')
        self.port = map.get('Port')
        return self


class CreateDBInstanceRequest(TeaModel):
    def __init__(self, region_id=None, engine=None, engine_version=None, dbinstance_class=None,
                 dbinstance_storage=None, system_dbcharset=None, dbinstance_net_type=None, dbinstance_description=None,
                 security_iplist=None, client_token=None, pay_type=None, zone_id=None, zone_id_slave_1=None, zone_id_slave_2=None,
                 instance_network_type=None, connection_mode=None, vpcid=None, v_switch_id=None, private_ip_address=None, used_time=None,
                 period=None, resource_group_id=None, dbinstance_storage_type=None, business_info=None,
                 encryption_key=None, role_arn=None, auto_renew=None, category=None, dedicated_host_group_id=None,
                 target_dedicated_host_id_for_master=None, target_dedicated_host_id_for_slave=None, target_dedicated_host_id_for_log=None,
                 dbparam_group_id=None, dbtime_zone=None, dbis_ignore_case=None, target_minor_version=None, storage_auto_scale=None,
                 storage_threshold=None, storage_upper_bound=None):
        # description: 地域ID，可以通过接口[DescribeRegions](~~26243~~)查看可用的地域ID。; 
        self.region_id = region_id      # type: str
        # description: 数据库类型，取值：* **MySQL**；* **SQLServer**；* **PostgreSQL**；* **PPAS**；* **MariaDB**。; 
        self.engine = engine            # type: str
        # description: 数据库版本，取值：* MySQL：**5.5/5.6/5.7/8.0**；* SQL Server：**2008r2/2012/2012_ent_ha/2012_std_ha/2012_web/2016_ent_ha/2016_std_ha/2016_web/2017_ent**；* PostgreSQL：**9.4/10.0**；* PPAS：**9.3/10.0**；* MariaDB：**10.3**。; 
        self.engine_version = engine_version  # type: str
        # description: 实例规格，详见[实例规格表](~~26312~~)。; 
        self.dbinstance_class = dbinstance_class  # type: str
        # description: 实例存储空间，单位：GB。每5GB进行递增，详见[实例规格表](~~26312~~)。; 
        self.dbinstance_storage = dbinstance_storage  # type: int
        # description: 字符集，取值：* MySQL/MariaDB实例：**utf8、gbk、latin1、utf8mb4**；* SQL Server实例：**Chinese_PRC_CI_AS、Chinese_PRC_CS_AS、SQL_Latin1_General_CP1_CI_AS、SQL_Latin1_General_CP1_CS_AS、Chinese_PRC_BIN**。; 
        self.system_dbcharset = system_dbcharset  # type: str
        # description: 实例的网络连接类型，取值：* **Internet**：公网连接；* **Intranet**：内网连接。; 
        self.dbinstance_net_type = dbinstance_net_type  # type: str
        # description: 实例名称，长度为2~256个字符。以中文、英文字母开头，可以包含数字、中文、英文、下划线（_）、短横线（-）。>不能以 http:// 和 https:// 开头。; 
        self.dbinstance_description = dbinstance_description  # type: str
        # description: 该实例的[IP白名单](~~43185~~)，多个IP地址请以英文逗号（,）隔开，不可重复，最多1000个。支持如下两种格式：* IP地址形式，例如：10.23.12.24；* CIDR形式，例如：10.23.12.24/24（无类域间路由，24表示了地址中前缀的长度，范围为1~32）。; 
        self.security_iplist = security_iplist  # type: str
        # description: 用于保证请求的幂等性，防止重复提交请求。由客户端生成该参数值，要保证在不同请求间唯一，最大值不超过64个ASCII字符，且该参数值中不能包含非ASCII字符。; 
        self.client_token = client_token  # type: str
        # description: 实例的付费类型，取值：* **Postpaid**：后付费（按量付费）；* **Prepaid**：预付费（包年包月）。; 
        self.pay_type = pay_type        # type: str
        # description: 可用区ID。多可用区用英文冒号（:）分隔。> 指定了VPC和交换机时，为匹配交换机对应的可用区，该参数必填。; 
        self.zone_id = zone_id          # type: str
        self.zone_id_slave_1 = zone_id_slave_1  # type: str
        self.zone_id_slave_2 = zone_id_slave_2  # type: str
        # description: 实例的网络类型，取值：* **VPC**：VPC网络；* **Classic**：经典网络。默认创建经典网络类型的实例。> * SQL Server2017集群版只支持VPC网络；* 如果数据库类型为MariaDB，该参数必填。; 
        self.instance_network_type = instance_network_type  # type: str
        # description: 实例的访问模式，取值：* **Standard**：标准访问模式；* **Safe**：数据库代理模式。默认为RDS系统分配。> SQL Server 2012/2016/2017只支持标准访问模式。; 
        self.connection_mode = connection_mode  # type: str
        # description: VPC ID。>如果数据库类型为MariaDB，该参数必填。; 
        self.vpcid = vpcid              # type: str
        # description: VSwitch ID，多个值用英文逗号（,）隔开。>如果数据库类型为MariaDB，该参数必填。; 
        self.v_switch_id = v_switch_id  # type: str
        # description: 设置实例的内网IP，需要在指定交换机的IP地址范围内。系统默认通过**VPCId**和**VSwitchId**自动分配。; 
        self.private_ip_address = private_ip_address  # type: str
        # description: 指定购买时长，取值：* 当参数**Period**为**Year**时，UsedTime取值为**1~3**；* 当参数**Period**为**Month**时，UsedTime取值为**1~9**。> 若付费类型为**Prepaid**则该参数必须传入。; 
        self.used_time = used_time      # type: str
        # description: 指定预付费实例为包年或者包月类型，取值：* **Year**：包年；* **Month**：包月。> 若付费类型为**Prepaid**则该参数必须传入。; 
        self.period = period            # type: str
        self.resource_group_id = resource_group_id  # type: str
        # description: 实例存储类型，取值：* **local_ssd**/**ephemeral_ssd**：本地SSD盘（推荐）；* **cloud_ssd**：SSD云盘；* **cloud_essd**：ESSD云盘。; 
        self.dbinstance_storage_type = dbinstance_storage_type  # type: str
        # description: 业务扩展参数。; 
        self.business_info = business_info  # type: str
        self.encryption_key = encryption_key  # type: str
        self.role_arn = role_arn        # type: str
        # description: 实例是否自动续费，取值：**true | false**>* 按月购买，则自动续费周期为1个月；* 按年购买，则自动续费周期为1年。; 
        self.auto_renew = auto_renew    # type: str
        self.category = category        # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.target_dedicated_host_id_for_master = target_dedicated_host_id_for_master  # type: str
        self.target_dedicated_host_id_for_slave = target_dedicated_host_id_for_slave  # type: str
        self.target_dedicated_host_id_for_log = target_dedicated_host_id_for_log  # type: str
        self.dbparam_group_id = dbparam_group_id  # type: str
        self.dbtime_zone = dbtime_zone  # type: str
        self.dbis_ignore_case = dbis_ignore_case  # type: str
        self.target_minor_version = target_minor_version  # type: str
        self.storage_auto_scale = storage_auto_scale  # type: str
        self.storage_threshold = storage_threshold  # type: int
        self.storage_upper_bound = storage_upper_bound  # type: int

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.dbinstance_class, 'dbinstance_class')
        self.validate_required(self.dbinstance_storage, 'dbinstance_storage')
        self.validate_required(self.dbinstance_net_type, 'dbinstance_net_type')
        self.validate_required(self.security_iplist, 'security_iplist')
        self.validate_required(self.pay_type, 'pay_type')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        result['DBInstanceClass'] = self.dbinstance_class
        result['DBInstanceStorage'] = self.dbinstance_storage
        result['SystemDBCharset'] = self.system_dbcharset
        result['DBInstanceNetType'] = self.dbinstance_net_type
        result['DBInstanceDescription'] = self.dbinstance_description
        result['SecurityIPList'] = self.security_iplist
        result['ClientToken'] = self.client_token
        result['PayType'] = self.pay_type
        result['ZoneId'] = self.zone_id
        result['ZoneIdSlave1'] = self.zone_id_slave_1
        result['ZoneIdSlave2'] = self.zone_id_slave_2
        result['InstanceNetworkType'] = self.instance_network_type
        result['ConnectionMode'] = self.connection_mode
        result['VPCId'] = self.vpcid
        result['VSwitchId'] = self.v_switch_id
        result['PrivateIpAddress'] = self.private_ip_address
        result['UsedTime'] = self.used_time
        result['Period'] = self.period
        result['ResourceGroupId'] = self.resource_group_id
        result['DBInstanceStorageType'] = self.dbinstance_storage_type
        result['BusinessInfo'] = self.business_info
        result['EncryptionKey'] = self.encryption_key
        result['RoleARN'] = self.role_arn
        result['AutoRenew'] = self.auto_renew
        result['Category'] = self.category
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['TargetDedicatedHostIdForMaster'] = self.target_dedicated_host_id_for_master
        result['TargetDedicatedHostIdForSlave'] = self.target_dedicated_host_id_for_slave
        result['TargetDedicatedHostIdForLog'] = self.target_dedicated_host_id_for_log
        result['DBParamGroupId'] = self.dbparam_group_id
        result['DBTimeZone'] = self.dbtime_zone
        result['DBIsIgnoreCase'] = self.dbis_ignore_case
        result['TargetMinorVersion'] = self.target_minor_version
        result['StorageAutoScale'] = self.storage_auto_scale
        result['StorageThreshold'] = self.storage_threshold
        result['StorageUpperBound'] = self.storage_upper_bound
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        self.dbinstance_class = map.get('DBInstanceClass')
        self.dbinstance_storage = map.get('DBInstanceStorage')
        self.system_dbcharset = map.get('SystemDBCharset')
        self.dbinstance_net_type = map.get('DBInstanceNetType')
        self.dbinstance_description = map.get('DBInstanceDescription')
        self.security_iplist = map.get('SecurityIPList')
        self.client_token = map.get('ClientToken')
        self.pay_type = map.get('PayType')
        self.zone_id = map.get('ZoneId')
        self.zone_id_slave_1 = map.get('ZoneIdSlave1')
        self.zone_id_slave_2 = map.get('ZoneIdSlave2')
        self.instance_network_type = map.get('InstanceNetworkType')
        self.connection_mode = map.get('ConnectionMode')
        self.vpcid = map.get('VPCId')
        self.v_switch_id = map.get('VSwitchId')
        self.private_ip_address = map.get('PrivateIpAddress')
        self.used_time = map.get('UsedTime')
        self.period = map.get('Period')
        self.resource_group_id = map.get('ResourceGroupId')
        self.dbinstance_storage_type = map.get('DBInstanceStorageType')
        self.business_info = map.get('BusinessInfo')
        self.encryption_key = map.get('EncryptionKey')
        self.role_arn = map.get('RoleARN')
        self.auto_renew = map.get('AutoRenew')
        self.category = map.get('Category')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.target_dedicated_host_id_for_master = map.get('TargetDedicatedHostIdForMaster')
        self.target_dedicated_host_id_for_slave = map.get('TargetDedicatedHostIdForSlave')
        self.target_dedicated_host_id_for_log = map.get('TargetDedicatedHostIdForLog')
        self.dbparam_group_id = map.get('DBParamGroupId')
        self.dbtime_zone = map.get('DBTimeZone')
        self.dbis_ignore_case = map.get('DBIsIgnoreCase')
        self.target_minor_version = map.get('TargetMinorVersion')
        self.storage_auto_scale = map.get('StorageAutoScale')
        self.storage_threshold = map.get('StorageThreshold')
        self.storage_upper_bound = map.get('StorageUpperBound')
        return self


class CreateDBInstanceResponse(TeaModel):
    def __init__(self, request_id=None, dbinstance_id=None, order_id=None, connection_string=None, port=None):
        # description: 请求ID。; 
        self.request_id = request_id    # type: str
        # description: 实例ID。; 
        self.dbinstance_id = dbinstance_id  # type: str
        # description: 订单ID。; 
        self.order_id = order_id        # type: str
        # description: 数据库连接地址。>参数**DBInstanceNetType**决定该地址为内网或外网。; 
        self.connection_string = connection_string  # type: str
        # description: 数据库连接端口。>参数**DBInstanceNetType**决定该端口为内网或外网。; 
        self.port = port                # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.connection_string, 'connection_string')
        self.validate_required(self.port, 'port')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DBInstanceId'] = self.dbinstance_id
        result['OrderId'] = self.order_id
        result['ConnectionString'] = self.connection_string
        result['Port'] = self.port
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.order_id = map.get('OrderId')
        self.connection_string = map.get('ConnectionString')
        self.port = map.get('Port')
        return self


class AllocateInstancePublicConnectionRequest(TeaModel):
    def __init__(self, dbinstance_id=None, connection_string_prefix=None, port=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.connection_string_prefix = connection_string_prefix  # type: str
        self.port = port                # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.connection_string_prefix, 'connection_string_prefix')
        self.validate_required(self.port, 'port')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['ConnectionStringPrefix'] = self.connection_string_prefix
        result['Port'] = self.port
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.connection_string_prefix = map.get('ConnectionStringPrefix')
        self.port = map.get('Port')
        return self


class AllocateInstancePublicConnectionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeDBInstancesByPerformanceRequest(TeaModel):
    def __init__(self, client_token=None, proxy_id=None, dbinstance_id=None, page_size=None, page_number=None,
                 sort_method=None, sort_key=None, tags=None, tag=None, region_id=None):
        self.client_token = client_token  # type: str
        self.proxy_id = proxy_id        # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.sort_method = sort_method  # type: str
        self.sort_key = sort_key        # type: str
        self.tags = tags                # type: str
        self.tag = tag                  # type: List[DescribeDBInstancesByPerformanceRequestTag]
        self.region_id = region_id      # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['proxyId'] = self.proxy_id
        result['DBInstanceId'] = self.dbinstance_id
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['SortMethod'] = self.sort_method
        result['SortKey'] = self.sort_key
        result['Tags'] = self.tags
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.proxy_id = map.get('proxyId')
        self.dbinstance_id = map.get('DBInstanceId')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.sort_method = map.get('SortMethod')
        self.sort_key = map.get('SortKey')
        self.tags = map.get('Tags')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = DescribeDBInstancesByPerformanceRequestTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        self.region_id = map.get('RegionId')
        return self


class DescribeDBInstancesByPerformanceRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['key'] = self.key
        result['value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('key')
        self.value = map.get('value')
        return self


class DescribeDBInstancesByPerformanceResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, total_record_count=None, page_record_count=None,
                 items=None):
        self.request_id = request_id    # type: str
        self.page_number = page_number  # type: int
        self.total_record_count = total_record_count  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items              # type: DescribeDBInstancesByPerformanceResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNumber'] = self.page_number
        result['TotalRecordCount'] = self.total_record_count
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_number = map.get('PageNumber')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeDBInstancesByPerformanceResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeDBInstancesByPerformanceResponseItemsDBInstancePerformance(TeaModel):
    def __init__(self, cpuusage=None, iopsusage=None, disk_usage=None, session_usage=None, dbinstance_id=None,
                 dbinstance_description=None):
        self.cpuusage = cpuusage        # type: str
        self.iopsusage = iopsusage      # type: str
        self.disk_usage = disk_usage    # type: str
        self.session_usage = session_usage  # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_description = dbinstance_description  # type: str

    def validate(self):
        self.validate_required(self.cpuusage, 'cpuusage')
        self.validate_required(self.iopsusage, 'iopsusage')
        self.validate_required(self.disk_usage, 'disk_usage')
        self.validate_required(self.session_usage, 'session_usage')
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbinstance_description, 'dbinstance_description')

    def to_map(self):
        result = {}
        result['CPUUsage'] = self.cpuusage
        result['IOPSUsage'] = self.iopsusage
        result['DiskUsage'] = self.disk_usage
        result['SessionUsage'] = self.session_usage
        result['DBInstanceId'] = self.dbinstance_id
        result['DBInstanceDescription'] = self.dbinstance_description
        return result

    def from_map(self, map={}):
        self.cpuusage = map.get('CPUUsage')
        self.iopsusage = map.get('IOPSUsage')
        self.disk_usage = map.get('DiskUsage')
        self.session_usage = map.get('SessionUsage')
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbinstance_description = map.get('DBInstanceDescription')
        return self


class DescribeDBInstancesByPerformanceResponseItems(TeaModel):
    def __init__(self, dbinstance_performance=None):
        self.dbinstance_performance = dbinstance_performance  # type: List[DescribeDBInstancesByPerformanceResponseItemsDBInstancePerformance]

    def validate(self):
        self.validate_required(self.dbinstance_performance, 'dbinstance_performance')
        if self.dbinstance_performance:
            for k in self.dbinstance_performance:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DBInstancePerformance'] = []
        if self.dbinstance_performance is not None:
            for k in self.dbinstance_performance:
                result['DBInstancePerformance'].append(k.to_map() if k else None)
        else:
            result['DBInstancePerformance'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_performance = []
        if map.get('DBInstancePerformance') is not None:
            for k in map.get('DBInstancePerformance'):
                temp_model = DescribeDBInstancesByPerformanceResponseItemsDBInstancePerformance()
                self.dbinstance_performance.append(temp_model.from_map(k))
        else:
            self.dbinstance_performance = None
        return self


class DescribeDBInstancesByExpireTimeRequest(TeaModel):
    def __init__(self, region_id=None, proxy_id=None, expire_period=None, expired=None, page_size=None,
                 page_number=None, tags=None):
        self.region_id = region_id      # type: str
        self.proxy_id = proxy_id        # type: str
        self.expire_period = expire_period  # type: int
        self.expired = expired          # type: bool
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.tags = tags                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['proxyId'] = self.proxy_id
        result['ExpirePeriod'] = self.expire_period
        result['Expired'] = self.expired
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['Tags'] = self.tags
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.proxy_id = map.get('proxyId')
        self.expire_period = map.get('ExpirePeriod')
        self.expired = map.get('Expired')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.tags = map.get('Tags')
        return self


class DescribeDBInstancesByExpireTimeResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, total_record_count=None, page_record_count=None,
                 items=None):
        self.request_id = request_id    # type: str
        self.page_number = page_number  # type: int
        self.total_record_count = total_record_count  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items              # type: DescribeDBInstancesByExpireTimeResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNumber'] = self.page_number
        result['TotalRecordCount'] = self.total_record_count
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_number = map.get('PageNumber')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeDBInstancesByExpireTimeResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeDBInstancesByExpireTimeResponseItemsDBInstanceExpireTime(TeaModel):
    def __init__(self, dbinstance_id=None, dbinstance_description=None, expire_time=None, dbinstance_status=None,
                 lock_mode=None, pay_type=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.expire_time = expire_time  # type: str
        self.dbinstance_status = dbinstance_status  # type: str
        self.lock_mode = lock_mode      # type: str
        self.pay_type = pay_type        # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbinstance_description, 'dbinstance_description')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.dbinstance_status, 'dbinstance_status')
        self.validate_required(self.lock_mode, 'lock_mode')
        self.validate_required(self.pay_type, 'pay_type')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBInstanceDescription'] = self.dbinstance_description
        result['ExpireTime'] = self.expire_time
        result['DBInstanceStatus'] = self.dbinstance_status
        result['LockMode'] = self.lock_mode
        result['PayType'] = self.pay_type
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbinstance_description = map.get('DBInstanceDescription')
        self.expire_time = map.get('ExpireTime')
        self.dbinstance_status = map.get('DBInstanceStatus')
        self.lock_mode = map.get('LockMode')
        self.pay_type = map.get('PayType')
        return self


class DescribeDBInstancesByExpireTimeResponseItems(TeaModel):
    def __init__(self, dbinstance_expire_time=None):
        self.dbinstance_expire_time = dbinstance_expire_time  # type: List[DescribeDBInstancesByExpireTimeResponseItemsDBInstanceExpireTime]

    def validate(self):
        self.validate_required(self.dbinstance_expire_time, 'dbinstance_expire_time')
        if self.dbinstance_expire_time:
            for k in self.dbinstance_expire_time:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DBInstanceExpireTime'] = []
        if self.dbinstance_expire_time is not None:
            for k in self.dbinstance_expire_time:
                result['DBInstanceExpireTime'].append(k.to_map() if k else None)
        else:
            result['DBInstanceExpireTime'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_expire_time = []
        if map.get('DBInstanceExpireTime') is not None:
            for k in map.get('DBInstanceExpireTime'):
                temp_model = DescribeDBInstancesByExpireTimeResponseItemsDBInstanceExpireTime()
                self.dbinstance_expire_time.append(temp_model.from_map(k))
        else:
            self.dbinstance_expire_time = None
        return self


class DescribeDBInstancesRequest(TeaModel):
    def __init__(self, client_token=None, proxy_id=None, engine=None, zone_id=None, resource_group_id=None,
                 dbinstance_status=None, expired=None, search_key=None, dbinstance_id=None, dbinstance_type=None, region_id=None,
                 page_size=None, page_number=None, instance_network_type=None, vpc_id=None, v_switch_id=None,
                 dbinstance_class=None, engine_version=None, pay_type=None, connection_mode=None, tags=None,
                 dedicated_host_group_id=None, dedicated_host_id=None, instance_level=None, need_vpc_name=None):
        self.client_token = client_token  # type: str
        self.proxy_id = proxy_id        # type: str
        self.engine = engine            # type: str
        self.zone_id = zone_id          # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.dbinstance_status = dbinstance_status  # type: str
        self.expired = expired          # type: str
        self.search_key = search_key    # type: str
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_type = dbinstance_type  # type: str
        self.region_id = region_id      # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.instance_network_type = instance_network_type  # type: str
        self.vpc_id = vpc_id            # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.engine_version = engine_version  # type: str
        self.pay_type = pay_type        # type: str
        self.connection_mode = connection_mode  # type: str
        self.tags = tags                # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.dedicated_host_id = dedicated_host_id  # type: str
        self.instance_level = instance_level  # type: int
        self.need_vpc_name = need_vpc_name  # type: bool

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['proxyId'] = self.proxy_id
        result['Engine'] = self.engine
        result['ZoneId'] = self.zone_id
        result['ResourceGroupId'] = self.resource_group_id
        result['DBInstanceStatus'] = self.dbinstance_status
        result['Expired'] = self.expired
        result['SearchKey'] = self.search_key
        result['DBInstanceId'] = self.dbinstance_id
        result['DBInstanceType'] = self.dbinstance_type
        result['RegionId'] = self.region_id
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['InstanceNetworkType'] = self.instance_network_type
        result['VpcId'] = self.vpc_id
        result['VSwitchId'] = self.v_switch_id
        result['DBInstanceClass'] = self.dbinstance_class
        result['EngineVersion'] = self.engine_version
        result['PayType'] = self.pay_type
        result['ConnectionMode'] = self.connection_mode
        result['Tags'] = self.tags
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['DedicatedHostId'] = self.dedicated_host_id
        result['InstanceLevel'] = self.instance_level
        result['NeedVpcName'] = self.need_vpc_name
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.proxy_id = map.get('proxyId')
        self.engine = map.get('Engine')
        self.zone_id = map.get('ZoneId')
        self.resource_group_id = map.get('ResourceGroupId')
        self.dbinstance_status = map.get('DBInstanceStatus')
        self.expired = map.get('Expired')
        self.search_key = map.get('SearchKey')
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbinstance_type = map.get('DBInstanceType')
        self.region_id = map.get('RegionId')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.instance_network_type = map.get('InstanceNetworkType')
        self.vpc_id = map.get('VpcId')
        self.v_switch_id = map.get('VSwitchId')
        self.dbinstance_class = map.get('DBInstanceClass')
        self.engine_version = map.get('EngineVersion')
        self.pay_type = map.get('PayType')
        self.connection_mode = map.get('ConnectionMode')
        self.tags = map.get('Tags')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.dedicated_host_id = map.get('DedicatedHostId')
        self.instance_level = map.get('InstanceLevel')
        self.need_vpc_name = map.get('NeedVpcName')
        return self


class DescribeDBInstancesResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, total_record_count=None, page_record_count=None,
                 items=None):
        self.request_id = request_id    # type: str
        self.page_number = page_number  # type: int
        self.total_record_count = total_record_count  # type: int
        self.page_record_count = page_record_count  # type: int
        self.items = items              # type: DescribeDBInstancesResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.total_record_count, 'total_record_count')
        self.validate_required(self.page_record_count, 'page_record_count')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNumber'] = self.page_number
        result['TotalRecordCount'] = self.total_record_count
        result['PageRecordCount'] = self.page_record_count
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_number = map.get('PageNumber')
        self.total_record_count = map.get('TotalRecordCount')
        self.page_record_count = map.get('PageRecordCount')
        if map.get('Items') is not None:
            temp_model = DescribeDBInstancesResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeDBInstancesResponseItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeDBInstancesResponseItemsDBInstanceReadOnlyDBInstanceIds(TeaModel):
    def __init__(self, read_only_dbinstance_id=None):
        self.read_only_dbinstance_id = read_only_dbinstance_id  # type: List[DescribeDBInstancesResponseItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId]

    def validate(self):
        self.validate_required(self.read_only_dbinstance_id, 'read_only_dbinstance_id')
        if self.read_only_dbinstance_id:
            for k in self.read_only_dbinstance_id:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ReadOnlyDBInstanceId'] = []
        if self.read_only_dbinstance_id is not None:
            for k in self.read_only_dbinstance_id:
                result['ReadOnlyDBInstanceId'].append(k.to_map() if k else None)
        else:
            result['ReadOnlyDBInstanceId'] = None
        return result

    def from_map(self, map={}):
        self.read_only_dbinstance_id = []
        if map.get('ReadOnlyDBInstanceId') is not None:
            for k in map.get('ReadOnlyDBInstanceId'):
                temp_model = DescribeDBInstancesResponseItemsDBInstanceReadOnlyDBInstanceIdsReadOnlyDBInstanceId()
                self.read_only_dbinstance_id.append(temp_model.from_map(k))
        else:
            self.read_only_dbinstance_id = None
        return self


class DescribeDBInstancesResponseItemsDBInstance(TeaModel):
    def __init__(self, dbinstance_id=None, dbinstance_description=None, pay_type=None, dbinstance_type=None,
                 region_id=None, expire_time=None, destroy_time=None, dbinstance_status=None, engine=None,
                 dbinstance_net_type=None, connection_mode=None, lock_mode=None, category=None, dbinstance_storage_type=None,
                 dbinstance_class=None, instance_network_type=None, vpc_cloud_instance_id=None, lock_reason=None, zone_id=None,
                 mutri_orsignle=None, create_time=None, engine_version=None, guard_dbinstance_id=None, temp_dbinstance_id=None,
                 master_instance_id=None, vpc_id=None, v_switch_id=None, resource_group_id=None, auto_upgrade_minor_version=None,
                 dedicated_host_group_id=None, dedicated_host_id_for_master=None, dedicated_host_id_for_slave=None,
                 dedicated_host_id_for_log=None, dedicated_host_name_for_master=None, dedicated_host_name_for_slave=None,
                 dedicated_host_name_for_log=None, dedicated_host_zone_id_for_master=None, dedicated_host_zone_id_for_slave=None,
                 dedicated_host_zone_id_for_log=None, vpc_name=None, dedicated_host_group_name=None, read_only_dbinstance_ids=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.pay_type = pay_type        # type: str
        self.dbinstance_type = dbinstance_type  # type: str
        self.region_id = region_id      # type: str
        self.expire_time = expire_time  # type: str
        self.destroy_time = destroy_time  # type: str
        self.dbinstance_status = dbinstance_status  # type: str
        self.engine = engine            # type: str
        self.dbinstance_net_type = dbinstance_net_type  # type: str
        self.connection_mode = connection_mode  # type: str
        self.lock_mode = lock_mode      # type: str
        self.category = category        # type: str
        self.dbinstance_storage_type = dbinstance_storage_type  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.vpc_cloud_instance_id = vpc_cloud_instance_id  # type: str
        self.lock_reason = lock_reason  # type: str
        self.zone_id = zone_id          # type: str
        self.mutri_orsignle = mutri_orsignle  # type: bool
        self.create_time = create_time  # type: str
        self.engine_version = engine_version  # type: str
        self.guard_dbinstance_id = guard_dbinstance_id  # type: str
        self.temp_dbinstance_id = temp_dbinstance_id  # type: str
        self.master_instance_id = master_instance_id  # type: str
        self.vpc_id = vpc_id            # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.auto_upgrade_minor_version = auto_upgrade_minor_version  # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.dedicated_host_id_for_master = dedicated_host_id_for_master  # type: str
        self.dedicated_host_id_for_slave = dedicated_host_id_for_slave  # type: str
        self.dedicated_host_id_for_log = dedicated_host_id_for_log  # type: str
        self.dedicated_host_name_for_master = dedicated_host_name_for_master  # type: str
        self.dedicated_host_name_for_slave = dedicated_host_name_for_slave  # type: str
        self.dedicated_host_name_for_log = dedicated_host_name_for_log  # type: str
        self.dedicated_host_zone_id_for_master = dedicated_host_zone_id_for_master  # type: str
        self.dedicated_host_zone_id_for_slave = dedicated_host_zone_id_for_slave  # type: str
        self.dedicated_host_zone_id_for_log = dedicated_host_zone_id_for_log  # type: str
        self.vpc_name = vpc_name        # type: str
        self.dedicated_host_group_name = dedicated_host_group_name  # type: str
        self.read_only_dbinstance_ids = read_only_dbinstance_ids  # type: DescribeDBInstancesResponseItemsDBInstanceReadOnlyDBInstanceIds

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.dbinstance_description, 'dbinstance_description')
        self.validate_required(self.pay_type, 'pay_type')
        self.validate_required(self.dbinstance_type, 'dbinstance_type')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.destroy_time, 'destroy_time')
        self.validate_required(self.dbinstance_status, 'dbinstance_status')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.dbinstance_net_type, 'dbinstance_net_type')
        self.validate_required(self.connection_mode, 'connection_mode')
        self.validate_required(self.lock_mode, 'lock_mode')
        self.validate_required(self.category, 'category')
        self.validate_required(self.dbinstance_storage_type, 'dbinstance_storage_type')
        self.validate_required(self.dbinstance_class, 'dbinstance_class')
        self.validate_required(self.instance_network_type, 'instance_network_type')
        self.validate_required(self.vpc_cloud_instance_id, 'vpc_cloud_instance_id')
        self.validate_required(self.lock_reason, 'lock_reason')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.mutri_orsignle, 'mutri_orsignle')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.guard_dbinstance_id, 'guard_dbinstance_id')
        self.validate_required(self.temp_dbinstance_id, 'temp_dbinstance_id')
        self.validate_required(self.master_instance_id, 'master_instance_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.auto_upgrade_minor_version, 'auto_upgrade_minor_version')
        self.validate_required(self.dedicated_host_group_id, 'dedicated_host_group_id')
        self.validate_required(self.dedicated_host_id_for_master, 'dedicated_host_id_for_master')
        self.validate_required(self.dedicated_host_id_for_slave, 'dedicated_host_id_for_slave')
        self.validate_required(self.dedicated_host_id_for_log, 'dedicated_host_id_for_log')
        self.validate_required(self.dedicated_host_name_for_master, 'dedicated_host_name_for_master')
        self.validate_required(self.dedicated_host_name_for_slave, 'dedicated_host_name_for_slave')
        self.validate_required(self.dedicated_host_name_for_log, 'dedicated_host_name_for_log')
        self.validate_required(self.dedicated_host_zone_id_for_master, 'dedicated_host_zone_id_for_master')
        self.validate_required(self.dedicated_host_zone_id_for_slave, 'dedicated_host_zone_id_for_slave')
        self.validate_required(self.dedicated_host_zone_id_for_log, 'dedicated_host_zone_id_for_log')
        self.validate_required(self.vpc_name, 'vpc_name')
        self.validate_required(self.dedicated_host_group_name, 'dedicated_host_group_name')
        self.validate_required(self.read_only_dbinstance_ids, 'read_only_dbinstance_ids')
        if self.read_only_dbinstance_ids:
            self.read_only_dbinstance_ids.validate()

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['DBInstanceDescription'] = self.dbinstance_description
        result['PayType'] = self.pay_type
        result['DBInstanceType'] = self.dbinstance_type
        result['RegionId'] = self.region_id
        result['ExpireTime'] = self.expire_time
        result['DestroyTime'] = self.destroy_time
        result['DBInstanceStatus'] = self.dbinstance_status
        result['Engine'] = self.engine
        result['DBInstanceNetType'] = self.dbinstance_net_type
        result['ConnectionMode'] = self.connection_mode
        result['LockMode'] = self.lock_mode
        result['Category'] = self.category
        result['DBInstanceStorageType'] = self.dbinstance_storage_type
        result['DBInstanceClass'] = self.dbinstance_class
        result['InstanceNetworkType'] = self.instance_network_type
        result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        result['LockReason'] = self.lock_reason
        result['ZoneId'] = self.zone_id
        result['MutriORsignle'] = self.mutri_orsignle
        result['CreateTime'] = self.create_time
        result['EngineVersion'] = self.engine_version
        result['GuardDBInstanceId'] = self.guard_dbinstance_id
        result['TempDBInstanceId'] = self.temp_dbinstance_id
        result['MasterInstanceId'] = self.master_instance_id
        result['VpcId'] = self.vpc_id
        result['VSwitchId'] = self.v_switch_id
        result['ResourceGroupId'] = self.resource_group_id
        result['AutoUpgradeMinorVersion'] = self.auto_upgrade_minor_version
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['DedicatedHostIdForMaster'] = self.dedicated_host_id_for_master
        result['DedicatedHostIdForSlave'] = self.dedicated_host_id_for_slave
        result['DedicatedHostIdForLog'] = self.dedicated_host_id_for_log
        result['DedicatedHostNameForMaster'] = self.dedicated_host_name_for_master
        result['DedicatedHostNameForSlave'] = self.dedicated_host_name_for_slave
        result['DedicatedHostNameForLog'] = self.dedicated_host_name_for_log
        result['DedicatedHostZoneIdForMaster'] = self.dedicated_host_zone_id_for_master
        result['DedicatedHostZoneIdForSlave'] = self.dedicated_host_zone_id_for_slave
        result['DedicatedHostZoneIdForLog'] = self.dedicated_host_zone_id_for_log
        result['VpcName'] = self.vpc_name
        result['DedicatedHostGroupName'] = self.dedicated_host_group_name
        if self.read_only_dbinstance_ids is not None:
            result['ReadOnlyDBInstanceIds'] = self.read_only_dbinstance_ids.to_map()
        else:
            result['ReadOnlyDBInstanceIds'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.dbinstance_description = map.get('DBInstanceDescription')
        self.pay_type = map.get('PayType')
        self.dbinstance_type = map.get('DBInstanceType')
        self.region_id = map.get('RegionId')
        self.expire_time = map.get('ExpireTime')
        self.destroy_time = map.get('DestroyTime')
        self.dbinstance_status = map.get('DBInstanceStatus')
        self.engine = map.get('Engine')
        self.dbinstance_net_type = map.get('DBInstanceNetType')
        self.connection_mode = map.get('ConnectionMode')
        self.lock_mode = map.get('LockMode')
        self.category = map.get('Category')
        self.dbinstance_storage_type = map.get('DBInstanceStorageType')
        self.dbinstance_class = map.get('DBInstanceClass')
        self.instance_network_type = map.get('InstanceNetworkType')
        self.vpc_cloud_instance_id = map.get('VpcCloudInstanceId')
        self.lock_reason = map.get('LockReason')
        self.zone_id = map.get('ZoneId')
        self.mutri_orsignle = map.get('MutriORsignle')
        self.create_time = map.get('CreateTime')
        self.engine_version = map.get('EngineVersion')
        self.guard_dbinstance_id = map.get('GuardDBInstanceId')
        self.temp_dbinstance_id = map.get('TempDBInstanceId')
        self.master_instance_id = map.get('MasterInstanceId')
        self.vpc_id = map.get('VpcId')
        self.v_switch_id = map.get('VSwitchId')
        self.resource_group_id = map.get('ResourceGroupId')
        self.auto_upgrade_minor_version = map.get('AutoUpgradeMinorVersion')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.dedicated_host_id_for_master = map.get('DedicatedHostIdForMaster')
        self.dedicated_host_id_for_slave = map.get('DedicatedHostIdForSlave')
        self.dedicated_host_id_for_log = map.get('DedicatedHostIdForLog')
        self.dedicated_host_name_for_master = map.get('DedicatedHostNameForMaster')
        self.dedicated_host_name_for_slave = map.get('DedicatedHostNameForSlave')
        self.dedicated_host_name_for_log = map.get('DedicatedHostNameForLog')
        self.dedicated_host_zone_id_for_master = map.get('DedicatedHostZoneIdForMaster')
        self.dedicated_host_zone_id_for_slave = map.get('DedicatedHostZoneIdForSlave')
        self.dedicated_host_zone_id_for_log = map.get('DedicatedHostZoneIdForLog')
        self.vpc_name = map.get('VpcName')
        self.dedicated_host_group_name = map.get('DedicatedHostGroupName')
        if map.get('ReadOnlyDBInstanceIds') is not None:
            temp_model = DescribeDBInstancesResponseItemsDBInstanceReadOnlyDBInstanceIds()
            self.read_only_dbinstance_ids = temp_model.from_map(map['ReadOnlyDBInstanceIds'])
        else:
            self.read_only_dbinstance_ids = None
        return self


class DescribeDBInstancesResponseItems(TeaModel):
    def __init__(self, dbinstance=None):
        self.dbinstance = dbinstance    # type: List[DescribeDBInstancesResponseItemsDBInstance]

    def validate(self):
        self.validate_required(self.dbinstance, 'dbinstance')
        if self.dbinstance:
            for k in self.dbinstance:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DBInstance'] = []
        if self.dbinstance is not None:
            for k in self.dbinstance:
                result['DBInstance'].append(k.to_map() if k else None)
        else:
            result['DBInstance'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance = []
        if map.get('DBInstance') is not None:
            for k in map.get('DBInstance'):
                temp_model = DescribeDBInstancesResponseItemsDBInstance()
                self.dbinstance.append(temp_model.from_map(k))
        else:
            self.dbinstance = None
        return self


class DescribeDBInstanceAttributeRequest(TeaModel):
    def __init__(self, dbinstance_id=None, expired=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.expired = expired          # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['Expired'] = self.expired
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.expired = map.get('Expired')
        return self


class DescribeDBInstanceAttributeResponse(TeaModel):
    def __init__(self, request_id=None, items=None):
        self.request_id = request_id    # type: str
        self.items = items              # type: DescribeDBInstanceAttributeResponseItems

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.items, 'items')
        if self.items:
            self.items.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.items is not None:
            result['Items'] = self.items.to_map()
        else:
            result['Items'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Items') is not None:
            temp_model = DescribeDBInstanceAttributeResponseItems()
            self.items = temp_model.from_map(map['Items'])
        else:
            self.items = None
        return self


class DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeSlaveZonesSlaveZone(TeaModel):
    def __init__(self, zone_id=None):
        self.zone_id = zone_id          # type: str

    def validate(self):
        self.validate_required(self.zone_id, 'zone_id')

    def to_map(self):
        result = {}
        result['ZoneId'] = self.zone_id
        return result

    def from_map(self, map={}):
        self.zone_id = map.get('ZoneId')
        return self


class DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeSlaveZones(TeaModel):
    def __init__(self, slave_zone=None):
        self.slave_zone = slave_zone    # type: List[DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeSlaveZonesSlaveZone]

    def validate(self):
        self.validate_required(self.slave_zone, 'slave_zone')
        if self.slave_zone:
            for k in self.slave_zone:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SlaveZone'] = []
        if self.slave_zone is not None:
            for k in self.slave_zone:
                result['SlaveZone'].append(k.to_map() if k else None)
        else:
            result['SlaveZone'] = None
        return result

    def from_map(self, map={}):
        self.slave_zone = []
        if map.get('SlaveZone') is not None:
            for k in map.get('SlaveZone'):
                temp_model = DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeSlaveZonesSlaveZone()
                self.slave_zone.append(temp_model.from_map(k))
        else:
            self.slave_zone = None
        return self


class DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeReadOnlyDBInstanceIdsReadOnlyDBInstanceId(TeaModel):
    def __init__(self, dbinstance_id=None):
        self.dbinstance_id = dbinstance_id  # type: str

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeReadOnlyDBInstanceIds(TeaModel):
    def __init__(self, read_only_dbinstance_id=None):
        self.read_only_dbinstance_id = read_only_dbinstance_id  # type: List[DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeReadOnlyDBInstanceIdsReadOnlyDBInstanceId]

    def validate(self):
        self.validate_required(self.read_only_dbinstance_id, 'read_only_dbinstance_id')
        if self.read_only_dbinstance_id:
            for k in self.read_only_dbinstance_id:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ReadOnlyDBInstanceId'] = []
        if self.read_only_dbinstance_id is not None:
            for k in self.read_only_dbinstance_id:
                result['ReadOnlyDBInstanceId'].append(k.to_map() if k else None)
        else:
            result['ReadOnlyDBInstanceId'] = None
        return result

    def from_map(self, map={}):
        self.read_only_dbinstance_id = []
        if map.get('ReadOnlyDBInstanceId') is not None:
            for k in map.get('ReadOnlyDBInstanceId'):
                temp_model = DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeReadOnlyDBInstanceIdsReadOnlyDBInstanceId()
                self.read_only_dbinstance_id.append(temp_model.from_map(k))
        else:
            self.read_only_dbinstance_id = None
        return self


class DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeExtraDBInstanceIds(TeaModel):
    def __init__(self, dbinstance_id=None):
        # DBInstanceId
        self.dbinstance_id = dbinstance_id  # type: List[str]

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        return self


class DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeExtra(TeaModel):
    def __init__(self, dbinstance_ids=None):
        self.dbinstance_ids = dbinstance_ids  # type: DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeExtraDBInstanceIds

    def validate(self):
        self.validate_required(self.dbinstance_ids, 'dbinstance_ids')
        if self.dbinstance_ids:
            self.dbinstance_ids.validate()

    def to_map(self):
        result = {}
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids.to_map()
        else:
            result['DBInstanceIds'] = None
        return result

    def from_map(self, map={}):
        if map.get('DBInstanceIds') is not None:
            temp_model = DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeExtraDBInstanceIds()
            self.dbinstance_ids = temp_model.from_map(map['DBInstanceIds'])
        else:
            self.dbinstance_ids = None
        return self


class DescribeDBInstanceAttributeResponseItemsDBInstanceAttribute(TeaModel):
    def __init__(self, dbinstance_id=None, pay_type=None, dbinstance_class_type=None, dbinstance_type=None,
                 region_id=None, connection_string=None, port=None, engine=None, engine_version=None, dbinstance_class=None,
                 dbinstance_memory=None, dbinstance_storage=None, vpc_cloud_instance_id=None, dbinstance_net_type=None,
                 dbinstance_status=None, dbinstance_description=None, lock_mode=None, lock_reason=None, dbmax_quantity=None,
                 account_max_quantity=None, creation_time=None, expire_time=None, maintain_time=None, availability_value=None,
                 max_iops=None, max_connections=None, master_instance_id=None, dbinstance_cpu=None,
                 increment_source_dbinstance_id=None, guard_dbinstance_id=None, temp_dbinstance_id=None, zone_id=None, instance_network_type=None,
                 dbinstance_storage_type=None, advanced_features=None, category=None, vpc_id=None, v_switch_id=None, connection_mode=None,
                 current_kernel_version=None, resource_group_id=None, readonly_instance_sqldelayed_time=None, security_ipmode=None,
                 time_zone=None, collation=None, master_zone=None, auto_upgrade_minor_version=None, proxy_type=None,
                 console_version=None, dedicated_host_group_id=None, super_permission_mode=None, slave_zones=None,
                 read_only_dbinstance_ids=None, extra=None):
        self.dbinstance_id = dbinstance_id  # type: str
        self.pay_type = pay_type        # type: str
        self.dbinstance_class_type = dbinstance_class_type  # type: str
        self.dbinstance_type = dbinstance_type  # type: str
        self.region_id = region_id      # type: str
        self.connection_string = connection_string  # type: str
        self.port = port                # type: str
        self.engine = engine            # type: str
        self.engine_version = engine_version  # type: str
        self.dbinstance_class = dbinstance_class  # type: str
        self.dbinstance_memory = dbinstance_memory  # type: int
        self.dbinstance_storage = dbinstance_storage  # type: int
        self.vpc_cloud_instance_id = vpc_cloud_instance_id  # type: str
        self.dbinstance_net_type = dbinstance_net_type  # type: str
        self.dbinstance_status = dbinstance_status  # type: str
        self.dbinstance_description = dbinstance_description  # type: str
        self.lock_mode = lock_mode      # type: str
        self.lock_reason = lock_reason  # type: str
        self.dbmax_quantity = dbmax_quantity  # type: int
        self.account_max_quantity = account_max_quantity  # type: int
        self.creation_time = creation_time  # type: str
        self.expire_time = expire_time  # type: str
        self.maintain_time = maintain_time  # type: str
        self.availability_value = availability_value  # type: str
        self.max_iops = max_iops        # type: int
        self.max_connections = max_connections  # type: int
        self.master_instance_id = master_instance_id  # type: str
        self.dbinstance_cpu = dbinstance_cpu  # type: str
        self.increment_source_dbinstance_id = increment_source_dbinstance_id  # type: str
        self.guard_dbinstance_id = guard_dbinstance_id  # type: str
        self.temp_dbinstance_id = temp_dbinstance_id  # type: str
        self.zone_id = zone_id          # type: str
        self.instance_network_type = instance_network_type  # type: str
        self.dbinstance_storage_type = dbinstance_storage_type  # type: str
        self.advanced_features = advanced_features  # type: str
        self.category = category        # type: str
        self.vpc_id = vpc_id            # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.connection_mode = connection_mode  # type: str
        self.current_kernel_version = current_kernel_version  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.readonly_instance_sqldelayed_time = readonly_instance_sqldelayed_time  # type: str
        self.security_ipmode = security_ipmode  # type: str
        self.time_zone = time_zone      # type: str
        self.collation = collation      # type: str
        self.master_zone = master_zone  # type: str
        self.auto_upgrade_minor_version = auto_upgrade_minor_version  # type: str
        self.proxy_type = proxy_type    # type: int
        self.console_version = console_version  # type: str
        self.dedicated_host_group_id = dedicated_host_group_id  # type: str
        self.super_permission_mode = super_permission_mode  # type: str
        self.slave_zones = slave_zones  # type: DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeSlaveZones
        self.read_only_dbinstance_ids = read_only_dbinstance_ids  # type: DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeReadOnlyDBInstanceIds
        self.extra = extra              # type: DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeExtra

    def validate(self):
        self.validate_required(self.dbinstance_id, 'dbinstance_id')
        self.validate_required(self.pay_type, 'pay_type')
        self.validate_required(self.dbinstance_class_type, 'dbinstance_class_type')
        self.validate_required(self.dbinstance_type, 'dbinstance_type')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.connection_string, 'connection_string')
        self.validate_required(self.port, 'port')
        self.validate_required(self.engine, 'engine')
        self.validate_required(self.engine_version, 'engine_version')
        self.validate_required(self.dbinstance_class, 'dbinstance_class')
        self.validate_required(self.dbinstance_memory, 'dbinstance_memory')
        self.validate_required(self.dbinstance_storage, 'dbinstance_storage')
        self.validate_required(self.vpc_cloud_instance_id, 'vpc_cloud_instance_id')
        self.validate_required(self.dbinstance_net_type, 'dbinstance_net_type')
        self.validate_required(self.dbinstance_status, 'dbinstance_status')
        self.validate_required(self.dbinstance_description, 'dbinstance_description')
        self.validate_required(self.lock_mode, 'lock_mode')
        self.validate_required(self.lock_reason, 'lock_reason')
        self.validate_required(self.dbmax_quantity, 'dbmax_quantity')
        self.validate_required(self.account_max_quantity, 'account_max_quantity')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.maintain_time, 'maintain_time')
        self.validate_required(self.availability_value, 'availability_value')
        self.validate_required(self.max_iops, 'max_iops')
        self.validate_required(self.max_connections, 'max_connections')
        self.validate_required(self.master_instance_id, 'master_instance_id')
        self.validate_required(self.dbinstance_cpu, 'dbinstance_cpu')
        self.validate_required(self.increment_source_dbinstance_id, 'increment_source_dbinstance_id')
        self.validate_required(self.guard_dbinstance_id, 'guard_dbinstance_id')
        self.validate_required(self.temp_dbinstance_id, 'temp_dbinstance_id')
        self.validate_required(self.zone_id, 'zone_id')
        self.validate_required(self.instance_network_type, 'instance_network_type')
        self.validate_required(self.dbinstance_storage_type, 'dbinstance_storage_type')
        self.validate_required(self.advanced_features, 'advanced_features')
        self.validate_required(self.category, 'category')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.connection_mode, 'connection_mode')
        self.validate_required(self.current_kernel_version, 'current_kernel_version')
        self.validate_required(self.resource_group_id, 'resource_group_id')
        self.validate_required(self.readonly_instance_sqldelayed_time, 'readonly_instance_sqldelayed_time')
        self.validate_required(self.security_ipmode, 'security_ipmode')
        self.validate_required(self.time_zone, 'time_zone')
        self.validate_required(self.collation, 'collation')
        self.validate_required(self.master_zone, 'master_zone')
        self.validate_required(self.auto_upgrade_minor_version, 'auto_upgrade_minor_version')
        self.validate_required(self.proxy_type, 'proxy_type')
        self.validate_required(self.console_version, 'console_version')
        self.validate_required(self.dedicated_host_group_id, 'dedicated_host_group_id')
        self.validate_required(self.super_permission_mode, 'super_permission_mode')
        self.validate_required(self.slave_zones, 'slave_zones')
        if self.slave_zones:
            self.slave_zones.validate()
        self.validate_required(self.read_only_dbinstance_ids, 'read_only_dbinstance_ids')
        if self.read_only_dbinstance_ids:
            self.read_only_dbinstance_ids.validate()
        self.validate_required(self.extra, 'extra')
        if self.extra:
            self.extra.validate()

    def to_map(self):
        result = {}
        result['DBInstanceId'] = self.dbinstance_id
        result['PayType'] = self.pay_type
        result['DBInstanceClassType'] = self.dbinstance_class_type
        result['DBInstanceType'] = self.dbinstance_type
        result['RegionId'] = self.region_id
        result['ConnectionString'] = self.connection_string
        result['Port'] = self.port
        result['Engine'] = self.engine
        result['EngineVersion'] = self.engine_version
        result['DBInstanceClass'] = self.dbinstance_class
        result['DBInstanceMemory'] = self.dbinstance_memory
        result['DBInstanceStorage'] = self.dbinstance_storage
        result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        result['DBInstanceNetType'] = self.dbinstance_net_type
        result['DBInstanceStatus'] = self.dbinstance_status
        result['DBInstanceDescription'] = self.dbinstance_description
        result['LockMode'] = self.lock_mode
        result['LockReason'] = self.lock_reason
        result['DBMaxQuantity'] = self.dbmax_quantity
        result['AccountMaxQuantity'] = self.account_max_quantity
        result['CreationTime'] = self.creation_time
        result['ExpireTime'] = self.expire_time
        result['MaintainTime'] = self.maintain_time
        result['AvailabilityValue'] = self.availability_value
        result['MaxIOPS'] = self.max_iops
        result['MaxConnections'] = self.max_connections
        result['MasterInstanceId'] = self.master_instance_id
        result['DBInstanceCPU'] = self.dbinstance_cpu
        result['IncrementSourceDBInstanceId'] = self.increment_source_dbinstance_id
        result['GuardDBInstanceId'] = self.guard_dbinstance_id
        result['TempDBInstanceId'] = self.temp_dbinstance_id
        result['ZoneId'] = self.zone_id
        result['InstanceNetworkType'] = self.instance_network_type
        result['DBInstanceStorageType'] = self.dbinstance_storage_type
        result['AdvancedFeatures'] = self.advanced_features
        result['Category'] = self.category
        result['VpcId'] = self.vpc_id
        result['VSwitchId'] = self.v_switch_id
        result['ConnectionMode'] = self.connection_mode
        result['CurrentKernelVersion'] = self.current_kernel_version
        result['ResourceGroupId'] = self.resource_group_id
        result['ReadonlyInstanceSQLDelayedTime'] = self.readonly_instance_sqldelayed_time
        result['SecurityIPMode'] = self.security_ipmode
        result['TimeZone'] = self.time_zone
        result['Collation'] = self.collation
        result['MasterZone'] = self.master_zone
        result['AutoUpgradeMinorVersion'] = self.auto_upgrade_minor_version
        result['ProxyType'] = self.proxy_type
        result['ConsoleVersion'] = self.console_version
        result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['SuperPermissionMode'] = self.super_permission_mode
        if self.slave_zones is not None:
            result['SlaveZones'] = self.slave_zones.to_map()
        else:
            result['SlaveZones'] = None
        if self.read_only_dbinstance_ids is not None:
            result['ReadOnlyDBInstanceIds'] = self.read_only_dbinstance_ids.to_map()
        else:
            result['ReadOnlyDBInstanceIds'] = None
        if self.extra is not None:
            result['Extra'] = self.extra.to_map()
        else:
            result['Extra'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_id = map.get('DBInstanceId')
        self.pay_type = map.get('PayType')
        self.dbinstance_class_type = map.get('DBInstanceClassType')
        self.dbinstance_type = map.get('DBInstanceType')
        self.region_id = map.get('RegionId')
        self.connection_string = map.get('ConnectionString')
        self.port = map.get('Port')
        self.engine = map.get('Engine')
        self.engine_version = map.get('EngineVersion')
        self.dbinstance_class = map.get('DBInstanceClass')
        self.dbinstance_memory = map.get('DBInstanceMemory')
        self.dbinstance_storage = map.get('DBInstanceStorage')
        self.vpc_cloud_instance_id = map.get('VpcCloudInstanceId')
        self.dbinstance_net_type = map.get('DBInstanceNetType')
        self.dbinstance_status = map.get('DBInstanceStatus')
        self.dbinstance_description = map.get('DBInstanceDescription')
        self.lock_mode = map.get('LockMode')
        self.lock_reason = map.get('LockReason')
        self.dbmax_quantity = map.get('DBMaxQuantity')
        self.account_max_quantity = map.get('AccountMaxQuantity')
        self.creation_time = map.get('CreationTime')
        self.expire_time = map.get('ExpireTime')
        self.maintain_time = map.get('MaintainTime')
        self.availability_value = map.get('AvailabilityValue')
        self.max_iops = map.get('MaxIOPS')
        self.max_connections = map.get('MaxConnections')
        self.master_instance_id = map.get('MasterInstanceId')
        self.dbinstance_cpu = map.get('DBInstanceCPU')
        self.increment_source_dbinstance_id = map.get('IncrementSourceDBInstanceId')
        self.guard_dbinstance_id = map.get('GuardDBInstanceId')
        self.temp_dbinstance_id = map.get('TempDBInstanceId')
        self.zone_id = map.get('ZoneId')
        self.instance_network_type = map.get('InstanceNetworkType')
        self.dbinstance_storage_type = map.get('DBInstanceStorageType')
        self.advanced_features = map.get('AdvancedFeatures')
        self.category = map.get('Category')
        self.vpc_id = map.get('VpcId')
        self.v_switch_id = map.get('VSwitchId')
        self.connection_mode = map.get('ConnectionMode')
        self.current_kernel_version = map.get('CurrentKernelVersion')
        self.resource_group_id = map.get('ResourceGroupId')
        self.readonly_instance_sqldelayed_time = map.get('ReadonlyInstanceSQLDelayedTime')
        self.security_ipmode = map.get('SecurityIPMode')
        self.time_zone = map.get('TimeZone')
        self.collation = map.get('Collation')
        self.master_zone = map.get('MasterZone')
        self.auto_upgrade_minor_version = map.get('AutoUpgradeMinorVersion')
        self.proxy_type = map.get('ProxyType')
        self.console_version = map.get('ConsoleVersion')
        self.dedicated_host_group_id = map.get('DedicatedHostGroupId')
        self.super_permission_mode = map.get('SuperPermissionMode')
        if map.get('SlaveZones') is not None:
            temp_model = DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeSlaveZones()
            self.slave_zones = temp_model.from_map(map['SlaveZones'])
        else:
            self.slave_zones = None
        if map.get('ReadOnlyDBInstanceIds') is not None:
            temp_model = DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeReadOnlyDBInstanceIds()
            self.read_only_dbinstance_ids = temp_model.from_map(map['ReadOnlyDBInstanceIds'])
        else:
            self.read_only_dbinstance_ids = None
        if map.get('Extra') is not None:
            temp_model = DescribeDBInstanceAttributeResponseItemsDBInstanceAttributeExtra()
            self.extra = temp_model.from_map(map['Extra'])
        else:
            self.extra = None
        return self


class DescribeDBInstanceAttributeResponseItems(TeaModel):
    def __init__(self, dbinstance_attribute=None):
        self.dbinstance_attribute = dbinstance_attribute  # type: List[DescribeDBInstanceAttributeResponseItemsDBInstanceAttribute]

    def validate(self):
        self.validate_required(self.dbinstance_attribute, 'dbinstance_attribute')
        if self.dbinstance_attribute:
            for k in self.dbinstance_attribute:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DBInstanceAttribute'] = []
        if self.dbinstance_attribute is not None:
            for k in self.dbinstance_attribute:
                result['DBInstanceAttribute'].append(k.to_map() if k else None)
        else:
            result['DBInstanceAttribute'] = None
        return result

    def from_map(self, map={}):
        self.dbinstance_attribute = []
        if map.get('DBInstanceAttribute') is not None:
            for k in map.get('DBInstanceAttribute'):
                temp_model = DescribeDBInstanceAttributeResponseItemsDBInstanceAttribute()
                self.dbinstance_attribute.append(temp_model.from_map(k))
        else:
            self.dbinstance_attribute = None
        return self


