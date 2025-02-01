"""Availability Migration."""

from masoniteorm.migrations import Migration


class Availability(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("availabilities") as table:
            table.increments("id")
            table.date("start_date")
            table.date("end_date")
            table.string("reason")
            table.integer("user_id").unsigned()
            table.foreign("user_id").references("id").on("users")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("availabilities")
