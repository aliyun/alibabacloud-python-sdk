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
        # The production studio ID.
        # 
        # - If you created the production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the CasterId parameter in the response.
        # 
        # - If you created the production studio in the ApsaraVideo Live console, go to **ApsaraVideo Live console** > **Production Studios** > **Cloud Production Studio** to view the ID.
        # 
        # > The production studio name in the production studio list on the Cloud Production Studio page is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The end time of the video clip. Unit: seconds.
        # 
        # > - The valid range of the clip time is 0 to the total duration of the show.
        # > - The default value is the end time of the video-on-demand file. The value cannot exceed the total duration of the show.
        # > - For example, to clip a video-on-demand file from the 2nd second to the 5th second, set StartTime to 2.0 and EndTime to 5.0.
        # > - You must specify at least one of StartTime and EndTime.
        self.end_time = end_time
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The ID of the show to be clipped. The referenced show must be of the video-on-demand material type (ResourceInfo.ResourceType=vod with a valid resourceId).
        # > Obtain the ShowId value from the response parameters of the [AddShowIntoShowList](https://help.aliyun.com/document_detail/2848051.html) operation.
        # 
        # This parameter is required.
        self.show_id = show_id
        # The start time of the video clip. Unit: seconds.
        # 
        # > - The valid range of the clip time is 0 to the total duration of the show. - By default, the clip starts from the beginning of the video-on-demand file. Value: 0.0.
        # > - For example, to clip a video-on-demand file from the 2nd second to the 5th second, set StartTime to 2.0 and EndTime to 5.0.
        # > - You must specify at least one of StartTime and EndTime.
        self.start_time = start_time
        # The storage information. This parameter is required. Description:
        # 
        # - **StorageLocation**: the video-on-demand storage address of the user.
        # - **FileName**: the custom file name.
        # 
        # > The video clip storage address must be a video-on-demand storage address under the same account. To obtain the video-on-demand storage address, see [Storage management](https://help.aliyun.com/document_detail/86097.html).
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

