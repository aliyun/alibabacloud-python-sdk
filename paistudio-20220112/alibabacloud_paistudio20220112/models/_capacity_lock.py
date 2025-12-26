# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CapacityLock(DaraModel):
    def __init__(
        self,
        available_count: int = None,
        crs_reservation_id: str = None,
        description: str = None,
        expire_time: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: str = None,
        instance_type: str = None,
        last_reconcile_attempt_time: str = None,
        last_sync_time: str = None,
        lock_provider: str = None,
        locked_count: int = None,
        operator: str = None,
        payment_type: str = None,
        private_pool_id: str = None,
        requested_count: int = None,
        status: str = None,
        tenant_id: str = None,
        used_count: int = None,
        zone_id: str = None,
    ):
        self.available_count = available_count
        self.crs_reservation_id = crs_reservation_id
        self.description = description
        self.expire_time = expire_time
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.id = id
        self.instance_type = instance_type
        self.last_reconcile_attempt_time = last_reconcile_attempt_time
        self.last_sync_time = last_sync_time
        self.lock_provider = lock_provider
        self.locked_count = locked_count
        self.operator = operator
        self.payment_type = payment_type
        self.private_pool_id = private_pool_id
        self.requested_count = requested_count
        self.status = status
        self.tenant_id = tenant_id
        self.used_count = used_count
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_count is not None:
            result['availableCount'] = self.available_count

        if self.crs_reservation_id is not None:
            result['crsReservationId'] = self.crs_reservation_id

        if self.description is not None:
            result['description'] = self.description

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.last_reconcile_attempt_time is not None:
            result['lastReconcileAttemptTime'] = self.last_reconcile_attempt_time

        if self.last_sync_time is not None:
            result['lastSyncTime'] = self.last_sync_time

        if self.lock_provider is not None:
            result['lockProvider'] = self.lock_provider

        if self.locked_count is not None:
            result['lockedCount'] = self.locked_count

        if self.operator is not None:
            result['operator'] = self.operator

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.private_pool_id is not None:
            result['privatePoolId'] = self.private_pool_id

        if self.requested_count is not None:
            result['requestedCount'] = self.requested_count

        if self.status is not None:
            result['status'] = self.status

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.used_count is not None:
            result['usedCount'] = self.used_count

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('availableCount') is not None:
            self.available_count = m.get('availableCount')

        if m.get('crsReservationId') is not None:
            self.crs_reservation_id = m.get('crsReservationId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('lastReconcileAttemptTime') is not None:
            self.last_reconcile_attempt_time = m.get('lastReconcileAttemptTime')

        if m.get('lastSyncTime') is not None:
            self.last_sync_time = m.get('lastSyncTime')

        if m.get('lockProvider') is not None:
            self.lock_provider = m.get('lockProvider')

        if m.get('lockedCount') is not None:
            self.locked_count = m.get('lockedCount')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('privatePoolId') is not None:
            self.private_pool_id = m.get('privatePoolId')

        if m.get('requestedCount') is not None:
            self.requested_count = m.get('requestedCount')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('usedCount') is not None:
            self.used_count = m.get('usedCount')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

