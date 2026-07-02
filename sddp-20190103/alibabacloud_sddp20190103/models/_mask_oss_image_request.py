# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MaskOssImageRequest(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        is_always_upload: bool = None,
        is_cover_object: bool = None,
        is_support_restore: bool = None,
        lang: str = None,
        mask_rule_id_list: str = None,
        object_key: str = None,
        service_region_id: str = None,
    ):
        # The name of the OSS bucket.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name
        # Specifies whether to always upload the processed image.
        # 
        # If you set this to false, the image is uploaded only if it matches a masking rule.
        # 
        # If you set this to true, the processed image is always uploaded.
        self.is_always_upload = is_always_upload
        self.is_cover_object = is_cover_object
        # Specifies whether you can restore the original image from the masked version.
        self.is_support_restore = is_support_restore
        self.lang = lang
        # A comma-separated list of masking rule IDs.
        # 
        # The following rule IDs correspond to the listed sensitive data types:
        # 
        # 3000: Images that contain ID card information (Chinese mainland)
        # 
        # 3009: Images that contain license plate information (Chinese mainland)
        # 
        # 3002: Images that contain faces
        # 
        # 1002: Names (Simplified Chinese)
        # 
        # 1003: Addresses (Chinese mainland)
        # 
        # 4003: Unified Social Credit Code
        # 
        # 63009: Images that contain eyes
        # 
        # This parameter is required.
        self.mask_rule_id_list = mask_rule_id_list
        # The full key of the object stored in OSS.
        # 
        # This parameter is required.
        self.object_key = object_key
        # The region where the bucket is located.
        # 
        # This parameter is required.
        self.service_region_id = service_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.is_always_upload is not None:
            result['IsAlwaysUpload'] = self.is_always_upload

        if self.is_cover_object is not None:
            result['IsCoverObject'] = self.is_cover_object

        if self.is_support_restore is not None:
            result['IsSupportRestore'] = self.is_support_restore

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.mask_rule_id_list is not None:
            result['MaskRuleIdList'] = self.mask_rule_id_list

        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('IsAlwaysUpload') is not None:
            self.is_always_upload = m.get('IsAlwaysUpload')

        if m.get('IsCoverObject') is not None:
            self.is_cover_object = m.get('IsCoverObject')

        if m.get('IsSupportRestore') is not None:
            self.is_support_restore = m.get('IsSupportRestore')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaskRuleIdList') is not None:
            self.mask_rule_id_list = m.get('MaskRuleIdList')

        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        return self

