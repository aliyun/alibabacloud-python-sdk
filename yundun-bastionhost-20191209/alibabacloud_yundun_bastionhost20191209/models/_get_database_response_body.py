# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GetDatabaseResponseBody(DaraModel):
    def __init__(
        self,
        database: main_models.GetDatabaseResponseBodyDatabase = None,
        request_id: str = None,
    ):
        # The returned detailed information about the database.
        self.database = database
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.database:
            self.database.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database is not None:
            result['Database'] = self.database.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            temp_model = main_models.GetDatabaseResponseBodyDatabase()
            self.database = temp_model.from_map(m.get('Database'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDatabaseResponseBodyDatabase(DaraModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        database_id: str = None,
        database_name: str = None,
        database_port: int = None,
        database_private_address: str = None,
        database_public_address: str = None,
        database_type: str = None,
        network_domain_id: str = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_region_id: str = None,
        source_instance_state: str = None,
    ):
        # The address type of the database. Valid values:
        # 
        # *   Public
        # *   Private
        self.active_address_type = active_address_type
        # The remarks of the database.
        self.comment = comment
        # The database ID.
        self.database_id = database_id
        # The name of the database.
        self.database_name = database_name
        # The port of the database.
        self.database_port = database_port
        # The internal endpoint of the database.
        self.database_private_address = database_private_address
        # The public endpoint of the database.
        self.database_public_address = database_public_address
        # The database engine. Valid values:
        # 
        # *   **mysql**
        # *   **sqlserver**
        # *   **postgresql**
        # *   **oracle**
        self.database_type = database_type
        # The ID of the network domain to which the database belongs.
        self.network_domain_id = network_domain_id
        # The database type. Valid values:
        # 
        # *   **Local**: on-premises database.
        # *   **Rds**: ApsaraDB RDS instance.
        # *   **PolarDB**: PolarDB cluster.
        self.source = source
        # The ID of the ApsaraDB RDS instance or PolarDB cluster.
        # 
        # > If **Source** is set to **Local**, this parameter is empty.
        self.source_instance_id = source_instance_id
        # The region ID of the ApsaraDB RDS instance or PolarDB cluster.
        self.source_instance_region_id = source_instance_region_id
        # The status of the database. Valid values:
        # 
        # *   **Normal**
        # *   **Release**
        self.source_instance_state = source_instance_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.database_port is not None:
            result['DatabasePort'] = self.database_port

        if self.database_private_address is not None:
            result['DatabasePrivateAddress'] = self.database_private_address

        if self.database_public_address is not None:
            result['DatabasePublicAddress'] = self.database_public_address

        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id

        if self.source is not None:
            result['Source'] = self.source

        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        if self.source_instance_region_id is not None:
            result['SourceInstanceRegionId'] = self.source_instance_region_id

        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DatabasePort') is not None:
            self.database_port = m.get('DatabasePort')

        if m.get('DatabasePrivateAddress') is not None:
            self.database_private_address = m.get('DatabasePrivateAddress')

        if m.get('DatabasePublicAddress') is not None:
            self.database_public_address = m.get('DatabasePublicAddress')

        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        if m.get('SourceInstanceRegionId') is not None:
            self.source_instance_region_id = m.get('SourceInstanceRegionId')

        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')

        return self

