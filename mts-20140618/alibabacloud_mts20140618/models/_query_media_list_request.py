# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMediaListRequest(DaraModel):
    def __init__(
        self,
        include_media_info: bool = None,
        include_play_list: bool = None,
        include_snapshot_list: bool = None,
        include_summary_list: bool = None,
        media_ids: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to include media information in the returned result.
        # 
        # *   Valid values: true and false.
        # *   Default value: **false**.
        self.include_media_info = include_media_info
        # Specifies whether to include playback information in the returned result.
        # 
        # *   Valid values: true and false.
        # *   Default value: **false**.
        self.include_play_list = include_play_list
        # Specifies whether to include snapshot information in the returned result.
        # 
        # *   Valid values: true and false.
        # *   Default value: **false**.
        self.include_snapshot_list = include_snapshot_list
        # Specifies whether to include summaries in the returned result.
        # 
        # *   Valid values: true and false.
        # *   Default value: **false**.
        self.include_summary_list = include_summary_list
        # The IDs of the media files. To obtain the ID of a media file, you can perform the following operations in the ApsaraVideo Media Processing (MPS) console: In the left-side navigation pane, choose **Media Management** > **Media List**. Find the required video and click Manage. The ID of the video is displayed on the Basics tab. Separate multiple IDs with commas (,). You can query up to 10 media files at a time.
        # 
        # This parameter is required.
        self.media_ids = media_ids
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_media_info is not None:
            result['IncludeMediaInfo'] = self.include_media_info

        if self.include_play_list is not None:
            result['IncludePlayList'] = self.include_play_list

        if self.include_snapshot_list is not None:
            result['IncludeSnapshotList'] = self.include_snapshot_list

        if self.include_summary_list is not None:
            result['IncludeSummaryList'] = self.include_summary_list

        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeMediaInfo') is not None:
            self.include_media_info = m.get('IncludeMediaInfo')

        if m.get('IncludePlayList') is not None:
            self.include_play_list = m.get('IncludePlayList')

        if m.get('IncludeSnapshotList') is not None:
            self.include_snapshot_list = m.get('IncludeSnapshotList')

        if m.get('IncludeSummaryList') is not None:
            self.include_summary_list = m.get('IncludeSummaryList')

        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

