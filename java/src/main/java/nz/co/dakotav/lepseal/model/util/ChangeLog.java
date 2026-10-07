package nz.co.dakotav.lepseal.model.util;

import java.time.OffsetDateTime;
import java.util.ArrayList;
import java.util.List;

/**
 * The ChangeLog class is responsible for maintaining a log of changes
 * with time-stamped entries. It provides methods to track additions,
 * updates, and removals, which are stored as messages in a list.
 */
public class ChangeLog {
    List<String> log;

    public ChangeLog() {
        this.log = new ArrayList<>();
    }

    /**
     * Adds a new message to the change log with a time-stamped "[ADD]" entry.
     * The message is stored in the log and returned for further usage.
     *
     * @param message the message to be added to the change log
     * @return the formatted time-stamped message that was added to the log
     */
    public String add(String message) {
        String input = "[ADD @ " + now() + "]:\n" + message;
        log.add(input);
        return input;
    }

    /**
     * Updates the change log with a time-stamped "[UPDATE]" entry.
     * The provided message is stored in the log with a formatted timestamp
     * and the updated message is returned for further usage.
     *
     * @param message the message to be updated in the change log
     * @return the formatted time-stamped message that was updated in the log
     */
    public String update(String message) {
        String input = "[UPDATE @ " + now() + "]:\n" + message;
        log.add(input);
        return input;
    }

    /**
     * Records the removal of a value by adding a time-stamped "[REMOVE]" entry to the change log.
     * The provided message is formatted with a timestamp and stored in the log.
     *
     * @param message the message to be recorded in the change log
     * @return the formatted time-stamped message that was added to the log
     */
    public String remove(String message) {
        String input = "[REMOVE @ " + now() + "]:\n" + message;
        log.add(input);
        return input;
    }

    private OffsetDateTime now() {
        return OffsetDateTime.now();
    }

}
