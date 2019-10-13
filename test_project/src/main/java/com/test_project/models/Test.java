package com.test_project.models;
import javax.persistence.*;
import java.time.ZonedDateTime;
@Entity
@Table(name = "test", schema = "schema")
public class Test {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name="id", unique = true)
    private long id;

     @Column(name="created_on")
    private ZonedDateTime created_on;

    public Test() {
    this.setCreated_on(ZonedDateTime.now());
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public ZonedDateTime getCreated_on() {
        return created_on;
    }
    public void setCreated_on(ZonedDateTime created_on) {
        this.created_on = created_on;
    }
}
