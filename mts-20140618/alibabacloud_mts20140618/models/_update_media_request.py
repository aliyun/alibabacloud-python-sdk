# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMediaRequest(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        cover_url: str = None,
        description: str = None,
        media_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: str = None,
        title: str = None,
    ):
        # The ID of the category to which the media file belongs. The value must be an integer.
        # 
        # *   If you do not specify this parameter, the value is NULL.
        # *   The value cannot be negative.
        self.cate_id = cate_id
        # The URL of the thumbnail. This parameter is used to specify the storage location of the thumbnail. To obtain the URL, you can log on to the **MPS console** and choose **Workflows** > **Media Buckets** in the left-side navigation pane. Alternatively, you can log on to the **OSS console** and click **Buckets** in the left-side navigation pane.
        # 
        # *   The value can be up to 3,200 bytes in length.
        # *   The URL complies with RFC 2396 and is encoded in UTF-8, with reserved characters being percent-encoded. For more information, see [URL encoding](https://help.aliyun.com/document_detail/423796.html).
        self.cover_url = cover_url
        # The description of the media file. Multiple character types, such as letters and digits, are supported.
        # 
        # *   If you do not specify this parameter, the value is NULL.
        # *   The value is encoded in UTF-8 and can be up to 1,024 bytes in length.
        self.description = description
        # The ID of the media file whose basic information you want to update. To obtain the ID of the media file, you can log on to the **ApsaraVideo Media Processing (MPS) console** and choose **Media Management** > **Media List** in the left-side navigation pane.
        # 
        # This parameter is required.
        self.media_id = media_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags that you want to add to the media file.
        # 
        # *   You can specify up to 16 tags for a media file. Separate multiple tags with commas (,).
        # *   Each tag can be up to 32 bytes in length.
        # *   The value is encoded in UTF-8.
        self.tags = tags
        # The title of the media file. Multiple character types, such as letters and digits, are supported.
        # 
        # *   If you do not specify this parameter, the value is NULL.
        # *   The value is encoded in UTF-8 and can be up to 128 bytes in length.
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

        if self.media_id is not None:
            result['MediaId'] = self.media_id

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

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

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

