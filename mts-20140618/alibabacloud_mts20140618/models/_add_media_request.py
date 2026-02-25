# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddMediaRequest(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        cover_url: str = None,
        description: str = None,
        file_url: str = None,
        input_unbind: bool = None,
        media_workflow_id: str = None,
        media_workflow_user_data: str = None,
        override_params: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: str = None,
        title: str = None,
    ):
        # The ID of the category to which the media file belongs. The value cannot be negative.
        self.cate_id = cate_id
        # The URL of the thumbnail. To obtain the URL, you can log on to the **MPS console** and choose **Workflows** > **Media Buckets**. Alternatively, you can log on to the **OSS console** and click **My OSS Paths**.
        # 
        # *   The value can be up to 3,200 bytes in length.
        # *   The URL complies with RFC 2396 and is encoded in UTF-8, with reserved characters being percent-encoded. For more information, see [URL encoding](https://help.aliyun.com/document_detail/423796.html).
        self.cover_url = cover_url
        # The description of the media file.
        # 
        # *   The description can be up to 1,024 bytes in length.
        # *   The value must be encoded in UTF-8.
        self.description = description
        # The URL of the input file. You can obtain the URL in the MPS or OSS console. For more information, see the **Triggering and matching rule for a workflow** section of this topic.
        # 
        # *   Only OSS HTTP URLs are supported. Alibaba Cloud CDN URLs and HTTPS URLs are not supported.
        # *   The value can be up to 3,200 bytes in size.
        # *   The URL complies with RFC 2396 and is encoded in UTF-8. For more information, see [URL encoding](https://help.aliyun.com/document_detail/423796.html).
        # 
        # This parameter is required.
        self.file_url = file_url
        # Specifies whether to check if the media workflow supports the specified input path. We recommend that you set this parameter to true to prevent errors that may result from invalid paths. Valid values:
        # 
        # *   **true**: checks whether the workflow supports the specified input path.
        # *   **false**: does not check whether the workflow supports the specified input path.
        self.input_unbind = input_unbind
        # The ID of the media workflow that you want to run for the media file. To query the ID of a media workflow, you can log on to the MPS console or call the [AddMediaWorkflow](https://help.aliyun.com/document_detail/44437.html) operation.
        self.media_workflow_id = media_workflow_id
        # The custom data of the media workflow.
        # 
        # *   The value can be up to 1,024 bytes in length.
        # *   The value must be encoded in UTF-8.
        self.media_workflow_user_data = media_workflow_user_data
        # The subtitle settings that are used to overwrite the original settings.
        # 
        # *   Example 1: Use `{"WebVTTSubtitleOverrides",[{"RefActivityName":"subtitleNode","WebVTTSubtitleURL":"http://test.oss-cn-hangzhou.aliyuncs.com/example1.vtt"}]}` to overwrite the original subtitle settings during HTTP Live Streaming (HLS) packaging.
        # *   Example 2: Use `{"subtitleTransNodeName":{"InputConfig":{"Format":"stl","InputFile":{"URL":"http://subtitleBucket.oss-cn-hangzhou.aliyuncs.com/package/example/CENG.stl"}}}}` to overwrite the original subtitle settings during Dynamic Adaptive Streaming over HTTP (DASH) packaging.
        self.override_params = override_params
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags that you want to add to the media file.
        # 
        # > In MPS, each tag that is specified for a media file is independent. You can search for all the media files that have the same tags in the Media Library.
        # 
        # *   You can specify up to 16 tags for a media file. Separate multiple tags with commas (,).
        # *   Each tag can be up to 32 bytes in size
        # *   The value must be encoded in UTF-8.
        self.tags = tags
        # The title of the media file.
        # 
        # *   The title can be up to 128 bytes in length.
        # *   The value must be encoded in UTF-8.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.description is not None:
            result['Description'] = self.description

        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.input_unbind is not None:
            result['InputUnbind'] = self.input_unbind

        if self.media_workflow_id is not None:
            result['MediaWorkflowId'] = self.media_workflow_id

        if self.media_workflow_user_data is not None:
            result['MediaWorkflowUserData'] = self.media_workflow_user_data

        if self.override_params is not None:
            result['OverrideParams'] = self.override_params

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('InputUnbind') is not None:
            self.input_unbind = m.get('InputUnbind')

        if m.get('MediaWorkflowId') is not None:
            self.media_workflow_id = m.get('MediaWorkflowId')

        if m.get('MediaWorkflowUserData') is not None:
            self.media_workflow_user_data = m.get('MediaWorkflowUserData')

        if m.get('OverrideParams') is not None:
            self.override_params = m.get('OverrideParams')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

