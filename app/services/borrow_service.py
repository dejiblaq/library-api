from schemas.borrow_schema import BorrowRecord


class BorrowService:
    def get_borrow_record(self, borrow_records: list[BorrowRecord], record_id: int):
        for record in borrow_records:
            if record["id"] == record_id:
                return record
        return None
    

borrow_service = BorrowService()