# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddPlaylistItemsRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        owner_id: int = None,
        program_config: str = None,
        program_id: str = None,
        program_items: str = None,
        region_id: str = None,
    ):
        # The production studio ID.
        # 
        # - If you created the production studio by calling the [CreateCaster operation](https://help.aliyun.com/document_detail/2848009.html), check the CasterId parameter value returned by the CreateCaster operation.
        # 
        # - If you created the production studio in the ApsaraVideo Live console, navigate to **ApsaraVideo Live console** > **Production Studios** > **Cloud Production Studio** to view the production studio name.
        # 
        # > The production studio name in the production studio list on the Cloud Production Studio page of the ApsaraVideo Live console is the production studio ID.
        # 
        # 
        # The production studio must meet the following configurations:
        # - **NormType**: **3**. Create a lightweight carousel production studio in advance. You can call the **CreateCaster** operation to create a production studio.
        # - **CasterTemplate**: lp_noTranscode.
        # - **channelEnable**: 0.
        # - **programEffect**: 1.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        self.owner_id = owner_id
        # The playlist item configuration. If this is the first time you add a playlist item, specify this parameter for initialization. For more information, see **ProgramConfig**.
        self.program_config = program_config
        # The playlist ID. If the production studio already has a playlist, you must specify the corresponding ProgramId. If no playlist has been created, you can leave this parameter empty, and the system performs automatic creation.
        self.program_id = program_id
        # The list of playlist item inputs. The value is a JSON string. For more information, see **InputProgramItem**.
        # 
        # This parameter is required.
        self.program_items = program_items
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.program_config is not None:
            result['ProgramConfig'] = self.program_config

        if self.program_id is not None:
            result['ProgramId'] = self.program_id

        if self.program_items is not None:
            result['ProgramItems'] = self.program_items

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProgramConfig') is not None:
            self.program_config = m.get('ProgramConfig')

        if m.get('ProgramId') is not None:
            self.program_id = m.get('ProgramId')

        if m.get('ProgramItems') is not None:
            self.program_items = m.get('ProgramItems')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

