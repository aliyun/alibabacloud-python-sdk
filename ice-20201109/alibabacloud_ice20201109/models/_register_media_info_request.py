# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterMediaInfoRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        cate_id: int = None,
        client_token: str = None,
        cover_url: str = None,
        description: str = None,
        input_url: str = None,
        media_tags: str = None,
        media_type: str = None,
        overwrite: bool = None,
        reference_id: str = None,
        register_config: str = None,
        smart_tag_template_id: str = None,
        title: str = None,
        user_data: str = None,
        workflow_id: str = None,
    ):
        # The business type of the media asset. Valid values:
        # 
        # *   subtitles
        # *   watermark
        # *   opening
        # *   ending
        # *   general
        self.business_type = business_type
        # The category ID.
        self.cate_id = cate_id
        # The client token that is used to ensure the idempotence of the request. The value must be a UUID that contains 32 characters.
        self.client_token = client_token
        # The thumbnail URL of the media asset.
        # 
        # *   The value can be up to 128 bytes in length.
        # *   The value must be encoded in UTF-8.
        self.cover_url = cover_url
        # The description of the media asset.
        # 
        # *   The value can be up to 1,024 bytes in length.
        # *   The value must be encoded in UTF-8.
        self.description = description
        # The URL of the media asset in another service. The URL is associated with the ID of the media asset in IMS. The URL cannot be modified once registered. The following types of URLs are supported:
        # 
        # *   OSS URL in one of the following formats:
        # 
        # http(s)://example-bucket.oss-cn-shanghai.aliyuncs.com/example.mp4
        # 
        # oss://example-bucket/example.mp4: In this format, it is considered by default that the region of the OSS bucket in which the media asset resides is the same as the region in which IMS is activated.
        # 
        # *   URL of an ApsaraVideo VOD media asset
        # 
        # vod://\\*\\*\\*20b48fb04483915d4f2cd8ac\\*\\*\\*\\*
        # 
        # This parameter is required.
        self.input_url = input_url
        # The tags of the media asset.
        # 
        # *   Up to 16 tags are supported.
        # *   Separate multiple tags with commas (,).
        # *   Each tag can be up to 32 bytes in length.
        # *   The value must be encoded in UTF-8.
        self.media_tags = media_tags
        # The type of the media asset. Valid values:
        # 
        # *   image
        # *   video
        # *   audio
        # *   text
        # 
        # We recommend that you specify this parameter based on your business requirements. If you set InputURL to an OSS URL, the media asset type can be automatically determined based on the file name extension. For more information
        # <props="china">, see [File formats](https://help.aliyun.com/document_detail/466207.html).
        self.media_type = media_type
        # Specifies whether to overwrite the media asset that has been registered by using the same URL. Default value: false. Valid values:
        # 
        # \\- true: If a media asset has been registered by using the same URL, the original media asset is deleted and the new media asset is registered.
        # 
        # \\- false: If a media asset has been registered by using the same URL, the new media asset is not registered. A URL cannot be used to register multiple media assets.
        self.overwrite = overwrite
        # The custom ID. The ID can be 6 to 64 characters in length and can contain only letters, digits, hyphens (-), and underscores (_). Make sure that the ID is unique among users.
        self.reference_id = reference_id
        # The registration configurations.
        # 
        # By default, a sprite is generated for the media asset. You can set NeedSprite to false to disable automatic sprite generation.
        # 
        # By default, a snapshot is generated for the media asset. You can set NeedSnapshot to false to disable automatic snapshot generation.
        self.register_config = register_config
        # The ID of the smart tagging template. Valid values:
        # 
        # *   S00000101-300080: the system template that supports natural language processing (NLP) for content recognition.
        # *   S00000103-000001: the system template that supports NLP for content recognition and all tagging capabilities.
        # *   S00000103-000002: the system template that supports all tagging capabilities but does not support NLP for content recognition.
        # 
        # After you configure this parameter, a smart tag analysis task is automatically initiated after the media asset is registered. For more information about the billable items<props="china">, see [Smart tagging](https://help.aliyun.com/zh/ims/media-ai-billing?spm=a2c4g.11186623.0.0.3147392dWwlSjL#p-k38-3rb-dug).
        self.smart_tag_template_id = smart_tag_template_id
        # The title. If you do not specify this parameter, a default title is automatically generated based on the date.
        # 
        # *   The value can be up to 128 bytes in length.
        # *   The value must be encoded in UTF-8.
        self.title = title
        # The user data. You can specify a custom callback URL. For more information<props="china"> ,see [Configure a callback upon editing completion](https://help.aliyun.com/document_detail/451631.html).
        # 
        # *   The value can be up to 1,024 bytes in length.
        # *   The value must be encoded in UTF-8.
        # *   The value must be in the JSON format.
        self.user_data = user_data
        # The workflow ID.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.description is not None:
            result['Description'] = self.description

        if self.input_url is not None:
            result['InputURL'] = self.input_url

        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.register_config is not None:
            result['RegisterConfig'] = self.register_config

        if self.smart_tag_template_id is not None:
            result['SmartTagTemplateId'] = self.smart_tag_template_id

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')

        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('RegisterConfig') is not None:
            self.register_config = m.get('RegisterConfig')

        if m.get('SmartTagTemplateId') is not None:
            self.smart_tag_template_id = m.get('SmartTagTemplateId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

