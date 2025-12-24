# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveAIStudioResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        studio_configs: main_models.DescribeLiveAIStudioResponseBodyStudioConfigs = None,
        total: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Valid values: 1 to 50.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The virtual studio templates.
        self.studio_configs = studio_configs
        # The total number of templates.
        self.total = total

    def validate(self):
        if self.studio_configs:
            self.studio_configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.studio_configs is not None:
            result['StudioConfigs'] = self.studio_configs.to_map()

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StudioConfigs') is not None:
            temp_model = main_models.DescribeLiveAIStudioResponseBodyStudioConfigs()
            self.studio_configs = temp_model.from_map(m.get('StudioConfigs'))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeLiveAIStudioResponseBodyStudioConfigs(DaraModel):
    def __init__(
        self,
        subtitle_config: List[main_models.DescribeLiveAIStudioResponseBodyStudioConfigsSubtitleConfig] = None,
    ):
        self.subtitle_config = subtitle_config

    def validate(self):
        if self.subtitle_config:
            for v1 in self.subtitle_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SubtitleConfig'] = []
        if self.subtitle_config is not None:
            for k1 in self.subtitle_config:
                result['SubtitleConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subtitle_config = []
        if m.get('SubtitleConfig') is not None:
            for k1 in m.get('SubtitleConfig'):
                temp_model = main_models.DescribeLiveAIStudioResponseBodyStudioConfigsSubtitleConfig()
                self.subtitle_config.append(temp_model.from_map(k1))

        return self

class DescribeLiveAIStudioResponseBodyStudioConfigsSubtitleConfig(DaraModel):
    def __init__(
        self,
        background_resource_id: str = None,
        background_resource_url: str = None,
        background_type: str = None,
        description: str = None,
        height: str = None,
        matting_layout: str = None,
        matting_type: str = None,
        media_layout: str = None,
        media_resource_id: str = None,
        media_resource_url: str = None,
        media_type: str = None,
        rule_ids: main_models.DescribeLiveAIStudioResponseBodyStudioConfigsSubtitleConfigRuleIds = None,
        template_id: str = None,
        template_name: str = None,
        width: str = None,
    ):
        # The ID of the background material.
        self.background_resource_id = background_resource_id
        # The URL of the background material. Make sure that the URL is accessible over the Internet. Either this parameter or the BackgroundResourceId parameter is returned.
        self.background_resource_url = background_resource_url
        # The type of the background material. Valid values:
        # 
        # *   VOD: a video in ApsaraVideo VOD
        # *   PIC: an image
        # *   LIVE: a live stream
        self.background_type = background_type
        # The custom description.
        self.description = description
        # The preview height. Unit: pixels.
        # 
        # The following preview specifications (width × height) are supported:
        # 
        # *   Landscape low definition 360p (640×360)
        # *   Portrait low definition 360p (360×640)
        # *   Landscape standard definition 480p (854×480)
        # *   Portrait standard definition 480p (480×854)
        # *   Landscape high definition 720p (1280×720)
        # *   Portrait high definition 720p (720×1280)
        # *   Landscape ultra-high definition 1080p (1920×1080)
        # *   Portrait ultra-high definition 1080p (1080×1920)
        self.height = height
        # The layout information of the multimedia material.
        self.matting_layout = matting_layout
        # The type of chroma key that is performed on ingested streams. Valid values:
        # 
        # *   green: green-key chroma key
        # *   blue: blue-screen chroma key
        # *   complex: background replacement
        self.matting_type = matting_type
        # LIVE, live streaming
        self.media_layout = media_layout
        # The ID of the multimedia material in ApsaraVideo VOD.
        self.media_resource_id = media_resource_id
        # The URL of the multimedia material.
        self.media_resource_url = media_resource_url
        # The type of the multimedia material. Valid values:
        # 
        # *   VOD: a video in ApsaraVideo VOD
        # *   PIC: an image
        # *   LIVE: a live stream
        self.media_type = media_type
        # The IDs of the bound rules.
        self.rule_ids = rule_ids
        # The ID of the virtual studio template.
        self.template_id = template_id
        # The name of the virtual studio template. The name is the same as the value of the StudioName parameter that was specified when you called the CreateLiveAiStudio operation to create the virtual studio template.
        self.template_name = template_name
        # The preview width.
        self.width = width

    def validate(self):
        if self.rule_ids:
            self.rule_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_resource_id is not None:
            result['BackgroundResourceId'] = self.background_resource_id

        if self.background_resource_url is not None:
            result['BackgroundResourceUrl'] = self.background_resource_url

        if self.background_type is not None:
            result['BackgroundType'] = self.background_type

        if self.description is not None:
            result['Description'] = self.description

        if self.height is not None:
            result['Height'] = self.height

        if self.matting_layout is not None:
            result['MattingLayout'] = self.matting_layout

        if self.matting_type is not None:
            result['MattingType'] = self.matting_type

        if self.media_layout is not None:
            result['MediaLayout'] = self.media_layout

        if self.media_resource_id is not None:
            result['MediaResourceId'] = self.media_resource_id

        if self.media_resource_url is not None:
            result['MediaResourceUrl'] = self.media_resource_url

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundResourceId') is not None:
            self.background_resource_id = m.get('BackgroundResourceId')

        if m.get('BackgroundResourceUrl') is not None:
            self.background_resource_url = m.get('BackgroundResourceUrl')

        if m.get('BackgroundType') is not None:
            self.background_type = m.get('BackgroundType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('MattingLayout') is not None:
            self.matting_layout = m.get('MattingLayout')

        if m.get('MattingType') is not None:
            self.matting_type = m.get('MattingType')

        if m.get('MediaLayout') is not None:
            self.media_layout = m.get('MediaLayout')

        if m.get('MediaResourceId') is not None:
            self.media_resource_id = m.get('MediaResourceId')

        if m.get('MediaResourceUrl') is not None:
            self.media_resource_url = m.get('MediaResourceUrl')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('RuleIds') is not None:
            temp_model = main_models.DescribeLiveAIStudioResponseBodyStudioConfigsSubtitleConfigRuleIds()
            self.rule_ids = temp_model.from_map(m.get('RuleIds'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class DescribeLiveAIStudioResponseBodyStudioConfigsSubtitleConfigRuleIds(DaraModel):
    def __init__(
        self,
        rule_id: List[str] = None,
    ):
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        return self

