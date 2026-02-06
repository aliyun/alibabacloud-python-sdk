# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMediaStorageClassRequest(DaraModel):
    def __init__(
        self,
        allow_update_without_time_limit: bool = None,
        media_ids: str = None,
        restore_tier: str = None,
        scope: str = None,
        storage_class: str = None,
    ):
        # Specifies whether to change the storage class of a media asset that is stored for less than the minimum storage duration. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  If you forcibly change the storage class of a media asset that is stored for less than the minimum storage duration, additional data retrieval fees are incurred.
        self.allow_update_without_time_limit = allow_update_without_time_limit
        # The media asset ID. You can specify a maximum of 20 IDs. Separate multiple IDs with commas (,). You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [ApsaraVideo VOD](https://vod.console.aliyun.com) console. In the left-side navigation pane, choose **Media Files** > **Audio/Video**. On the Video and Audio page, you can view the ID of the media asset. This method is applicable to files that are uploaded by using the ApsaraVideo VOD console.
        # *   Obtain the value of the VideoId parameter from the response to the [CreateUploadVideo](https://help.aliyun.com/document_detail/55407.html) operation that you call to upload media assets.
        # *   Obtain the value of the VideoId parameter from the response to the [SearchMedia](https://help.aliyun.com/document_detail/86044.html) operation that you call to query the media ID after the media asset is uploaded.
        # 
        # This parameter is required.
        self.media_ids = media_ids
        # The restoration priority. This parameter is required only when you restore a Cold Archive media asset. Valid values:
        # 
        # *   **Expedited**
        # *   **Standard**
        # *   **Bulk**
        self.restore_tier = restore_tier
        # The modification range. Valid values:
        # 
        # *   **All**: modifies the storage classes of all resources including the source files and transcoded streams.
        # *   **SourceFile**: modifies the storage classes of only the source files. The storage class of other resources is Standard.
        self.scope = scope
        # The storage class. Valid values:
        # 
        # *   **Standard**
        # *   **IA**
        # *   **Archive**
        # *   **ColdArchive**
        # 
        # This parameter is required.
        self.storage_class = storage_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_update_without_time_limit is not None:
            result['AllowUpdateWithoutTimeLimit'] = self.allow_update_without_time_limit

        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        if self.restore_tier is not None:
            result['RestoreTier'] = self.restore_tier

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowUpdateWithoutTimeLimit') is not None:
            self.allow_update_without_time_limit = m.get('AllowUpdateWithoutTimeLimit')

        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        if m.get('RestoreTier') is not None:
            self.restore_tier = m.get('RestoreTier')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        return self

