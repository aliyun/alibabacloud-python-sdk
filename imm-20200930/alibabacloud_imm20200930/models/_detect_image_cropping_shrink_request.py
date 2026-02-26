# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetectImageCroppingShrinkRequest(DaraModel):
    def __init__(
        self,
        aspect_ratios: str = None,
        credential_config_shrink: str = None,
        project_name: str = None,
        source_uri: str = None,
    ):
        # The cropping ratios. You can specify up to five cropping ratios. Take note of the following requirements:
        # 
        # *   The ratio must be an integer between 0 and 20.
        # *   The ratio must range from 0.5 to 2.
        # *   If you leave this parameter empty, the default processing logic is `["auto"]`.
        # 
        # >  Errors are reported in one of the following cases:\\
        # You specify more than five cropping ratios.\\
        # You pass an empty list to the system.\\
        # You specify a ratio that is not an integer, such as `4.1:3`.\\
        # The ratio is beyond the range of 0.5 to 2.
        self.aspect_ratios = aspect_ratios
        # **If you have no special requirements, leave this parameter empty.**
        # 
        # The authorization chain settings. For more information, see [Use authorization chains to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The name of the project.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The URI of the Object Storage Service (OSS) bucket in which you store the image.
        # 
        # Specify the value in the oss://${Bucket}/${Object} format. `${Bucket}` specifies the name of the OSS bucket that resides in the same region as the current project. `${Object}` specifies the complete path to the image file that has an extension.
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

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        return self

