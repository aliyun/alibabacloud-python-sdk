# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class SearchImageResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        image_response: main_models.SearchImageResponseBodyImageResponse = None,
        request_id: str = None,
        success: str = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.image_response = image_response
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.image_response:
            self.image_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.image_response is not None:
            result['ImageResponse'] = self.image_response.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('ImageResponse') is not None:
            temp_model = main_models.SearchImageResponseBodyImageResponse()
            self.image_response = temp_model.from_map(m.get('ImageResponse'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SearchImageResponseBodyImageResponse(DaraModel):
    def __init__(
        self,
        image_list: List[main_models.SearchImageResponseBodyImageResponseImageList] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.image_list = image_list
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.image_list:
            for v1 in self.image_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageList'] = []
        if self.image_list is not None:
            for k1 in self.image_list:
                result['ImageList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_list = []
        if m.get('ImageList') is not None:
            for k1 in m.get('ImageList'):
                temp_model = main_models.SearchImageResponseBodyImageResponseImageList()
                self.image_list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class SearchImageResponseBodyImageResponseImageList(DaraModel):
    def __init__(
        self,
        descriptive_tones: str = None,
        height: int = None,
        image_category: str = None,
        image_ratio: str = None,
        image_uuid: str = None,
        oss_key: str = None,
        quantitative_palette: str = None,
        tags_from_image: str = None,
        url: str = None,
        width: int = None,
    ):
        self.descriptive_tones = descriptive_tones
        self.height = height
        self.image_category = image_category
        self.image_ratio = image_ratio
        self.image_uuid = image_uuid
        # oss key
        self.oss_key = oss_key
        self.quantitative_palette = quantitative_palette
        self.tags_from_image = tags_from_image
        self.url = url
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.descriptive_tones is not None:
            result['DescriptiveTones'] = self.descriptive_tones

        if self.height is not None:
            result['Height'] = self.height

        if self.image_category is not None:
            result['ImageCategory'] = self.image_category

        if self.image_ratio is not None:
            result['ImageRatio'] = self.image_ratio

        if self.image_uuid is not None:
            result['ImageUuid'] = self.image_uuid

        if self.oss_key is not None:
            result['OssKey'] = self.oss_key

        if self.quantitative_palette is not None:
            result['QuantitativePalette'] = self.quantitative_palette

        if self.tags_from_image is not None:
            result['TagsFromImage'] = self.tags_from_image

        if self.url is not None:
            result['Url'] = self.url

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DescriptiveTones') is not None:
            self.descriptive_tones = m.get('DescriptiveTones')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')

        if m.get('ImageRatio') is not None:
            self.image_ratio = m.get('ImageRatio')

        if m.get('ImageUuid') is not None:
            self.image_uuid = m.get('ImageUuid')

        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')

        if m.get('QuantitativePalette') is not None:
            self.quantitative_palette = m.get('QuantitativePalette')

        if m.get('TagsFromImage') is not None:
            self.tags_from_image = m.get('TagsFromImage')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

