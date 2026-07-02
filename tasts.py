from builtins import AssertionError, print

import pytest
import math
# נניח ששם הקובץ שלכם הוא linked_list.py
from node import Node, LinkedList


class LinkedList:
    pass


def test_init_and_is_empty():
    """בדיקת אתחול רשימה ריקה ומתודת is_empty"""
    ll = LinkedList()
    try:
        assert ll.head is None, "ראש הרשימה אינו None לאחר אתחול"
        assert ll.is_empty() is True, "הרשימה אינה מזוהה כריקה לאחר אתחול"
        print("\n✅ טסט אתחול ו-is_empty: הצליח! הרשימה אותחלה כריקה כנדרש.")
    except AssertionError as e:
        print(f"\n❌ טסט אתחול ו-is_empty: נכשל! שגיאה: {e}")
        raise


def test_push():
    """בדיקת הוספה לתחילת הרשימה"""
    ll = LinkedList()
    try:
        ll.push(10)
        assert ll.head.data == 10, "הערך בחוליה הראשונה אינו 10 לאחר push"

        ll.push(20)
        assert ll.head.data == 20, "הערך בראש הרשימה לא התעדכן ל-20 לאחר push נוסף"
        assert ll.head.next.data == 10, "החוליה השנייה אינה מכילה את הערך הקודם (10)"
        print("\n✅ טסט push (הוספה להתחלה): הצליח! החוליות נוספו בסדר הנכון.")
    except AssertionError as e:
        print(f"\n❌ טסט push: נכשל! שגיאה: {e}")
        raise


def test_append():
    """בדיקת הוספה לסוף הרשימה"""
    ll = LinkedList()
    try:
        ll.append(5)
        assert ll.head.data == 5, "האיבר הראשון אינו 5 לאחר append לרשימה ריקה"

        ll.append(15)
        assert ll.head.next.data == 15, "האיבר השני אינו 15 לאחר append"
        assert ll.head.next.next is None, "החוליה האחרונה אינה מצביעה ל-None"
        print("\n✅ טסט append (הוספה לסוף): הצליח! האיברים נוספו לסוף הרשימה בהצלחה.")
    except AssertionError as e:
        print(f"\n❌ טסט append: נכשל! שגיאה: {e}")
        raise


def test_length():
    """בדיקת חישוב אורך הרשימה"""
    ll = LinkedList()
    try:
        assert ll.length() == 0, "אורך רשימה ריקה אינו 0"
        ll.push(1)
        ll.push(2)
        ll.append(3)
        assert ll.length() == 3, f"אורך הרשימה היה צריך להיות 3, אך התקבל {ll.length()}"
        print("\n✅ טסט length (אורך הרשימה): הצליח! חישוב האורך מדויק.")
    except AssertionError as e:
        print(f"\n❌ טסט length: נכשל! שגיאה: {e}")
        raise


def test_delete_first():
    """בדיקת מחיקת החוליה הראשונה"""
    ll = LinkedList()
    try:
        ll.push(10)
        ll.push(20)

        deleted = ll.delete_first()
        assert deleted == 20, f"delete_first החזירה {deleted} במקום 20"
        assert ll.head.data == 10, "ראש הרשימה לא התעדכן לחוליה הבאה לאחר מחיקה"

        ll.delete_first()
        assert ll.is_empty() is True, "הרשימה אינה ריקה למרות שכל האיברים נמחקו"
        print("\n✅ טסט delete_first (מחיקת איבר ראשון): הצליח! האיבר נמחק והערך הוחזר כראוי.")
    except AssertionError as e:
        print(f"\n❌ טסט delete_first: נכשל! שגיאה: {e}")
        raise


def test_find():
    """בדיקת חיפוש חוליה לפי ערך"""
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    try:
        node = ll.find(20)
        assert isinstance(node, Node), "find לא החזירה אובייקט מסוג Node עבור ערך קיים"
        assert node.data == 20, "החוליה שנמצאה אינה מכילה את הערך המבוקש"

        # בדיקת ערך לא קיים (מחזיר NAN לפי הדרישה)
        res = ll.find(99)
        assert res == "NAN" or (isinstance(res, float) and math.isnan(res)), "עבור ערך לא קיים לא הוחזר NAN כמצופה"
        print("\n✅ טסט find (חיפוש לפי ערך): הצליח! מציג חוליות קיימות ומחזיר NAN כשלא נמצא.")
    except AssertionError as e:
        print(f"\n❌ טסט find: נכשל! שגיאה: {e}")
        raise


def test_find_index():
    """בדיקת חיפוש חוליה לפי אינדקס"""
    ll = LinkedList()
    ll.append(10)  # אינדקס 0
    ll.append(20)  # אינדקס 1
    try:
        node = ll.find_index(1)
        assert node.data == 20, f"באינדקס 1 צפוי 20, אך התקבל {node.data}"

        res = ll.find_index(5)
        assert res == "NAN" or (isinstance(res, float) and math.isnan(res)), "אינדקס מחוץ לטווח לא החזיר NAN"
        print("\n✅ טסט find_index (חיפוש לפי אינדקס): הצליח! הניווט לפי אינדקסים עובד.")
    except AssertionError as e:
        print(f"\n❌ טסט find_index: נכשל! שגיאה: {e}")
        raise


def test_delete_after():
    """בדיקת מחיקת החוליה שאחרי חוליה נתונה"""
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    try:
        node_10 = ll.find(10)
        deleted_val = ll.delete_after(node_10)

        assert deleted_val == 20, f"הערך שנמחק היה צריך להיות 20, אך התקבל {deleted_val}"
        assert node_10.next.data == 30, "הקשר בין החוליות לא התעדכן בצורה נכונה לאחר המחיקה"
        print("\n✅ טסט delete_after (מחיקה אחרי חוליה): הצליח! החוליה העוקבת נמחקה והרצף נשמר.")
    except AssertionError as e:
        print(f"\n❌ טסט delete_after: נכשל! שגיאה: {e}")
        raise