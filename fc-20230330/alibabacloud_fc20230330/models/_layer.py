# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class Layer(DaraModel):
    def __init__(
        self,
        acl: str = None,
        code: main_models.OutputCodeLocation = None,
        code_checksum: str = None,
        code_size: int = None,
        compatible_runtime: List[str] = None,
        create_time: str = None,
        description: str = None,
        layer_name: str = None,
        layer_version_arn: str = None,
        license: str = None,
        version: int = None,
    ):
        # The permission of the layer. Valid value: 0 and 1. 0 specifies that the layer is private, and 1 specifies that the layer is public. By default, public layers are public. Custom layers can be set to private or public.
        self.acl = acl
        # The information about the code package of the layer.
        self.code = code
        # The crc64 verification code of the layer code package, which is calculated based on ECMA-182.
        self.code_checksum = code_checksum
        # The size of the layer code package. Unit: bytes.
        self.code_size = code_size
        # The runtimes that are supported by the layer.
        self.compatible_runtime = compatible_runtime
        # The time when the layer version was created.
        self.create_time = create_time
        # The description of the layer version.
        self.description = description
        # The name of the layer.
        # 
        # This parameter is required.
        self.layer_name = layer_name
        # The name of the resource in the layer version. The name is in the acs:fc:{region}:{accountID}:layers/{layerName}/versions/{layerVersion} format.
        self.layer_version_arn = layer_version_arn
        # The license agreement.
        self.license = license
        # The layer version.
        self.version = version

    def validate(self):
        if self.code:
            self.code.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl is not None:
            result['acl'] = self.acl

        if self.code is not None:
            result['code'] = self.code.to_map()

        if self.code_checksum is not None:
            result['codeChecksum'] = self.code_checksum

        if self.code_size is not None:
            result['codeSize'] = self.code_size

        if self.compatible_runtime is not None:
            result['compatibleRuntime'] = self.compatible_runtime

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.layer_name is not None:
            result['layerName'] = self.layer_name

        if self.layer_version_arn is not None:
            result['layerVersionArn'] = self.layer_version_arn

        if self.license is not None:
            result['license'] = self.license

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')

        if m.get('code') is not None:
            temp_model = main_models.OutputCodeLocation()
            self.code = temp_model.from_map(m.get('code'))

        if m.get('codeChecksum') is not None:
            self.code_checksum = m.get('codeChecksum')

        if m.get('codeSize') is not None:
            self.code_size = m.get('codeSize')

        if m.get('compatibleRuntime') is not None:
            self.compatible_runtime = m.get('compatibleRuntime')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('layerName') is not None:
            self.layer_name = m.get('layerName')

        if m.get('layerVersionArn') is not None:
            self.layer_version_arn = m.get('layerVersionArn')

        if m.get('license') is not None:
            self.license = m.get('license')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

