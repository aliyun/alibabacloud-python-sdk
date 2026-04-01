# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCollationTimeZoneRequest(DaraModel):
    def __init__(
        self,
        collation: str = None,
        dbinstance_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        timezone: str = None,
    ):
        # The character set collation of the instance. By default, the system does not modify the character set collation of the instance. Valid values:
        # 
        # *   **Chinese_PRC_CI_AS**
        # *   **Chinese_PRC_CS_AS**
        # *   **Chinese_PRC_BIN**
        # *   **Latin1_General_CI_AS**
        # *   **Latin1_General_CS_AS**
        # *   **SQL_Latin1_General_CP1_CI_AS**
        # *   **SQL_Latin1_General_CP1_CS_AS**
        # *   **Japanese_CI_AS**
        # *   **Japanese_CS_AS**
        # *   **Chinese_Taiwan_Stroke_CI_AS**
        # *   **Chinese_Taiwan_Stroke_CS_AS**
        # 
        # > *   The default character set collation of the instance is **Chinese_PRC_CI_AS**.
        # > *   You must specify one of the **Collation** and **Timezone** parameters.
        self.collation = collation
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The time zone of the instance. By default, the system does not modify the time zone.
        # 
        # > *   The default time zone of the instance is **China Standard Time**.
        # > *   You must specify one of the **Collation** and **Timezone** parameters.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collation is not None:
            result['Collation'] = self.collation

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collation') is not None:
            self.collation = m.get('Collation')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        return self

