# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListAllPublicMediaTagsResponseBody(DaraModel):
    def __init__(
        self,
        media_tag_list: List[main_models.ListAllPublicMediaTagsResponseBodyMediaTagList] = None,
        request_id: str = None,
    ):
        # The tags of media assets in the public media library.
        self.media_tag_list = media_tag_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.media_tag_list:
            for v1 in self.media_tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MediaTagList'] = []
        if self.media_tag_list is not None:
            for k1 in self.media_tag_list:
                result['MediaTagList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.media_tag_list = []
        if m.get('MediaTagList') is not None:
            for k1 in m.get('MediaTagList'):
                temp_model = main_models.ListAllPublicMediaTagsResponseBodyMediaTagList()
                self.media_tag_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAllPublicMediaTagsResponseBodyMediaTagList(DaraModel):
    def __init__(
        self,
        media_tag_id: str = None,
        media_tag_name_chinese: str = None,
        media_tag_name_english: str = None,
        options: List[main_models.ListAllPublicMediaTagsResponseBodyMediaTagListOptions] = None,
    ):
        # The ID of the media tag.
        self.media_tag_id = media_tag_id
        # The name of the media tag in Chinese.
        self.media_tag_name_chinese = media_tag_name_chinese
        # The name of the material tag in English.
        self.media_tag_name_english = media_tag_name_english
        # The options.
        self.options = options

    def validate(self):
        if self.options:
            for v1 in self.options:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_tag_id is not None:
            result['MediaTagId'] = self.media_tag_id

        if self.media_tag_name_chinese is not None:
            result['MediaTagNameChinese'] = self.media_tag_name_chinese

        if self.media_tag_name_english is not None:
            result['MediaTagNameEnglish'] = self.media_tag_name_english

        result['Options'] = []
        if self.options is not None:
            for k1 in self.options:
                result['Options'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaTagId') is not None:
            self.media_tag_id = m.get('MediaTagId')

        if m.get('MediaTagNameChinese') is not None:
            self.media_tag_name_chinese = m.get('MediaTagNameChinese')

        if m.get('MediaTagNameEnglish') is not None:
            self.media_tag_name_english = m.get('MediaTagNameEnglish')

        self.options = []
        if m.get('Options') is not None:
            for k1 in m.get('Options'):
                temp_model = main_models.ListAllPublicMediaTagsResponseBodyMediaTagListOptions()
                self.options.append(temp_model.from_map(k1))

        return self

class ListAllPublicMediaTagsResponseBodyMediaTagListOptions(DaraModel):
    def __init__(
        self,
        option_chinese_name: str = None,
        option_english_name: str = None,
        option_id: str = None,
    ):
        # The option name in Chinese.
        self.option_chinese_name = option_chinese_name
        # The option name in English.
        self.option_english_name = option_english_name
        # The option ID.
        self.option_id = option_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.option_chinese_name is not None:
            result['OptionChineseName'] = self.option_chinese_name

        if self.option_english_name is not None:
            result['OptionEnglishName'] = self.option_english_name

        if self.option_id is not None:
            result['OptionId'] = self.option_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OptionChineseName') is not None:
            self.option_chinese_name = m.get('OptionChineseName')

        if m.get('OptionEnglishName') is not None:
            self.option_english_name = m.get('OptionEnglishName')

        if m.get('OptionId') is not None:
            self.option_id = m.get('OptionId')

        return self

