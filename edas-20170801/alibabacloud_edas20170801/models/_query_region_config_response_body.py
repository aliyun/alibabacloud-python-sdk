# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class QueryRegionConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        region_config: main_models.QueryRegionConfigResponseBodyRegionConfig = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The additional information that is returned.
        self.message = message
        # The information about region configurations.
        self.region_config = region_config
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.region_config:
            self.region_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.region_config is not None:
            result['RegionConfig'] = self.region_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RegionConfig') is not None:
            temp_model = main_models.QueryRegionConfigResponseBodyRegionConfig()
            self.region_config = temp_model.from_map(m.get('RegionConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryRegionConfigResponseBodyRegionConfig(DaraModel):
    def __init__(
        self,
        address_server_host: str = None,
        agent_install_script: str = None,
        file_server_config: main_models.QueryRegionConfigResponseBodyRegionConfigFileServerConfig = None,
        file_server_type: str = None,
        id: str = None,
        image_id: str = None,
        name: str = None,
        no: int = None,
        tag: str = None,
    ):
        # The domain name of Address Server.
        self.address_server_host = address_server_host
        # The installation path of the script for EDAS Agent.
        self.agent_install_script = agent_install_script
        # The information about the file server.
        self.file_server_config = file_server_config
        # The type of the file server.
        self.file_server_type = file_server_type
        # The configured ID of the region.
        self.id = id
        # The ID of the official image.
        self.image_id = image_id
        # The configured name of the region.
        self.name = name
        # The serial number of the region. This parameter is deprecated.
        self.no = no
        # The tag of the region. The value is fixed to `ALIYUN_SHARE`.
        self.tag = tag

    def validate(self):
        if self.file_server_config:
            self.file_server_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_server_host is not None:
            result['AddressServerHost'] = self.address_server_host

        if self.agent_install_script is not None:
            result['AgentInstallScript'] = self.agent_install_script

        if self.file_server_config is not None:
            result['FileServerConfig'] = self.file_server_config.to_map()

        if self.file_server_type is not None:
            result['FileServerType'] = self.file_server_type

        if self.id is not None:
            result['Id'] = self.id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.name is not None:
            result['Name'] = self.name

        if self.no is not None:
            result['No'] = self.no

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressServerHost') is not None:
            self.address_server_host = m.get('AddressServerHost')

        if m.get('AgentInstallScript') is not None:
            self.agent_install_script = m.get('AgentInstallScript')

        if m.get('FileServerConfig') is not None:
            temp_model = main_models.QueryRegionConfigResponseBodyRegionConfigFileServerConfig()
            self.file_server_config = temp_model.from_map(m.get('FileServerConfig'))

        if m.get('FileServerType') is not None:
            self.file_server_type = m.get('FileServerType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('No') is not None:
            self.no = m.get('No')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

class QueryRegionConfigResponseBodyRegionConfigFileServerConfig(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        internal_url: str = None,
        public_url: str = None,
        vpc_url: str = None,
    ):
        # The Object Storage Service (OSS) bucket of the file server.
        self.bucket = bucket
        # The internal endpoint of the file server.
        self.internal_url = internal_url
        # The public endpoint of the file server.
        self.public_url = public_url
        # The virtual private cloud (VPC) endpoint of the file server.
        self.vpc_url = vpc_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.internal_url is not None:
            result['InternalUrl'] = self.internal_url

        if self.public_url is not None:
            result['PublicUrl'] = self.public_url

        if self.vpc_url is not None:
            result['VpcUrl'] = self.vpc_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('InternalUrl') is not None:
            self.internal_url = m.get('InternalUrl')

        if m.get('PublicUrl') is not None:
            self.public_url = m.get('PublicUrl')

        if m.get('VpcUrl') is not None:
            self.vpc_url = m.get('VpcUrl')

        return self

