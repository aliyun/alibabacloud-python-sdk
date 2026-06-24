# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListImageRequest(DaraModel):
    def __init__(
        self,
        biz_region_id_list: List[str] = None,
        biz_type: int = None,
        biz_type_list: List[int] = None,
        distro: str = None,
        feature_list: List[str] = None,
        fota_version: str = None,
        image_id: str = None,
        image_name: str = None,
        image_type: str = None,
        language_type: str = None,
        os_type: str = None,
        package_type: str = None,
        page_number: int = None,
        page_size: int = None,
        platform_name: str = None,
        platform_name_list: List[str] = None,
        product_type: str = None,
        product_type_list: List[str] = None,
        protocol_type: str = None,
        resource_instance_type: str = None,
        status: str = None,
        tag_list: List[main_models.ListImageRequestTagList] = None,
    ):
        # The list of supported regions.
        # WUYING images are centralized. Use this parameter to query the regions where the image is deployed.
        self.biz_region_id_list = biz_region_id_list
        # The business type. This parameter is not publicly available.
        self.biz_type = biz_type
        # The list of all business types. This parameter is not publicly available.
        self.biz_type_list = biz_type_list
        self.distro = distro
        # The list of features supported by the image.
        self.feature_list = feature_list
        # The image version information.
        self.fota_version = fota_version
        # The image ID.
        self.image_id = image_id
        # The image name. Fuzzy match is supported.
        self.image_name = image_name
        # The image type.
        self.image_type = image_type
        # The language.
        self.language_type = language_type
        # The operating system type of the image.
        self.os_type = os_type
        # The image package type.
        self.package_type = package_type
        # The page number.
        self.page_number = page_number
        # The number of entries per page for paging queries. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        # The operating system platform name.
        self.platform_name = platform_name
        # The list of supported platform types. For valid values, refer to PlatformName above.
        self.platform_name_list = platform_name_list
        # The product type.
        self.product_type = product_type
        # The list of products supported when the image supports multiple products.
        self.product_type_list = product_type_list
        # The protocol type of the image.
        self.protocol_type = protocol_type
        # Queries images of specific defined specifications.
        self.resource_instance_type = resource_instance_type
        # The image status. Specifies the status of images to query. By default, all images that are not deleted are queried.
        self.status = status
        # The tags for query.
        self.tag_list = tag_list

    def validate(self):
        if self.tag_list:
            for v1 in self.tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_region_id_list is not None:
            result['BizRegionIdList'] = self.biz_region_id_list

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list

        if self.distro is not None:
            result['Distro'] = self.distro

        if self.feature_list is not None:
            result['FeatureList'] = self.feature_list

        if self.fota_version is not None:
            result['FotaVersion'] = self.fota_version

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.language_type is not None:
            result['LanguageType'] = self.language_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name

        if self.platform_name_list is not None:
            result['PlatformNameList'] = self.platform_name_list

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.product_type_list is not None:
            result['ProductTypeList'] = self.product_type_list

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.resource_instance_type is not None:
            result['ResourceInstanceType'] = self.resource_instance_type

        if self.status is not None:
            result['Status'] = self.status

        result['TagList'] = []
        if self.tag_list is not None:
            for k1 in self.tag_list:
                result['TagList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionIdList') is not None:
            self.biz_region_id_list = m.get('BizRegionIdList')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')

        if m.get('Distro') is not None:
            self.distro = m.get('Distro')

        if m.get('FeatureList') is not None:
            self.feature_list = m.get('FeatureList')

        if m.get('FotaVersion') is not None:
            self.fota_version = m.get('FotaVersion')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('LanguageType') is not None:
            self.language_type = m.get('LanguageType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')

        if m.get('PlatformNameList') is not None:
            self.platform_name_list = m.get('PlatformNameList')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ProductTypeList') is not None:
            self.product_type_list = m.get('ProductTypeList')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('ResourceInstanceType') is not None:
            self.resource_instance_type = m.get('ResourceInstanceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag_list = []
        if m.get('TagList') is not None:
            for k1 in m.get('TagList'):
                temp_model = main_models.ListImageRequestTagList()
                self.tag_list.append(temp_model.from_map(k1))

        return self

class ListImageRequestTagList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The custom tag key.
        self.key = key
        # The custom tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

