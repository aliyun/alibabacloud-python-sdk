# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class TranslateChannelDraftResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.TranslateChannelDraftResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # The detailed reason why access is denied.
        self.access_denied_detail = access_denied_detail
        # Indicates whether a retry is allowed.
        self.allow_retry = allow_retry
        # The application name. The application with this name is queried.
        self.app_name = app_name
        # The dynamic code. This parameter is not in use. Ignore this parameter.
        self.dynamic_code = dynamic_code
        # The dynamic error message, which is used to replace the `%s` variable in the **ErrMessage** parameter.
        # > For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the specified **DtsJobId** request parameter is invalid.
        self.dynamic_message = dynamic_message
        # The error arguments.
        self.error_args = error_args
        # Indicates whether the deletion is successful.
        self.module = module
        # Id of the request
        self.request_id = request_id
        # The error code.
        self.root_error_code = root_error_code
        # The root error message.
        self.root_error_msg = root_error_msg
        # Indicates whether the request is processed synchronously.
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code

        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('Module') is not None:
            temp_model = main_models.TranslateChannelDraftResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class TranslateChannelDraftResponseBodyModule(DaraModel):
    def __init__(
        self,
        adapt_status: str = None,
        adapted_content: str = None,
        adapted_title: str = None,
        channel: str = None,
        channel_account: str = None,
        channel_name: str = None,
        channel_type: str = None,
        cover_images: List[main_models.TranslateChannelDraftResponseBodyModuleCoverImages] = None,
        draft_id: str = None,
        external_id: str = None,
        external_url: str = None,
        fail_reason: str = None,
        publish_config: str = None,
        published_at: int = None,
        status: str = None,
    ):
        # The AI adaptation status. Valid values: NONE, ADAPTING, DONE, FAILED.
        self.adapt_status = adapt_status
        # The channel-adapted content body.
        self.adapted_content = adapted_content
        # The channel-adapted title.
        self.adapted_title = adapted_title
        # The channel enumeration value.
        self.channel = channel
        # The snapshot of the publishing account.
        self.channel_account = channel_account
        # The display name of the channel.
        self.channel_name = channel_name
        # The channel type. Valid values: DOMESTIC, OVERSEA, INTERNAL.
        self.channel_type = channel_type
        # The list of channel cover images.
        self.cover_images = cover_images
        # The ID of the channel draft.
        self.draft_id = draft_id
        # The ID returned by the platform.
        self.external_id = external_id
        # The redirect URL on the platform.
        self.external_url = external_url
        # The reason for the failure.
        self.fail_reason = fail_reason
        # The channel-specific publishing configuration in JSON format.
        self.publish_config = publish_config
        # The publishing time, in millisecond timestamp format.
        self.published_at = published_at
        # The status. Valid values: EDITING, PUBLISHING, SUCCESS, FAILED.
        self.status = status

    def validate(self):
        if self.cover_images:
            for v1 in self.cover_images:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adapt_status is not None:
            result['AdaptStatus'] = self.adapt_status

        if self.adapted_content is not None:
            result['AdaptedContent'] = self.adapted_content

        if self.adapted_title is not None:
            result['AdaptedTitle'] = self.adapted_title

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.channel_account is not None:
            result['ChannelAccount'] = self.channel_account

        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name

        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        result['CoverImages'] = []
        if self.cover_images is not None:
            for k1 in self.cover_images:
                result['CoverImages'].append(k1.to_map() if k1 else None)

        if self.draft_id is not None:
            result['DraftId'] = self.draft_id

        if self.external_id is not None:
            result['ExternalId'] = self.external_id

        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url

        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason

        if self.publish_config is not None:
            result['PublishConfig'] = self.publish_config

        if self.published_at is not None:
            result['PublishedAt'] = self.published_at

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptStatus') is not None:
            self.adapt_status = m.get('AdaptStatus')

        if m.get('AdaptedContent') is not None:
            self.adapted_content = m.get('AdaptedContent')

        if m.get('AdaptedTitle') is not None:
            self.adapted_title = m.get('AdaptedTitle')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('ChannelAccount') is not None:
            self.channel_account = m.get('ChannelAccount')

        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        self.cover_images = []
        if m.get('CoverImages') is not None:
            for k1 in m.get('CoverImages'):
                temp_model = main_models.TranslateChannelDraftResponseBodyModuleCoverImages()
                self.cover_images.append(temp_model.from_map(k1))

        if m.get('DraftId') is not None:
            self.draft_id = m.get('DraftId')

        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')

        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')

        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')

        if m.get('PublishConfig') is not None:
            self.publish_config = m.get('PublishConfig')

        if m.get('PublishedAt') is not None:
            self.published_at = m.get('PublishedAt')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class TranslateChannelDraftResponseBodyModuleCoverImages(DaraModel):
    def __init__(
        self,
        material_file_id: str = None,
        oss_url: str = None,
        sort_order: int = None,
    ):
        # The file ID in the material center.
        self.material_file_id = material_file_id
        # The CDN URL of the image.
        self.oss_url = oss_url
        # The sort order number.
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.material_file_id is not None:
            result['MaterialFileId'] = self.material_file_id

        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialFileId') is not None:
            self.material_file_id = m.get('MaterialFileId')

        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

