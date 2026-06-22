# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetectImageCroppingShrinkRequest(DaraModel):
    def __init__(
        self,
        aspect_ratios: str = None,
        credential_config_shrink: str = None,
        inclusion_hints_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        # The list of cropping aspect ratios. You can specify up to 5 ratios. Each ratio must meet the following requirements:
        # 
        # - The ratio must consist of integers in the range of (0, 20).
        # 
        # - The ratio value must be in the range of [0.5, 2].
        # 
        # - If you do not specify this parameter, the default value `["auto"]` is used.
        # 
        # > The following cases cause an error:<br>- More than 5 ratios are specified.<br>- An empty list is passed.<br>- The ratio contains non-integer values, such as `4.1:3`.<br>- The ratio value is less than 0.5 or greater than 2.
        self.aspect_ratios = aspect_ratios
        # **Leave this parameter empty unless otherwise required.**
        # 
        # The China authorization configuration. This parameter is optional. For more information, see [Use chained authorization to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The list of semantic text descriptions for objects that you want the cropping result to include. Each element is free-form text, such as "signboard" or "dish".
        # 
        # > Usage limits of the InclusionHints parameter:
        # <br>- You can pass in up to 1 hint in the array to specify the type of object to include in the cropping result, such as "signboard".
        # <br>- The algorithm detects all objects in the image that match the hint and generates cropping regions that include as many matched objects as possible.
        # <br>- Each cropping region includes up to 10 matched objects. If more than 10 objects match in the image, the cropping region includes up to 10 of them.
        # <br>- You can use the MatchedInclusionHints response field to determine whether the hint was successfully matched.
        # <br>- This parameter is supported only in regions in the Chinese mainland.
        self.inclusion_hints_shrink = inclusion_hints_shrink
        # The project name.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The OSS URI of the image.
        # 
        # The OSS URI follows the format oss://${Bucket}/${Object}, where `${Bucket}` is the name of an OSS bucket in the same region as the current project, and `${Object}` is the full path of the file including the file name extension.
        self.source_uri = source_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aspect_ratios is not None:
            result['AspectRatios'] = self.aspect_ratios

        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink

        if self.inclusion_hints_shrink is not None:
            result['InclusionHints'] = self.inclusion_hints_shrink

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AspectRatios') is not None:
            self.aspect_ratios = m.get('AspectRatios')

        if m.get('CredentialConfig') is not None:
            self.credential_config_shrink = m.get('CredentialConfig')

        if m.get('InclusionHints') is not None:
            self.inclusion_hints_shrink = m.get('InclusionHints')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        return self

