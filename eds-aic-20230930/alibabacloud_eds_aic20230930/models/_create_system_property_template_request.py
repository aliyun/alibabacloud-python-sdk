# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class CreateSystemPropertyTemplateRequest(DaraModel):
    def __init__(
        self,
        enable_auto: bool = None,
        file_path: str = None,
        system_property_info: main_models.CreateSystemPropertyTemplateRequestSystemPropertyInfo = None,
        template_name: str = None,
    ):
        # Specifies whether to automatically generate preset system properties.
        self.enable_auto = enable_auto
        # The URL of the property template file. The API parses the file synchronously. An error is returned if the file format is invalid.
        # 
        # > The file must be in the following format: `{ "properties":{"key1":"value1"}}`.
        self.file_path = file_path
        # The information about the system property template.
        self.system_property_info = system_property_info
        # The name of the template. The name must meet the following requirements:
        # 
        # - Be 2 to 32 characters in length.
        # 
        # - Start with an uppercase or lowercase letter or a Chinese character. It cannot start with `http://` or `https://`.
        # 
        # - Contain letters, digits, colons (:), underscores (_), and hyphens (-). Periods (.) are not supported.
        self.template_name = template_name

    def validate(self):
        if self.system_property_info:
            self.system_property_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_auto is not None:
            result['EnableAuto'] = self.enable_auto

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.system_property_info is not None:
            result['SystemPropertyInfo'] = self.system_property_info.to_map()

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAuto') is not None:
            self.enable_auto = m.get('EnableAuto')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('SystemPropertyInfo') is not None:
            temp_model = main_models.CreateSystemPropertyTemplateRequestSystemPropertyInfo()
            self.system_property_info = temp_model.from_map(m.get('SystemPropertyInfo'))

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class CreateSystemPropertyTemplateRequestSystemPropertyInfo(DaraModel):
    def __init__(
        self,
        custom_property_infos: List[main_models.CreateSystemPropertyTemplateRequestSystemPropertyInfoCustomPropertyInfos] = None,
        ro_bootloader: str = None,
        ro_build_display_id: str = None,
        ro_build_fingerprint: str = None,
        ro_build_host: str = None,
        ro_build_id: str = None,
        ro_build_product: str = None,
        ro_build_tags: str = None,
        ro_build_type: str = None,
        ro_build_user: str = None,
        ro_product_board: str = None,
        ro_product_brand: str = None,
        ro_product_device: str = None,
        ro_product_manufacturer: str = None,
        ro_product_model: str = None,
        rw_ro_serial_no: str = None,
    ):
        # A list of custom properties.
        self.custom_property_infos = custom_property_infos
        # > This parameter is not yet available for use.
        self.ro_bootloader = ro_bootloader
        # > This parameter is not yet available for use.
        self.ro_build_display_id = ro_build_display_id
        # > This parameter is not yet available for use.
        self.ro_build_fingerprint = ro_build_fingerprint
        # > This parameter is not yet available for use.
        self.ro_build_host = ro_build_host
        # > This parameter is not yet available for use.
        self.ro_build_id = ro_build_id
        # > This parameter is not yet available for use.
        self.ro_build_product = ro_build_product
        # > This parameter is not yet available for use.
        self.ro_build_tags = ro_build_tags
        # > This parameter is not yet available for use.
        self.ro_build_type = ro_build_type
        # > This parameter is not yet available for use.
        self.ro_build_user = ro_build_user
        # > This parameter is not yet available for use.
        self.ro_product_board = ro_product_board
        # > This parameter is not yet available for use.
        self.ro_product_brand = ro_product_brand
        # > This parameter is not yet available for use.
        self.ro_product_device = ro_product_device
        # > This parameter is not yet available for use.
        self.ro_product_manufacturer = ro_product_manufacturer
        # > This parameter is not yet available for use.
        self.ro_product_model = ro_product_model
        # > This parameter is not yet available for use.
        self.rw_ro_serial_no = rw_ro_serial_no

    def validate(self):
        if self.custom_property_infos:
            for v1 in self.custom_property_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomPropertyInfos'] = []
        if self.custom_property_infos is not None:
            for k1 in self.custom_property_infos:
                result['CustomPropertyInfos'].append(k1.to_map() if k1 else None)

        if self.ro_bootloader is not None:
            result['RoBootloader'] = self.ro_bootloader

        if self.ro_build_display_id is not None:
            result['RoBuildDisplayId'] = self.ro_build_display_id

        if self.ro_build_fingerprint is not None:
            result['RoBuildFingerprint'] = self.ro_build_fingerprint

        if self.ro_build_host is not None:
            result['RoBuildHost'] = self.ro_build_host

        if self.ro_build_id is not None:
            result['RoBuildId'] = self.ro_build_id

        if self.ro_build_product is not None:
            result['RoBuildProduct'] = self.ro_build_product

        if self.ro_build_tags is not None:
            result['RoBuildTags'] = self.ro_build_tags

        if self.ro_build_type is not None:
            result['RoBuildType'] = self.ro_build_type

        if self.ro_build_user is not None:
            result['RoBuildUser'] = self.ro_build_user

        if self.ro_product_board is not None:
            result['RoProductBoard'] = self.ro_product_board

        if self.ro_product_brand is not None:
            result['RoProductBrand'] = self.ro_product_brand

        if self.ro_product_device is not None:
            result['RoProductDevice'] = self.ro_product_device

        if self.ro_product_manufacturer is not None:
            result['RoProductManufacturer'] = self.ro_product_manufacturer

        if self.ro_product_model is not None:
            result['RoProductModel'] = self.ro_product_model

        if self.rw_ro_serial_no is not None:
            result['RwRoSerialNo'] = self.rw_ro_serial_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_property_infos = []
        if m.get('CustomPropertyInfos') is not None:
            for k1 in m.get('CustomPropertyInfos'):
                temp_model = main_models.CreateSystemPropertyTemplateRequestSystemPropertyInfoCustomPropertyInfos()
                self.custom_property_infos.append(temp_model.from_map(k1))

        if m.get('RoBootloader') is not None:
            self.ro_bootloader = m.get('RoBootloader')

        if m.get('RoBuildDisplayId') is not None:
            self.ro_build_display_id = m.get('RoBuildDisplayId')

        if m.get('RoBuildFingerprint') is not None:
            self.ro_build_fingerprint = m.get('RoBuildFingerprint')

        if m.get('RoBuildHost') is not None:
            self.ro_build_host = m.get('RoBuildHost')

        if m.get('RoBuildId') is not None:
            self.ro_build_id = m.get('RoBuildId')

        if m.get('RoBuildProduct') is not None:
            self.ro_build_product = m.get('RoBuildProduct')

        if m.get('RoBuildTags') is not None:
            self.ro_build_tags = m.get('RoBuildTags')

        if m.get('RoBuildType') is not None:
            self.ro_build_type = m.get('RoBuildType')

        if m.get('RoBuildUser') is not None:
            self.ro_build_user = m.get('RoBuildUser')

        if m.get('RoProductBoard') is not None:
            self.ro_product_board = m.get('RoProductBoard')

        if m.get('RoProductBrand') is not None:
            self.ro_product_brand = m.get('RoProductBrand')

        if m.get('RoProductDevice') is not None:
            self.ro_product_device = m.get('RoProductDevice')

        if m.get('RoProductManufacturer') is not None:
            self.ro_product_manufacturer = m.get('RoProductManufacturer')

        if m.get('RoProductModel') is not None:
            self.ro_product_model = m.get('RoProductModel')

        if m.get('RwRoSerialNo') is not None:
            self.rw_ro_serial_no = m.get('RwRoSerialNo')

        return self

class CreateSystemPropertyTemplateRequestSystemPropertyInfoCustomPropertyInfos(DaraModel):
    def __init__(
        self,
        property_name: str = None,
        property_value: str = None,
    ):
        # The key of the custom property.
        self.property_name = property_name
        # The value of the custom property.
        self.property_value = property_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.property_name is not None:
            result['PropertyName'] = self.property_name

        if self.property_value is not None:
            result['PropertyValue'] = self.property_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')

        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')

        return self

