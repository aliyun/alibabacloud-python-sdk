# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class AddConnectorRequest(DaraModel):
    def __init__(
        self,
        connector_name: str = None,
        connector_type: str = None,
        description: str = None,
        file_connector_config: main_models.AddConnectorRequestFileConnectorConfig = None,
    ):
        # The name of the connector.
        # 
        # This parameter is required.
        self.connector_name = connector_name
        # The type of the connector.
        # 
        # This parameter is required.
        self.connector_type = connector_type
        # The description for the connector.
        # 
        # This parameter is required.
        self.description = description
        # The parameters for the file connector.
        self.file_connector_config = file_connector_config

    def validate(self):
        if self.file_connector_config:
            self.file_connector_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_name is not None:
            result['ConnectorName'] = self.connector_name

        if self.connector_type is not None:
            result['ConnectorType'] = self.connector_type

        if self.description is not None:
            result['Description'] = self.description

        if self.file_connector_config is not None:
            result['FileConnectorConfig'] = self.file_connector_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorName') is not None:
            self.connector_name = m.get('ConnectorName')

        if m.get('ConnectorType') is not None:
            self.connector_type = m.get('ConnectorType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileConnectorConfig') is not None:
            temp_model = main_models.AddConnectorRequestFileConnectorConfig()
            self.file_connector_config = temp_model.from_map(m.get('FileConnectorConfig'))

        return self

class AddConnectorRequestFileConnectorConfig(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        region_id: str = None,
        storage_type: str = None,
    ):
        # The name of the bucket.
        self.bucket_name = bucket_name
        # The region of the bucket.
        self.region_id = region_id
        # The file storage location. Valid values:<br>`OSS_CUSTOM`: Use your own Object Storage Service (OSS) bucket.<br>`OSS_PLATFORM`: Use the platform-provided OSS bucket.<br><br>
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

