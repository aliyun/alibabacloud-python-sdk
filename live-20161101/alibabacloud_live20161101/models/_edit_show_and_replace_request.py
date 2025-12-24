# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EditShowAndReplaceRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        end_time: float = None,
        owner_id: int = None,
        region_id: str = None,
        show_id: str = None,
        start_time: float = None,
        storage_info: str = None,
        user_data: str = None,
    ):
        # The ID of the production studio.
        # 
        # *   If the production studio was created by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the value of the response parameter CasterId to obtain the ID.
        # *   If the production studio was created by using the ApsaraVideo Live console, obtain the ID on the **Production Studio Management** page. To go to the page, log on to the **ApsaraVideo Live console** and click **Production Studios** in the left-side navigation pane.
        # 
        # >  You can find the ID of the production studio in the Instance ID/Name column.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The end time of the editing task. Unit: seconds.
        # 
        # > 
        # 
        # *   The valid values range from 0 to the value indicated by the total length of the episode.
        # 
        # *   By default, this parameter is set to the value that indicates the total length of the episode. The editing period cannot exceed the total length of the episode.
        # 
        # *   If you want to edit a VOD file from the 2nd second to the 5th second, set the StartTime parameter to 2.0 and the EndTime parameter to 5.0.
        self.end_time = end_time
        self.owner_id = owner_id
        self.region_id = region_id
        # The ID of the episode to be edited.
        # 
        # >  You can obtain the ID from the response parameter ShowId of the [AddShowIntoShowList](https://help.aliyun.com/document_detail/2848051.html) operation.
        # 
        # This parameter is required.
        self.show_id = show_id
        # The start time of the editing task. Unit: seconds.
        # 
        # > 
        # 
        # *   The valid values range from 0 to the value indicated by the total length of the episode. By default, the editing task starts from the beginning of the episode. Default value: 0.0.
        # 
        # *   If you want to edit a VOD file from the 2nd second to the 5th second, set the StartTime parameter to 2.0 and the EndTime parameter to 5.0.
        self.start_time = start_time
        # The storage information of the episode. The following fields are included:
        # 
        # *   **StorageLocation**: the storage location of ApsaraVideo VOD.
        # *   **FileName**: the custom file name.
        # 
        # >  Editing outputs must be stored in the VOD bucket within the same account that is used to access both ApsaraVideo VOD and ApsaraVideo Live. For more information about how to obtain the storage location, see [Manage VOD resources](https://help.aliyun.com/document_detail/86097.html).
        self.storage_info = storage_info
        # The user information.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.show_id is not None:
            result['ShowId'] = self.show_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.storage_info is not None:
            result['StorageInfo'] = self.storage_info

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ShowId') is not None:
            self.show_id = m.get('ShowId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StorageInfo') is not None:
            self.storage_info = m.get('StorageInfo')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

